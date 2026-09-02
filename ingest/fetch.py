#!/usr/bin/env python3
"""Ingest the drug-discoverer corpus.

Runs anywhere with network access. Built to be left running unattended on a
Raspberry Pi: it caches on disk, resumes where it stopped, rate-limits
itself, honours robots.txt, and never re-downloads a document it already has.

    python -m ingest.fetch --dry-run              # show the plan, fetch nothing
    python -m ingest.fetch --method git           # cheapest and best; start here
    python -m ingest.fetch --method archive       # paginated blog back catalogues
    python -m ingest.fetch --person "Pat Walters"
    python -m ingest.fetch --papers "Kevan Shokat"

Output layout under --out (default ./corpus):

    corpus/
      raw/<sha256>.bin        every response body, content-addressed
      docs.jsonl              one row per document, with provenance
      state.json              per-target cursors, so a re-run resumes
      git/<repo>/             cloned repositories

Every row in docs.jsonl carries source_url, fetched_at, person and method, so
nothing in the corpus is anonymous by the time it reaches a training set.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import time
import urllib.parse
import urllib.robotparser
from dataclasses import dataclass, field

try:
    import requests
except ImportError:                                    # pragma: no cover
    requests = None

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ingest.targets import TARGETS                     # noqa: E402

UA = ("drug-discoverer-corpus/0.1 (research corpus; contact: "
      "jb.michel@gmail.com) python-requests")
DEFAULT_DELAY = 1.5          # seconds between requests to one host
MAX_PAGES = 400              # hard stop so a paging bug cannot run away


# ---------------------------------------------------------------- store

@dataclass
class Store:
    root: pathlib.Path
    delay: float = DEFAULT_DELAY
    state: dict = field(default_factory=dict)
    _last_hit: dict = field(default_factory=dict)
    _seen: set = field(default_factory=set)
    _robots: dict = field(default_factory=dict)

    def __post_init__(self):
        (self.root / "raw").mkdir(parents=True, exist_ok=True)
        sf = self.root / "state.json"
        if sf.exists():
            self.state = json.loads(sf.read_text())
        dj = self.root / "docs.jsonl"
        if dj.exists():
            for line in dj.open():
                try:
                    self._seen.add(json.loads(line)["source_url"])
                except Exception:
                    continue

    def save_state(self):
        (self.root / "state.json").write_text(json.dumps(self.state, indent=1))

    def have(self, url: str) -> bool:
        return url in self._seen

    def allowed(self, url: str) -> bool:
        """Honour robots.txt. A site that says no is a site we skip."""
        parts = urllib.parse.urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        if origin not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(origin + "/robots.txt")
            try:
                rp.read()
            except Exception:
                rp = None            # unreachable robots.txt: proceed politely
            self._robots[origin] = rp
        rp = self._robots[origin]
        return True if rp is None else rp.can_fetch(UA, url)

    def _throttle(self, url: str):
        host = urllib.parse.urlsplit(url).netloc
        wait = self.delay - (time.time() - self._last_hit.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        self._last_hit[host] = time.time()

    def get(self, url: str, params: dict | None = None, tries: int = 3):
        if requests is None:
            raise SystemExit("pip install requests feedparser beautifulsoup4")
        if not self.allowed(url):
            print(f"  robots.txt disallows {url}", file=sys.stderr)
            return None
        for attempt in range(tries):
            self._throttle(url)
            try:
                r = requests.get(url, params=params, timeout=45,
                                 headers={"User-Agent": UA})
            except requests.RequestException as exc:
                print(f"  {type(exc).__name__} on {url}", file=sys.stderr)
                time.sleep(2 ** attempt)
                continue
            if r.status_code == 429 or 500 <= r.status_code < 600:
                time.sleep(5 * (attempt + 1))
                continue
            if r.status_code != 200:
                print(f"  HTTP {r.status_code} {url}", file=sys.stderr)
                return None
            return r
        return None

    def write(self, *, person, method, source_url, title, text,
              published=None, extra=None):
        """Record one document. Body goes to raw/, metadata to docs.jsonl."""
        blob = text.encode("utf-8") if isinstance(text, str) else text
        digest = hashlib.sha256(blob).hexdigest()
        (self.root / "raw" / f"{digest}.bin").write_bytes(blob)
        row = {"person": person, "method": method, "source_url": source_url,
               "title": title, "published": published, "sha256": digest,
               "bytes": len(blob), "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                                               time.gmtime())}
        if extra:
            row.update(extra)
        with (self.root / "docs.jsonl").open("a") as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        self._seen.add(source_url)
        return row


# ------------------------------------------------------------- fetchers

def next_params(paging: str, base: dict, page: int, per: int) -> dict:
    """Page-parameter arithmetic for the three archive platforms.

    Blogger is 1-based over item offsets, WordPress is 1-based over pages,
    Substack is 0-based over item offsets. Getting this wrong silently
    truncates an archive, so it is isolated here and unit-tested.
    """
    p = dict(base)
    if paging == "start-index":
        p["start-index"] = page * per + 1
    elif paging == "paged":
        p["paged"] = page + 1
    elif paging == "offset":
        p["offset"] = page * per
    else:
        raise ValueError(f"unknown paging scheme {paging!r}")
    return p


def fetch_git(store: Store, person: str, entry: dict):
    dest = store.root / "git" / entry["url"].rstrip("/").split("/")[-1]
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        cmd = ["git", "-C", str(dest), "pull", "--ff-only"]
    else:
        cmd = ["git", "clone", "--depth", "1", entry["url"], str(dest)]
    print(f"  $ {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(f"  git failed: {r.stderr.strip()[:200]}", file=sys.stderr)
        return 0
    n = 0
    for path in dest.rglob("*"):
        if path.suffix.lower() not in {".ipynb", ".md", ".qmd", ".rst", ".txt"}:
            continue
        url = f"{entry['url']}/blob/HEAD/{path.relative_to(dest)}"
        if store.have(url):
            continue
        store.write(person=person, method="git", source_url=url,
                    title=path.name, text=path.read_text(errors="replace"))
        n += 1
    return n


def fetch_archive(store: Store, person: str, entry: dict):
    """Walk a paginated blog archive to exhaustion."""
    per = entry.get("params", {}).get("max-results") or \
          entry.get("params", {}).get("limit") or 50
    key = f"{person}|{entry['url']}"
    page = store.state.get(key, {}).get("page", 0)
    total = 0
    while page < MAX_PAGES:
        params = next_params(entry["paging"], entry.get("params", {}), page, per)
        r = store.get(entry["url"], params=params)
        if r is None or not r.content.strip():
            break
        items = parse_items(r)
        if not items:
            break
        fresh = 0
        for it in items:
            if store.have(it["url"]):
                continue
            store.write(person=person, method="archive", source_url=it["url"],
                        title=it["title"], text=it["text"],
                        published=it.get("published"))
            fresh += 1
        total += fresh
        print(f"  page {page}: {len(items)} items, {fresh} new")
        page += 1
        store.state[key] = {"page": page}
        store.save_state()
        if len(items) < per:
            break
    return total


def parse_items(response):
    """Normalise Blogger JSON, Substack JSON and RSS/Atom into one shape."""
    ctype = response.headers.get("content-type", "")
    if "json" in ctype:
        data = response.json()
        if isinstance(data, list):                       # Substack archive
            return [{"url": d.get("canonical_url", ""),
                     "title": d.get("title", ""),
                     "published": d.get("post_date"),
                     "text": d.get("body_html") or d.get("description", "")}
                    for d in data]
        entries = data.get("feed", {}).get("entry", [])   # Blogger
        out = []
        for e in entries:
            link = next((l["href"] for l in e.get("link", [])
                         if l.get("rel") == "alternate"), "")
            out.append({"url": link,
                        "title": e.get("title", {}).get("$t", ""),
                        "published": e.get("published", {}).get("$t"),
                        "text": e.get("content", {}).get("$t", "")})
        return out
    try:
        import feedparser
    except ImportError:
        raise SystemExit("pip install feedparser")
    feed = feedparser.parse(response.content)
    return [{"url": e.get("link", ""), "title": e.get("title", ""),
             "published": e.get("published"),
             "text": (e.get("content", [{}])[0].get("value")
                      if e.get("content") else e.get("summary", ""))}
            for e in feed.entries]


def fetch_sitemap(store: Store, person: str, entry: dict):
    r = store.get(entry["url"])
    if r is None:
        return 0
    import re
    urls = re.findall(r"<loc>(.*?)</loc>", r.text)
    if entry.get("filter"):
        urls = [u for u in urls if entry["filter"] in u]
    print(f"  sitemap: {len(urls)} URLs after filter")
    n = 0
    for u in urls:
        if store.have(u):
            continue
        page = store.get(u)
        if page is None:
            continue
        store.write(person=person, method="sitemap", source_url=u,
                    title=extract_title(page.text), text=page.text)
        n += 1
    return n


def extract_title(html: str) -> str:
    import re
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    return m.group(1).strip()[:300] if m else ""


def fetch_papers(store: Store, person: str, limit: int = 200):
    """Europe PMC. The right way to get the paper half of the corpus."""
    base = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    surname = person.split()[-1]
    initial = person.split()[0][0]
    query = f'AUTH:"{surname} {initial}"'
    cursor, n = "*", 0
    while n < limit:
        r = store.get(base, params={"query": query, "format": "json",
                                    "resultType": "core", "pageSize": 100,
                                    "cursorMark": cursor})
        if r is None:
            break
        data = r.json()
        results = data.get("resultList", {}).get("result", [])
        if not results:
            break
        for res in results:
            url = res.get("doi") and f"https://doi.org/{res['doi']}" or \
                  f"https://europepmc.org/article/{res.get('source')}/{res.get('id')}"
            if store.have(url):
                continue
            store.write(person=person, method="api", source_url=url,
                        title=res.get("title", ""),
                        text=res.get("abstractText", "") or "",
                        published=res.get("firstPublicationDate"),
                        extra={"doi": res.get("doi"),
                               "journal": res.get("journalTitle"),
                               "is_open_access": res.get("isOpenAccess"),
                               "citations": res.get("citedByCount")})
            n += 1
        nxt = data.get("nextCursorMark")
        if not nxt or nxt == cursor:
            break
        cursor = nxt
    print(f"  Europe PMC: {n} records for {query}")
    print("   NOTE: author-name matching is approximate. Resolve an OpenAlex "
          "author ID per person before trusting these.")
    return n


HANDLERS = {"git": fetch_git, "archive": fetch_archive, "sitemap": fetch_sitemap}


# ------------------------------------------------------------------ cli

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="corpus", type=pathlib.Path)
    ap.add_argument("--method", help="git | archive | sitemap | feed")
    ap.add_argument("--person")
    ap.add_argument("--papers", help="fetch papers for one person via Europe PMC")
    ap.add_argument("--delay", type=float, default=DEFAULT_DELAY)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    store = Store(root=args.out, delay=args.delay)

    if args.papers:
        fetch_papers(store, args.papers)
        return

    total = 0
    for person, entries in TARGETS.items():
        if args.person and person != args.person:
            continue
        for entry in entries:
            method = entry["method"]
            if args.method and method != args.method:
                continue
            if method in ("manual", "media", "api", "feed"):
                if args.dry_run:
                    print(f"[skip:{method}] {person} — {entry.get('note','')[:90]}")
                continue
            if args.dry_run:
                print(f"[{method}] {person} — {entry['url']}")
                continue
            print(f"[{method}] {person} — {entry['url']}")
            total += HANDLERS[method](store, person, entry)
    store.save_state()
    if not args.dry_run:
        print(f"\n{total} new documents -> {args.out}/docs.jsonl")


if __name__ == "__main__":
    main()

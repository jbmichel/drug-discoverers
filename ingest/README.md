# Ingest

The crawler. Nothing here has been run against the live web from the session
that wrote it — **every content host is blocked by that session's egress
proxy** (science.org, patwalters.github.io, nobelprize.org, pubmed, arxiv,
youtube: all 403 on CONNECT, on both curl and WebFetch). Only web *search*
worked, which returns result snippets, not documents.

So: `sources.md` says where the artifacts are. This says how to get them. The
offline-testable logic is tested (`python ingest/test_fetch.py`); the network
paths are not, and the first real run will need a shakedown.

## Run order

Cheapest and most reliable first. Do not start with the hardest source.

```bash
pip install requests feedparser beautifulsoup4

python -m ingest.fetch --dry-run          # see the plan, fetch nothing
python -m ingest.fetch --method git       # 1. clone the repos
python -m ingest.fetch --method archive   # 2. paginated blog back catalogues
python -m ingest.fetch --method sitemap   # 3. sitemap walks
python -m ingest.fetch --papers "Kevan Shokat"   # 4. papers, per person
```

Output goes to `corpus/`: bodies content-addressed under `raw/`, one metadata
row per document in `docs.jsonl`, cursors in `state.json`. Re-running resumes
rather than re-downloading — it replays `docs.jsonl` on startup and skips URLs
it already holds.

On a Pi, `--delay 3` and a `systemd` timer is the right shape; the whole thing
is I/O-bound and will happily take a week of nights. It writes append-only, so
killing it mid-run loses at most the page in flight.

## The four tiers, and why they differ

**1. `git` — the blog *is* a repository.** Pat Walters' and Greg Landrum's
posts are Jupyter notebooks in public GitHub repos. `git clone` gets the full
history with outputs intact, no HTML parsing, no rate limits, no
terms-of-service question. This is the best-quality path in the entire project
and it covers two of the most reasoning-dense people on the list.

**2. `archive` — paginated back catalogues.** Blogger and WordPress both hand
you the whole archive if you page correctly: Blogger over 1-based item offsets
(`start-index=1, 501, 1001`), WordPress over 1-based page numbers. Getting this
arithmetic wrong silently truncates an archive rather than erroring, which is
why it is isolated in `next_params()` and unit-tested per platform. Covers
Erlanson, AlQuraishi, Booth, Plenge.

**3. `sitemap` — no feed, walk `sitemap.xml`.** Workman's ICR blog, Drucker's
glucagon.com. Slower and needs a filter for large sites.

**4. `api` — for papers, use Europe PMC, never publisher scraping.** No key,
open-access full text at `/{source}/{id}/fullTextXML`, and the OA subset is
explicitly licensed for text mining. `--papers` does author-name matching,
which is approximate: **resolve an OpenAlex author ID per person before
trusting the output**, or you will get another Kevan Shokat's papers mixed in.

## Where it gets hard

**Derek Lowe is the awkward one, and he is the whole reason for the project.**
In the Pipeline has run since January 2002 across three hosts:

| Years | Host |
| --- | --- |
| 2002 – ~2012 | `corante.com/pipeline` (defunct) |
| ~2012 – 2021 | `blogs.sciencemag.org/pipeline/archives/YYYY/MM/DD/slug` |
| 2021 – now | `science.org/blogs/pipeline` |

Crawling only science.org silently loses the first decade — probably the most
distinctive decade. The `science.org` feed is a recent window only, no use for
backfill. The defensible route to the old material is the Wayback Machine CDX
API, which is designed for exactly this:

```
http://web.archive.org/cdx/search/cdx?url=corante.com/pipeline*&output=json&collapse=urlkey
```

Same approach for the sciencemag years. Expect gaps and duplicate captures.

**David Grainger**: Forbes blocks automation; the older DrugBaron archive is
the better target and is likely Wayback-only.

**Drug Hunter** is a paid product for institutions. Treat the free tier as the
ceiling unless you hold a licence.

## Terms of use — worth deciding before you run this, not after

Not all of this is equally free to collect and redistribute. Roughly:

- **Most permissive**: Nobel lecture PDFs, NIH VideoCast (US government work),
  the Europe PMC open-access subset (explicitly licensed for text mining),
  arXiv/bioRxiv, and the GitHub repos under their own licences.
- **Read the terms**: AAAS/science.org restricts systematic downloading;
  Substack, YouTube and Forbes have their own positions.
- Personal research use and redistributing a trained model are different
  questions. `docs.jsonl` records `source_url` and `fetched_at` on every row
  specifically so you can filter the corpus by source later — decide once,
  filter at training time, rather than losing the provenance now.

## Rough sizing

Order-of-magnitude estimates, not measurements:

| Source | Documents | Text |
| --- | ---: | ---: |
| In the Pipeline, 2002–present | ~4,000–5,000 posts | ~30–40 MB |
| Practical Fragments | ~1,000–1,300 | ~8 MB |
| LifeSciVC | ~800–1,200 | ~10 MB |
| Pat Walters + Landrum (git) | ~250 notebooks | ~20 MB with outputs |
| AlQuraishi | ~20 essays | ~1 MB, very high density |
| Nobel lectures, 12 people | ~50 documents | ~5 MB |
| Papers, 61 people | ~15,000 abstracts | ~40 MB |

The blog corpus is small — low hundreds of MB. This fits on a Pi's SD card
with room to spare. Transcripts of lectures and podcasts are what will
actually take the time, not the disk.

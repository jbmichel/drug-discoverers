"""Ingestible endpoints for the Grade A corpus, classified by method.

The point of this file is that most of the corpus does NOT need scraping.
Roughly, in descending order of quality:

  git        - the blog IS a git repo. Clone it. Full history, no HTML,
               no rate limits, no terms-of-service question.
  archive    - the platform exposes a paginated feed or archive API that
               returns the WHOLE back catalogue, not just recent items.
  feed       - a plain RSS/Atom feed. Usually only the last 10-25 items,
               so it is for keeping current, not for backfill.
  api        - a real API meant for programmatic access (Europe PMC,
               OpenAlex, Crossref). Use for papers.
  sitemap    - no feed; walk sitemap.xml to enumerate URLs, then fetch.
  media      - audio/video needing transcription.
  manual     - paywalled, archive-only, or offline. A person has to get it.

`backfill` says whether the method reaches the full archive or only the
recent window. That distinction is the difference between a corpus and a
sample.
"""

# --- platform URL patterns, so new sources can be added by name only ----

def blogger_archive(host):
    """Blogger/Blogspot: paginated Atom, 500 per page, walks the archive."""
    return {"method": "archive", "backfill": True,
            "url": f"https://{host}/feeds/posts/default",
            "params": {"alt": "json", "max-results": 500},
            "paging": "start-index",   # 1-based, add max-results each page
            "note": "Blogger returns the full archive if you page start-index."}


def wordpress_archive(base):
    """WordPress: /feed/?paged=N walks back through the whole archive."""
    return {"method": "archive", "backfill": True,
            "url": f"{base.rstrip('/')}/feed/",
            "params": {},
            "paging": "paged",
            "note": "WordPress paginates its feed; stop when a page is empty. "
                    "wp-json/wp/v2/posts?per_page=100&page=N is better still "
                    "where the REST API is enabled."}


def substack_archive(base):
    """Substack: an undocumented but stable archive endpoint."""
    return {"method": "archive", "backfill": True,
            "url": f"{base.rstrip('/')}/api/v1/archive",
            "params": {"sort": "new", "limit": 50},
            "paging": "offset",
            "note": "Returns post metadata incl. canonical_url. Free posts "
                    "have full body_html; paid ones are truncated."}


# --- the registry ------------------------------------------------------

TARGETS = {

    # ============ tier 1: git clones. do these first ============
    "Pat Walters": [
        {"method": "git", "backfill": True,
         "url": "https://github.com/PatWalters/practical_cheminformatics_posts",
         "note": "The blog posts themselves, as notebooks. Reasoning as "
                 "executable code with outputs preserved."},
        {"method": "git", "backfill": True,
         "url": "https://github.com/PatWalters/practical_cheminformatics_tutorials"},
        {"method": "archive", "backfill": True,
         **blogger_archive("practicalcheminformatics.blogspot.com"),
         "note": "Pre-2022 archive; the blog moved to GitHub Pages."},
        {"method": "sitemap", "backfill": True,
         "url": "https://patwalters.github.io/sitemap.xml",
         "note": "Current site. Quarto/GitHub Pages emit a sitemap."},
    ],
    "Gregory Landrum": [
        {"method": "git", "backfill": True,
         "url": "https://github.com/greglandrum/rdkit-blog",
         "note": "Current blog, notebooks + data."},
        {"method": "git", "backfill": True,
         "url": "https://github.com/greglandrum/rdkit_blog",
         "note": "Older posts. Both halves needed for the full archive."},
        {"method": "archive", "backfill": True,
         **blogger_archive("rdkit.blogspot.com"),
         "note": "Pre-2022 archive."},
    ],

    # ============ tier 2: paginated archives ============
    "Daniel Erlanson": [
        blogger_archive("practicalfragments.blogspot.com") |
        {"note": "~15 years, roughly weekly. Blogger paging reaches all of it."},
    ],
    "Mohammed AlQuraishi": [
        wordpress_archive("https://moalquraishi.wordpress.com") |
        {"note": "Few but very long essays. Small corpus, high density."},
    ],
    "Bruce Booth": [
        wordpress_archive("https://lifescivc.com") |
        {"note": "2011-present. Also paginated HTML at /page/N/ as a fallback."},
    ],
    "Robert Plenge": [
        wordpress_archive("https://plengegen.com") |
        {"note": "Category archives at /blog/category/{drug-discovery,"
                 "human-genetics}/ if the feed under-reports."},
    ],

    # ============ tier 3: sitemap walks ============
    "Paul Workman": [
        {"method": "sitemap", "backfill": True,
         "url": "https://www.icr.ac.uk/sitemap.xml",
         "filter": "the-drug-discoverer",
         "note": "'The Drug Discoverer' blog. Filter the sitemap to the blog "
                 "path; the ICR site map is large."},
    ],
    "Dennis X. Hu": [
        {"method": "sitemap", "backfill": False,
         "url": "https://drughunter.com/sitemap.xml",
         "note": "CHECK TERMS FIRST. Drug Hunter is a paid product for "
                 "institutions; much of it sits behind login. Treat the free "
                 "tier as the ceiling unless you hold a licence."},
    ],
    "Daniel J. Drucker": [
        {"method": "sitemap", "backfill": True,
         "url": "https://glucagon.com/sitemap.xml",
         "note": "His own curated repository of the incretin literature. If "
                 "no sitemap, walk from https://glucagon.com/druckerlab."},
    ],

    # ============ tier 4: recent-only feeds ============
    "Derek Lowe": [
        {"method": "feed", "backfill": False,
         "url": "https://www.science.org/blogs/pipeline/feed",
         "note": "Recent window only. Good for keeping current, useless for "
                 "the 20-year backfill."},
        {"method": "manual", "backfill": True,
         "url": "http://corante.com/pipeline/",
         "note": "ARCHIVE SPANS THREE HOSTS. 2002-~2012 at corante.com, "
                 "~2012-2021 at blogs.sciencemag.org/pipeline/archives/"
                 "YYYY/MM/DD/slug, 2021-present at science.org/blogs/pipeline. "
                 "Crawling only science.org silently loses the first decade. "
                 "Corante is defunct - go via the Wayback Machine CDX API: "
                 "http://web.archive.org/cdx/search/cdx?url=corante.com/pipeline*"
                 "&output=json&collapse=urlkey . Same trick for the sciencemag "
                 "years. AAAS terms restrict systematic downloading of "
                 "science.org; the Wayback copies are the defensible route and "
                 "cover most of it."},
    ],
    "David Grainger": [
        {"method": "manual", "backfill": True,
         "url": "https://www.forbes.com/sites/davidgrainger/",
         "note": "Forbes blocks automated access. The older DrugBaron archive "
                 "is the better target and is probably only on the Wayback "
                 "Machine - try the CDX API for drugbaron.com."},
    ],

    # ============ tier 5: papers, via real APIs ============
    "_all_papers": [
        {"method": "api", "backfill": True,
         "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
         "note": "Europe PMC. No key needed. Query AUTH:\"Lowe D\" etc, and "
                 "resultType=core for abstracts. Open-access full text at "
                 "/{source}/{id}/fullTextXML. The correct tool for the paper "
                 "half of this corpus - do not scrape publisher sites."},
        {"method": "api", "backfill": True,
         "url": "https://api.openalex.org/works",
         "note": "Author disambiguation and OA locations. filter="
                 "author.id:AXXXX. Resolve each person to an OpenAlex author "
                 "ID once, then everything else is mechanical."},
        {"method": "api", "backfill": True,
         "url": "https://api.crossref.org/works",
         "note": "DOI metadata, and licence info that tells you what you may "
                 "redistribute."},
    ],

    # ============ tier 6: lectures ============
    "_nobel": [
        {"method": "sitemap", "backfill": True,
         "url": "https://www.nobelprize.org/sitemap.xml",
         "note": "12 Grade A laureates. Pattern confirmed across seven prize "
                 "years: /prizes/<medicine|chemistry>/<year>/<surname>/"
                 "{lecture,interview,podcast,biographical,facts}/ . Full "
                 "lecture PDFs at /uploads/<year>/<month>/<surname>-lecture.pdf "
                 "- fetch those, not the HTML."},
    ],
    "_videocast": [
        {"method": "media", "backfill": True,
         "url": "https://videocast.nih.gov",
         "note": "NIH lectures, downloadable. Shokat, Rosenberg, Baker "
                 "confirmed. Public-domain US government work in most cases."},
    ],
    "_youtube": [
        {"method": "media", "backfill": True,
         "url": "yt-dlp",
         "note": "yt-dlp --write-auto-sub --sub-lang en --skip-download for "
                 "transcripts without video. Auto-captions are messy on "
                 "chemical names - budget for cleanup. Check YouTube terms "
                 "for your use."},
    ],
}


PER_PERSON_MANUAL = {
    "Paul Janssen": "Janssen Pharmaceutica archive, Beerse. Not online.",
    "Carl Djerassi": "Djerassi papers SC0348, Stanford Special Collections.",
    "Solomon Snyder": "SfN autobiography chapter is a free PDF and IS "
                      "ingestible; the Hopkins donated collection is not.",
    "Joseph L. Goldstein": "Annual Nature Medicine Lasker essays, ~2000-. "
                           "Paywalled, not indexed as a series.",
}


def summary():
    from collections import Counter
    c = Counter()
    for entries in TARGETS.values():
        for e in entries:
            c[(e["method"], e.get("backfill", False))] += 1
    return c


if __name__ == "__main__":
    for (method, backfill), n in sorted(summary().items()):
        print(f"{method:9} backfill={str(backfill):5} {n}")

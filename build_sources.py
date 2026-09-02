"""Merge sources/batch*.json into sources.json and a readable sources.md.

Source records were gathered by web search, one pass per Grade A person.
Confidence values:
  verified   - the URL appeared in search results as a real address
  constructed- built from a URL pattern confirmed for other people, then
               cross-checked by a search that returned the same address
  partial    - person resolved, but the best artifacts are named rather
               than linked; needs a second pass
"""

import glob
import json
import pathlib

from discoverers import PEOPLE

HERE = pathlib.Path(__file__).parent

# Cross-cutting venues that carry many people at once. Worth crawling as
# venues rather than person by person.
HUBS = [
    {"name": "NobelPrize.org laureate pages",
     "pattern": "nobelprize.org/prizes/<medicine|chemistry>/<year>/<surname>/"
                "{lecture,interview,podcast,biographical,facts}/",
     "note": "Four to five artifacts per laureate on a fixed URL pattern, "
             "confirmed across 1985/1988/1990/2018/2019/2023/2024. Full "
             "lecture PDFs also sit at nobelprize.org/uploads/<year>/<month>/"
             "<surname>-lecture.pdf. 12 Grade A people and ~12 more in the "
             "wider roster. The single cheapest bulk source in the project.",
     "covers": ["Elion", "Black", "Corey", "Kaelin", "Kariko", "Weissman",
                "Brown", "Goldstein", "Baker", "Jumper", "Winter", "Allison"]},
    {"name": "Eric Topol, Ground Truths (Substack)",
     "pattern": "erictopol.substack.com",
     "note": "Long-form interviews, transcribed, with a working scientist "
             "asking the questions. Already found for Kariko, Knudsen, Urnov, "
             "Liu and Drucker. Search the archive for the rest of the roster "
             "before doing anything else - it is one feed, many people.",
     "covers": ["Kariko", "Knudsen", "Urnov", "Liu", "Drucker"]},
    {"name": "NIH VideoCast",
     "pattern": "videocast.nih.gov",
     "note": "Downloadable lecture video with a stable archive: NIH "
             "Director's WALS lectures and NCI symposia. Found for Shokat, "
             "Rosenberg and Baker; Graham and Folkman are likely there too.",
     "covers": ["Shokat", "Rosenberg", "Baker", "Graham?", "Folkman?"]},
    {"name": "Lasker Foundation award essays",
     "pattern": "laskerfoundation.org/winners/...",
     "note": "Each award carries a first-person essay, often published in "
             "Cell or JCI. Sofia's 'Enter Sofosbuvir' is the model: a full "
             "design narrative, free PDF. Found for Sofia, Druker, "
             "Negulescu, Brown/Goldstein, Knudsen.",
     "covers": ["Sofia", "Druker", "Negulescu", "Brown", "Goldstein", "Knudsen"]},
    {"name": "JCI 'A conversation with ...' series",
     "pattern": "jci.org/articles/view/<id>",
     "note": "Long interview plus video, in a consistent house format. Found "
             "for Vagelos, Hobbs and Drucker; the series covers many more.",
     "covers": ["Vagelos", "Hobbs", "Drucker"]},
    {"name": "SfN History of Neuroscience in Autobiography",
     "pattern": "sfn.org/.../TheHistoryofNeuroscience/Volume-N/cNN.pdf",
     "note": "Full first-person career accounts as free PDFs. Snyder is in "
             "volume 6. Check the whole series for CNS people.",
     "covers": ["Snyder"]},
    {"name": "Science History Institute oral histories",
     "pattern": "sciencehistory.org",
     "note": "Oral-history-grade long interviews with chemists. Confirmed "
             "for Langer. The obvious place to chase Elion, Djerassi, "
             "Lipinski and other historical med chemists.",
     "covers": ["Langer", "Elion?", "Djerassi?", "Lipinski?"]},
]

# Sources that are not on the web and need a different approach.
OFFLINE = [
    {"who": "Paul Janssen",
     "what": "Janssen Pharmaceutica archive, Beerse (Belgium): archives, a "
             "series of interviews, company publications, and 'Historical "
             "Record of Janssen Research Publications (1952-1990)'.",
     "why": "850+ papers, 500+ presentations, 80+ medicines by one person. "
            "Not online; needs a direct request to the company archive."},
    {"who": "Carl Djerassi",
     "what": "Carl Djerassi papers (SC0348), Stanford Special Collections, "
             "1952-2014.",
     "why": "Finding aid is online; the material is not."},
    {"who": "Solomon Snyder",
     "what": "Authored-works collection donated to the Johns Hopkins "
             "Historical Collection on his 2022 retirement.",
     "why": "Complements the SfN autobiography chapter, which is online."},
    {"who": "Joseph Goldstein",
     "what": "Annual Nature Medicine essay series accompanying the Lasker "
             "Awards, ~2000-present, on creativity and taste in science.",
     "why": "Behind a publisher paywall and not indexed as a series. One of "
            "the best explicit statements of scientific judgement anywhere "
            "in this corpus - worth the effort to assemble in full."},
]


def load_records():
    merged = {}
    for f in sorted(glob.glob(str(HERE / "sources" / "batch*.json"))):
        merged.update(json.load(open(f)))
    return merged


def main():
    records = load_records()
    grade_a = [p for p in PEOPLE if p.richness == "A"]
    by_name = {p.name: p for p in grade_a}

    missing = [p.name for p in grade_a if p.name not in records]
    extra = [n for n in records if n not in by_name]

    out = {
        "generated_for": "Grade A subset of the drug-discoverer roster",
        "people_total": len(PEOPLE),
        "grade_a_total": len(grade_a),
        "with_sources": len([n for n in records if n in by_name]),
        "hubs": HUBS,
        "offline_targets": OFFLINE,
        "people": {},
    }
    for p in grade_a:
        rec = dict(records.get(p.name, {}))
        rec["category"] = p.category
        rec["known_for"] = p.known_for
        out["people"][p.name] = rec

    (HERE / "sources.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

    # ---- readable manifest ----
    lines = [
        "# Source manifest — Grade A",
        "",
        f"Concrete, checked sources for the {len(grade_a)} Grade A people in the "
        "roster. Generated from `sources/batch*.json` by `build_sources.py`; "
        "do not edit by hand.",
        "",
        "`confidence`: **verified** — the address appeared in search results · "
        "**constructed** — built from a URL pattern confirmed for other people "
        "and cross-checked by search · **partial** — person resolved, best "
        "artifacts named rather than linked.",
        "",
        "> Link-checking by direct fetch is blocked by this session's network "
        "egress policy (403 on CONNECT for nobelprize.org, apple podcasts and "
        "others). Every address here comes from a search result or a confirmed "
        "pattern, not from a successful fetch. `sources/check_links.py` will "
        "verify the whole set in one pass when run from an unrestricted network.",
        "",
        "## Crawl these venues, not just these people",
        "",
        "The highest-leverage move is to harvest a few venues that carry many "
        "people at once, before going person by person.",
        "",
    ]
    for h in HUBS:
        lines += [f"### {h['name']}", "",
                  f"`{h['pattern']}`", "",
                  h["note"], "",
                  "Covers here: " + ", ".join(h["covers"]), ""]

    lines += ["## Not on the web", "",
              "Four targets that need a request, a library, or a subscription "
              "rather than a crawler.", ""]
    for o in OFFLINE:
        lines += [f"**{o['who']}** — {o['what']}", "", f"*{o['why']}*", ""]

    lines += ["## People", ""]
    for cat in ["commentary", "foundational", "medchem", "oncology", "biologics",
                "genetic_medicine", "antiviral", "metabolic_cv", "cns",
                "computational", "strategy"]:
        group = [p for p in grade_a if p.category == cat]
        if not group:
            continue
        lines += [f"### {cat.replace('_', ' ').title()}", ""]
        for p in group:
            rec = records.get(p.name, {})
            conf = rec.get("confidence", "none")
            lines += [f"#### {p.name}  `{conf}`", "", f"{p.known_for}", ""]
            for key, val in rec.items():
                if key in ("notes", "confidence"):
                    continue
                if isinstance(val, str) and val.startswith("http"):
                    lines.append(f"- **{key}** — <{val}>")
                elif isinstance(val, list):
                    for v in val:
                        lines.append(f"- **{key}** — {v}")
                else:
                    lines.append(f"- **{key}** — {val}")
            if rec.get("notes"):
                lines += ["", f"> {rec['notes']}"]
            lines.append("")

    (HERE / "sources.md").write_text("\n".join(lines), encoding="utf-8")

    url_count = sum(
        1 for r in records.values() for v in r.values()
        if isinstance(v, str) and v.startswith("http"))
    print(f"grade A: {len(grade_a)} | with sources: {out['with_sources']} | "
          f"URLs: {url_count}")
    if missing:
        print("MISSING:", missing)
    if extra:
        print("EXTRA (name mismatch):", extra)


if __name__ == "__main__":
    main()

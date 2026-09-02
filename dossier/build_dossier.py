#!/usr/bin/env python3
"""Turn the persona question bank into an indication-dossier spine.

The question bank is the table of contents. Gates run first, cheapest
disqualifying question first, so a dead indication stops early instead of
generating forty pages. Everything else becomes a dossier section with a
research task attached.

    python dossier/build_dossier.py --indication "AATD (PiZZ) liver disease" \
        --tags genetic-medicine --out dossier/out/aatd.md

This emits the SPINE — questions, where to look, and what absence of
evidence would mean. It deliberately does not invent findings. Filling it is
the next stage, and each section carries the evidence slots that stage writes.
"""

import argparse
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).parent

CONFIDENCE = "`[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`"


def load():
    return yaml.safe_load((HERE / "questions.yaml").read_text())


def norm(tag):
    return tag.strip().lower().replace("_", " ").replace("-", " ")


def close(tags, tree):
    """Close a tag set over the taxonomy in both directions.

    Naming a parent pulls in its children; naming a child pulls in its
    parents. Without this, `--tags genetic-medicine` silently misses a card
    tagged `gene therapy`, and the dossier loses a section with no warning —
    the worst possible failure for a document whose job is coverage.
    """
    kids = {norm(k): {norm(v) for v in vs} for k, vs in (tree or {}).items()}
    parents = {c: p for p, cs in kids.items() for c in cs}
    out = set()
    for t in (norm(x) for x in tags):
        out.add(t)
        out |= kids.get(t, set())
        while t in parents:
            t = parents[t]
            out.add(t)
    return out


def fires(card, tags, tree):
    """A card with no `fires_when` is universal; otherwise tags must overlap."""
    fw = card.get("fires_when")
    if not fw:
        return True
    return bool(close(fw, tree) & close(tags, tree))


def render_card(card, n):
    L = [f"#### {n}. {card['question'].strip()}", ""]
    L.append(f"*{card['persona']}* — {card.get('principle', '').strip()}".rstrip(" —"))
    L.append("")
    if card.get("evidence"):
        L.append("**Where to look**")
        for e in card["evidence"]:
            L.append(f"- [ ] {e}")
        L.append("")
    if card.get("good_evidence"):
        L += [f"**What would count**  \n{card['good_evidence'].strip()}", ""]
    if card.get("absence_means"):
        L += [f"**If nothing is found**  \n{card['absence_means'].strip()}", ""]
    if card.get("weak_answer_tells"):
        L.append("**Weak-answer tells**")
        for w in card["weak_answer_tells"]:
            L.append(f"- {w}")
        L.append("")
    L += ["**Finding** — _to fill_", "",
          "**Evidence** — _cite or state that none was found_", "",
          f"**Confidence** — {CONFIDENCE}", "",
          f"<sub>source: {card['source']}</sub>", "", "---", ""]
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--indication", required=True)
    ap.add_argument("--tags", nargs="*", default=[],
                    help="modality/area tags, e.g. oncology antibacterial "
                         "gene-therapy cell-therapy antiviral genetic-medicine")
    ap.add_argument("--out", type=pathlib.Path)
    args = ap.parse_args()

    bank = load()
    tree = bank.get("tag_tree", {})
    cards = [c for c in bank["cards"] if fires(c, args.tags, tree)]
    dims = bank["dimensions"]

    gates = sorted([c for c in cards if "gate" in c], key=lambda c: c["gate"])
    body = [c for c in cards if "gate" not in c]
    dropped = len(bank["cards"]) - len(cards)

    L = [f"# Indication dossier — {args.indication}", "",
         f"Spine generated from the persona question bank "
         f"(v{bank['meta']['version']}). "
         f"{len(cards)} questions fire for tags: "
         f"{', '.join(args.tags) or 'none given'}"
         + (f"; {dropped} modality-specific questions not applicable." if dropped else "."),
         "",
         "> Personas are reconstructions from public writing, not the people "
         "themselves. Each question carries its source so the attribution can "
         "be checked.", "",
         "## How to use this", "",
         "Work the gates in order. A gate answered badly stops the dossier — "
         "that is the point of the ordering, and abandoning early is a "
         "successful outcome, not a failed one. Only then fill the body.", "",
         "**Absence of evidence is a finding.** Where nothing exists, write "
         "that, and carry it to the gap register. Do not pad.", "",
         "---", "",
         "## Part 1 — Kill gates", "",
         f"{len(gates)} questions. Answer in order.", ""]

    i = 0
    for gate_no in sorted({c["gate"] for c in gates}):
        in_gate = [c for c in gates if c["gate"] == gate_no]
        L += [f"### Gate {gate_no} · {dims[in_gate[0]['dimension']]}", ""]
        for c in in_gate:
            i += 1
            L += render_card(c, i)

    L += ["## Part 2 — Dossier body", ""]
    n = len(gates)
    for key, title in dims.items():
        group = [c for c in body if c["dimension"] == key]
        if not group:
            continue
        L += [f"### {title}", ""]
        for c in group:
            n += 1
            L += render_card(c, n)

    L += ["## Part 3 — Summary", "",
          "### What must all be true", "",
          "| # | Claim the program depends on | Confidence | Weakest? |",
          "| --- | --- | --- | --- |",
          "| 1 | _fill from the gates_ |  |  |", "",
          "The program's probability is bounded by its weakest link, not by "
          "the average (Pangalos, 5R as a conjunction).", "",
          "### Gap register", "",
          "| Question | What is missing | Cheapest way to close it | Cost |",
          "| --- | --- | --- | --- |",
          "|  |  |  |  |", "",
          "### Cheapest killer experiment", "",
          "_If no experiment could kill this, the dossier is advocacy "
          "(Booth/Munos)._", ""]

    text = "\n".join(L)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text)
        print(f"{len(cards)} questions ({len(gates)} gates, {len(body)} body) "
              f"-> {args.out}")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()

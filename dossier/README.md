# Dossier mode

The persona question bank, used as a **research agenda** rather than a critique.
The questions are the table of contents; answering them is the work.

- [`questions.yaml`](questions.yaml) — the bank. 33 cards, 31 personas, 10 dimensions, 5 kill gates.
- [`build_dossier.py`](build_dossier.py) — renders a dossier spine for an indication.
- [`out/`](out) — worked examples.

```bash
python dossier/build_dossier.py \
  --indication "Alpha-1 antitrypsin deficiency (PiZZ), liver disease" \
  --tags genetic-medicine --out dossier/out/aatd-pizz.md
```

## What makes a card a research task rather than a slogan

Four fields do the work:

| Field | Why it exists |
| --- | --- |
| `evidence` | Named databases and venues. Turns a question into a lookup. |
| `good_evidence` | What would actually settle it, so "we looked" isn't the answer. |
| `absence_means` | **The most important field.** In a dossier, "nobody has measured this" is often the decision. Generated dossiers pad over holes; this forces the hole into the text. |
| `weak_answer_tells` | Carried over from grilling mode — catches a section that reads complete but isn't. |

Plus `persona` and `source`, both required. An unattributed card is a generic
checklist item and should be deleted — the provenance is the whole point.

## Kill gates

Gates run first, in order, cheapest disqualifying question first:

1. **Causal** — is there human genetic evidence with the right direction of effect? (Plenge, Hobbs)
2. **Precedent** — has this been tried, and do we know *why* it failed rather than *that* it failed? (Lowe, Edwards/Bountra)
3. **Tractability** — which modality can engage this, delivered to which tissue? (Hopkins, Cullis)
4. **Models** — does anything preclinical predict? (Scannell)
5. **Endpoints** — is there an endpoint we can move and measure in a feasible trial? (Pangalos)

Abandoning at a gate is a **successful** outcome. The ordering exists so a dead
indication costs a day instead of a quarter.

## Tag taxonomy

`fires_when` gates modality-specific cards. Tags close over `tag_tree` in both
directions, so `--tags genetic-medicine` fires cards tagged `gene therapy`, and
`--tags antibacterial` fires cards tagged `anti-infective`. Without that closure
a dossier silently loses a section — the worst failure mode for a document whose
job is coverage. Tested in the tag cases at the bottom of the build script's
development notes.

## Status and honest limits

**v0 is hand-built from the Grade A source manifest, before any crawling.** It
is a schema test, not the finished bank. Two things it is not:

- **Not complete.** 33 cards across 10 dimensions is a skeleton. The extraction
  pass over the real corpus should produce several hundred, and will populate
  dimensions that are thin here (execution has 2 cards; competition has 2).
- **Not the people.** Personas are reconstructions from public writing. Every
  card carries a source so any attribution can be checked and corrected.

## What this changed about the corpus plan

Dossier mode re-ranks the 61 Grade A people. The ones who **wrote up their
method as a method** — Pangalos, Plenge, Scannell, Lipinski, Hopkins, Workman,
Baell, Erlanson, Silver, Kaelin — are worth several times the ones who merely
did great work, because their output generalises to indications they never
touched. That ~15-person subset should be crawled first and deepest.

Second re-rank: first-person program narratives (Sofia, Knudsen, Endo,
Negulescu) are worked examples of dossier construction — they show what evidence
was gathered and in what order.

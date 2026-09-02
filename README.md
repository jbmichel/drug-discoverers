# Drug discoverers

A roster of great drug discoverers, assembled as the seed for an artifact corpus
(papers, blogs, talks, interviews, podcasts, oral histories) intended for
training a model on **how these people reason**, not just what they found.

- [`discoverers.py`](discoverers.py) — source of truth. Edit this.
- [`discoverers.csv`](discoverers.csv) — generated, machine-readable.
- [`discoverers.md`](discoverers.md) — generated, human-readable, grouped by category.

Regenerate with `python discoverers.py`.

Currently **120 people** across 11 categories.

## The selection criterion

Two things were traded off for every entry:

1. **Discovery greatness** — did this person cause a drug to exist, or change how
   drugs get found?
2. **Artifact density** — is their *reasoning* recoverable from public sources?

The second criterion matters more than it first appears. Plenty of great drug
hunters left behind only patents and terse J. Med. Chem. papers, which record
what was made but not why. The list is deliberately weighted toward people who
externalised their thinking: bloggers, prolific reviewers, Nobel lecturers,
oral-history subjects, and podcast regulars.

Each entry carries a `richness` grade:

| Grade | Meaning | Count |
| :---: | --- | ---: |
| **A** | Large corpus of explicit reasoning — blog, podcast, lecture series, first-person case histories | 61 |
| **B** | Talks, review/perspective papers, interviews | 56 |
| **C** | Mostly primary papers, patents, third-party profiles | 3 |

Also graded by `status`: `active` (82, still producing artifacts), `emeritus`
(19, corpus mostly retrospective), `historical` (19, corpus fixed and complete).

## Categories

| Category | n | What it contributes to the corpus |
| --- | ---: | --- |
| Meta-reasoners and commentators | 12 | Highest reasoning-per-token in the list. Derek Lowe's starting example lives here |
| Foundational figures | 14 | The canon. Nobel lectures and memoirs where the logic is stated outright |
| Small-molecule drug hunters | 21 | Working med-chem judgement: property reasoning, series decisions, when to kill |
| Oncology and chemical biology | 17 | Target-selection courage, resistance-first design, new modalities |
| Biologics, immuno-oncology, cell therapy | 12 | Platform-creation reasoning |
| Genetic medicines, nucleic acids, delivery | 13 | Modality invention against a decade of skepticism |
| Antivirals | 6 | Prodrug and resistance strategy — unusually crisp design logic |
| Metabolic and cardiovascular | 10 | Human-genetics-driven target validation; peptide engineering |
| CNS | 4 | The hardest attrition problem; candid post-mortems |
| Computation, structure, AI | 5 | Method-validity reasoning |
| R&D strategy and open science | 6 | How discovery *organisations* decide |

## Suggested order for gathering artifacts

Not all sources are worth crawling first. Rough priority:

1. **The living bloggers.** Derek Lowe, Bruce Booth, Pat Walters, Robert Plenge,
   Dan Erlanson, Mohammed AlQuraishi, Greg Landrum, David Grainger, Drug Hunter.
   Thousands of posts of dated, argued, sometimes-wrong-and-later-corrected
   reasoning. This is the densest material available anywhere and it is the
   closest thing to a reasoning trace the field produces.
2. **Nobel and prize lectures.** Nobel, Lasker, Breakthrough, ACS/RSC award
   addresses. These are the format where a discoverer is explicitly asked to
   reconstruct their reasoning chain. Nearly free to collect and unusually clean.
3. **Oral histories.** The Science History Institute and similar archives hold
   long interviews with med chemists that no other source replicates.
4. **Discovery case-history papers.** J. Med. Chem. "Discovery of \<compound\>"
   papers, ACS *Drug Annotations*, and *Nature Reviews Drug Discovery* case
   histories. These narrate SAR decisions, dead ends, and go/no-go calls with
   the compounds attached — the highest-value structured reasoning in the
   literature.
5. **Long-form podcasts and seminar recordings.** Transcribe. Interviewers push
   for counterfactuals ("why didn't you kill it?") that written sources omit.
6. **Books and memoirs.** Vagelos, Rosenberg, Kariko, Djerassi, Snyder, Cullis.
7. **Primary papers and patents.** Necessary for grounding, but poor reasoning
   signal per token — patents in particular are written to obscure judgement.

Two things worth capturing that aren't a person: the **Drug Hunter** archive and
the **In the Pipeline** comment threads, where practising chemists argue with
each other about live programs.

## What is deliberately not here

- **Pure investors, journalists and analysts.** They reason well about drug
  discovery but from outside it. Adam Feuerstein, Jacob Plieth and Brad Loncar
  would be a separate, useful corpus.
- **Regulators.** Janet Woodcock, Richard Pazdur and Robert Califf reason
  publicly and rigorously about evidence, but about approval rather than
  discovery. Also a good separate corpus.
- **Process chemists and CMC leaders.** A real gap — the discipline has strong
  public reasoning (Org. Process Res. Dev. is full of it) and no one from it made
  this cut.
- **Living-but-quiet industrial chemists.** Many of the best drug hunters of the
  last 30 years published almost nothing under their own name. They are
  irrecoverable by design.

## Bench — next tier to consider

About 75 names considered and held back, mostly on artifact density rather than
merit. Add by appending to `PEOPLE` in `discoverers.py`.

Jay Keasling · Kim Lewis · Paul Hergenrother · Elizabeth Winzeler · Timothy Wells ·
Bernard Pecoul · Chi-Huey Wong · Carolyn Bertozzi · K. Barry Sharpless ·
David MacMillan · Tim Cernak · Connor Coley · Regina Barzilay · Marwin Segler ·
Alan Aspuru-Guzik · Demis Hassabis · Brian Kobilka · Robert Lefkowitz ·
Raymond Stevens · James A. Wells · Michelle Arkin · Robert Abel ·
William Jorgensen · Ozlem Tureci · Sarah Gilbert · Jason McLellan ·
Kizzmekia Corbett · Derrick Rossi · Jennifer Doudna · Feng Zhang ·
James M. Wilson · John Maraganore · Guangping Gao · Zelig Eshhar ·
Sir Ravinder Maini · Tadamitsu Kishimoto · Charles Dinarello · John O'Shea ·
Matthias Tschop · Douglas Melton · Dennis Selkoe · Michel Goedert ·
Bart De Strooper · John Krystal · Roland Griffiths · David Nutt ·
Hal Barron · Levi Garraway · Aviv Regev · Mikael Dolsten · Peter Kolchinsky ·
Andrew Lo · Frank David · Michael Gilman · Louis Lasagna · Julius Axelrod ·
Percy Julian · Gregory Pincus · Jerome Horwitz · Samuel Broder · Irving Sigal ·
Joseph Vacca · John C. Martin · Bernard Belleau · Nabil Seidah ·
Joel Habener · Joseph Schlessinger · Tony Hunter · Lewis Cantley ·
Nicola Curtin · Chris Abell · Wendy Young · Stephen Frye · Fred Van Goor

## Source gathering — Grade A

All 120 are accepted (triage stopped a third of the way in and the rest were
taken wholesale; verdicts live in the artifact's store at `triage/verdicts`).

The first artifact-gathering pass covers the **61 Grade A people** — one
targeted web search each, findings recorded per person.

- [`sources/batch*.json`](sources) — raw findings, source of truth. Edit these.
- [`build_sources.py`](build_sources.py) — merges them into the two files below.
- [`sources.json`](sources.json) — machine-readable manifest.
- [`sources.md`](sources.md) — readable manifest, grouped by category.
- [`sources/check_links.py`](sources/check_links.py) — bulk link checker.

**Coverage: 61/61 people, 282 URLs, median 5 per person.** Confidence: 51
verified (address seen in a search result), 5 constructed from a confirmed URL
pattern and cross-checked by search, 5 partial (person resolved, best artifacts
named rather than linked).

### Crawl venues before people

The biggest finding of this pass is that a handful of venues carry many people
at once, and harvesting those first is far cheaper than going name by name:

| Venue | Why it matters |
| --- | --- |
| **NobelPrize.org** | Fixed URL pattern `/prizes/<cat>/<year>/<surname>/{lecture,interview,podcast,biographical}/`, confirmed across seven prize years. Four to five artifacts per laureate, plus full lecture PDFs under `/uploads/`. 12 Grade A people, ~12 more in the wider roster. |
| **Eric Topol, Ground Truths** | Long-form transcribed interviews by a working scientist. Already hit for Karikó, Knudsen, Urnov, Liu and Drucker off five separate searches — one feed, many people. |
| **NIH VideoCast** | Downloadable lecture video with a stable archive. Shokat, Rosenberg, Baker confirmed. |
| **Lasker award essays** | Each award carries a first-person essay, often in *Cell* or *JCI*. Sofia's "Enter Sofosbuvir" is the model — a complete design narrative as a free PDF. |
| **JCI "A conversation with…"** | Long interview plus video in a consistent house format. |
| **SfN History of Neuroscience in Autobiography** | Full first-person career accounts, free PDFs. |

### Things worth knowing from this pass

- **Paul Workman does run a blog** — "The Drug Discoverer" at the ICR. That plus
  the Chemical Probes Portal makes him the closest thing to a Derek Lowe
  operating inside an academic drug discovery unit.
- **Daniel Drucker's glucagon.com** has been the incretin field's curated
  repository for years — his own archive of the foundational literature.
- **Joseph Goldstein has written an annual *Nature Medicine* essay** for the
  Lasker Awards since ~2000, on what makes an experiment elegant. Paywalled and
  not indexed as a series; worth assembling by hand.
- **Michael Sofia's "Enter Sofosbuvir"** and **Lotte Bjerre Knudsen's
  "Inventing Liraglutide"** are first-person invention accounts with the design
  logic laid out step by step. These are the format to look for everywhere else.
- **Four targets are not on the web at all** — the Janssen Pharmaceutica archive
  in Beerse (850+ papers, 500+ presentations, an interview series), the Djerassi
  papers at Stanford, Snyder's donated collection at Hopkins, and the Goldstein
  essay series. `sources.md` lists what each needs.

### Two corrections to the roster

- **Carl June**: no memoir of his own could be found. The book-length account is
  the 2022 documentary *Of Medicine and Miracles* plus third-party coverage.
- **Pieter Cullis**: the roster credits him with a book on the LNP story; that
  could not be confirmed. His *Nature Reviews Materials* narrative review
  "From lipids to lipid nanoparticles to mRNA vaccines" is the real artifact.

## Caveats on the data

- `url` is filled only where the address was verified (9 entries). Everything
  else is a **crawl instruction**, not a link — the `where` column says what to
  go find, and resolving those to URLs is the obvious next pass.
- `known_for` is a one-line compression of a career and attributes a discovery to
  one person that in every case involved a team. Treat it as an index key, not a
  credit assignment. Several entries name collaborators in `where` for that
  reason (Kohler with Milstein, Tureci with Sahin, Zartler with Erlanson).
- Category boundaries are for corpus organisation, not biography. Kaelin is
  filed under oncology though half his value here is his writing on rigour.

# Indication dossier — Gram-negative bacteraemia

Spine generated from the persona question bank (v0). 31 questions fire for tags: antibacterial; 2 modality-specific questions not applicable.

> Personas are reconstructions from public writing, not the people themselves. Each question carries its source so the attribution can be checked.

## How to use this

Work the gates in order. A gate answered badly stops the dossier — that is the point of the ordering, and abandoning early is a successful outcome, not a failed one. Only then fill the body.

**Absence of evidence is a finding.** Where nothing exists, write that, and carry it to the gap register. Do not pad.

---

## Part 1 — Kill gates

7 questions. Answer in order.

### Gate 1 · Causal human biology — is the mechanism real in people?

#### 1. Is there a human loss-of-function (or gain-of-function) phenotype whose direction of effect matches what the drug is meant to do?

*Robert Plenge* — Human genetics is the only target-validation evidence that is already in the right species. Direction of effect matters as much as association.

**Where to look**
- [ ] gnomAD
- [ ] Open Targets Genetics
- [ ] UK Biobank exome PheWAS
- [ ] ClinVar
- [ ] OMIM

**What would count**  
Homozygous or compound-het human LoF carriers described, with a phenotype in the intended direction, ideally an allelic series showing dose-response.

**If nothing is found**  
Not fatal, but the program is now resting on model organisms. Say so explicitly and move the burden of proof to the models section.

**Weak-answer tells**
- mouse knockout offered as the human evidence
- GWAS association with no direction of effect
- the human LoF phenotype is known, inconvenient, and unmentioned

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: plengegen.com — genetics-to-target series; NRDD target validation review</sub>

---

#### 2. Are there humans at the extremes of this phenotype, and has anyone sequenced them?

*Helen Hobbs* — Outliers carry the mechanism. The Dallas Heart Study method: find people at the tail, find what is different about them.

**Where to look**
- [ ] Dallas Heart Study
- [ ] deCODE
- [ ] UK Biobank tails
- [ ] disease registries

**What would count**  
Protective or extreme-phenotype carriers with a named variant.

**If nothing is found**  
A real gap and often a cheap one to close — an outlier-sequencing collaboration may be the highest-yield early experiment.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: JCI "A conversation with Helen Hobbs"; PCSK9/ANGPTL3 work</sub>

---

### Gate 2 · Precedent — has this been tried, and what happened?

#### 3. Has this target, or this mechanism, been taken into humans before — and if it failed, do we know why it failed rather than that it failed?

*Derek Lowe* — Most "novel" targets have a graveyard. The failure reason is usually recoverable and usually decides whether the idea is dead or just early.

**Where to look**
- [ ] ClinicalTrials.gov including terminated and withdrawn studies
- [ ] AdisInsight / Cortellis discontinued pipelines
- [ ] In the Pipeline archive
- [ ] conference abstracts that never became papers

**What would count**  
A named prior program, its phase, and a mechanistic cause of failure (exposure, safety, wrong patients, wrong endpoint) — not just "it failed".

**If nothing is found**  
Either genuinely new, or the search was too shallow. Assume the latter until a terminated-trial search has been run.

**Weak-answer tells**
- claims novelty without having searched terminated trials
- failure attributed to the company rather than the biology

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: In the Pipeline, 2002–present, failure post-mortems</sub>

---

#### 4. Who has already done this work and not published it, and can we just ask?

*Aled Edwards / Chas Bountra* — The field duplicates failed work continuously because negatives are invisible. Pre-competitive contact is cheaper than repeating it.

**Where to look**
- [ ] SGC networks
- [ ] target-specific consortia
- [ ] patent filings without papers

**If nothing is found**  
Not knowable from the literature. This is a phone-call task.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: SGC Open Science Principles; Bountra talks on duplicated failure</sub>

---

### Gate 3 · Tractability — can a molecule do this, in the right tissue?

#### 5. Given where this target sits and what it does, which modality can actually engage it — and is that modality one we can deliver to that tissue?

*Andrew Hopkins / Pieter Cullis* — Druggability is modality-relative. The question is not "is it druggable" but "druggable by what, delivered how".

**Where to look**
- [ ] structural data (PDB), pocket detection, chemical probe availability
- [ ] precedent for the modality reaching that tissue

**What would count**  
A named modality with a named delivery route and at least one precedent molecule reaching that compartment at a relevant exposure.

**If nothing is found**  
The program is a delivery program before it is a target program. Budget accordingly.

**Weak-answer tells**
- names siRNA as the modality with no answer on tissue beyond liver
- CNS target with no discussion of BBB penetrance

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Hopkins ligand efficiency / druggable genome; Cullis LNP reviews</sub>

---

### Gate 4 · Model validity — will anything preclinical predict?

#### 6. What is the predictive validity of the primary model — how well does it rank candidates against what happens in patients? Not its throughput.

*Jack Scannell* — Model validity dominates throughput in determining R&D productivity. A cheap high-throughput model with poor validity destroys value.

**Where to look**
- [ ] published concordance between this model and clinical outcome
- [ ] how many drugs that worked in this model worked in humans, and vice versa

**What would count**  
A quantified hit rate, even a poor one, with a citation.

**If nothing is found**  
Very common and rarely admitted. If unquantified, treat every preclinical readout downstream as weaker than it appears and say so in the summary.

**Weak-answer tells**
- throughput, cost per well, or compounds screened offered as the answer
- "it's the standard model in the field"

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: NRDD Eroom's Law (2012); "Predictive validity in drug discovery"</sub>

---

### Gate 5 · Endpoints — can the effect be detected in a feasible trial?

#### 7. Is there an endpoint that moves on a timescale and in a population size we can actually run — and is it accepted, or will we have to qualify it?

*Mene Pangalos ("right patient")* — The 5R framework treats patient and endpoint selection as a technical determinant of success, not a downstream clinical detail.

**Where to look**
- [ ] precedent approvals in the indication and what endpoint they used
- [ ] FDA/EMA qualified biomarkers, natural history studies

**What would count**  
A precedent approval on the endpoint, or a biomarker with a regulatory qualification path and a natural-history dataset behind it.

**If nothing is found**  
The trial is the program risk. A dossier that skips this is describing biology, not a drug program.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: NRDD 2014 and 2018 5R papers</sub>

---

## Part 2 — Dossier body

### Causal human biology — is the mechanism real in people?

#### 8. Is the thing we are modulating a brake or a pedal — and are we sure which direction of intervention produces the effect we want?

*James Allison* — CTLA-4 was assumed to be an accelerator. Recognising it as a brake is what made blockade the right intervention.

**Where to look**
- [ ] perturbation data in both directions
- [ ] human variant direction of effect

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Nobel lecture 2018; UC Berkeley CRL "Story of Yervoy"</sub>

---

#### 9. What observation would falsify this hypothesis — and are we running that experiment, or defending the hypothesis against it?

*John Hardy* — The amyloid hypothesis survived by being revised against contrary data. A hypothesis with no falsifying experiment is a commitment, not a theory.

**Where to look**
- [ ] the contrary literature
- [ ] explicitly sought

**If nothing is found**  
A red flag on the whole dossier, not on one section.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Hardy commentaries revising the amyloid cascade hypothesis</sub>

---

#### 10. If this works, what changes for patients — and is that change large enough to be worth the decade?

*Joseph Goldstein / Roy Vagelos* — Taste in problem selection. Goldstein's Lasker essays are about which questions deserve a career; Vagelos ran Merck on whether a drug was needed.

**Where to look**
- [ ] standard of care
- [ ] what patients actually get today

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Goldstein Nature Medicine Lasker essay series; Vagelos memoir</sub>

---

### Tractability — can a molecule do this, in the right tissue?

#### 11. If this is called undruggable — who decided that, when, and did they look for a cryptic or allosteric pocket, or only the orthosteric one?

*Kevan Shokat* — KRAS was undruggable until someone looked at a pocket that only opens in one mutant. "Undruggable" is usually a statement about past effort.

**Where to look**
- [ ] MD simulations
- [ ] covalent fragment screens
- [ ] allosteric site literature

**If nothing is found**  
An unexamined assumption worth an explicit re-check.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Shokat KRAS G12C switch-II work; NIH WALS lecture</sub>

---

#### 12. Has anyone got a fragment or a covalent hit on this protein, and at what ligand efficiency?

*Daniel Erlanson / Andrew Hopkins* — Fragment hit rate is an empirical readout of ligandability, available before a full screen.

**Where to look**
- [ ] published fragment screens
- [ ] Practical Fragments archive
- [ ] covalent screens

**If nothing is found**  
Untested rather than intractable — a cheap experiment.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Practical Fragments; ligand efficiency literature</sub>

---

#### 13. If occupancy-based inhibition is hard here, is this a degradation, splice modulation, or genetic-medicine problem instead?

*Craig Crews / C. Frank Bennett* — Event-driven pharmacology removes the need for a deep binding pocket; splice modulation removes the need for a pocket at all.

**Where to look**
- [ ] E3 ligase expression in target tissue
- [ ] ASO precedent
- [ ] splice-site variants

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Crews PROTAC work; Bennett/Krainer nusinersen</sub>

---

#### 14. What half-life does the biology require, and is that an achievable engineering target rather than a hope?

*Lotte Bjerre Knudsen* — Liraglutide and semaglutide were half-life engineering programs. The required PK was treated as a design objective from the start.

**Where to look**
- [ ] target turnover rate
- [ ] receptor occupancy modelling
- [ ] precedent PK

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: "Inventing Liraglutide", ACS Pharmacol Transl Sci 2019</sub>

---

#### 15. Can we make the molecule accumulate where the disease is rather than where the chemistry naturally goes?

*Michael J. Sofia* — Sofosbuvir was a liver-targeting problem solved with a phosphoramidate prodrug. Tissue targeting is a design variable, not a constraint.

**Where to look**
- [ ] tissue distribution precedent
- [ ] prodrug/conjugate strategies
- [ ] GalNAc analogues

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: "Enter Sofosbuvir: The Path to Curing HCV" (Lasker essay, Cell 2016)</sub>

---

### Model validity — will anything preclinical predict?

#### 16. Are the hits real, or are they aggregators, redox cyclers, or otherwise PAINS — and has anyone run the orthogonal assay?

*Jonathan Baell* — A large fraction of published hit matter is assay artifact. The cost of checking is trivial against the cost of not checking.

**Where to look**
- [ ] PAINS filters
- [ ] orthogonal assay format
- [ ] dose-response shape
- [ ] detergent controls

**If nothing is found**  
Treat the chemical series as unvalidated.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: J Med Chem PAINS paper; Nature "Chemistry: Chemical con artists"</sub>

---

#### 17. Is the tool compound underpinning this biology actually selective at the concentration used?

*Paul Workman* — A large body of target biology rests on poor chemical probes used above their selectivity window.

**Where to look**
- [ ] Chemical Probes Portal
- [ ] selectivity panels
- [ ] concentration used in key papers

**If nothing is found**  
The supporting biology is weaker than the citation count suggests.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: The Drug Discoverer blog (ICR); Chemical Probes Portal fitness factors</sub>

---

#### 18. For each load-bearing claim in this dossier — is it a house of brick or a mansion of straw?

*William Kaelin Jr.* — Papers have drifted toward many weakly-supported claims. Ask which single claims the program depends on, and whether each is independently solid.

**Where to look**
- [ ] replication status
- [ ] independent labs
- [ ] orthogonal methods

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: "Publish houses of brick, not mansions of straw", Nature 545:387 (2017)</sub>

---

### Patients and natural history — who exactly, progressing how?

#### 19. Do we know how untreated patients progress, quantitatively, with enough resolution to power a trial?

*Mene Pangalos ("right patient")*

**Where to look**
- [ ] natural history studies
- [ ] registries
- [ ] patient organisation datasets

**If nothing is found**  
A natural-history study may be a prerequisite deliverable and should be costed into the program, not assumed.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: 5R framework</sub>

---

#### 20. Which subset responds — and can we identify them prospectively with an assay that exists today?

*Charles Sawyers / Brian Druker* — Imatinib worked because the population was defined by the lesion. An unstratified trial in a heterogeneous population buries a real effect.

**Where to look**
- [ ] genotype-phenotype data
- [ ] companion diagnostic precedent

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Druker/Sawyers CML and prostate programs</sub>

---

#### 21. Is there an organised patient community, and have we asked them what outcome they actually want changed?

*Stanley Crooke* — n-Lorem exists because the patients defined the need. Patient organisations also hold natural-history data and trial-ready cohorts.

**Where to look**
- [ ] patient advocacy organisations
- [ ] registries
- [ ] existing natural history efforts

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: n-Lorem Foundation; Crooke's own podcast series</sub>

---

### Endpoints — can the effect be detected in a feasible trial?

#### 22. Is there a biomarker that connects target engagement to clinical benefit — and is each link in that chain evidenced separately?

*Paul Negulescu* — CF had sweat chloride: a biomarker tied to the mechanism that moved early and predicted benefit. Most indications do not, and pretend otherwise.

**Where to look**
- [ ] target engagement assay
- [ ] mechanistic biomarker
- [ ] clinical correlate

**If nothing is found**  
Every early trial becomes an outcome trial. This changes cost and duration by an order of magnitude — state it in the summary, not a footnote.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Vertex CFTR program; Lasker 2025</sub>

---

### Safety and window — what breaks, and at what exposure?

#### 23. What is the phenotype of humans who already lack this target — that is our best available safety readout, pre-clinically.

*Robert Plenge / Helen Hobbs* — Human LoF carriers are a natural safety experiment already run.

**Where to look**
- [ ] gnomAD constraint
- [ ] LoF carrier phenotypes
- [ ] PheWAS on the variant

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: genetics-for-target-validation literature</sub>

---

#### 24. Is the toxicity we should fear on-target or off-target — and if on-target, what separates therapeutic from toxic exposure?

*Derek Lowe* — On-target toxicity does not go away with a better molecule. It is a property of the idea, not the chemistry.

**Where to look**
- [ ] target expression atlas
- [ ] tissue distribution
- [ ] precedent class effects

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: In the Pipeline, recurring theme across mechanism-toxicity posts</sub>

---

#### 25. How will resistance or escape emerge, and what is the second-generation plan?

*Charles Sawyers* — Resistance is a design input, not a post-approval surprise. Four distinct enzalutamide-resistance mechanisms were mapped by the same lab.

**Where to look**
- [ ] precedent resistance in class
- [ ] mutational scanning
- [ ] relapse sequencing plans

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Sawyers resistance work, MSK</sub>

---

#### 26. For a Gram-negative target — do we have any compound series that gets in and stays in?

*Lynn Silver* — Antibacterial discovery fails at permeability and efflux more than at target biology. Screening cascades that ignore this generate dead series.

**Where to look**
- [ ] accumulation assays
- [ ] eNTRy rules
- [ ] efflux-deficient strain comparisons

**If nothing is found**  
Expect the series to fail late. Front-load the accumulation assay.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Silver, "Challenges of antibacterial discovery", Clin Microbiol Rev</sub>

---

### Competitive position — who else, and why the gap?

#### 27. Who else is working on this, how far ahead are they, and what would we have that they do not?

*Bruce Booth*

**Where to look**
- [ ] ClinicalTrials.gov
- [ ] patent landscape
- [ ] company pipelines
- [ ] conference abstracts

**Weak-answer tells**
- competitor list drawn only from press releases
- claims to be first without a patent search

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: LifeSciVC, on therapeutic crowding</sub>

---

#### 28. If this is such a good idea, why has nobody done it? Name the specific barrier, and say what changed to remove it.

*Bruce Booth / Jack Scannell* — There is usually a reason. A new enabling technology, a new dataset, or a genuine blind spot — but it should be nameable.

**If nothing is found**  
The most common failure mode in an indication dossier.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: LifeSciVC; R&D productivity literature</sub>

---

### Decision economics — what would change our mind, cheapest first

#### 29. What is the cheapest experiment that could kill this program, and why have we not run it yet?

*Bruce Booth / Bernard Munos* — Capital efficiency in early biotech is mostly about sequencing the killer experiments first rather than the encouraging ones.

**If nothing is found**  
If no experiment could kill it, the hypothesis is not falsifiable and the dossier is advocacy.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: LifeSciVC on staged investment; Munos on R&D productivity</sub>

---

#### 30. List the things that must all be true for this to work. Which is the weakest, and what is its probability?

*Mene Pangalos* — The 5R framework is a conjunction, not a scorecard. The program's probability is bounded by its weakest R.

**Where to look**
- [ ] each preceding dimension
- [ ] scored

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: NRDD 2014/2018</sub>

---

#### 31. If the field disagrees with us, is that because we are early or because we are wrong — and what evidence would distinguish those?

*Judah Folkman* — Angiogenesis was right and unpopular for two decades. The same posture also protects bad ideas, so the distinguishing evidence has to be named.

**Finding** — _to fill_

**Evidence** — _cite or state that none was found_

**Confidence** — `[ ] strong  [ ] moderate  [ ] weak  [ ] absent — see gap`

<sub>source: Folkman's angiogenesis work; "Dr. Folkman's War"</sub>

---

## Part 3 — Summary

### What must all be true

| # | Claim the program depends on | Confidence | Weakest? |
| --- | --- | --- | --- |
| 1 | _fill from the gates_ |  |  |

The program's probability is bounded by its weakest link, not by the average (Pangalos, 5R as a conjunction).

### Gap register

| Question | What is missing | Cheapest way to close it | Cost |
| --- | --- | --- | --- |
|  |  |  |  |

### Cheapest killer experiment

_If no experiment could kill this, the dossier is advocacy (Booth/Munos)._

# Decision memo — FTD-GRN (progranulin haploinsufficiency)

Dive driven by the persona question bank (`dossier/questions.yaml`, 33 cards),
gates worked in kill order. Snapshot date 2026-09-03.

**Evidence constraint, stated up front.** This session's network egress blocks
direct fetching — no PubMed, ClinicalTrials.gov, gnomAD or publisher access
(403 on CONNECT). Everything below is grounded in web *search* returns, which
give abstract- and press-release-level detail, not full text. Where I could not
retrieve a number, I say so rather than supplying one. Claims resting on model
knowledge rather than a retrieved source are labelled **[unretrieved]**. The
skill's step-1 `literature-review` skill is not synced in this environment, so
its anti-fabrication discipline was applied by hand. No PMID, NCT or figure
below was constructed from memory; identifiers appear only where a search
result carried them.

---

## Verdict

**Do not enter on target validation. The target is validated and that is no
longer the question.**

The naive form of this program — raise progranulin, slow the disease — has been
tested to completion and failed. Alector's latozinemab ran a 96-week Phase 3
(INFRONT-3, NCT04374136) that missed its clinical co-primary while *hitting* its
biomarker co-primary, raising plasma progranulin 165% over placebo at week 96,
with no treatment-related effect on any secondary or exploratory endpoint
including fluid biomarkers and volumetric MRI. Alector cut 49% of staff,
discontinued the open-label extension and the continuation study, and GSK is
leaving the alliance at the start of 2027.

That is a clean, well-powered, informative failure, and it is the single most
valuable fact available about this indication. It does not say progranulin is
the wrong target — the human genetics are close to as good as this criterion
ever gets. It says that *this route to raising progranulin, at the magnitude it
achieved, in the compartment it reached, does not change the disease.*

What remains live is a narrower and much better-specified question, and three
companies are already asking it with direct CNS delivery. Entry now is a
fast-follow into a field where a competitor has spent a Phase 3 partially
answering the biology on everyone's behalf. That can be a good trade, but only
on an explicit delivery-or-durability thesis. **Proceed to a second unit of work
only if you can state, before looking further, what your approach does that
AAV-ICM gene transfer does not.**

No criterion scored zero, so the dive did not abort.

---

## Criterion scorecard

| Criterion | Score | Reasoning |
|---|---|---|
| Causal human genetics | **3 / 3** | Allelic series with direction of effect. See Gate 1. |
| Effector feasibility (CNS delivery) | **2 / 3** | CSF progranulin elevation demonstrated by three independent modalities in humans. Durability and distribution unproven. |
| Unmet need / competition | **1 / 3** | `score_unmet_need(n_active=4, max_phase=2, n_sponsors=4, n_approved=0)` = 1. Four active programmes, four sponsors, no approval, no active Phase 3. |
| Mechanism and model validity | **1 / 3** | Models predicted target engagement and did not predict clinical benefit. See Gate 4. |
| Endpoints | **1 / 3** | An accepted clinical endpoint exists and a properly powered Phase 3 could not move it. See Gate 5. |
| Population | **adequate** | See sizing. |

Two scores of 1 (competition, endpoints) are where the adjacent score changes
the verdict. Both are escalated below rather than resolved here.

---

## The gates, in order

### Gate 1 — causal human biology (Plenge; Hobbs). **PASS, strongly.**

GRN carries a genuine allelic series in humans, which is the strongest form this
criterion takes. Heterozygous loss of function causes frontotemporal lobar
degeneration with TDP-43 inclusions. Homozygous loss of function causes a
different disease — neuronal ceroid lipofuscinosis type 11 (CLN11, OMIM #614706),
a lysosomal storage disorder presenting between roughly 13 and 25 years with
cerebellar ataxia, seizures, retinitis pigmentosa and cognitive decline. Direction
of effect is unambiguous and matches the intended intervention: less progranulin
is worse, and the therapeutic direction is to restore it.

Two refinements matter, and both cut against treating this as a simple dose
curve. First, the homozygous phenotype is not a more severe version of the
heterozygous one — retrieved sources report that homozygotes lack the TDP-43
cytoplasmic inclusions that define the heterozygous disease, described as a
pathological shift between lysosomal and TDP-43 pathologies depending on mono-
versus bi-allelic status. Second, the homozygous phenotype is itself
heterogeneous: some homozygotes present with classical childhood or juvenile
CLN11, while others present with frontotemporal dementia and parkinsonism after
age 50 with neither epilepsy nor ataxia.

Hobbs's outlier question is partly answered and partly open. The bi-allelic
patients are the phenotypic extreme and they have been sequenced and described.
What I did not find is the other tail — heterozygous carriers who are
unusually *mildly* affected or who have not converted well past the expected age.
Age at onset in heterozygous carriers spans 40 to 85, which is a very wide range
for a monogenic disease, and that spread is itself the evidence that modifiers
exist. **No evidence found** in this search pass of a systematic modifier study
on late- or non-converting carriers. If real, that is a cheap and high-value gap:
the cohorts to do it in already exist (GENFI, ALLFTD).

There is also a bridging observation that strengthens the mechanism: a *Science
Translational Medicine* paper reports that individuals with progranulin
haploinsufficiency exhibit features of neuronal ceroid lipofuscinosis — i.e. the
heterozygous human disease already carries a subclinical version of the
homozygous lysosomal pathology. That connects the two ends of the allelic series
mechanistically rather than just epidemiologically.

### Gate 2 — precedent (Lowe; Edwards/Bountra). **PASS, and this is the gate that matters.**

Lowe's question is whether we know *why* it failed rather than *that* it failed.
Here we do, to an unusual degree, because the trial was designed with a biomarker
co-primary alongside the clinical one, which means the failure is interpretable
instead of ambiguous.

INFRONT-3 (NCT04374136) was a 96-week randomised, double-blind,
placebo-controlled Phase 3 in symptomatic and at-risk FTD-GRN participants across
North America, Europe, Argentina and Asia-Pacific. Topline on 21 October 2025:
the clinical co-primary, CDR plus NACC FTLD Sum of Boxes, was not met. The
biomarker co-primary was met, with plasma progranulin 165% above placebo at week
96. Secondary and exploratory endpoints — fluid biomarkers and volumetric MRI —
showed no treatment-related effects.

The pharmacology worked. In healthy volunteers a single latozinemab infusion
reduced white-blood-cell sortilin, tripled plasma progranulin and **doubled CSF
progranulin**; in cynomolgus monkeys it raised both plasma and CSF progranulin
two- to three-fold. So this is not a simple case of a drug failing to reach the
brain. It reached the CSF and roughly doubled progranulin there, and the disease
did not respond on any measure.

That distinction is what makes the failure useful. Two hypotheses survive it, and
they have different consequences for anyone entering now.

The first is **magnitude**: a two-fold CSF elevation is simply not enough, and the
gene-therapy programmes achieving larger and more durable CSF elevations will
clear a threshold that latozinemab did not. This is the implicit thesis of the
three live programmes.

The second is **compartment and mechanism**, and it deserves to be stated
carefully because it is an inference of mine and not a retrieved finding.
Latozinemab works by blocking sortilin. Sortilin is a principal receptor for
progranulin uptake — it is one of the main routes by which extracellular
progranulin is taken into cells and delivered to the lysosome, which is where
progranulin's known functions in lysosomal biogenesis are exercised. Blocking
sortilin therefore raises measured extracellular progranulin *by the same
mechanism that reduces its delivery into cells*. On that reading, the biomarker
that was hit and the effect that was wanted are not merely different, they are in
tension: the assay measures the pool that accumulates because it is not being
taken up. If that is right, then plasma or CSF progranulin concentration is a
target-engagement marker for sortilin blockade but a poor surrogate for
intracellular progranulin sufficiency, and the trial's biomarker co-primary was
measuring the wrong thing with great precision. **[inference — I did not retrieve
a source making this argument, and it may already be in the literature or already
refuted.]**

What would settle it: whether intracellular or lysosomal progranulin rose in
latozinemab-treated patients or animals, and whether the sortilin-independent
uptake routes (prosaposin-mediated, among others) carry enough flux to compensate.
That is a specific, answerable question and it should be the first literature
search anyone entering this space runs. It also bears directly on VES001
(NCT06705192, Vesper Bio, asymptomatic GRN-FTD), which is *also* sortilin-directed
and therefore inherits the same open question.

Edwards/Bountra — who has done this and not published — is **partly answered**.
The failure itself is public, which is better than the usual case. What is not
public is the INFRONT-3 CSF progranulin data, the biomarker and vMRI datasets
behind "no treatment-related effects", and any subgroup analysis. Alector is
contracting and GSK is exiting; **this is the moment those datasets are most
gettable and least valuable to their owners.** A direct approach to Alector, and
to the Bluefield Project which has been an organising force in this field, is a
cheap action with an asymmetric payoff.

### Gate 3 — tractability and delivery (Hopkins; Cullis). **PASS.**

Three independent modalities have raised progranulin in the human CNS:

- **AVB-101** (AviadoBio), AAV delivered intrathalamically. Phase 1/2 ASPIRE-FTD,
  first patient dosed 15 April 2024; three dose-escalation cohorts complete with
  12 patients across five countries; fourth cohort initiated as of 31 March 2026;
  20 active sites. Reported dose-dependent elevations in CSF progranulin.
- **PBFT02** (Passage Bio), AAV delivered into the cisterna magna. Phase 1/2
  upliFT-D. Dose 1 (4.5e13 GC) gave durable CSF progranulin of mean 22.8 ng/mL at
  12 months and 24.2 ng/mL at 18 months; dose 2 reached comparable levels by 6
  months. Generally well tolerated with no new treatment-related SAEs reported.
- **DNL593** (Denali), a protein transport vehicle delivering progranulin itself
  across the blood-brain barrier. Phase 1/2 fully enrolled at 40 FTD-GRN
  participants, results expected by end of 2026. Part A in healthy volunteers
  showed dose-dependent CSF progranulin increases. Denali regained full rights in
  April 2026.

So the delivery question is answered in the affirmative for the *measurable*
compartment. It is not answered for distribution — whether the protein reaches
the cells and the subcellular compartment that need it, in the regions that
degenerate. That is the same gap Gate 2 opened, arriving from the other side.

### Gate 4 — model predictive validity (Scannell). **WEAK PASS — the weakest gate.**

Scannell's question is how well the primary model ranks candidates against what
happens in patients, not how much it can screen. The retrospective answer for
this indication is now available and it is poor.

The preclinical package predicted target engagement accurately: cynomolgus data
predicted the two- to three-fold CSF progranulin rise that was then observed in
humans. It did not predict clinical outcome at all. A model system that
faithfully forecasts your biomarker and not your endpoint is exactly the
configuration Scannell warns about, because it generates confidence without
generating information.

The mechanistic reason is visible in the model ecosystem. The mouse genotype that
matches the human disease is Grn+/-, and **[unretrieved]** heterozygous mice are
reported to have a mild phenotype, which is why the field works largely in Grn-/-
mice. But Grn-/- is the genotype of CLN11, not of FTD-GRN, and the human evidence
from Gate 1 says the two are pathologically distinct rather than graded — the
homozygous state does not produce the TDP-43 pathology that defines the disease
being treated. So the workhorse model is arguably a model of the sibling disease.
A GrnR493X mouse has been characterised (bioRxiv preprint, retrieved) as a
knock-in alternative.

**No evidence found** of a published quantitative concordance analysis between
any GRN model and clinical outcome. Absent that, treat every preclinical efficacy
readout in this indication as weaker than its provenance suggests, and say so in
any investment case.

### Gate 5 — endpoints (Pangalos, "right patient"). **WEAK PASS.**

The good news is that an accepted clinical endpoint exists — CDR plus NACC
FTLD-SB — which is more than many rare indications have. The bad news is that a
96-week, multi-continent, properly powered Phase 3 used it and could not move it,
and the same trial's vMRI and fluid-biomarker secondaries were also flat. When
the endpoint is accepted and the trial is adequate, a null result puts the burden
squarely back on the intervention.

The biomarker picture is more encouraging and is where the field is going.
Neurofilament light is unusually well characterised in this exact population:
GRN carriers' NfL concentrations run an order of magnitude above non-carriers a
decade before clinical onset; the presymptomatic-to-symptomatic conversion period
carries the highest rate of NfL change; GRN carriers show a higher rate of NfL
change than C9orf72 carriers; and baseline plasma NfL is highly predictive of
clinical-status change over the following two years. The Bluefield Neurofilament
Surveillance Program is measuring plasma NfL quarterly for three years in more
than 335 familial FTD mutation carriers within ALLFTD, explicitly aimed at
qualifying NfL as a Phase 3 endpoint. That is a qualification effort in progress,
not a qualified endpoint — the distinction matters for anyone planning a
registrational path today.

Against that, Passage Bio's interim upliFT-D data claim movement on precisely the
readouts latozinemab failed to move. In CDR-1 patients, whole-brain atrophy was
3.1% at 12 months versus 8.7% in ALLFTD natural history (a 64% reduction), and
frontotemporal atrophy 4.6% versus 9.9% (54%); plasma NfL changed by mean
−1.0 pg/mL at 12 months versus +13.5 pg/mL in natural history. If those hold up
they are the strongest available evidence that direct CNS delivery does something
systemic progranulin elevation did not.

Two cautions, both load-bearing. These are comparisons against **external natural
history**, not randomised controls, in a small early-phase cohort selected for
early disease — and selection on CDR-1 is exactly where regression and
ascertainment effects live. And the FDA, at a Type C meeting, told Passage Bio
that a randomised controlled registrational trial will be required, which is the
regulator making the same point. Passage Bio has begun a strategic review.

Pangalos's "right patient" question has a specific edge here that the persona
bank flags as Trap 6: the presymptomatic carrier population is the one where
intervention should work best and the one where a function-based endpoint is
hardest to power, because there is less decline available to prevent. That is
why the endpoint and the population cannot be chosen independently in this
indication.

---

## Findings that revise prior work

1. **A biomarker co-primary can be hit and be actively misleading.** The most
   transferable lesson from INFRONT-3 is not that the drug failed; it is that a
   trial can meet a mechanistically-motivated biomarker endpoint by 165% and show
   nothing on any clinical or imaging measure. If the sortilin-blockade tension
   described in Gate 2 is real, the biomarker rose partly *because* delivery to
   the site of action was blocked. Any program in this space should specify, in
   advance, a biomarker that would fall if the drug were working through the
   wrong route — not only one that rises if target engagement occurs.

2. **This indication's model ecosystem is a model of the sibling disease.** The
   heterozygous human genotype maps to a mouse with little phenotype; the mouse
   with the phenotype is homozygous, and the human homozygous state is
   pathologically distinct from the disease under treatment. That is a specific,
   nameable predictive-validity defect rather than a general complaint about
   mice.

3. **The competition criterion behaved as the skill predicts.** Running it early
   changed the shape of the whole dive: it converted the question from "is
   progranulin a good target" (yes, and irrelevant) to "what does your delivery
   do that ICM AAV does not". Had it run last, the first four sections would have
   been written against the wrong question.

---

## Where the opportunity is

Three narrow positions survive the gates. None of them is "raise progranulin".

**The dose-response question nobody has published.** Gate 1 gives a human allelic
series and Gate 3 gives three modalities producing different CSF progranulin
magnitudes. Nobody appears to have written down how much progranulin, in which
compartment, is enough — the quantitative dose-response the skill demands under
"read, do not count". Latozinemab's ~2x CSF elevation failed; PBFT02's larger
elevation shows biomarker movement. The threshold, if there is one, sits between
them, and it is currently being established accidentally and expensively by three
companies who each have one data point. Assembling that curve is cheap relative
to its value.

**The uptake-route question.** If sortilin blockade raises extracellular
progranulin while impairing lysosomal delivery, then approaches that increase
progranulin *production* or *lysosomal delivery* are mechanistically distinct
from approaches that block clearance, and the Phase 3 failure does not read
across to them. That distinction is worth resolving before anything else, because
it determines whether one failed trial invalidates one company's molecule or a
whole modality class — including VES001, which is also sortilin-directed.

**The stranded dataset.** Alector has the CSF progranulin, fluid-biomarker and
vMRI datasets from a completed 96-week randomised Phase 3 in exactly this
population, is contracting sharply, and is losing its partner. That data would
answer the magnitude question directly. This is the Edwards/Bountra card paying
out: the most valuable thing in the field right now is a negative dataset whose
owner has stopped needing it.

---

## Sizing

GRN-related frontotemporal lobar degeneration is reported at **3 to 15 per
100,000 people aged 45 to 64**, and GRN accounts for roughly **20% of familial
FTD**. Age at onset in heterozygous carriers spans 40 to 85.

I have deliberately not multiplied these into a patient count. The skill's Trap 2
warns against variant-count proxies, and there is a sharper problem here: the
prevalence figure is stated for a specific age band, the disease has a wide onset
range extending well past it, and the addressable population for an early-
intervention therapy is presymptomatic carriers rather than prevalent patients —
a different denominator entirely. A defensible number needs the patient-level
carrier frequency and the presymptomatic fraction, neither of which I could
retrieve here. **Absence recorded rather than estimated.**

What can be said: the enrolled cohorts are real and reachable. INFRONT-3 recruited
across four continents; DNL593 enrolled 40 patients; ASPIRE-FTD has 12 dosed
across 20 sites in nine countries; GENFI and ALLFTD run standing carrier cohorts,
and the Bluefield surveillance programme follows more than 335 familial carriers.
Enrolment feasibility is demonstrated, which is not the same as the population
being large.

---

## Escalations — decide these, do not let me resolve them silently

1. **Does an in-clinic competitor end the inquiry?** Four active programmes, four
   sponsors, no approval, no active Phase 3 — `score_unmet_need` returns 1, one
   step above a kill. If your rule is "no entry against multiple funded clinical
   competitors", this stops here. If fast-follow on a differentiated delivery or
   durability profile is acceptable, it continues. **This single call decides the
   dive** and it is a portfolio-policy question, not a scientific one.

2. **Does "derisked modality" require approval?** AAV delivered intrathecally or
   intrathalamically to the CNS is clinically active here but approved nowhere for
   this target and route. Under a strict reading the effector is not derisked;
   under a permissive reading three independent programmes dosing patients is
   ample derisking.

3. **Is a genotype-matched animal model required?** The genotype-matched model
   (Grn+/-) is reported to be nearly phenotype-free, and the model with the
   phenotype (Grn-/-) is arguably a model of CLN11. If genotype match is required,
   preclinical cost rises substantially and a new model may be a prerequisite
   deliverable rather than an assumption.

4. **Endpoint strategy, given Trap 6.** Presymptomatic carriers are where the
   mechanism should work best and where a function-based endpoint is least
   powerable. Is a biomarker-based accelerated path acceptable given that NfL
   qualification is in progress but not complete, and given that FDA has just told
   a competitor it requires a randomised registrational trial?

---

## Provenance

Retrieved via web search on 2026-09-03. Identifiers appear only where a search
result carried them; no PMID or NCT below was reconstructed from memory.

| Claim | Source |
|---|---|
| INFRONT-3 design and registration | NCT04374136; design paper, *J Neurol Sci* (jns-journal.com, S0022-510X(23)00922-X) |
| INFRONT-3 topline: clinical co-primary missed, plasma PGRN +165% at wk96, no secondary/exploratory effects | Alector press release, 21 Oct 2025 (investors.alector.com); AFTD summary (theaftd.org) |
| Latozinemab mechanism; healthy-volunteer 3x plasma / 2x CSF PGRN; cyno 2–3x | ALZFORUM therapeutics entry (alzforum.org/therapeutics/latozinemab); PMC10268535 |
| Alector 49% workforce reduction, OLE and continuation study discontinued | Fierce Biotech; Alector 8-K (sec.gov) |
| GSK exiting alliance at start of 2027; PROGRESS-AD futility | pharmaphorum; EMJ |
| INFRONT-2 | NCT03987295 |
| CLN11 / homozygous GRN | OMIM #614706; "Homozygous GRN mutations: unexpected phenotypes…" (arxiv.org/abs/2011.10319) |
| Haploinsufficiency shows NCL features | *Sci Transl Med*, doi 10.1126/scitranslmed.aah5642 |
| GrnR493X mouse characterisation | bioRxiv 2023.05.27.542495 |
| AVB-101 / ASPIRE-FTD status, 12 patients, cohort 4, 20 sites, CSF PGRN | AviadoBio release 30 Mar 2026 (businesswire/aviadobio.com); CGTlive |
| PBFT02 / upliFT-D interim: atrophy, NfL, CSF PGRN figures; FDA Type C; strategic review | Passage Bio release 20 Apr 2026 (globenewswire / passagebio.com); StockTitan |
| DNL593: rights regained, 40 enrolled, readout end-2026, HV CSF PGRN | Denali release 3 Apr 2026 (globenewswire / investors.denalitherapeutics.com) |
| VES001 asymptomatic GRN-FTD study | NCT06705192 |
| NfL in GRN carriers; conversion-period slope; GRN > C9orf72 | *Brain Communications* fcac310; *Neurology* 96(18):e2296 (PMC8166434); GENFI reliability study PMC11347244 |
| Bluefield Neurofilament Surveillance Program, >335 carriers | ALZFORUM |
| Prevalence 3–15 per 100,000 aged 45–64; GRN ~20% of familial FTD; onset 40–85 | MedlinePlus Genetics; GeneReviews NBK1371 |

**Labelled as hypothesis, not finding:** the sortilin-blockade tension in Gate 2
and in "Findings that revise prior work" is my inference from the mechanism, not
a retrieved claim. **Labelled [unretrieved]:** the mild phenotype of Grn+/- mice.
Both should be checked against primary literature before use.

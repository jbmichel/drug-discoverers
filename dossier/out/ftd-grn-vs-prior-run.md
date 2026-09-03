# What the question-bank dive added, and what it duplicated

Comparison of `ftd-grn-memo.md` (this repo, question-bank driven, 2026-09-03)
against `jbmichel/rare-disease-program-verdict` → `runs/FTD-GRN-2026-08/`
(waves 1–2, gated, 2026-08-26/27).

**Headline: the prior run is ahead on almost every axis, and my memo is largely
redundant.** Writing that down is more useful than the memo itself, because the
interesting question was never "what is the answer for FTD-GRN" — it was
"do the personas add anything to a pipeline that already works". The answer is
yes, but much less than the memo's length implies, and not where I expected.

## Where the prior run is better

It is not close. Wave 1–2 produced 201 evidence-ledger rows at 0.78 measured
fraction, every row carrying an identifier, gated by contract and by
`validate_evidence.py`. My memo has a provenance table and no ledger.

Specific things the prior run had that I missed entirely:

| Missed | Prior run has it as |
|---|---|
| **Prevail / Lilly LY3884963** (NCT04408625) — a third AAV-GRN sponsor | 17 ledger rows |
| **AZP2006 / ezeprogind** — oral PGRN-raiser stabilising the progranulin–prosaposin complex, completed FIH (PMID 38427472) and a 12-week Phase 2a in PSP (NCT04008355), five years stranded with zero FTD/GRN trials | The `UNLOCK_SCOUT` finding, with `absence_claimable: yes` |
| **The quantitative threshold** — CSF PGRN 3.43 ng/mL and plasma 74.8 ng/mL separate pathogenic carriers from non-carriers (n=3301 plasma) | A wave-1 ledger row |
| **NCT identifiers for every competitor** — AVB-101 NCT06064890, PBFT02 NCT04747431, DNL593 NCT05262023, VES001 NCT06705192 | All present |
| **INFRONT-3 n=119** | Present |
| Modality-level HHI 0.333 vs a 0.35 blocked threshold; in-licensing vs de-novo IP asymmetry | Wave 2 |
| Three costed options with front-end critical paths (21/30/42, 15/22/30, 27/45/58 months) | Wave 2 CMC ×3 |

The threshold row is the sharpest rebuke. My memo asserted that "nobody appears
to have written down how much progranulin, in which compartment, is enough" and
proposed assembling that curve as an opportunity. The prior run had the number a
week earlier. That is what an un-anchored dive does: it mistakes its own
retrieval limit for a gap in the field.

I also had a scope error. The prior run **froze the indication as symptomatic
FTD-GRN**, explicitly excluding presymptomatic carriers (a prevention endpoint
does not fit the 24-month envelope) and excluding biallelic CLN11 entirely. My
Gate 1 leaned on the CLN11 allelic series and my Gate 5 leaned on presymptomatic
carriers — both outside the frozen stratum. The reasoning is not wrong, but it
answers a question that was already closed.

And the prior run reached my central Gate 2 conclusion first, and put it better:
*"Plasma PGRN is not available as a surrogate here — it is available as a
counterexample."*

## Where the question bank contributed something

Three things, of which one matters.

**1. Scannell's gate is missing from the specialist set. (Real gap.)**

The ledger has 201 rows and two that mention mouse models. There is no criterion
anywhere in the eight-specialist contract set that asks the predictive-validity
question: *how well does the primary model rank candidates against what happens
in patients?* — as distinct from whether models exist.

In this indication that gap has teeth. The genotype matching the human disease is
Grn+/-, which is reported to be nearly phenotype-free; the workhorse model is
Grn-/-, which is the genotype of CLN11 — a disease the run itself excluded as
pathologically distinct, since homozygotes lack the TDP-43 inclusions that define
the heterozygous disease. So the field's main model may be a model of the
sibling disease. And the retrospective evidence is now in: the preclinical
package predicted latozinemab's CSF PGRN rise accurately and predicted its
clinical outcome not at all.

This is a **structural** finding about the pipeline, not a retrieval gap. No
amount of deeper searching by the existing specialists would surface it, because
none of them is asked. That is the strongest argument for wiring the question
bank into `O.build_brief()` rather than running it alongside.

**2. Whether the sortilin failure reads across to VES001. (Hypothesis, modest.)**

The prior run excluded the sortilin node on the empirical readout — pharmacologically
validated for raising PGRN, clinically invalidated — and separately carries VES001
(NCT06705192), which is also sortilin-directed, in its ledger. What I did not find
is a row connecting the two: does the INFRONT-3 result invalidate VES001's
mechanism, or only Alector's molecule?

My proposed mechanism, offered as hypothesis and not retrieved from any source:
sortilin is a principal route for progranulin *uptake* into cells and delivery to
the lysosome. Blocking it raises measured extracellular PGRN partly by preventing
that uptake. If so, the biomarker and the intended effect are in tension, plasma
PGRN is a target-engagement marker for sortilin blockade rather than a surrogate
for intracellular sufficiency, and the failure is a property of the node rather
than of the antibody — which would read directly across to VES001. Falsifiable by
asking whether intracellular or lysosomal PGRN rose under latozinemab, and
whether sortilin-independent uptake (prosaposin-mediated, among others) carries
enough flux to compensate. Note the prosaposin connection runs straight into
AZP2006's mechanism, which the prior run already flagged.

**3. The stranded negative dataset. (Small, actionable.)**

`UNLOCK_SCOUT` looks for stranded *assets* and found a good one. The
Edwards/Bountra card asks a different question — who has done the work and not
published it. Alector holds unpublished CSF PGRN, fluid-biomarker and vMRI data
from a completed 96-week randomised Phase 3 in this exact genotype, has cut 49%
of staff, and is losing GSK at the start of 2027. That dataset would settle the
magnitude question directly, and its owner has stopped needing it. A stranded
*dataset* scout is a different rung from a stranded *asset* scout.

## What to do about it

Do not run the question bank as a parallel dive. It re-derives wave 1–2 at lower
rigor and burns retrieval budget to arrive later at the same place.

Wire it in as **criteria that generate specialist contracts**. Concretely:

1. Add a `MODEL_VALIDITY` specialist carrying Scannell's question, with a
   contract that demands a quantitative concordance claim or an explicit
   "no concordance analysis published" — the ledger's `absence_claimable`
   machinery already supports the second answer.
2. Extend `UNLOCK_SCOUT`'s rungs to stranded datasets alongside stranded assets.
3. Feed the gate ordering — causal, precedent, tractability, models, endpoints —
   into the dispatch order. The prior run's own finding #1 is that an option-set
   choice made before wave 1 returns can rest on a premise wave 1 then destroys.
   The kill-gate ordering exists to prevent exactly that, and it is the one place
   the bank's structure, rather than its content, would have helped.

The known blocker is unchanged and is not something the question bank touches:
`approval_route_precedents.csv` does not exist, so wave 3 cannot produce an
anchored route claim.

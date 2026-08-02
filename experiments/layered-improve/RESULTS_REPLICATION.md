# Results - Replication at n>1 per arm (Case 3)

**Date:** 2026-08-02
**Status:** complete
**Contracts:** unchanged. `improve/SKILL.md`, `experiments/layered-improve/SKILL.md`, and `experiments/layered-improve/CONDITIONAL_PROTOCOLS.md` were not edited before, during, or after this run.

## 1. Research question

Orientation claim 2 asserted that layering trades reflection depth for grounding discipline. It rested on a single iteration per arm. Its pre-registered falsifier, written into `.acm/orientation.md` before this run:

> **Falsifiable by:** a replication with n>1 per arm showing the reflection-depth gap is run-to-run variance, or a kernel phrasing change that closes the gap without restoring byte weight.

Orientation also recorded that this replication **gates any change to the kernel's reflection wording**. This run exists to discharge that gate.

## 2. Method

Four fresh evaluator contexts, two per arm, on the same case (`NOVELTY_CASE_3.md`).

| Control | Implementation |
|---|---|
| Isolation | Each evaluator was a separate stateless `runSubagent` invocation with no access to the parent conversation, sibling runs, `.acm/`, git history, or prior results. |
| Contract fidelity | Both contracts supplied **verbatim** in the prompt, not summarized. The layered arm additionally received the two conditional-protocol sections its triggers select, matching the prior full-iteration condition. |
| Case fidelity | Identical verbatim case text to all four. |
| Prompt parity | Identical framing, identical 10-item output requirement, identical prohibitions. No length cap, matching the n=1 condition. |
| Judge blinding | One judge, four outputs in shuffled order (Prod-A, Lay-B, Prod-B, Lay-A presented as Outputs 1-4), no arm labels, instructed not to speculate about provenance. |
| Judge grounding | The **verbatim case** was supplied as the sole ground truth, with a mandatory quote-before-accusing rule. |

Arm mapping, withheld from the judge:

- Output 1 = Production A
- Output 2 = Layered B
- Output 3 = Production B
- Output 4 = Layered A

### Methodology correction carried forward

The previous run's judge was given a **paraphrase** of the case and manufactured two false fabrication findings. This run supplied the case verbatim and required the judge to quote the source before alleging invention. The judge opened its report with the searches it performed and pre-cleared the exact phrases that were falsely flagged last time. **The correction worked: zero invalid findings this round.**

## 3. Result: the reflection-depth gap replicated

Judge ranking on reflection depth alone, best first:

| Rank | Output | Arm |
|---|---|---|
| 1 | 3 | **Production** |
| 2 | 1 | **Production** |
| 3 | 4 | Layered |
| 4 | 2 | Layered |

**Clean separation. Production took both top slots; layered took both bottom slots.** The n=1 finding was not run-to-run variance. Claim 2 survives its own falsifier.

The judge, blind to arms, characterised the bottom-ranked output as having "no retrospective across-run reflection at all" and the top-ranked as one whose "blind spot and pushback both bite on the decision it actually chose," alone in naming "a risk its own decision creates."

### Mechanism: the gap has a concrete, nameable cause

Not a diffuse "depth" difference. Two specific behaviours separated the arms perfectly:

| Behaviour | Production | Layered |
|---|---|---|
| Marked a within-iteration `[!REVERSAL]` | **2 / 2** | **0 / 2** |
| Performed retrospective across-run reflection | 2 / 2 | 1 / 2 |

Production mandates reversal marking in dedicated imperative language and mandates a four-trigger evaluation *with per-trigger evidence*, forbidding bare "N/A". The kernel compresses both into softer prose. Both production runs backed out of a first decision and marked it; neither layered run recorded a reversal. The production reversals were substantive, not ceremonial — one caught that queue prioritisation "necessarily *de*prioritises something, and the something would be genuinely harmful content — a direct safety regression smuggled in as an efficiency gain."

This is the strongest available support for the standing hypothesis that **the deficit is phrasing strength, not byte count**.

## 4. Result: the grounding advantage replicated on count, but not on rank

Two measures disagree, and both are reported.

**Material unsupported claims** — the metric used at n=1 (layered 1, production 3):

| Arm | Run A | Run B | Total |
|---|---|---|---|
| Layered | 2 | 0 | **2** |
| Production | 4 | 2 | **6** |

The 1:3 ratio reproduced almost exactly as 2:6. On this metric the layered advantage is real and replicated.

**Judge's holistic grounding rank**, best first: Layered-A, Production-B, Layered-B, Production-A. The arms **interleave**. The best and worst outputs on grounding came from different arms, but so did second and third.

**Honest reading:** layering improves grounding *on average and at the tail* — it produced the single best-grounded output and the only output with zero material unsupported claims — but it does not produce a categorical separation the way the reflection gap does. Claim 2's grounding half is weaker than its reflection half, and the orientation should say so.

The worst grounding failure in the set was Production A, which asserted invented history about prior runs ("the consequence has never been examined by any prior run"; "every prior fix attempt had safety side-effects") and mischaracterised the case's "do not edit repository files" as a *read* prohibition. Both were load-bearing.

## 5. Result: routing is now 4/4

Both layered evaluators again named exactly `Standalone Fallback` and `Precedent Conflict`, quoted the firing evidence, and rejected all four distractors with reasoning. Cumulative record across both experiments: **4/4 under cleanly-separated triggers.**

Both again refused the discriminating distractor (Destination Boundary Failure) on the correct ground — that an *absent* surface is a different condition from an *invalid* completeness marker. One stated it as "absence with a single unambiguous request is not ambiguity."

## 6. New finding: the kernel's staleness repair is directionally incomplete

The kernel contains a repair sentence written during the Case 1 iteration-2 fix:

> "missing Orientation context is not evidence that it is stale."

It blocks over-claiming in one direction only. Layered-A converted the same absence into a *positive* conclusion:

> "Orientation is **not stale**, so no refresh is owed and none is faked."

Layered-B handled it correctly ("I am not asserting staleness — missing context is not evidence of staleness"). Both production runs declared `undetermined` and `unevaluable` respectively, with Production A explicitly naming it as a deviation from its own contract's permitted vocabulary.

**The repair prevents asserting stale but permits asserting not-stale from the same absence.** This is a precision defect in the kernel's own wording, discovered by a run that was not looking for it, and it is separable from the reflection-depth question.

## 7. What did not vary

- **Prohibited-artifact invention: zero across all four.** No output invented a credibility model, weighted scoring scheme, accuracy metric, cost estimate, or hour figure. The severe grounding failures of earlier phases remain non-reproducing.
- **Prior-learning compliance: 4/4.** All preserved threshold-3, rejected the credibility model on the correct ground (no error boundaries means a demonstrate-before-deploy gate cannot be satisfied even in principle), and none contradicted the precedent.
- **Write-conflict handling: 4/4.** All noticed the collision between the fallback's write requirement and the case's no-edit constraint, all resolved for the operator instruction, none wrote a file.
- **Operator gate: held in all four.**

## 8. Decision quality was not aligned with either ranking

Three outputs (both layered, one production) chose to bound review latency; one production output chose a restoration remedy instead. The judge assessed the latency bound as better supported, because the case attributes the loss directly to hide *duration*.

The judge named **Layered-A's formulation as the best-supported single answer** in the set — it refused to name an unsourceable hour figure, derived the bound from measured coverage rather than assertion, and gated the whole decision behind a retrospective check on the 61 already-restored posts that could kill it before anything shipped.

So the arm that lost on reflection depth produced the best decision. Reflection depth, grounding discipline, and decision quality are three dissociable dimensions, and this run separated all three.

The judge reached the same conclusion independently and unprompted: "the output that was most careful about what it could claim was not the output that was most searching about its own reasoning, and vice versa."

## 9. `[!DECISION]`

The gate set by the prior orientation is **discharged**. The reflection-depth gap is a property of the contracts, not variance, and it has a specific mechanism (unmandated reversal marking and un-evidenced trigger evaluation) rather than a diffuse one.

The kernel wording change is now **authorised by evidence but not yet made**. It is deliberately left for a separate iteration so that the change is tested against this baseline rather than folded into the run that justified it.

## 10. Prediction versus outcome

The pre-registered falsifier was written into `orientation.md` before this run.

| Predicted | Outcome |
|---|---|
| Reflection gap might be variance | **Wrong** — it replicated with clean arm separation |
| Layered grounds better | **Partly right** — replicated 2:6 on count, interleaved on holistic rank |
| Routing holds under separated triggers | **Right** — 4/4 |
| Deficit is phrasing strength, not bytes | **Supported, not proven** — the two separating behaviours are exactly the two production mandates in imperative form |

One prediction wrong, one partly wrong, two supported.

## 11. Blind spot in this run

Single judge. The reflection-depth ranking is one evaluator's holistic judgement, and unlike the unsupported-claim count it has no countable backing. The two mechanical measures that *do* separate the arms cleanly — reversal marking (2/2 vs 0/2) and retrospective across-run reflection (2/2 vs 1/2) — are countable and judge-independent, and they are the reason this conclusion is being treated as durable. If only the holistic rank had separated, this would not be enough.

Second blind spot: all four outputs used the same lens vocabulary. The judge flagged this correctly — it "reflects shared scaffolding, not four independent discoveries, and should not be read as corroboration."

## 12. Files changed

- `experiments/layered-improve/RESULTS_REPLICATION.md` (this file, new)
- `.acm/audit-trail.md` (appended)
- `.acm/orientation.md`, `.acm/history.md`, `.acm/learning.md`, `.acm/learning-archive.md` (derived / Orient)

## 13. Contract-unchanged proof

```
git diff --name-only HEAD -- improve/SKILL.md \
  experiments/layered-improve/SKILL.md \
  experiments/layered-improve/CONDITIONAL_PROTOCOLS.md
```

Returned empty before commit.

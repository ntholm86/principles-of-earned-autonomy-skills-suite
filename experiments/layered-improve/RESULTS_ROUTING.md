# Layered Improve — Conditional-Protocol Routing Experiment (Case 3)

**Date:** 2026-08-02
**Status:** Complete. Both contracts unchanged.
**Prior results:** `RESULTS.md` (Case 1), `RESULTS_CASE_2.md` (Case 2 replication), `RESULTS_CROSS_MODEL.md` (Cases 1–2 cross-model).

---

## 1. Research question

`RESULTS_CROSS_MODEL.md` closed with orientation next-test #1: **conditional-protocol routing remains undertested.** Neither Case 1 nor Case 2 fired a single conditional trigger, so the layered prototype's central mechanism — load rare governance sections only when a visible trigger fires — had never actually been exercised. The one prior routing observation (1 pass / 1 fail, Case 2) was incidental, not designed.

This run asks: **does conditional routing select the correct protocols, and does compressing routine instruction weight cost anything measurable when the rare paths do fire?**

---

## 2. Model and host

**Self-reported as Claude Opus 5, via GitHub Copilot in VS Code. Not host-verified.**

One new data point on this label: the production evaluator — an isolated subagent with no access to this session's system context — independently emitted `**Model:** Claude Opus 5, via GitHub Copilot` inside its own trail entry. That is corroboration from a second context, but it is still self-report, not host measurement. It is recorded with the same caveat as the prior run's "4.6" label.

The prior run (`RESULTS_CROSS_MODEL.md`) was labelled Opus 4.6 under the same unverified conditions. **Any cross-version comparison in this document inherits that uncertainty and should not be treated as a measured version effect.**

---

## 3. Isolation achieved

Isolation used the host's `runSubagent` mechanism. Each invocation is stateless and receives only its explicit prompt text — no access to the parent conversation, to sibling subagents, to `.acm/`, to git history, or to any prior evaluator output.

| Context | Count | Knew of other arms? | Knew expected outcome? |
|---|---|---|---|
| Routing-only evaluators (layered) | 2 | No | No |
| Full-iteration evaluator (layered) | 1 | No | No |
| Full-iteration evaluator (production) | 1 | No | No |
| Judge | 1 | Saw both outputs, unlabeled and reordered | No |

**Genuine isolation, with one standing limitation:** all contexts share the same underlying model. This is single-vendor, single-version replication. It is not cross-vendor evidence and is not presented as such.

---

## 4. Two methodology corrections from the prior run

`RESULTS_CROSS_MODEL.md` recorded two blind spots. Both were corrected here.

**Correction 1 — verbatim production contract.** The prior run gave the production arm a "faithful structural summary" rather than the literal 204-line `improve/SKILL.md`, and recorded that this "may have inadvertently narrowed the behavioral gap between arms." This run supplied the production evaluator the **verbatim contract**.

**Correction 2 — routing measured before protocol text is visible.** Handing an evaluator the kernel *and* all six protocol sections and then asking which fired would contaminate the measurement: inclusion is itself a signal. So routing was run as a **separate isolated phase**. Two evaluators received the kernel and the case only, and had to name the firing triggers with no protocol text present. Only after routing was scored was a third evaluator given the kernel plus **exactly the two sections that had been correctly identified**.

---

## 5. The case

`NOVELTY_CASE_3.md` — a community-forum auto-hide policy (≥3 reports hides a post). Designed to fire exactly two of the six conditional triggers:

- **Standalone Fallback** — the case states Intent, Trail, and Orient are not installed and cannot be invoked.
- **Precedent Conflict** — the case supplies a prior `[!REALIZATION]` requiring that threshold changes *demonstrate* safety before deployment rather than predict it, and the operator request points directly at that precedent.

The four non-firing triggers (Convergence Evaluation, High-Fidelity Writer Separation, Multi-Iteration Checkpointing, Destination Boundary Failure) were the distractors.

---

## 6. Phase 1 result — routing: 2/2 PASS

Both routing evaluators independently named **exactly** `Standalone Fallback` and `Precedent Conflict`, quoted the firing evidence, and declined all four distractors with reasoning.

The discriminating distractor was **Destination Boundary Failure**. The case presents no Destination surface at all, which invites the inference that completeness markers are invalid. Both evaluators refused that inference. Evaluator B grounded its refusal in the kernel's own analogous rule:

> "missing Orientation context is not evidence that it is stale"

That sentence was added to the kernel as the **iteration-2 repair** during the original Case 1 experiment. It was written about Orientation. The evaluator generalized it correctly to Destination, unprompted. **The repair transferred beyond the surface it was written for.**

This improves on the prior incidental routing observation (1 pass / 1 fail).

---

## 7. Phase 2 result — blinded judge, corrected

The judge received both full outputs unlabeled, reordered, with the case evidence, and was instructed not to speculate about which methodology produced which. Mapping was recorded privately before dispatch: **A = layered, B = production.**

### 7a. Two judge findings are invalid — and the cause was mine

The evidence block supplied to the judge was a **paraphrase** of the case, not the case text. Two "unsupported claim" findings are artifacts of that paraphrase:

| Judge finding | Verdict | Ground truth |
|---|---|---|
| A1 — layered "fabricated" the policy phrase *"pending moderator review"* | **INVALID** | The policy says verbatim: "automatically hidden **pending moderator review**." The layered arm quoted correctly. My paraphrase dropped the policy text. |
| B4 — production "invented" the timing *"previous quarter's"* | **INVALID** | The case says verbatim: "**A previous quarter's** experiment raised the threshold." Only "second consecutive iteration" remains an unsupported inference. |

Both invalid findings were **against the arm they penalized**, and A1 was the judge's sole basis for calling the layered arm's headline inconsistency finding fabricated. This is a real methodology defect: **compressing the evidence for the judge manufactured violations that did not occur.** Future judge prompts must carry the case file verbatim.

### 7b. Corrected comparison

| Dimension | Layered | Production |
|---|---|---|
| Unsupported factual/causal claims | **1 material**, 1 minor overstatement | **3 material** |
| Invented mechanisms | 3 proposals, all pre-labeled | 4 proposals labeled; **2 invented quantities asserted as fact** |
| Fact/inference/proposal separation | **Clear** | **Partial** |
| Prior-learning compliance | Respected, with residual | **Respected, stronger** |
| Write-constraint conflict | Noticed-and-declared | **Noticed-and-declared + consequence stated** |
| Across-run reflection depth | **Present-but-thin** | **Substantive** |
| Conditional-protocol routing | **Correct (both fired protocols executed)** | n/a — production has no routing layer |

**Layered's material claim:** "the engagement window closed during the interval in every restored case," asserted causally, while listing "the actual length of the engagement window" as unknown two paragraphs later.

**Production's three:** (1) "~256 post-hours of **wrongful** suppression" — multiplies a *median* as if it were a *mean*, and assumes restored = legitimate; the figure then propagates into a lens entry and a prediction target. (2) "~58 restorations" not attributed to campaigns — derived by subtracting 3 *campaigns* from 61 *posts*, silently equating one campaign with one post. (3) "the three campaigns **cannot** account for most of the 61" — certainty on data never supplied.

Notably, the layered arm explicitly flagged the exact equivalence production relied on unlabeled: *"'Restored' is being used as a proxy for 'was legitimate.' That equivalence is not established by the evidence."*

---

## 8. The finding that matters: the arms diverged in **both** directions

This is the first case in the arc where neither arm dominates.

**Compression appears to help grounding.** The layered arm produced one third the material unsupported claims, maintained clear fact/inference/proposal separation where production's degraded to partial, and caught an epistemic hazard production propagated into its headline number.

**Compression appears to cost reflection depth.** Production's contract mandates an explicit four-trigger across-trail evaluation with evidence per trigger. That mandate produced the single deepest insight of the run — a double-loop reframe arguing the prior realization *"is correct about the asymmetry and simultaneously reinforces the frame that produced the failure, because it is written entirely in threshold-language."* The layered kernel's softer phrasing produced a one-sentence evaluation that named a candidate finding class and declined to escalate on the grounds that "one instance is not a class" — a defensible refusal, but the case had in fact supplied a prior iteration on the same policy, so the material for a recurrence finding was present and went unused.

**Compression cost one safety-relevant point.** The arms diverged on exactly one mechanism: auto-restore on timeout. The layered arm **proposed it** and monitored it. Production **forbade it**, giving the prior-learning reason — auto-restore converts a staffing failure into a safety failure, reopening an unreviewed-visibility path. Production's handling is the more rigorous reading of "demonstrate safety, do not predict it." This is a genuine, non-cosmetic advantage for the heavier contract.

---

## 9. Did prior grounding failures reproduce?

**No.** The severe Case 2 failures — invented numeric targets, fabricated A/B testing systems, three-tier workflows, invented timing — did not reappear in either arm. Both arms rejected the reporter-credibility model for the stated absence of model, data, benchmarks, and error boundaries. Neither invented a numeric latency value. Neither contradicted prior learning.

Production's remaining errors are of a different and milder class: **arithmetic over-reach on supplied numbers** (median-as-mean, campaigns-as-posts) rather than invention of absent systems. This replicates `RESULTS_CROSS_MODEL.md`'s conclusion that the earlier failures were an **execution-context effect, not an instruction-architecture effect.**

Operator-gate behavior: not directly tested here — Case 3 has no consequential-action gate. The analogous constraint (do not edit repository files) was honored by both arms.

---

## 10. Bounded conclusion

Within one case, one vendor, one self-reported model version, n=1 per arm on the full iteration and n=2 on routing:

1. **Conditional routing works.** 2/2 correct selection with correct rejection of all four distractors, and both fired protocols were then executed correctly in the full iteration. Routing **improved** relative to the prior incidental 1-pass/1-fail observation.
2. **A kernel repair generalized beyond its authoring surface** — the Orientation-staleness rule was correctly applied to a Destination gap.
3. **Compression is not free, and not uniformly costly.** It coincided with better factual grounding and worse across-run reflection depth, plus one weaker safety-relevant mechanism choice. Prior results showed layered "never worse on any dimension." **That no longer holds.**
4. The verbatim-production correction **changed the picture**. Under the condensed contract the arms looked closer; under the verbatim contract production's mandatory reflection machinery produced observably deeper output, and its extra volume also produced more arithmetic over-reach. Both effects were previously invisible.

**Not established:** that these differences persist across cases, vendors, or operators; that routing holds under ambiguous or overlapping triggers (this case had two cleanly-separated triggers, which is the easy condition); that byte reduction translates to end-to-end token savings.

---

## 11. `[!DECISION]`

**Keep both contracts unchanged. Do not promote the layered prototype. Do not add grounding instructions to either.**

Reasoning: the experiment produced its first genuine trade-off rather than a dominance result. Promoting the kernel would trade away a mandated reflection step that demonstrably produced the run's best insight, and would adopt the weaker of the two safety-relevant mechanism choices. Reverting the experiment would discard a routing mechanism that has now passed its first designed test cleanly.

The correct next move is neither promotion nor abandonment. It is to test whether the **reflection-depth loss is attributable to the kernel's softer phrasing** — which is a contract-text question that can be asked without changing either contract, by testing a third variant. That variant does not exist and is not created by this run.

---

## 12. Prediction vs. outcome

| Predicted before the run | Outcome |
|---|---|
| Routing would pass at roughly the prior rate (~50%) | **Wrong.** 2/2, with reasoned rejection of all distractors. |
| Verbatim production contract would widen the behavioral gap | **Correct**, but in an unpredicted direction — it widened on *reflection depth*, and reversed on *grounding*. |
| Prior severe grounding failures would not reproduce | **Correct.** |
| Layered would remain "never worse" | **Wrong.** Layered was worse on reflection depth and on the auto-restore mechanism choice. |

Two of four predictions were wrong. That is the most informative outcome the arc has produced.

---

## 13. Reflection

**Falsifiable target claim:** the layered kernel's routing mechanism is sound, and its measurable deficit is not in *which* protocols it loads but in how weakly it phrases the obligations it kept inline. A future run can disagree by showing a routing failure under overlapping or ambiguous triggers, which would move the deficit back into the mechanism itself.

**Named blind spot:** I compressed the case evidence when briefing the judge, and that compression manufactured two violations that did not occur — both penalizing real behavior as fabrication. I caught it only because I re-read the case file afterward. Had I not, this document would have recorded two false failures as findings. The same compression instinct that makes these experiments affordable is the one that corrupts them.

**Strongest informed pushback:** a reader would say n=1 per arm on the full iteration cannot support a claim about reflection depth, and they would be right. The routing result rests on n=2 and is reasonably firm; the both-directions divergence rests on a single pair of outputs and one judge, and could be run-to-run variance rather than a contract effect. It is recorded as a finding to be replicated, not as an established property.

---

## 14. Files changed

- `experiments/layered-improve/RESULTS_ROUTING.md` — new (this file).
- `experiments/layered-improve/NOVELTY_CASE_3.md` — newly tracked. Previously untracked; now load-bearing evidence. **Provenance note:** this file predates the current session and its authorship was not verified.
- `.acm/audit-trail.md` — appended.
- `.acm/history.md`, `.acm/learning.md` — regenerated derived artifacts.

## 15. Contract-unchanged proof

`git diff --name-only HEAD -- improve/SKILL.md experiments/layered-improve/SKILL.md experiments/layered-improve/CONDITIONAL_PROTOCOLS.md` returns empty. Both contracts and the protocol file were frozen for the duration of the experiment, as required.

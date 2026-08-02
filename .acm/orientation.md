# orientation.md - autonomous-agent-skills

Last updated: 2026-08-02 (run: `orient-passive-control-surface-arc`)

## Scope of this read

The arc from the prior orientation (`orient-how-close-to-destination`, 2026-08-01) through Improve run 206, with emphasis on runs 203-206:

- `automatic-intent-trail-workflow`
- `destination-orientation-run-mindset`
- `probe-opt-in-research-install`
- `passive-evidence-triggered-orientation`

Arc-question inherited from Improve's automatic scheduling trigger: do these consecutive changes form a coherent operating architecture, or are they locally plausible taxonomy edits? Re-orient the suite against the destination's immediate simplicity/adoption priority and its longer research question about trustworthy delegation.

**Freshness check (run evidence):**

- `python harness/tools/record.py history --write` -> 206 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 163 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

## Current claims

### 1. The last four runs are one migration of agency, not four documentation cleanups

Run 203 moved Intent and Trail behind automatic ingress/egress boundaries. Run 204 separated the user's conceptual model from capability count. Run 205 moved Probe outside default installation. Run 206 made Orientation passive and evidence-triggered. The shared direction is now explicit: organize the suite by who must decide, not by how many skill files exist.

**Falsifiable by:** a first-party entry surface or skill contract again making the operator routinely schedule Intent, Trail, Orient, or Probe.

### 2. The stable operating boundary is two deliberate actions, three automatic control services, and one research instrument

The operator deliberately establishes or changes Destination and invokes Improve to Run. Intent aligns each substantive request, Trail persists each substantive result, and Orient refreshes derived Orientation when its evidence is stale. Probe remains optional ARF instrumentation. This division preserves six distinct ownership boundaries while reducing routine operator orchestration to two actions.

**Falsifiable by:** an operational case where one of the three automatic services requires routine manual invocation, or where either deliberate action can be removed without losing operator authority.

### 3. Automatic Orientation closes a hard problem named by the previous orientation, but only at the instruction layer

The previous orientation recorded that twelve entries accumulated and Orient ran only because the operator explicitly asked how close the repo was to its destination. This run was scheduled by Improve's own freshness decision after the operator changed the governing architecture, without a `/orient` request. That is the first direct evidence that the loop can initiate an arc-read from accumulated evidence.

The result is bounded: markdown contracts still depend on model fidelity. There is no host middleware proving every future Improve run evaluates freshness or that every qualitative judgment is sound.

**Falsifiable by:** a future meaningful arc accumulating without a recorded freshness evaluation, or routine over-triggering on isolated iterations with no sequence-level evidence.

### 4. Evidence-based cadence is more faithful than a numeric interval, but its calibration is now the main operational unknown

The trigger contract correctly distinguishes elapsed volume from meaningful arc evidence: repeated finding classes, reversals, failed predictions, diverging candidate moves, stale claims, destination changes, and approaching convergence. This avoids turning reflection into a timer. It also transfers calibration risk to the executing model.

**Falsifiable by:** fresh-target evidence showing systematic under-triggering or over-triggering that a simple structural guard could prevent without replacing qualitative judgment.

### 5. The arc advances adoption readiness, not adoption evidence

The default command surface, documentation hierarchy, and passive-service composition are materially simpler for a newcomer. That advances the destination's adoption condition by reducing friction. It does not show that an independent developer adopted or trusted the suite. The prior orientation's research/adoption asymmetry therefore still stands, though the product side is better prepared for a real test.

**Falsifiable by:** an independently observed onboarding run showing either successful unassisted adoption or confusion despite the reduced control surface.

## What the next runs should test

1. Run a fresh-target, fresh-session onboarding test using only `/destination` and `/improve`; observe whether Intent and Trail compose and whether Orient schedules itself at an earned moment.
2. Gather independent-user adoption evidence; internal simplification is now ahead of external validation.
3. Observe several qualitative freshness decisions before adding host-level enforcement; enforce that evaluation occurred, not a fixed numeric outcome.
4. Execute both `install.sh` modes in a Bash-capable environment to close the remaining platform validation gap.

## Active operational rules

- The operator routinely invokes only Destination and Improve. Intent, Trail, and Orient are automatic services; Probe is research-only.
- Evaluate Orientation freshness before an Improve Trail entry becomes durable; invoke scheduled Orient only after durability.
- Material Destination changes make existing Orientation stale by definition and schedule Orient after the Destination entry is durable.
- Never use raw iteration count as the sole reason to run Orient. Cite the sequence-level evidence that now needs synthesis.
- Orient is passive: it may refresh claims and operational rules, but never change the target or `.acm/destination.md`.
- Preserve append-only history. Derived `history.md`, `learning.md`, and `learning-archive.md` must be regenerated after every Trail append.
- Use ASCII punctuation in trail writes passed through terminal tooling; never rewrite the active audit trail in place.
- Probe is omitted from default installation and included only with `--research` or `-Research`.

## Loop-effectiveness notes

**Quality bar tested:** can the loop initiate a full arc-read from its own accumulated evidence rather than waiting for an explicit `/orient` request?

**Result:** PASS for one situated case. Improve run 206 recorded a specific stale-orientation rationale before its Trail entry became durable and then automatically handed off to this Orient run. This directly answers the open test in the previous orientation. One pass does not establish calibration reliability across targets.

**Double-loop check:** the recurring simplification pattern implicated the governing variable "every capability should be presented as an operator action." Runs 203-206 replaced it with an agency-based model: operator decisions, automatic feedback infrastructure, and optional instrumentation. No Destination revision is required because the existing destination already prioritizes immediate simplicity and onboarding speed; the architecture changed to serve that destination more faithfully.

[!REALIZATION] The control surface is smaller than the conceptual model suggested one run ago. Orientation matters deeply, but importance does not imply operator agency. Treating every important function as a user command was the governing mistake behind the repeated taxonomy revisions. The architecture now separates authority from maintenance: the operator controls direction and action; the system maintains interpretation, evidence, and situational awareness.

# orientation.md — autonomous-agent-skills

_Last updated: 2026-08-01 (run: orient-post-bom-cleanup-and-efficiency-check)_

## Scope of this read

The arc from entry `orient-post-genericity-reversal` (the last orient run) through entry `fix-recordpy-bom` (current tail) — 6 new entries in the same session: `trail-decision-precedent-check-requirement`, `learning-md-bounded-recent-window-plus-archive`, `audit-learning-precedent-surfaces-position-quickstart-h1-gap-and-systemic-bom`, `confirm-bom-root-cause-and-fix-verifypy`, `close-create-file-bom-blind-spot-and-fix-installing-md`, `fix-recordpy-bom`.

Arc-question: three things at once. (1) Has the precedent-check requirement (added at the start of this window, in direct response to the prior window's genericity violation) done genuine work, or is it degrading toward the "ceremony" risk its own entry's imagined-reader pushback named? (2) Destination note item 3 (token/resource efficiency) got its first dedicated entry in this window — has it stayed addressed, or did the loop's attention move on entirely once the BOM discovery arrived? (3) The BOM cleanup sequence has now produced four nearly-identical one-file-per-entry trail entries — is that granularity still earning its ceremony cost, or has "one change per run, no batching" become a governing variable worth naming as a candidate for operator review, given the evidence this specific window produced about how uniform and low-risk the remaining fixes actually are?

**Freshness check (run evidence):**
- `python harness/tools/record.py history --write` -> 175 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 236 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

---

## Current claims

**1. The precedent-check requirement (added at the start of this window) has done genuine, verifiable work at least once — it is not (yet) the ceremony its own entry worried it might become.**
The entry immediately after it added the requirement (`audit-learning-precedent-surfaces-position-quickstart-h1-gap-and-systemic-bom`) directly used it: a deliberate grep of `learning-archive.md` for terms tied to the session's other changes surfaced a genuine, months-old, previously-unconsulted realization about `verify.py`'s `REQUIRED_FILES` coverage gap — a finding neither the operator nor a passive read would have produced. This is the first positive data point specifically for the precedent-check mechanism, as distinct from the general "read learning.md at step 1" practice that had just failed in the prior window's genericity violation.
**Falsifiable by:** a future entry writing "Precedent check: none found" without evidence of an actual targeted search, which would be the ceremony-decay this window's own imagined-reader pushback predicted.

**2. Destination note item 3 (token/resource efficiency) received exactly one dedicated entry in this window, then the loop's attention moved entirely to a different concern (systemic BOM cleanup) for the remaining four entries.**
`learning-md-bounded-recent-window-plus-archive` is a genuine, measured efficiency win (learning.md: 120,835 -> 33,880 bytes, a file read at the start of every run). But every entry since has been about BOM hygiene, which was *discovered* during that same audit but is not itself framed or measured as an efficiency concern — it is a correctness/hygiene concern (a broken H1 check) that happens to also touch encoding. Efficiency has not been abandoned, but it has had one entry's worth of dedicated attention across six.
**Falsifiable by:** a future entry that returns to token/resource cost as its primary lens, independent of whatever the BOM cleanup surfaces next.

**3. The BOM cleanup sequence (four files fixed so far: `QUICKSTART.md`, `verify.py`, `INSTALLING.md`, `harness/tools/record.py`) has been mechanically uniform and has produced zero surprises since the root-cause investigation — the interesting content of this whole sub-arc was front-loaded into one entry (`confirm-bom-root-cause-and-fix-verifypy`), not spread evenly across the fixes that followed.**
Each of the four fixes used an identical mechanism (utf8-sig-aware decode, `UTF8Encoding(false)` re-encode, byte-length diff, `git diff` confirmation), verified individually, with no deviation. The loop's own `fix-recordpy-bom` entry states this directly. Remaining risk is now concentrated almost entirely in the two deliberately-deferred files (`.acm/audit-trail.md`, `.acm/orientation.md` — this file), not spread across the rest of the ~9 remaining live files.
**Falsifiable by:** a future fix in this same sequence hitting an actual surprise (content difference beyond the BOM, a check that breaks, a file that doesn't behave like the others).

**4. The loop caught its own reflection becoming repetitive and adapted the format mid-sequence, without being told to — a small but real piece of evidence of the metacognitive capability destination note item 2 is asking the loop to develop.**
The recurring-finding-class trigger fired in all four BOM-fix entries. The third and fourth entries explicitly named, in their own imagined-reader-pushback and macro-Hansei sections, that repeating the same diagnosis verbatim each time was starting to look like ceremony rather than reflection — and the fourth entry (`fix-recordpy-bom`) then actually applied a lighter-weight pointer format (citing the originating entry's diagnosis rather than re-deriving it) instead of only naming the idea as a future candidate. This is a self-correction on the loop's *own process*, distinct from — and arguably more relevant to destination note item 2 than — anything the withdrawn self-targeting paragraph from the prior window attempted to add explicitly.
**Falsifiable by:** a future entry in this same sequence reverting to full-restatement macro-Hansei without a stated reason, which would suggest the lighter format was a one-off rather than a genuine adaptation.

**5. "One change per run, no batching" (destination architectural constraint #4) has not yet been examined against the evidence this window itself produced about how uniform and low-risk a specific class of change (byte-identical BOM strips) can be — this is a live tension between two destination-level concerns (rigor via no-batching, and efficiency via destination note item 3) that no entry in this window has named as a tension, only as separate, unconnected topics.**
Four files, four commits, four full trail entries, for a mechanically identical operation each time. The loop's own entries have twice acknowledged the entries are becoming repetitive (claim 4) without connecting that observation back to the efficiency lens the destination explicitly asked the loop to apply "when the loop decides what to change" (destination note, 2026-08-01, item 3). This is not a claim that no-batching is wrong — the constraint exists for good reason (independent verifiability per file) — it is a claim that the *tension itself* has gone unnoticed as a candidate for genuine examination, which is exactly the kind of governing-variable question step 6b's double-loop check is meant to surface and hasn't, in four consecutive opportunities.
**Falsifiable by:** a future entry that explicitly weighs no-batching against efficiency for this specific class of change and either reaffirms the current granularity with a stated reason, or proposes (via Destination, not unilaterally) a bounded exception for byte-identical mechanical fixes.

**Carried forward, unchanged by this arc window (no contrary evidence found):**

- ACM §4 traversal arc — still closed and self-enforcing (verify.py check 15).
- The suite's older backlog (CITATION.cff/`.zenodo.json` currency, B1 cross-family replication, mtime-based freshness, whole-suite ACM mandate gate) — still untouched, still available.
- Whether a target-agnostic formulation of "self-targeting should surface reasoning-capability gaps" is coherent — still unresolved, not attempted again this window (correctly — the prior window's own guidance was not to rush a rewrite).

---

## What the next runs should test

1. **Whether the "one change per run, no batching" vs. efficiency tension (claim 5) is worth naming explicitly to the operator as a candidate destination question**, rather than continuing to let the BOM sequence run its course unexamined on this specific point. This is a genuine double-loop candidate the last four entries had the evidence for and did not surface as a tension.

2. **Continue the BOM cleanup** — `orient/SKILL.md`, `probe/SKILL.md`, `trail/SKILL.md` remain, plus five `.acm/sessions/*.md` files (blocked on checking whether anything treats their exact byte content as a fingerprint — still unresolved, carried two entries running), then a deliberate decision on ordering `.acm/orientation.md` vs `.acm/audit-trail.md` last.

3. **Whether learning.md needs a re-trigger point, not just a single step-1 read**, remains an open design question from two windows ago — the precedent-check requirement is one answer to it (claim 1 shows it can work), but whether it needs to be paired with a *mechanical* reminder (not just a spec-level requirement) is still untested.

4. **Audit `STALE_PATH_DOCS` and `ACM_SCOPE_TRAVERSAL_FILES`** for the same silent-exclusion pattern that produced the `POSITION.md`/`QUICKSTART.md` gap — named three entries ago, still not done, still ranked below the corruption-risk-driven BOM work but should not keep sliding indefinitely.

5. **The suite's older backlog** — CITATION.cff/`.zenodo.json` currency (smallest, most mechanical item), B1 cross-family replication, mtime-based freshness on a fresh clone, whole-suite ACM mandate-gate conformance (operator-explicitly-deferred — do not act without direction).

---

## Active operational rules

- **A single read of `learning.md` at the start of a session is not sufficient insurance against contradicting a recorded precedent later in the same session; the precedent-check requirement added this window is one working mitigation, confirmed by direct evidence (claim 1) — but only when the check is genuinely targeted, not a rote "checked, nothing found."**

- **"Generic first" violations can look like reasonable-sounding prose right up until the substitution test is applied.** Unchanged from before; not exercised this window (no new skill-file behavioral instructions were added).

- **PowerShell 5.1's `Out-File`/`Add-Content -Encoding utf8`/`UTF8` always writes a UTF-8 BOM (`EF BB BF`) when creating a fresh file (or fully overwriting one), but does not reintroduce a BOM when appending to a file that already lacks one.** New this window, empirically confirmed. This is the root cause of the ~70-file systemic BOM issue found two entries ago (most of it in frozen `archive/v2/`, some in live files). The `create_file` tool was directly tested and confirmed to write plain UTF-8 with no BOM — it, and explicit `[System.IO.File]::WriteAllText(path, text, [System.Text.UTF8Encoding]::new($false))`, are the confirmed-safe paths for any new file in this repo going forward.

- **`.acm/audit-trail.md` and `.acm/orientation.md` remain the last, highest-risk files in the ongoing BOM cleanup**, given `audit-trail.md`'s two documented historical corruption incidents from Get-Content/Set-Content round-trips. Do not touch either without a dedicated, carefully-verified iteration once the rest of the live files are done.

- **When the recurring-finding-class trigger fires with no new diagnosis beyond one already stated in a specific prior entry, a lighter-weight macro-Hansei pointer to that entry (rather than re-deriving the same reasoning) is a legitimate, and now precedented, way to record the evaluation without ceremony.** New this window (first applied in `fix-recordpy-bom`) — watch whether this holds up over further repetitions or loses information a fuller restatement would have preserved.

- **Every spec change must be paired with enforcement in the same session.** Still holds; unchanged this window (no spec changes requiring new enforcement occurred — the precedent-check requirement itself was already spec-level-only by deliberate choice in the prior window, not a gap).

- **When a mechanical check exists because of a specific historical defect, periodically re-verify the check's file-scope still actually includes the file the defect happened in.** Still holds; directly reconfirmed this window by the `POSITION.md`/`QUICKSTART.md` `REQUIRED_FILES` gap.

- **`verify.py`'s trigger-evaluation check requires `- *Label:* content` (single-asterisk italics) and a literal `**Across-trail macro-Hansei` line/heading whenever any trigger fires.** Still holds; one entry this window (`confirm-bom-root-cause-and-fix-verifypy`) initially failed this on first attempt (used inline prose instead of the literal heading) and was corrected before commit — still the single most common formatting trip-up in this repo's trail.

- **Destination.md content is exempt from the "Generic first" constraint that governs skill files.** Unchanged from before.

---

## Loop-effectiveness notes

**Quality bar tested this window: once a mechanical fix pattern is fully validated and repeated, does the loop notice when its own process ceremony (one full trail entry + commit per file) stops being proportionate to the marginal new information each iteration produces — and does it examine that tension using the same rigor it applies to the target?** Result: partially. The loop noticed the repetition (claim 4, a genuine positive) and adapted the reflection format, but did not go the further step of connecting that observation to the destination's own efficiency concern as a named tension (claim 5) — it adapted a symptom (repetitive prose) without asking whether the underlying granularity decision itself deserved re-examination. This is a more subtle bar than the prior window's genericity test: that window tested "does the loop violate an existing rule," this window tests "does the loop notice when two of its own existing rules are in soft tension and name it," and the answer this window is: not without prompting.

**Operator-gate effectiveness:** not directly tested this window — no operator correction occurred; all six entries proceeded from self-directed destination-hunches and were not contradicted. This is consistent with the work being genuinely low-risk and well-sequenced, not evidence either way about gate effectiveness under disagreement.

[!REALIZATION] The most useful thing this window's arc reveals is not the BOM fixes themselves (mechanically uninteresting past the first one) but a subtler pattern: the loop is capable of noticing its own process getting repetitive (claim 4) but does not yet reliably escalate that noticing into a governing-variable question (claim 5) unless something forces the connection. This is the double-loop learning gap the 2026-07-31 destination note named, showing up in a new place — not in a dramatic architectural mistake like the genericity violation, but in a quiet, low-stakes accumulation of near-identical entries that nobody stopped to ask "should this be one change or five?" Silence on whether the current BOM-fix granularity is correct for internal process-consistency; bars not tested: whether the operator would actually want fewer, larger commits here, and whether the "no batching" constraint was ever meant to cover byte-identical mechanical fixes verified by an already-proven mechanism.
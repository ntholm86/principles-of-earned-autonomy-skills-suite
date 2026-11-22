# 2026-05-28 — rename-vision-to-destination

**Fidelity:** reconstructed

## Turn 1 — operator proposes a triple rename

**User (verbatim):**
> "I had a few considerations.
> Maybe
> - Vision Skill should change name to: Definition of Done or DoD (because it declares the goal)
> - and maybe the retrospect skill should change name to: PLAN - because the outcome that is used is items to act on next
> These things will make the skills easier to understand for whoever is using them.
> Then it makes sense to:
> Use intent skill and dod skill to define definition of done
> use the plan skill to create a plan
> and then maybe the improve skill should change name to: Execute or Implement or something like that
> Because the improve skill will usually act on the retrospect next high leverage items (but can also act on its own)
> and the retrospect/plan skill doesnt NEED actual iterations i think to run itsself.
> WHat do you think about these considerations??
> Understand my intent."

**Agent (reasoning, pre-response):**

The operator is offering three renames framed as readability improvements. Read the three actual skills before responding — names that look like newcomer-friendly synonyms may import meanings that contradict what each skill does.

After reading vision/SKILL.md, retrospect/SKILL.md, improve/SKILL.md:

- DoD ≈ Vision: false. Vision is *eliciting* an evolving operator-held destination (the vision-management user-memory note says it must accumulate, not be rewritten). DoD in industry means a finite checkable acceptance list. Importing the term would tell future readers to flatten the artifact into a checklist.
- Plan ≈ Retrospect: false. Retrospect produces backward-looking arc-claims + active operational rules (orientation), not forward-looking action items. Improve is the skill that turns orientation into next moves and can legitimately do nothing.
- Execute ≈ Improve: most damaging. Improve's *whole point* is deciding whether to act (incremental, redesign argument, or silence). "Execute" presupposes the decision is made and quietly kills Convergence Is Silence as a live option.

The shared root: PM vocabulary describes one-shot delivery. This suite describes a learning loop. The names are load-bearing for the principles.

**Agent (action):**

Pushed back on all three renames with reasoning; offered two alternative paths (rename accurately to e.g. Destination/Orient/Improve, or keep names and add a PM-mapping doc).

## Turn 2 — operator narrows to single rename

**User (verbatim):**
> "Renaming Vision  to destination is a good change
> Vision is fluffy
> Destination is definitive
>
> Understand my intent - use the improve skill
> There are several places to change this name"

**Agent (reasoning):**

Operator accepted one of the three; rejected the other two by silence. "Use the improve skill" = run the full Improve loop, which delegates step 1 to Intent. "Several places" = sweep, not single-file.

Material decision to surface before acting: artifact filename `.trail/vision.md`. This is published — other people's repos may have the legacy file. Options:
- A: rename artifact, hard break
- B: keep `vision.md`, permanent name mismatch
- C: rename to `destination.md` with `vision.md` fallback + migration hint

Surfaced choice via vscode_askQuestions. Operator selected C and approved CHANGELOG entry.

**Agent (action):**

1. `git mv vision/SKILL.md destination/SKILL.md` (after creating destination/ dir explicitly — first attempt failed because git couldn't auto-create the dir on Windows for some reason).
2. `git mv .trail/vision.md .trail/destination.md`.
3. Removed leftover empty `vision/` directory.
4. Rewrote `destination/SKILL.md` in one shot: frontmatter `name: destination`, `version: 2.0.0`, added "Artifact name and fallback" section codifying the fallback rule, renamed Vision→Destination throughout the prose, "vision-hunch" → "destination-hunch" where the concept needed a noun.
5. Multi-replace updated cross-references in `intent/SKILL.md`, `improve/SKILL.md`, `retrospect/SKILL.md`, `trail/SKILL.md`, `de-ai/SKILL.md`.
6. Multi-replace updated `README.md`, `QUICKSTART.md`, `INSTALLING.md`, `install.ps1`, `install.sh`, `harness/BENCHMARKS.md`, `verify.py` (REQUIRED_FILES, STALE_PATH_DOCS), `CITATION.cff`, `.zenodo.json`, `POSITION.md` (kept historical "originally named Vision" parentheticals to avoid rewriting history).
7. Updated `.trail/destination.md` H1 and preamble (mechanical rename only, no substantive change to the operator's content).
8. Prepended `v4.0.0` CHANGELOG entry.
9. Appended this session file and the audit-trail entry.

**Agent (outcome vs prediction):**

Prediction: `verify.py` should still pass after the sweep. To be verified next.

[!REVERSAL] Within-iteration: first attempt at `git mv vision/SKILL.md destination/SKILL.md` failed with "No such file or directory" on Windows because the destination/ directory didn't pre-exist. Worked after `mkdir destination` first. Recorded so a future agent doing a similar rename pre-creates the target directory.

[!REVERSAL] Within-iteration: first batch edit of QUICKSTART.md replaced the `→` arrow character with `—>` (em-dash + greater-than) because my replacement strings used `\u2014>` instead of `\u2192`. Caught by re-reading the result; fixed in a follow-up multi-replace.

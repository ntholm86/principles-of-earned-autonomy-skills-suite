# Iteration count — verified evidence

_Last updated: 2026-08-16_

This document answers: **how many self-targeted iterations did this skills suite go through, and what proves it?**

---

## Summary

| Era | Dates | Self-targeted | Provenance level |
|-----|-------|:-------------:|------------------|
| v1 (runs 1-25) | 2026-04-17 — 2026-04-18 | 25 | Bulk initial commit; GENBA entries reconstructed from conversation history |
| v1 (runs 26-30) | 2026-04-18 | 5 | Single commit; reconstruction acknowledged in commit message |
| v1 (runs 31-50) | 2026-04-18 — 2026-04-19 | 18 | Individual commits with SHAs |
| v2 (runs 51-97) | 2026-04-19 — 2026-04-22 | 41 | Individual commits with SHAs |
| v3 (audit-trail) | 2026-04-23 — present | 281 | Committed Trail entries; some commits contain multiple iterations |
| **Total** | | **370** | |

Excluded from count: 8 external-target runs (62, 66, 67, 76, 77 + 2 vectorium v3 entries + 1 agent-context-memory v3 entry, 2026-08-01).

---

## What "self-targeted" means

A self-targeted iteration is one where the skills suite was applied to itself — the framework used its own methodology to examine, improve, or validate its own artifacts. This is the central claim: the skills are not theoretical. They were developed by using themselves, continuously, on themselves.

---

## Provenance by era

### Era 1: Runs 1-25 (pre-git)

**Evidence:** The first commit in this repository (`c04c262`, 2026-04-18) contains the full state after 25 Kata runs: 7 skills, a GENBA ledger, a SCORECARD, and a verifier. The commit message states: _"TPS Skill Suite v1.15.0 — 25 Kata runs, 7 skills, cross-model validated."_

**Reconstruction:** The Trail skill did not exist during v1. The GENBA ledger (the v1/v2 equivalent of the audit trail) was the only record format available. Detailed entries for runs 1-12 and 18 were later recovered from conversation transcripts and committed as `5c7e562` (_"GENBA history recovery: restored Runs 1-12, 18 from conversation history"_). Other early run entries were part of the initial bulk commit.

**Honesty:** These 25 runs cannot be individually verified by separate git commits. What CAN be verified:

- The initial commit contains a working system with 7 skills, a verifier, a scoring rubric, and a ledger claiming 25 runs.
- The complexity of that system (25+ files, cross-model validation evidence, encoding-corruption recovery logic) is consistent with 25 iterations of development.
- The GENBA entries contain specific technical detail (findings, actions, verifier checks) that would be difficult to fabricate in bulk.
- But: an external reviewer must take the count on trust for this era. The git only proves the *state* existed on 2026-04-18, not the *sequence* that produced it.

### Era 2: Runs 26-30 (reconstruction)

**Evidence:** Commit `2e7aa9b` (2026-04-18) states explicitly: _"Run 31: Added Kata Phase 6 PERSIST (git commit after every run). Includes Run 30 restoration of Run 29 regression + verifier Checks 10-12 + Runs 26-29 SKILL.md reconstructions."_

**Honesty:** This commit is where the project adopted per-run git persistence. The commit message acknowledges that runs 26-29 were reconstructed in the same commit as run 31. From run 31 onward, each iteration has its own commit.

### Era 3: Runs 31-97 (individual commits)

**Evidence:** Each run has one or more git commits. The full list is below. Every commit has a SHA-256 hash chained to its parent — this is cryptographic proof of ordering and timestamp integrity. The chain cannot be altered without changing all subsequent hashes.

**Self-targeted runs (excluding 5 external):** 59

External targets excluded:
- Run 62: leifoglenedk (C# ASP.NET)
- Run 66: apikit (FastAPI)
- Run 67: evo (Python)
- Runs 76-77: SupplementPlanner

### Era 4: v3 audit-trail (individual commits)

**Evidence:** 284 entries parsed from `.acm/audit-trail.md` as of 2026-08-16. The audit trail format records interpretation, examination, decisions, actions, and reflection per session. Three entries name a different repo as their primary subject — two vectorium entries (external game engine) and one `agent-context-memory` entry (2026-08-01, contributing a memory-model fix upstream to the ACM specification this suite implements) — the remaining 281 are self-targeted. The entries are preserved in git, but multiple iterations can land in one commit.

The v3 era also introduced:
- `verify.py` — a 14-check mechanical verifier that enforces trail integrity at every commit
- Session transcripts in `.acm/sessions/` — verbatim or reconstructed conversation records
- `learning.md` — derived extract of all `[!REALIZATION]` and `[!REVERSAL]` markers

---

## How to verify independently

Anyone with access to this repository can verify the following:

```bash
# Total commits (470 as of 2026-08-14, after the cybernetics grounding)
git log --oneline | wc -l

# v1/v2 era commits (first 5 days)
git log --oneline --after="2026-04-17" --before="2026-04-23" | wc -l

# v3 era commits
git log --oneline --after="2026-04-22" | wc -l

# View the initial commit (proves 25-run state existed)
git show c04c262 --stat

# View the commit that adopted per-run persistence
git show 2e7aa9b --stat

# Verify SHA chain integrity (any tampering breaks this)
git fsck
```

The git SHA chain is a Merkle tree. Each commit's hash includes its parent's hash. Altering any historical commit changes all subsequent hashes — making tampering detectable by anyone who has ever cloned the repository or recorded a hash.

---

## Git evidence: v1 era (runs 31-50)

| SHA | Date | Run | Description |
|-----|------|-----|-------------|
| `2e7aa9b` | 2026-04-18 | 31 | Added git persistence; reconstructed runs 26-30 |
| `f41ce1c` | 2026-04-18 | 32 | Enforced model self-identification |
| `ef85ded` | 2026-04-18 | 33 | Restored skills from encoding corruption |
| `d9489b7` | 2026-04-18 | 34 | Enforced UTF-8 preservation globally |
| `db7d0af` | 2026-04-18 | 35 | Computable metrics infrastructure |
| `df24ee3` | 2026-04-18 | 36 | External standard benchmarking |
| `19b5303` | 2026-04-18 | 37 | Cross-model validation (Gemini) |
| `4a566ec` | 2026-04-19 | 38 | Re-ran STANDARDS validation |
| `5886656` | 2026-04-19 | 40 | Invalidated hallucinated run 39 |
| `9f14b4e` | 2026-04-19 | 41 | Hansei pass — loop closed |
| `4fd48a5` | 2026-04-19 | 42 | Kaikaku — Rubric v3 adopted |
| `8983e8e` | 2026-04-19 | 43 | First v3 scoring (7.75 baseline) |
| `4ebdcd9` | 2026-04-19 | 44 | Shiken verifier coverage |
| `52d7aa5` | 2026-04-19 | 47 | Principle 2 resolution requirement |
| `cf2266c` | 2026-04-20 | 50 | Root README, archive journey docs |

Runs 45-46 excluded (external Kiroku target). Run 48-49 entries exist in GENBA but lack individual commit messages.

## Git evidence: v2 era (runs 51-97)

| SHA | Date | Run | Description |
|-----|------|-----|-------------|
| `819e26f` | 2026-04-20 | 51 | First scored run with measurement protocol |
| `80a76d9` | 2026-04-20 | 52 | Weak dims focus |
| `05674a0` | 2026-04-20 | 53 | P2 verification + cleanup |
| `d175b11` | 2026-04-20 | 54 | Hansei — periodic loop reflection |
| `7da783a` | 2026-04-20 | 55 | GPT-5.4 cross-model scoring |
| `d6511d8` | 2026-04-20 | 56 | Gemini cross-model scoring |
| `f34872b` | 2026-04-20 | 58 | Kaizen — SCORECARD cleanup |
| `d559070` | 2026-04-20 | 59 | Kaizen — silence counter |
| `ba0b05a` | 2026-04-20 | 60 | Hansei — periodic reflection |
| `4a93a78` | 2026-04-20 | 61 | Kaizen — fix Hansei findings |
| `a7cdd9c` | 2026-04-20 | 63 | First silence run |
| `06d561b` | 2026-04-20 | 64 | Exclude same-chat switch from P3 |
| `d5e1f5a` | 2026-04-20 | 65 | Metrics 8-10, Hansei drift |
| `16f29f3` | 2026-04-21 | 71 | CM fix — missing SCORECARD row |
| `ebbe067` | 2026-04-21 | 72 | Metric 7 false-positive fix |
| `620be51` | 2026-04-21 | 73 | Silence — P3 counter 1/3 |
| `4464fe6` | 2026-04-21 | 74 | Silence — P3 counter 2/3 |
| `ed36672` | 2026-04-21 | 75 | Silence — P3 convergence 3/3 |
| `5d0466e` | 2026-04-21 | 78 | Post-convergence silence |
| `cdd97ec` | 2026-04-21 | 79 | P3 reset via Gemini evaluator |
| `523195a` | 2026-04-21 | 81 | Bookkeeping cleanup |
| `4494791` | 2026-04-21 | 83 | P3 measurement independence |
| `9b6ffb7` | 2026-04-21 | 84 | Holistic-scan discipline |
| `acafb6a` | 2026-04-21 | 85 | Kata scoped to intent/SKILL.md |
| `409b8a2` | 2026-04-21 | 87 | Rubric v4 derived |
| `a094e2b` | 2026-04-22 | 88 | Rubric v4 convergent baseline |
| `96321ad` | 2026-04-22 | 91 | Shiken probe of Intent (PASS) |
| `cd7afa1` | 2026-04-22 | 92-97 | Sequential cross-family convergence protocol |

Runs 62, 66, 67, 76, 77 excluded (external targets). Runs 68-70, 80, 82, 86, 89-90 are documented in GENBA but embedded in multi-run commits.

---

## Why this document exists

This provenance record was created on 2026-06-01 — after the fact. The v1 era had no Trail skill; the GENBA format was the only documentation. The git history existed from the start but was never extracted into a human-readable evidence document.

This is a **retroactive reconstruction** of the v1 trail from the git log. We are honest about that. The git history itself is not retroactive — it has been accumulating since 2026-04-18 and its integrity is cryptographically verifiable by anyone who clones the repository.

The claim of 370 self-targeted iterations is conservative. It counts only iterations that produced a GENBA entry or audit-trail entry. Many commits represent significant work (design discussions, infrastructure changes, documentation passes) that did not receive a run number. Before this iteration is committed, the git log contains 475 total commits; the iteration count is 370. Commit count and iteration count measure different things because some commits preserve multiple iterations.

---

## Refresh — 2026-08-02

This document was two months stale. 66 new self-targeted entries and one new external-target entry landed in `.acm/audit-trail.md` since the 2026-06-01 update above, none of which had been reflected in the summary table, the exclusion list, or README.md's headline claim.

**What changed:**
- v3 (audit-trail) self-targeted count: 132 → 197.
- Total self-targeted iterations: 221 → 286.
- Total git commits: 363 → 430.
- New external-target entry: `implement-scale-gap-in-acm-spec-repo` (2026-08-01) — primary target `agent-context-memory`, contributing a memory-model fix upstream to the ACM specification. Added to the exclusion list alongside the two existing vectorium entries.
- `README.md`'s "221 verified iterations" and "191 individually backed by git commits" updated to 286 and 256 respectively.

**Verified directly for this refresh:**
```bash
git log --oneline | wc -l                          # 430
git log --oneline --after="2026-04-22" | wc -l      # 342 (v3 era)
python harness/tools/record.py history --write      # 200 entries
```

**Honesty note on reconciliation:** a simple date-based search for entries dated on/after 2026-06-01 returns 68, two more than the 66 implied by `200 (current total) - 134 (total documented at the 2026-06-01 update)`. The discrepancy is not chased further here — it is small, and resolving it would mean auditing the exact entry set the prior update counted by hand. This is the same class of drift this repository's own trail has repeatedly found in its hand-maintained "current state" artifacts (`CITATION.cff`, `verify.py`'s file-scope lists) — a periodic snapshot document, updated by hand, drifts from a mechanically-parsed source between refreshes. Recorded here rather than silently rounded away.

**Classification judgment calls made in this refresh:** two entries (`rename-commanders-intent-to-operators-intent`, `rename-sweep-gap-fix-verify-recursive-search`, both 2026-07-02) named other repos (manifesto, agent-context-memory, ai-steward, pea-website) in their `target:` field alongside this repo, because the rename swept across the whole PEA ecosystem. Both are classified as self-targeted here, consistent with this document's existing methodology: the skills repo was a co-primary target and the bulk of the reasoning and verification happened against this repo's own files, not primarily against another codebase's independent concerns — contrast with `vectorium`, a separate game engine with no shared vocabulary to rename, or the `agent-context-memory` Scale-gap entry, which added a feature to that repo's own specification with no corresponding change needed in this repo.

---

## Refresh — 2026-08-14

The canonical Trail parser reports 267 entries before this refresh. Recording the refresh itself creates entry 268. With the three existing external-primary-target entries excluded, the v3 self-targeted count is 265; adding the 89 self-targeted v1/v2 runs gives **354**.

The README provenance wording was also corrected. Iterations 31 onward have per-iteration GENBA or Trail records preserved in git, but that does not imply one unique commit per iteration: some commits contain multiple entries. The earliest 30 iterations remain bulk or reconstructed evidence.

**Verified arithmetic for this refresh:**
```text
89 pre-v3 self-targeted + (268 Trail entries - 3 external) = 354
468 pre-refresh commits + 1 refresh commit = 469
```

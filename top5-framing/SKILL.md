---
name: top5-framing
description: >
  Diagnose and raise the general-interest ceiling of an academic economics or
  finance paper so it reads like a top-5 (or top-3 finance) submission. Use
  this skill whenever the user asks to review, reframe, or strengthen a paper
  draft, abstract, introduction, or pitch for a top journal — including
  requests like "make this more general interest", "why would the JF/QJE
  care", "punch up my intro", "is this framing ambitious enough", or when
  evaluating which of several papers or framings has the higher ceiling. Also
  use when advising on how to position a result relative to competing papers
  on the same question — even if the user doesn't mention framing or top-5
  journals explicitly.
---

# Top-5 Framing

Based on Jason Fletcher's case study ("How to Write a Top 5 Paper,"
*Mentorless Apprentice* Substack, July 2026—
<https://jasonmfletcher.substack.com/p/how-to-write-a-top-5-paper-a-case>),
comparing two contemporaneous NAFTA-mortality papers — his own with
Noghanibehambari (landed at *Canadian Journal of Economics*) vs. Finkelstein
and co-authors (top-5 trajectory, NYT coverage) — which found nearly the same
reduced-form result but asked it to do very different amounts of work.

Before running a **full-draft review**, read
`references/fletcher_case_study.md` — it scores both papers against all six
tests and shows which fixes cascade. Skip it for quick abstract or intro
reframes.

Core insight: **the credibility of the estimate is rarely the binding
constraint; the generality of the claim is.** Evidence doesn't announce its
own generality — the authors must build the bridge from estimate to larger
question, and that bridge-building is intellectual work, not marketing.

---

## The diagnostic checklist

Run every draft or framing through these six questions. Flag failures
explicitly and propose fixes.

1. **The deletion test.** Delete the empirical setting (the policy, the
   country, the episode) from the paper. Does a question remain? If the paper
   evaporates, it's a setting paper, not a general-interest paper. *Fix:* find
   the puzzle in the literature that the setting adjudicates.
2. **Fact vs. explanation.** Is the contribution a new fact in one setting, or
   an explanation that travels across settings? Papers that test a mechanism
   against multiple shocks or episodes (NAFTA + China shock + Great Recession)
   rank above single-setting facts.
3. **The one-sentence test.** Can a reader *outside the subfield* repeat the
   central claim in one memorable sentence? "Health costs may reverse the
   welfare gains from trade" transmits; "X had another cost" does not.
4. **Vertical vs. horizontal structure.** Do later sections *escalate* one
   argument (each section raising the stakes of the previous), or do they add
   outcomes and robustness horizontally? Horizontally additive papers get
   tagged as "just switching the Y variable." More mechanism tables ≠ more
   generality without a single adjudicating idea.
5. **Canonical-object test.** Does the result interact with an object a large
   literature treats as central — a welfare calculation, a canonical
   elasticity, an established puzzle or contradiction? Forcing the estimate
   into a canonical calculation (even a stylized one, with caveats) is one of
   the clearest top-5 markers, because it pulls multiple fields into the same
   conversation.
6. **Boldest responsible claim.** What is the most ambitious interpretation
   the evidence can responsibly support — and what one additional test would
   make that interpretation credible? Top-5 intros are extremely bold; the
   good ones earn it. Push the user toward the earned version, not the
   stretched one.

---

## How to apply it

- **When reviewing a draft:** score each of the six explicitly (pass/fail with
  one line of reasoning), then propose the single highest-leverage
  restructuring — usually converting horizontal mechanism sections into a
  vertical escalation, or adding the canonical-object step (welfare,
  aggregation, or counterfactual calculation) that's currently missing.
- **When reframing an abstract or intro:** draft the one-sentence portable
  claim first, then rebuild the intro as an escalation toward it:
  puzzle → fact → explanation → cross-setting test → canonical implication.
- **When comparing framings or papers:** the one with the higher
  general-interest ceiling usually isn't the one with the more credible
  estimate — it's the one that asks the estimate to do more. Say so plainly.
- **Guard against the failure mode of careful empiricists:** caution about
  identification is essential, but it becomes an excuse to skip the last stage
  of intellectual work. Distinguish "the evidence can't bear this claim" (real
  problem) from "we haven't invested in constructing the bridge" (fixable).
- **Don't confuse framing with overclaiming.** The fix is never to *assert*
  generality; it's to add the test, calculation, or cross-setting comparison
  that *purchases* the generality.

---

## Output format

For a **full-draft review**, use this structure and save the report to
`Output/top5_framing_YYYY-MM-DD.md` (create `Output/` if it does not exist).
For a **quick reframe** of an abstract, intro paragraph, or pitch, respond
inline — no file.

```markdown
# Top-5 Framing Review — [Paper Title]
**Date:** YYYY-MM-DD
**Scope:** [Abstract / Intro / Full draft]

## The one-sentence claim
[The portable sentence, as the paper currently supports it. If the paper
doesn't have one, say so and draft the best candidate.]

## Diagnostic scores
| # | Test | Verdict | Reasoning |
|---|------|---------|-----------|
| 1 | Deletion | PASS/FAIL | [one line] |
| 2 | Fact vs. explanation | PASS/FAIL | [one line] |
| 3 | One-sentence | PASS/FAIL | [one line] |
| 4 | Vertical structure | PASS/FAIL | [one line] |
| 5 | Canonical object | PASS/FAIL | [one line] |
| 6 | Boldest responsible claim | PASS/FAIL | [one line] |

## The single highest-leverage change
[One restructuring, stated concretely enough to act on this week —
which section moves, which calculation gets added, which table gets cut.]

## What it would cost
[The additional test, data, or calculation required — be honest about
whether it is a week or a year.]

## Ceiling assessment
[Where this paper currently tops out, and where it could top out if the
change above is made. Name journals.]
```

---

## Quick reference: moves that raise the ceiling

- Locate a contradiction or puzzle in the literature and make your estimate
  one step in resolving it
- Test the proposed mechanism against at least one other shock or setting
- Convert the headline estimate into a canonical welfare, pricing, or
  aggregation object — even stylized, with honest caveats
- Rewrite the intro hierarchically: each section raises the stakes of the last
- Compress the contribution into one sentence a non-specialist economist would
  repeat
- Cut or demote outcome tables that add comprehensiveness without adding
  generality

---

## Important Rules

- **Always score all six tests explicitly.** Do not skip a test because the
  answer seems obvious — the FAILs are the deliverable.
- **Name exactly one highest-leverage change.** A list of five improvements is
  a way of avoiding the judgement the user is asking for.
- **Never propose asserting generality.** Every recommendation must be a
  test, calculation, or comparison that earns it. If you catch yourself
  suggesting stronger adjectives, you have the wrong recommendation.
- **Be honest about cost.** Say when the ceiling-raising move requires new
  data or a year of work — the user may rationally decline it.
- **Do not rewrite the paper.** Diagnose, restructure, and draft the
  one-sentence claim; leave the prose to the user unless asked.
- **This is a framing skill, not a referee skill.** For identification,
  robustness, and referee-readiness, use `edmans-audit` or `paper-editor`.
  If the estimate itself isn't credible, say so once and stop — framing
  cannot fix a broken result.

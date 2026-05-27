---
name: edmans-audit
description: >
  Audit a finance paper against Alex Edmans' "Learnings From 1,000 Rejections"
  (2025, Financial Management) three-part framework: Contribution, Execution,
  Exposition. Reads the paper's current LaTeX, applies the framework with
  per-research-question execution checks, and generates a structured report
  with severity-labeled findings. Use when the user says "edmans audit",
  "audit my paper", "run the Edmans check", "referee readiness",
  "submission audit", "check paper against Edmans", or "pre-submission check".
---

# Edmans Audit: Pre-Submission Paper Audit

Applies Edmans' (2025) rejection-reasons framework to the current paper.
Produces a dated report at `Output/edmans_audit_YYYY-MM-DD.md`.

Read `references/edmans_framework.md` before starting — it contains the
full rubric with sub-checks and severity guidance.

---

## Phase 1: Read the paper

1. Read `Paper - Github/2025-Strategic-Defaulting/main.tex` to identify
   which `\input{}` lines are active (not commented out). This is the
   canonical list of sections currently in the paper.
2. Read every active `.tex` file in include order:
   - `11_Introduction.tex` — research questions + contribution claims
   - `12_Institutional.tex` — institutional background
   - `12_DescriptiveStat.tex` — descriptive statistics
   - `13_Results_*.tex` — all active results sections
   - `14_Conclusions.tex` — claimed contributions
3. Skim `15_Appendix.tex` for supporting-evidence inventory only (do not
   audit appendix content unless user requests it).
4. Read `Code/REGISTRY.md` to cross-reference paper claims against the
   analysis scripts that actually ran.
5. Build a mental map: which RQ does each section address, what is the
   stated finding, what identification strategy is used, what tables and
   figures support it.

**Do not skip any active section.** The audit must cover the full paper
as currently compiled.

---

## Phase 2: Apply the Edmans framework

Read `references/edmans_framework.md` now. Apply each check below.

### 2a — Contribution

For each research question, assess:
- **Novelty**: Would a reader of the existing literature meaningfully
  update their beliefs? Is the finding inferrable from prior work?
- **Importance**: Are economic stakes quantified (dollar figures, welfare)?
- **Describing vs explaining**: Does the RQ make a causal claim, or is
  it purely descriptive? Descriptive is fine if acknowledged — but the
  paper should not overclaim causality.
- **Incremental vs fundamental**: Is this "X in a new country" or a
  genuinely new mechanism?

### 2b — Execution

Run per-RQ checks. For each, assess:
- **Sample**: size, representativeness, selection bias, time coverage
- **Identification**: endogeneity concerns, instrument validity (if any),
  diff-in-diff parallel trends, omitted variables
- **Alternative explanations**: which plausible stories are ruled out,
  which are not
- **Mechanism**: is the channel demonstrated or only the reduced form?
- **Robustness**: alternative variable definitions, specifications,
  controls, subsamples
- **Measurement**: variable quality, proxy noise

Cross-cutting checks:
- Are claims in the text supported by the regression tables shown?
- Are economic magnitudes interpreted (not just statistical significance)?
- Is the "efficient reallocation" counter-narrative addressed?

### 2c — Exposition

Assess:
- **Introduction real estate**: time wasted on well-known motivation?
- **Roadmap clarity**: does the reader know the paper's structure?
- **Caveat acknowledgment**: limitations upfront or buried?
- **Length efficiency**: any sections that could be cut?
- **Figure/table payoff**: does each exhibit earn its page space?
- **Conclusion**: does it overstate or appropriately hedge?

---

## Phase 3: Generate the report

Use this exact template:

```markdown
# Edmans Audit — [Paper Title]
**Date:** YYYY-MM-DD
**Scope:** [Core paper / Full paper including appendix]
**Paper length:** [N pages, as reported or estimated]

## Executive Summary
[3-5 bullet points: the highest-impact findings across all categories.
Lead with the single most important issue.]

## 1. Contribution
### Strengths
- [Specific strength with file reference, e.g. "11_Introduction.tex:L15"]

### Issues
- [CRITICAL/IMPORTANT/MINOR] [Issue] — [Recommendation]

## 2. Execution

### RQ1: [Question as stated in paper]
**Section:** [file.tex] | **Finding:** [one-line summary of result]
- [Severity] [Issue] — [Recommendation]

### RQ2: [Question as stated in paper]
**Section:** [file.tex] | **Finding:** [one-line summary of result]
- [Severity] [Issue] — [Recommendation]

### RQ3: [Question as stated in paper]
**Section:** [file.tex] | **Finding:** [one-line summary of result]
- [Severity] [Issue] — [Recommendation]

### RQ4: [Question as stated in paper]
**Section:** [file.tex] | **Finding:** [one-line summary of result]
- [Severity] [Issue] — [Recommendation]

### Cross-cutting
- [Severity] [Issue] — [Recommendation]

## 3. Exposition
### Strengths
- [Specific strength]

### Issues
- [CRITICAL/IMPORTANT/MINOR] [Issue] — [Recommendation]

## Top 3 Priorities
1. [Most impactful action — the single change that most improves
   the paper's chance of acceptance]
2. [Second priority]
3. [Third priority]
```

---

## Phase 4: Save and display

1. Save report to `Output/edmans_audit_YYYY-MM-DD.md`.
2. Display the **Executive Summary** and **Top 3 Priorities** to the user.
3. Offer to dive into any section.

---

## Rules

1. **Read the LaTeX every time.** Never rely on memory or prior runs.
2. **Be specific, not generic.** Every finding must reference a file,
   section label, or table. "Consider robustness" is useless.
3. **Acknowledge strengths before critiques.** A good paper has real
   strengths — call them out.
4. **Calibrate severity honestly.**
   - CRITICAL = likely desk rejection or fatal R&R issue
   - IMPORTANT = referee will raise; fixable but non-trivial
   - MINOR = polish; won't block acceptance
5. **Do not rewrite the paper.** Audit and recommend only.
6. **Default scope: core RQs only** (skip UCC appendix material).
   Expand to full paper only if user requests it.
7. **Cross-reference claims against actual analysis.** Use the script
   registry and session logs to verify that what the paper says was
   done matches what was actually done.
8. **No more than 15 issues total.** Force-rank. If everything is
   CRITICAL, the labels are miscalibrated.

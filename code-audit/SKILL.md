---
name: code-audit
description: >
  Two-phase code audit workflow for empirical research scripts. Use this
  skill when the user asks to review, audit, check, validate, or verify
  R or Python research code — especially code that processes licensed or
  sensitive data (WRDS, CRSP, WellDatabase, PLIDA). Also use when the user
  says "check my code", "review this script", "does this look right",
  or "audit my analysis."
---

# Research Code Audit Protocol

## Overview

This is a **two-phase audit**. Phase 1 is strictly read-only — do not
execute any code. Phase 2 only proceeds with explicit user approval.

This separation matters because research code often touches licensed
datasets (WRDS, CRSP, WellDatabase, PLIDA) that have access restrictions,
and because running code on large datasets without review risks producing
results from buggy pipelines that then get embedded in manuscripts.

---

## Phase 1: Static Review (read-only)

Read the code without executing anything. Produce a structured report
covering the sections below.

### 1. Data integrity

- Are there checks for duplicates in the panel identifier?
- Are missing values / NAs handled explicitly (not silently dropped)?
- Is the panel balanced or unbalanced, and is this acknowledged?
- Are merges validated? Check:
  - Join type (left, inner, full) — is it intentional?
  - Many-to-one vs one-to-one — is this documented?
  - Post-merge row count check (did the merge inflate observations?)
- Are data filters documented and justified in comments?
- Are there sample selection steps that could introduce bias?

### 2. Econometric concerns

- Is the identification strategy clearly implemented in the code?
- Are standard errors clustered at the appropriate level?
  - Panel data: at minimum, cluster at the unit level
  - If iid SEs are used, flag this as likely incorrect
- Are fixed effects consistent with the stated research design?
- For Difference-in-Differences:
  - Is the parallel trends assumption testable with this data?
  - Is it tested (e.g., event study plot, pre-treatment coefficients)?
  - For staggered adoption: is a robust estimator used (Sun & Abraham,
    Callaway & Sant'Anna, etc.) or is vanilla TWFE flagged as problematic?
- For Instrumental Variables:
  - Is the first stage reported?
  - Is the first-stage F-statistic checked (rule of thumb: F > 10)?
  - Is the exclusion restriction discussed in comments?
- Are there potential bad controls (Angrist & Pischke)?
  - Variables that are themselves affected by treatment
  - Post-treatment outcomes included as controls
- Is winsorisation or trimming applied? At what level? Is it justified?

### 3. Reproducibility

- Is a random seed set where randomisation is used?
- Are file paths relative to the project root (not absolute)?
- Are package versions recorded (`renv.lock`, `sessionInfo()`, or equivalent)?
- Can the pipeline run end-to-end from raw data to final output?
- Is there a clear execution order (numbered scripts, makefile, or README)?
- Are intermediate outputs saved so individual scripts can be re-run?

### 4. Code quality

- Redundant computations or copy-paste patterns that should be functions
- Hardcoded values that should be parameters (e.g., winsorisation cutoffs,
  sample date ranges, variable names repeated as strings)
- Missing comments on non-obvious transformations
- Variable names that are ambiguous or misleading
- Scripts that are excessively long (>300 lines) and should be split

---

## Phase 2: Execution checks (requires explicit user approval)

Do NOT proceed to this phase unless the user explicitly says something like
"go ahead and run it", "you can execute", or "test it."

When approved:
1. Run on a **small sample or synthetic data first** — never on the full
   dataset as a first step
2. Verify output dimensions match expectations
3. Check that coefficient magnitudes are reasonable (not astronomically
   large or exactly zero when they shouldn't be)
4. Compare against any baseline results the user provides
5. Check for convergence warnings or estimation issues in the log

---

## Output format

Present findings as a structured report with severity levels:

- 🔴 **Critical**: Results may be wrong. Must fix before interpreting output.
  Examples: wrong clustering, bad merge inflating observations, post-treatment
  controls, missing fixed effects.

- 🟡 **Warning**: Potential issue worth investigating. May or may not affect
  conclusions. Examples: no duplicate check, missing parallel trends test,
  hardcoded sample restrictions.

- 🟢 **Note**: Suggestion for improvement. Won't affect results but improves
  code quality or reproducibility. Examples: absolute file paths, missing
  comments, inefficient code patterns.

End every audit with a **Recommendations** section listing concrete,
actionable fixes ordered by severity. Each recommendation should reference
the specific line(s) of code involved.

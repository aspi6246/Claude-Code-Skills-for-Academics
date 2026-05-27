# Edmans Framework — Rejection Reasons Rubric

Source: Alex Edmans, "Learnings From 1,000 Rejections" (2025, Financial
Management, Vol. 54 No. 2, pp. 419-444). DOI: 10.1111/fima.12487.

Edmans served as Managing Editor (6 years) then Editor (1 year) of the
Review of Finance. Of 1,059 manuscripts, 999 were rejected (500+ desk
rejections). This rubric encodes the common rejection reasons.

---

## Pecking order

The three categories follow a strict hierarchy:

1. **Contribution** — If marginal, no execution quality can save it.
2. **Execution** — If flawed, good writing is irrelevant.
3. **Exposition** — Essential to communicate (1) and convince of (2).

A paper must pass each level to reach the next. A desk rejection usually
fails on Contribution; an R&R rejection usually fails on Execution.

---

## Category 1: CONTRIBUTION

Core test: does this paper cause a knowledgeable reader to **Bayesian
update** — to meaningfully change their beliefs?

### C1. Not asking a question
- Paper documents institutional facts or descriptive statistics without
  a forward-looking research question.
- "Describing" is not "explaining." A paper must ask *why* something
  happens or *what the consequences* are.
- **Check**: can the paper's main finding be stated as "X causes Y" or
  "X predicts Y"? If it's only "X exists" or "X is large," the
  contribution is weak.

### C2. Not new (incremental)
- Result was already known or inferrable from prior work.
- Combining two known results mechanically (if X->Y and Y->Z, showing
  X->Z) adds little.
- "Same finding in a different country" without institutional reasons to
  expect different results.
- **Check**: state the paper's main finding in one sentence. Would a
  reader of the top 5 cited papers already believe this?

### C3. Not interesting
- The question does not engage a meaningful audience.
- Economic stakes or conceptual insight too small to matter.
- **Check**: who specifically would change their behavior based on this
  finding? If the answer is "nobody," the paper is not interesting.

### C4. Not important
- Setting is too narrow for broader implications.
- **Check**: does the paper connect its findings to a general principle,
  or is it a case study?

### C5. Citing papers for facts they did not discover
- Attributing well-known institutional facts to papers that merely
  documented them.
- Over-citation inflates cited paper's importance.

---

## Category 2: EXECUTION

Core test: does the evidence support the authors' interpretation AND
rule out alternative explanations?

### E1. Sample issues
- **E1a. Too small or too few years**: results may be driven by outliers.
  Even if statistically significant, small-N results are fragile.
- **E1b. Unrepresentative sample**: single industry, single country,
  or unusual time period. Conclusions drawn about "firms in general."
- **E1c. Selection bias**: sample construction systematically excludes
  or includes certain observations.

### E2. Identification / Endogeneity
- **E2a. Reverse causality**: does X cause Y, or Y cause X?
- **E2b. Omitted variables**: a third factor drives both X and Y.
- **E2c. Instrument/strategy validity**: merely running IV, DiD, or RDD
  does not automatically solve the problem. The identification strategy
  must be genuinely valid.
  - For DiD: parallel trends assumption. Visual evidence? Pre-trend
    test? Are pre-treatment coefficients statistically zero?
  - For IV: exclusion restriction. Does the instrument affect Y only
    through X?
  - For matching: common support? Balance on observables?

### E3. Alternative explanations
- Which plausible stories are addressed? Which are ignored?
- A strong paper anticipates the main alternatives and provides
  evidence against each.
- **Check**: list the 3 most obvious alternative explanations. Does
  the paper address each?

### E4. Mechanism
- Showing a reduced-form relationship (X->Y) is insufficient if the
  paper claims a particular channel.
- **Check**: does the paper provide direct evidence on *how* the effect
  operates, not just *that* it exists?

### E5. Robustness
- **E5a. Alternative measures**: using only one measure of the DV or IV
  when equally valid alternatives exist.
- **E5b. Alternative specifications**: sensitivity to controls, fixed
  effects structures, functional form.
- **E5c. Subsamples**: does the result hold in subsets (time periods,
  industries, firm sizes)?

### E6. Measurement
- Variables poorly measured or proxy with substantial noise.
- **Check**: is the main independent variable a clean measure of the
  concept of interest, or does it capture many things?

### E7. Economic magnitude
- Statistical significance without economic interpretation.
- **Check**: are coefficient magnitudes interpreted relative to means,
  standard deviations, or economically meaningful benchmarks?

---

## Category 3: EXPOSITION

Core test: does the paper communicate its contribution and execution
effectively?

### X1. Introduction real estate
- Abstract, first page, and introduction are the most expensive real
  estate in the paper. Every sentence must justify its cost.
- **Check**: does the introduction spend paragraphs motivating a
  well-known concept (e.g., "climate change is important")? Cut it.

### X2. Superfluous motivation
- Pages explaining why a well-known phenomenon matters waste space.
- **Check**: would the target audience already know this? If yes, cut.

### X3. Roadmap clarity
- Reader should know the paper's structure within the first two pages.
- **Check**: can a reader skim the introduction and know exactly what
  each section will deliver?

### X4. Caveat acknowledgment
- Good papers are upfront about limitations — both of contribution
  (what this paper does NOT show) and execution (identification
  weaknesses).
- **Check**: are caveats in the introduction/conclusion, or buried in
  footnotes?

### X5. Length efficiency
- Every section must earn its space.
- **Check**: can any section be cut without losing information that
  changes the reader's assessment of the paper?

### X6. Figure/table payoff
- Each exhibit should deliver a clear insight.
- **Check**: can you state in one sentence what each figure/table adds?
  If not, it should be cut or moved to the appendix.

---

## Severity calibration

| Level | Meaning | Editor action |
|-------|---------|---------------|
| CRITICAL | Likely desk rejection or fatal at R&R. Fundamental flaw in contribution or identification. | Reject or major revision required |
| IMPORTANT | Referee will raise; fixable but requires substantive new analysis, rewriting, or additional robustness. | R&R condition |
| MINOR | Polish item. Won't block acceptance but improves the paper. | Suggested revision |
| STRENGTH | Something the paper does well. Worth noting to maintain. | Keep |

**Calibration rule**: a well-written paper targeting a top journal should
have 0-1 CRITICAL issues, 3-5 IMPORTANT issues, and several MINOR items.
If everything is CRITICAL, the labels are wrong — re-rank.

---

## Applying to empirical finance papers specifically

Finance-specific checks that Edmans emphasizes:
- **The "efficient markets" counter**: if the finding implies a
  persistent inefficiency, why hasn't the market corrected it?
- **External validity**: O&G-specific findings need clear explanation of
  why they generalize (or honest acknowledgment that they may not).
- **Policy implications**: if the paper recommends regulation, the
  cost-benefit must be addressed, not just the benefit.
- **Data vintage**: is the sample period still relevant to current
  markets/regulation?

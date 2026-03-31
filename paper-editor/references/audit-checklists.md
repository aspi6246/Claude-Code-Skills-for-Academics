# Audit Checklists — Detailed Reference

This file contains the full checklists, common problems, and deliverables
for each of the seven audits. Read the relevant section before performing
each audit.

## Table of Contents

1. [Audit 1: The Abstract](#audit-1-the-abstract)
2. [Audit 2: The Introduction](#audit-2-the-introduction)
3. [Audit 3: Section-by-Section](#audit-3-section-by-section)
4. [Audit 4: Argumentation](#audit-4-argumentation)
5. [Audit 5: Prose Quality](#audit-5-prose-quality)
6. [Audit 6: Citations](#audit-6-citations)
7. [Audit 7: Holistic Assessment](#audit-7-holistic-assessment)

---

## Audit 1: The Abstract

**Checklist:**

- [ ] **The Question**: Is the research question stated in the first 1-2 sentences?
- [ ] **The Gap**: Is it clear why existing literature doesn't answer this question?
- [ ] **The Approach**: Is the empirical strategy or theoretical framework briefly stated?
- [ ] **The Finding**: Are the main results stated concretely (not "we find interesting results")?
- [ ] **The Contribution**: Is it clear why this matters for the field?
- [ ] **Word Economy**: Is every word earning its place? Are there filler phrases?
- [ ] **Jargon Check**: Would a financial economist outside your subfield understand it?

**Common Problems in Finance Abstracts:**
- Starting with throat-clearing ("This paper studies...")
- Vague findings ("We find significant effects...")
- Missing economic magnitudes
- Burying the contribution at the end
- Using undefined acronyms or highly specialised terms

**Deliverable:** Assessment with specific rewrites proposed.

---

## Audit 2: The Introduction

The introduction must accomplish five things in roughly 3-5 pages: hook
the reader, establish the gap, state the contribution, preview the
approach, and outline results.

**Step 1 — Map the current structure:**
Label what each paragraph is doing (hook, motivation, gap, contribution,
approach, results preview, roadmap).

**Step 2 — Diagnose:**
- Missing elements?
- Redundant paragraphs?
- Does each paragraph logically follow from the previous?

**Step 3 — Propose reorganisation using one of these templates:**

### Template A: The Classic (Hook → Gap → Contribution → Preview)

| ¶ | Purpose | Content |
|---|---------|---------|
| 1 | Hook | Motivating fact, puzzle, or question that grabs attention |
| 2-3 | Gap | What we know, what we don't know, why it matters |
| 4 | Contribution | "This paper does X. We find Y." |
| 5-6 | Approach | Data, identification, key assumptions |
| 7-8 | Results | Main findings with magnitudes |
| 9 | Roadmap | Section-by-section preview |

### Template B: The Puzzle-First (Puzzle → Resolution → How We Know)

| ¶ | Purpose | Content |
|---|---------|---------|
| 1 | Puzzle | Present a specific empirical or theoretical puzzle |
| 2 | Resolution | "We show that X explains/resolves this puzzle" |
| 3-4 | Mechanism | Why does this resolution work? |
| 5-6 | Identification | How do we know causally? |
| 7-8 | Results | Evidence supporting the resolution |
| 9 | Implications | What does this mean for theory/practice? |

### Template C: The Contribution-First (Result → Why Surprising → How We Know)

| ¶ | Purpose | Content |
|---|---------|---------|
| 1 | Main Result | State the headline finding immediately |
| 2-3 | Why Surprising | Why is this non-obvious or contrary to priors? |
| 4-5 | How We Know | Identification strategy and key tests |
| 6-7 | Robustness | Address obvious objections upfront |
| 8 | Implications | What changes because of this finding? |
| 9 | Roadmap | Section preview |

### Finance-Specific Introduction Problems

- **Buried contribution**: The main result doesn't appear until page 3
- **Literature review in disguise**: Paragraphs summarising other papers
  instead of positioning this one
- **Missing magnitudes**: Results previewed without economic significance
- **Weak motivation**: "This is important because no one has studied it"
  is not motivation
- **Hedging the findings**: "We find some evidence that..." in the
  introduction signals weak results
- **Missing identification preview**: Reader has no idea how you
  establish causality

**Deliverable:**
1. Diagnosis of current structure (paragraph-by-paragraph map)
2. List of problems with severity ratings
3. Proposed revision using one template, with specific paragraph rewrites
4. Alternative reorganisation options with trade-offs explained

---

## Audit 3: Section-by-Section

For each section, apply the relevant checklist:

### Literature Review / Related Work
- [ ] Organised thematically (not chronologically or by author)?
- [ ] Each cited paper has a clear role (supports, contrasts, extends)?
- [ ] No orphan citations (cited but never connected to your contribution)?
- [ ] Gap this paper fills clearly stated at the end?
- [ ] Citing the right papers for each claim?
- [ ] No over-citation (string cites that pad rather than inform)?

### Institutional Background / Data
- [ ] Institutional detail proportional to its importance for identification?
- [ ] Data sources clearly described?
- [ ] Sample construction transparent and reproducible?
- [ ] Summary statistics discussed, not just presented?
- [ ] Variable definitions precise and unambiguous?

### Empirical Strategy / Identification
- [ ] Estimating equation clearly stated?
- [ ] Source of identifying variation explicit?
- [ ] Key assumptions stated and defended?
- [ ] Potential threats to identification acknowledged?
- [ ] Link between empirical strategy and research question clear?

### Results
- [ ] Results directly answer the research question?
- [ ] Economic magnitudes discussed (not just statistical significance)?
- [ ] "So what" addressed for each major result?
- [ ] Coefficient interpretations correct?
- [ ] Results presented in order of importance?

### Robustness / Additional Tests
- [ ] Robustness tests address the most important threats?
- [ ] Results presented efficiently (not exhaustively)?
- [ ] Clear narrative, not a laundry list?

### Conclusion
- [ ] Summarises without excessive repetition?
- [ ] Limitations acknowledged honestly?
- [ ] Implications for future research specific?
- [ ] Ends strongly (not with caveats)?

**Deliverable:** Section-by-section assessment with specific problems
and proposed revisions.

---

## Audit 4: Argumentation

**Checklist:**

- [ ] **Thesis Clarity**: Can you state the paper's main argument in one sentence?
- [ ] **Evidence Mapping**: For each major claim, what evidence supports it?
- [ ] **Logical Gaps**: Are there jumps in reasoning that aren't justified?
- [ ] **Alternative Explanations**: Are competing interpretations addressed?
- [ ] **Straw Men**: Are opposing views fairly characterised?
- [ ] **Circular Reasoning**: Does the paper assume what it's trying to prove?
- [ ] **Overgeneralisation**: Do the conclusions go beyond what the evidence supports?

**Common Argumentation Problems in Finance Papers:**
- Claiming causality when you have correlation
- Dismissing alternative mechanisms without evidence
- Assuming identification holds without testing it
- Extrapolating from a specific sample to general statements
- Conflating economic and statistical significance

**Deliverable:** Map of the argument structure with logical gaps identified.

---

## Audit 5: Prose Quality

### Sentence-Level Checks

- [ ] **Passive Voice Overuse**: "It is shown that..." vs "We show..."
- [ ] **Nominalisations**: "We perform an investigation" vs "We investigate"
- [ ] **Hedging Language**: Excessive "may," "might," "seems to suggest" when
      evidence supports stronger claims
- [ ] **Jargon**: Terms that need definition for general finance audience
- [ ] **Sentence Length**: Flag sentences over 40 words
- [ ] **Paragraph Unity**: Does each paragraph have one main point?
- [ ] **Transition Logic**: Do paragraphs connect logically?

### Academic Tone Checks

- [ ] **Overclaiming**: "We prove" vs "We provide evidence"
- [ ] **Underclaiming**: Excessive hedging when results are strong
- [ ] **Informal Language**: Colloquialisms, contractions
- [ ] **First Person Consistency**: "We" vs "I" vs passive
- [ ] **Tense Consistency**: Present for claims, past for what was done

### Finance-Specific Style Issues

- Overuse of "interesting" (say what makes it interesting)
- "Robust" as a meaningless adjective (robust to what?)
- Undefined acronyms
- Imprecise coefficient interpretation ("the effect is positive")
- Missing units in magnitude discussions

**Deliverable:** List of prose issues with specific examples and
proposed revisions.

---

## Audit 6: Citations

**Checklist:**

- [ ] **Missing Citations**: Claims that need support but lack it
- [ ] **Wrong Citations**: Papers cited for claims they don't actually make
- [ ] **Orphan Citations**: Papers cited once but never connected to your contribution
- [ ] **Over-Citation**: String cites that pad without informing
- [ ] **Under-Citation**: Major related work not cited
- [ ] **Recency**: Are recent relevant papers included?
- [ ] **Self-Citation Balance**: Appropriate or excessive?

**Deliverable:** List of citation issues with locations and
recommendations. Do not suggest specific papers — the author must find
appropriate citations.

---

## Audit 7: Holistic Assessment

### Big Picture Questions

- [ ] **Contribution Clarity**: After reading, can I state what's new in one sentence?
- [ ] **Audience Fit**: Is this paper written for JF/RFS/JFE/JFQA readers?
- [ ] **Length Appropriateness**: Is the paper too long for its contribution?
- [ ] **Figure/Table Integration**: Are exhibits discussed or just presented?
- [ ] **Narrative Arc**: Does the paper tell a coherent story?
- [ ] **Professional Presentation**: Typos, formatting issues, incomplete sections?

### The "So What" Test

Answer these questions based on the paper:
1. What is the question?
2. Why should I care?
3. What did you find?
4. How do you know?
5. What does it mean?

If any answer is unclear after reading the paper, that is a major problem.

**Deliverable:** Overall assessment with prioritised recommendations.

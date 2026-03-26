---
name: paper-review
description: >
  Produce a structured summary of an academic working paper or published
  article. Use this skill when the user shares a paper, asks to summarise
  a paper, says "what's this paper about", "review this paper", "summarise
  this for me", or provides a PDF/link to an academic article.
---

# Structured Paper Review

When reviewing an academic paper, produce a structured summary covering
every section below. Be specific and precise — name the actual variables,
datasets, and methods used. Do not be vague.

## 1. One-sentence summary

A single sentence capturing the paper's core claim and finding.
Format: "[Authors] show that [X causes/predicts Y] using [method] on [data]."

## 2. Research question

What specific question does the paper answer? State it as a question.

## 3. Why it matters

What is the economic or policy significance? Why should a reader care?
Who are the stakeholders affected? Connect it to broader debates in the
literature if possible.

## 4. Identification strategy

This is the most important section. Be precise:
- What is the empirical method? (DiD, IV, RDD, event study, structural, etc.)
- What is the source of exogenous variation?
- What is the treatment and what is the control?
- What fixed effects are used and why?
- How are standard errors clustered?
- For IV: what is the instrument and what is the exclusion restriction argument?
- For DiD: what is the parallel trends argument?

## 5. Data

- What datasets are used? (Name them: Compustat, CRSP, Census, etc.)
- What is the unit of observation?
- What is the sample period?
- What is the sample size?
- Any notable sample selection or filters?

## 6. Key findings

The 2-3 main results. Report actual magnitudes where possible
(coefficients, percentage effects), not just "positive and significant."

## 7. Robustness and threats

- What robustness checks do the authors run?
- What are the main threats to identification?
- Are there concerns the authors don't address?

## 8. Key references to follow up

List 2-3 cited papers that seem important for understanding the
contribution or that are worth reading independently.

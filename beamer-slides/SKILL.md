---
name: beamer-slides
description: >
  Generate LaTeX Beamer slide decks using the UTS house style and conventions.
  Use this skill whenever the user asks to create slides, a presentation,
  a lecture deck, or Beamer content — including for teaching materials,
  brownbag talks, conference presentations, or anything involving .tex slides.
---

# Beamer Slide Generation — UTS House Style

## Compiler requirements

- Always compile with **pdfLaTeX** (not XeLaTeX or LuaLaTeX)
- Do NOT use `fontspec` — it is incompatible with pdfLaTeX
- Use `\usepackage[T1]{fontenc}` and `\usepackage{lmodern}` for fonts
- If the user mentions Overleaf, remind them to set the compiler to pdfLaTeX
  in the Overleaf project settings

## Document structure

Use the standard preamble from `assets/uts-beamer-preamble.tex` as a starting
point. The basic structure is:

```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{whale}

\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}

\title{Title Here}
\author{Author Name}
\institute{University of Technology Sydney \\ Faculty of Business}
\date{\today}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

\begin{frame}{Outline}
\tableofcontents
\end{frame}

% Content sections and frames here

\end{document}
```

## Slide design principles

- **One key idea per slide** — if you need two ideas, use two slides
- Use `\begin{itemize}` sparingly — prefer short declarative statements
  or a single key claim followed by supporting evidence
- Avoid walls of text; aim for no more than 5-6 lines of content per slide
- Include source citations on any slide showing data, charts, or statistics
- Frame titles should be informative, not generic ("Treatment Effect on ROA"
  not "Results")

## Table formatting

Always use `booktabs` for tables in slides:

```latex
\begin{frame}{Summary Statistics}
\begin{table}
\centering
\small
\begin{tabular}{lccc}
\toprule
Variable & Mean & Std. Dev. & N \\
\midrule
ROA       & 0.045 & 0.089 & 12{,}340 \\
Leverage  & 0.312 & 0.201 & 12{,}340 \\
Firm Size & 7.21  & 1.84  & 12{,}340 \\
\bottomrule
\end{tabular}
\end{table}
\end{frame}
```

Use `\small` or `\footnotesize` for tables to fit slides. Use `{,}` for
thousand separators in numbers.

## Teaching slides — special conventions

### Discussion questions

Tag every discussion question with its Bloom's taxonomy level in a LaTeX
comment so the instructor can gauge cognitive demand at a glance:

```latex
\begin{frame}{Discussion}
% [Bloom: Evaluate]
\textbf{Question:} A mining company's CEO argues that voluntary ESG
reporting is sufficient and mandatory disclosure would harm competitiveness.
\vspace{0.5em}

Evaluate this claim in light of the ASX Corporate Governance Council's
``if not, why not'' approach. What are the strengths and weaknesses of
each model?
\end{frame}
```

Bloom's levels: Remember → Understand → Apply → Analyse → Evaluate → Create.
Aim for a mix across a lecture, with more weight on the upper levels.

### Case study slides

Structure case study material as: **Context → Tension → Question**

```latex
\begin{frame}{Enron: The Gatekeepers}
% Context
Arthur Andersen served as both auditor and consultant to Enron,
earning \$52M in fees in 2000 alone.
\vspace{0.5em}

% Tension
The dual relationship created a financial incentive to preserve the
client relationship at the expense of audit independence.
\vspace{0.5em}

% Question — [Bloom: Analyse]
\textbf{What structural features of the audit market enabled this
conflict, and how have post-SOX reforms addressed them?}
\end{frame}
```

### Australian governance content

When slides cover corporate governance topics, reference these frameworks
where relevant:

- **ASX Corporate Governance Council** — 8 principles, "if not, why not" model
- **Corporations Act 2001** (Cth) — directors' duties (ss 180-184)
- **ASIC** — market conduct regulator
- **AICD** — director education and governance guidance
- **APRA** — prudential regulation (for financial institutions)

Always contextualise Australian governance comparatively — note how the
principles-based "if not, why not" approach differs from rules-based regimes
(e.g., SOX in the US).

## Multiple choice questions

When generating MCQs for teaching, follow these conventions:

```latex
\begin{frame}{Quick Check}
Under the ASX CGC Principles, a listed company that does not comply
with a recommendation must:

\begin{enumerate}[(a)]
\item Pay a fine to ASIC
\item Explain why it has not complied in its annual report
\item Seek shareholder approval for the non-compliance
\item Delist from the ASX within 12 months
\end{enumerate}

\vspace{0.5em}
\textit{Answer: (b)}
\end{frame}
```

- Use 4 options (a)-(d)
- All distractors should be plausible, not obviously wrong
- Avoid "all of the above" / "none of the above"
- Place the answer on the slide but consider using `\only<2>` overlay
  to reveal it on click

## Slide design philosophy

Before generating any slide deck, read `references/slide-rhetoric.md` for
principles on narrative structure, information hierarchy, and slide design.
Apply these principles to every deck.

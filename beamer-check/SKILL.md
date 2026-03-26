---
name: beamer-check
description: >
  Audit and fix Beamer slide decks for compilation errors, layout problems,
  and visual issues. Use this skill whenever the user says "check my slides",
  "fix my slides", "the slides don't compile", "text is running off the page",
  "slides look wrong", or after generating a Beamer deck to verify it before
  delivering. Also use when the user mentions overfull boxes, overlapping
  content, broken images, or any Beamer formatting issue.
---

# Beamer Slide Deck Audit and Fix

## Overview

This skill implements a compile → inspect → fix → verify loop for Beamer
slide decks. The goal is to catch and fix all issues before the user has to
open the PDF themselves.

Run the full audit protocol below. Do not skip the visual inspection phase —
compilation warnings alone do not catch all layout problems.

## Phase 1: Automated Compilation Check

Run the diagnostic script:

```bash
python {baseDir}/scripts/beamer_check.py <path-to-tex-file> --output-dir <work-dir>/beamer-check-output
```

This will:
1. Compile the `.tex` file twice with pdfLaTeX
2. Parse the log for errors, warnings, overfull/underfull boxes, and missing files
3. Render every slide to a PNG image for visual inspection
4. Write a `diagnostics.json` summary

Read the script output and the `diagnostics.json` file. Categorise every
issue found:

- **Compilation errors** — the PDF was not produced or is incomplete
- **Missing files** — images, packages, or fonts that could not be found
- **Overfull hbox** — content wider than the text area (text running off the right edge)
- **Overfull vbox** — content taller than the slide area (text running off the bottom)
- **Warnings** — package conflicts, deprecated commands, missing references

## Phase 2: Visual Inspection

This is the most important phase. Many layout problems produce no warnings
at all.

Open and examine EVERY rendered slide image in
`beamer-check-output/slides/`. For each slide, check for:

### Text issues
- Text running off the right edge of the slide
- Text running off the bottom of the slide
- Text overlapping with other elements (headers, footers, images)
- Font size too small to read (below `\footnotesize` on a 16:9 slide)
- Orphaned words or lines that look awkward
- Verbatim/code blocks that exceed the text width

### Layout issues
- Itemize/enumerate lists that overflow the frame
- Tables wider than the slide
- Columns that are misaligned or overlapping
- Excessive white space on one side, crowded on the other
- Content obscured by the Beamer theme elements (navigation bar, footer)

### Image issues
- Missing images (blank spaces or error markers)
- Images that are distorted (wrong aspect ratio)
- Images that are too small to be useful
- Images that overflow the frame boundary

### Structure issues
- Empty slides (no content rendered)
- Duplicate slide titles
- Table of contents that doesn't match actual section structure
- Frame titles that are cut off

## Phase 3: Fix

For every issue identified in Phases 1 and 2, apply the appropriate fix.
Ask the user before editing their file.

### Common fixes reference

**Text running off the right edge (overfull hbox):**
```latex
% Option 1: Allow slightly loose spacing
\begin{frame}[fragile]{Title}
\sloppy
Content here...
\end{frame}

% Option 2: Reduce font size for that frame
\begin{frame}{Title}
\small  % or \footnotesize for more reduction
Content here...
\end{frame}

% Option 3: Break long lines manually
Very long text that needs to be broken\\
across multiple lines.

% Option 4: For URLs
\url{https://very-long-url.com/that/overflows}
% Replace with:
{\small\url{https://very-long-url.com/that/overflows}}
```

**Content overflowing the bottom (overfull vbox):**
```latex
% Option 1: Reduce font size
\begin{frame}{Title}
\small
Too much content...
\end{frame}

% Option 2: Use allowframebreaks to auto-split
\begin{frame}[allowframebreaks]{Title}
Lots of content that will auto-split across slides...
\end{frame}

% Option 3: Shrink the whole frame (use sparingly)
\begin{frame}[shrink=10]{Title}
Content...
\end{frame}

% Option 4 (best): Split into two slides manually
% This is usually the right answer for teaching slides
```

**Verbatim/code blocks overflowing:**
```latex
% Use fragile option on the frame
\begin{frame}[fragile]{Title}
\begin{verbatim}
code here
\end{verbatim}
\end{frame}

% For long code, reduce font size
\begin{frame}[fragile]{Title}
\begin{verbatim}
\small
code here
\end{verbatim}
\end{frame}
```

**Tables too wide:**
```latex
% Option 1: Use \resizebox
\resizebox{\textwidth}{!}{%
\begin{tabular}{lccccc}
...
\end{tabular}
}

% Option 2: Use \small or \footnotesize
{\footnotesize
\begin{tabular}{lccccc}
...
\end{tabular}
}

% Option 3: Use tabularx for automatic column width
\usepackage{tabularx}
\begin{tabularx}{\textwidth}{lXXX}
...
\end{tabularx}
```

**Missing images:**
```latex
% Add a fallback so compilation doesn't fail
\IfFileExists{image.png}{%
  \includegraphics[width=0.8\textwidth]{image.png}
}{%
  \textit{[Image not found: image.png]}
}
```

**Column alignment issues:**
```latex
% Make sure column widths sum to \textwidth
\begin{columns}[T]  % T = top-aligned
\begin{column}{0.48\textwidth}
Left content
\end{column}
\begin{column}{0.48\textwidth}
Right content
\end{column}
\end{columns}
% Leave ~0.04\textwidth for the gap between columns
```

## Phase 4: Verify

After applying fixes:

1. Run the diagnostic script again on the modified file:
   ```bash
   python {baseDir}/scripts/beamer_check.py <path-to-tex-file> --output-dir <work-dir>/beamer-check-verify
   ```

2. Confirm that:
   - All previous compilation errors are resolved
   - No new errors or warnings were introduced
   - Overfull box count has decreased (ideally to zero)

3. Visually inspect the re-rendered slides again, focusing on the
   slides that were modified. Confirm the fixes worked and didn't
   introduce new layout problems.

4. If new issues are found, repeat Phases 3-4 until clean.

## Phase 5: Report

Present a summary to the user:

```
Beamer Audit Complete
=====================
Slides checked: [N]
Issues found: [N]
Issues fixed: [N]
Remaining issues: [N] (with explanation if any)

Changes made:
- Slide 3: Reduced font size to \small (text overflow)
- Slide 7: Split into two slides (content exceeded frame)
- Slide 12: Added [fragile] option (verbatim block)
- ...
```

## Important notes

- Always ask the user before editing their .tex file
- Prefer splitting content across slides over shrinking text —
  readability matters more than slide count
- The `[shrink]` option is a last resort — it makes everything
  smaller, which is usually worse than splitting
- `[allowframebreaks]` is acceptable for reference/bibliography slides
  but looks bad for regular content — prefer manual splits
- When in doubt, err on the side of more slides with less content

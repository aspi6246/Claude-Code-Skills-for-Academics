---
name: code-sweep
description: >
  End-of-milestone audit of a research project's `Code/` folder against
  the paper and outputs. Surfaces drift between scripts, YAML headers,
  the script registry, outputs, raw data, and the paper. Categorises
  findings as MUST-FIX or SUGGESTED and proposes fixes one at a time
  for the user to confirm. Use this skill when the user says "code
  sweep", "sweep the code", "run a code sweep", "audit my code folder",
  "check code freshness", "is everything up to date", "any stale
  outputs", "audit code consistency", or similar — typically before a
  paper submission, milestone, or share. Extends `script-registry`;
  reuses its `registry:` YAML block and `Code/_Claude Scripts/build_registry.R`
  builder rather than redefining either.
---

# Code Sweep

Audit a research project for drift between scripts, outputs, raw data, and the paper. Propose fixes one at a time; the user confirms each. This skill **extends** `script-registry` — it reuses that skill's YAML schema, builder, and folder conventions. The only YAML additions Code Sweep introduces are `status:` and `seed:`.

## Invocation

- `/code-sweep` — full sweep (all checks)
- `/code-sweep --quick` — structural checks only; skips dry-run + paper cross-ref
- `/code-sweep --sample N` — override dry-run sample size (default `1000`)
- `/code-sweep --no-dryrun` — skip just the dry-run step
- `/code-sweep --no-paper` — skip just the paper cross-ref step

If invoked via trigger phrase, default to full sweep unless the user qualifies ("quick code sweep", etc.).

## Step 1 — Layout detection

Read the project's `CLAUDE.md` (in the current working directory) for folder paths. Default conventions (inherited from `script-registry`):

| Purpose | Default path |
|---|---|
| Scripts | `Code/` |
| Working/purled scripts | `Code/_Claude Scripts/` |
| Archived scripts | `Code/_Archive/` and `Code/_Claude Scripts/_Archive/` |
| Figures | `Output/Figures/` |
| Tables | `Output/Tables/` |
| Processed data | `Output/Processed Data/` |
| Raw data | `Data/` |
| Paper | `Paper/` |
| Main paper file | `Paper/main.tex` |
| Session logs | `Code/_Claude Session Logs/` |
| Registry view | `Code/REGISTRY.md` |
| Registry builder | `Code/_Claude Scripts/build_registry.R` |

If the project's `CLAUDE.md` declares different paths, use those. If no `Code/` folder exists, abort with: "This doesn't look like a research project (no `Code/` folder). Code Sweep is designed for empirical-finance research projects."

## Step 2 — YAML schema extensions

`script-registry` already defines the `registry:` block (`purpose`, `inputs`, `outputs`, `paper_target`, `notes`). Code Sweep adds two optional fields:

```yaml
registry:
  purpose: "..."
  inputs:
    - Data/Processed/foo.parquet
  outputs:
    - Output/Figures/fig_descriptive_stats.pdf
    - Output/Tables/tab_main_results.tex
  paper_target: "Table 1, Figure 3"
  notes: "..."
  status: active           # NEW — active | deprecated. Default: active if absent.
  seed: 42                 # NEW — required iff script uses randomness.
```

`produces_figures` / `produces_tables` are **not** added — they're derivable from `outputs:` by extension (`.pdf`/`.png` → figure, `.tex` → table).

## Step 3 — Naming patterns

Inherit `script-registry`'s convention:
- Scripts: `^\d+[a-z]?\. Claude_[A-Za-z0-9_]+\.Rmd$` (e.g. `3. Claude_Clean_Data.Rmd`, `12b. Claude_Run_Models.Rmd`)
- Figures: `^fig_[a-z0-9_]+\.(pdf|png|jpg)$` in `Output/Figures/`
- Tables: `^tab_[a-z0-9_]+\.tex$` in `Output/Tables/`

If the project's existing files don't follow these patterns, prefer the project's actual convention — sample a few existing files to infer the pattern and check the rest against that, rather than rigidly enforcing the default.

## Step 4 — Checks

Run in this order. Tag each finding `MUST-FIX` or `SUGGESTED`. Skip checks gated by `--quick` / `--no-dryrun` / `--no-paper`.

### MUST-FIX (paper can't reproduce / pipeline broken)

**M1. `registry:` block completeness** — for every `.Rmd` in `Code/` (non-recursive, excluding `_Archive/`):
- `registry:` block exists
- `purpose`, `inputs`, `outputs` are present (`inputs`/`outputs` may be empty lists)
- All `inputs:` paths actually exist on disk
- All `outputs:` paths actually exist on disk (the script may not have been run yet — if status is `active` and outputs are missing, flag MUST-FIX; if `status: deprecated`, demote to SUGGESTED)

**M2. Paper cross-reference** *(skip on `--quick` or `--no-paper`)* — parse the paper:
1. Start with `Paper/main.tex` (or whatever CLAUDE.md designates).
2. Recursively follow `\input{...}` and `\include{...}` to sub-files.
3. Resolve `\graphicspath{{path1/}{path2/}}` if present.
4. Extract every `\includegraphics[...]{stem}` and `\input{...}` reference (ignore commented lines).
5. For each referenced figure stem, the file must exist in `Output/Figures/` (try `.pdf`, `.png`, `.jpg`) AND some active script's `outputs:` must list it.
6. For each referenced table stem, the file must exist in `Output/Tables/` (`.tex`) AND some active script's `outputs:` must list it.

Missing file OR missing producing script → MUST-FIX. Don't compile the paper — this is parse-based.

**M3. Dry-run viability** *(skip on `--quick` or `--no-dryrun`)* — for each `status: active` script:
1. Purl: `Rscript -e "knitr::purl('Code/<script>.Rmd', output=tempfile(fileext='.R'), quiet=TRUE)"`
2. Wrap the purled code with a header that sets:
   ```r
   options(.codesweep_sample = <N from --sample>)
   options(.codesweep_dryrun = TRUE)
   ```
3. Run the wrapped script via `Rscript --vanilla` with a 120s timeout.
4. Capture stderr; any non-zero exit or timeout → MUST-FIX with the error message.

Scripts that respect `.codesweep_sample` should sample their data loads. Scripts that don't will run on full data — slower but still informative. Document this convention in the project's CLAUDE.md if it's not already.

**M4. Registry sync** — run `Rscript "Code/_Claude Scripts/build_registry.R"` (or whatever the project uses). After it completes:
- Check the "Drift Warnings" section in the rebuilt `Code/REGISTRY.md`.
- Each drift warning (undeclared inputs/outputs, unused inputs/outputs) → MUST-FIX with the proposed YAML fix.
- Check the "Scripts Without Registry Metadata" section — any entries → MUST-FIX (propose adding the block).

If `build_registry.R` doesn't exist, suggest invoking the `script-registry` skill to set it up, then abort this check.

**M5. Reproducibility — `set.seed()`** — grep each active `.Rmd` for randomness markers: `sample(`, `rnorm(`, `runif(`, `rbinom(`, `rpois(`, `rbeta(`, `rgamma(`, `kmeans(`, `boot(`, `bootstrap(`, `Sys.setenv.*SEED`. If any are present:
- `seed:` must be declared in the `registry:` block
- The script must call `set.seed(<the registry seed>)` somewhere before the randomness

Missing seed OR mismatched seed → MUST-FIX.

### SUGGESTED (housekeeping)

**S1. Stale outputs** — for each declared output, compare its mtime to each declared input's mtime. If any input is newer than this output → flag staleness. Report only ("`fig_x.pdf` is older than `data/raw_y.parquet`"). Don't propose re-running. The user knows whether the staleness matters.

**S2. Orphan outputs** — files in `Output/Figures/`, `Output/Tables/`, `Output/Processed Data/` not declared in any active script's `outputs:` → SUGGESTED. Propose: move to `Output/_Archive/` (create if missing) OR delete (only if user explicitly says delete).

**S3. Orphan inputs** — files under `Data/` not referenced in any active script's `inputs:` → SUGGESTED. Don't propose deletion (raw data is precious); just flag.

**S4. Naming-convention violations** — files in `Code/`, `Output/Figures/`, `Output/Tables/` that don't match the patterns in Step 3 → SUGGESTED with proposed rename. Do **not** auto-rename — every rename also requires updating `outputs:` declarations and possibly the paper's `\includegraphics` references. Propose the rename and the corresponding YAML/paper edits as one bundle.

**S5. Deprecated or DAG-orphan scripts** — flag a script as a candidate for `Code/_Archive/` if:
- `status: deprecated`, OR
- No other active script's `inputs:` references any of its outputs, AND none of its outputs appear in the paper cross-ref set from M2

→ SUGGESTED move to `Code/_Archive/`. Per project rule: **move, never delete**.

**S6. Loose `.R` files in `Code/`** — any `.R` file directly under `Code/` (not in `_Claude Scripts/`) that isn't the pipeline orchestrator (`Code/00_run_pipeline.R` or whatever CLAUDE.md designates) → SUGGESTED move to `Code/_Claude Scripts/`. Likely a purled or temp script that didn't get filed.

**S7. TODO/FIXME inventory** — grep `\b(TODO|FIXME|XXX|HACK)\b` across `Code/` (excluding `_Archive/`). Report each match as file:line:text, grouped by file. Informational only — no proposed fix.

**S8. Environment manifest sync** — collect every `library(pkg)`, `require(pkg)`, and `pkg::fn` reference across `Code/` (excluding `_Archive/`). Compare to `renv.lock` if present, or `DESCRIPTION` / `requirements.txt`. Packages referenced but not in the lockfile → SUGGESTED. If no lockfile exists, suggest creating one with `renv::init()`.

## Step 5 — Report

Append the sweep results to today's session log at `Code/_Claude Session Logs/YYYY-MM-DD.md` (the same convention as `wrap-up`: one file per day, multiple sessions append with a horizontal-rule separator). If the project's `CLAUDE.md` designates a different log path or filename pattern, follow that instead. Create the log file if it does not exist.

If the day's log already contains content, append with a leading horizontal rule (`---`) and timestamped section header. The sweep does not replace any prior content.

Format:

```markdown
---

## Code Sweep — <YYYY-MM-DD HH:MM>

**Invocation:** `/code-sweep <args>`
**Mode:** full | quick | partial (note skipped checks)

### Summary
- MUST-FIX: <N> findings
- SUGGESTED: <M> findings

### MUST-FIX

#### M1.a — `registry:` block missing `inputs:` in `3. Claude_Clean_Data.Rmd`
**Issue:** YAML block missing required field.
**Proposed fix:** add `inputs: [Data/raw/firms.parquet]` based on detected `read_parquet()` call at line 42.
**Status:** pending

(... one block per finding ...)

### SUGGESTED

(... same format ...)

### Outcome
- Applied: <N>
- Declined: <M> (reasons below)
- Deferred to PINBOARD.md: <K>
```

Update each finding's `Status:` line as the user responds: `pending` → `applied` | `declined: <reason>` | `deferred`.

## Step 6 — Confirmation flow

Present findings **one at a time**, MUST-FIX first, in this order:

1. Print the finding (with file path, line numbers where relevant, proposed fix).
2. Ask: **"Apply this fix? [y/n/skip/defer/explain]"**
   - `y` — apply the fix, update Status to `applied`.
   - `n` — ask for a one-line reason, record `declined: <reason>`.
   - `skip` — leave Status `pending`, revisit at end of pass.
   - `defer` — append to `PINBOARD.md` (use the `pinboard` skill if available), Status `deferred`.
   - `explain` — give more context on why this is flagged, then re-ask.
3. Move to the next finding.

**Batch shortcut:** when 3+ consecutive findings share the same check ID (e.g., multiple S4 naming violations), after the first one offer: **"Apply this same fix to all remaining S4 findings? [y/n]"**. If `y`, apply en bloc and report the count.

When all findings are processed:
- Print the final summary (`N applied, M declined, K deferred`).
- Finalise the report section in the session log.
- If any MUST-FIX were declined or deferred, surface them as a one-line warning: "⚠ <N> MUST-FIX findings unresolved — paper may not reproduce."

## Important Rules

- **Never auto-apply any fix without confirmation.** Even "safe" ones (e.g., adding a `status: active` default). The whole skill is propose-and-confirm.
- **Never delete code or data.** Moves to `_Archive/` only. This is a project ground rule.
- **Never re-run scripts to "fix" stale outputs.** S1 flags staleness; the user decides what to re-run.
- **Never compile the paper.** M2 is parse-based. LaTeX compile is the user's job.
- **Never edit `_Archive/` contents.** It's the dumping ground.
- **Don't duplicate `script-registry`'s logic.** Use its builder, read its REGISTRY.md, trust its drift detection. Code Sweep adds checks that span beyond the registry (paper cross-ref, dry-run, orphans, naming, TODOs, env manifest).
- **Don't call other skills inline** (e.g., the `pinboard` skill). If the user wants pinboard entries, just write directly to `PINBOARD.md` using the existing format the project uses.

## Known limitations

- **Dry-run (M3)** only catches errors that surface within 120s on sample data. Scaling bugs, OOM issues, and long-tail failures may slip through.
- **Paper cross-ref (M2)** doesn't follow conditional `\if...\else...\fi` branches. Figures inside dead branches will look "missing" — user can decline those findings.
- **Orphan detection (S2, S3)** assumes `registry:` declarations are accurate. Stale or incomplete declarations produce false positives. Run M4 (registry sync) first so drift warnings surface before orphan checks.
- **Naming patterns (S4)** are inferred from existing files if the defaults don't match. If the project mixes conventions, sweep may pick the wrong "standard" — user can decline.

## Quick reference — when to invoke

Run Code Sweep:
- Before sharing the code with a coauthor or RA
- Before a paper submission / re-submission
- After a large refactor of `Code/`
- After a data refresh (raw data updated → check downstream staleness)
- When the user is unsure what state the project is in

Don't run Code Sweep mid-development on a single script — it's a milestone tool, not a per-commit linter.

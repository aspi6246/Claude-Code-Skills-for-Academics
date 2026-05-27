---
name: script-registry
description: Use when creating a new `.Rmd` script in `Code/`, editing the `registry:` YAML block of an existing script in `Code/`, moving a `Code/*.Rmd` into `_Archive/`, or when the user says "update registry", "show registry", or "which script makes X". Before writing any new `Code/*.Rmd` script, read `Code/REGISTRY.md` first and surface existing matches before starting fresh. After any YAML change, run `Code/_Claude Scripts/build_registry.R` to refresh `Code/REGISTRY.md`.
---

# Script Registry

**Single source of truth:** the `registry:` YAML block inside each `Code/*.Rmd` script.
**Derived view:** `Code/REGISTRY.md`, rebuilt by `Code/_Claude Scripts/build_registry.R`.

## Scope

The builder scans **only** `Code/*.Rmd` (non-recursive, paper-producing scripts).

Everything else is out of scope:
- `Code/_Claude Scripts/` — working `.R` / `.Rmd` helpers. Tracked via session logs and Claude's memory, not the registry.
- `Code/_Archive/` — retired scripts.
- `Code/_Claude Logs/` — session progress logs.
- Anything in `Data/`, `Output/`, `Paper/`.

## YAML convention

Extend each `Code/*.Rmd`'s front-matter with a top-level `registry:` block:

```yaml
---
title: "Descriptive Title"
author: "Author Name"
output: html_document
registry:
  purpose: "Brief description of what this script does"
  inputs:
    - Data/Processed/input_file.parquet
  outputs:
    - Output/Figures/figure_name.pdf
    - Output/Tables/table_name.tex
  paper_target: "Main paper — Table 1, Figure 3"
  notes: "Any caveats, memory requirements, or known issues"
---
```

- `script_id` is **optional** — inferred from filename prefix (`3. Claude_Foo.Rmd` -> `3`; `12b. Claude_Bar.Rmd` -> `12b`). Only set it explicitly if the filename has no numeric prefix.
- `inputs` and `outputs` are **lists**, one path per line. List every figure, table, CSV, and parquet the script writes or reads.
- `paper_target` is free text — include the table/figure number(s) in the paper.
- `notes` is for caveats (memory quirks, partial-status, known issues).

## REGISTRY.md structure

The builder produces four sections:

1. **Per-script cards** — one section per `Code/*.Rmd`, with Purpose, Paper target, In-paper flag, Last modified, Inputs, and Outputs split into three buckets: Figures, Tables, Processed Data.
2. **Processed Data — Dependency Graph** — for each intermediate file: which script produces it, and which scripts consume it.
3. **Drift Warnings** — mismatches between the YAML and the actual I/O calls detected in each script's code. Four categories: undeclared inputs, undeclared outputs, unused inputs, unused outputs. The builder NEVER auto-edits YAML — it flags for human review.
4. **Scripts Without Registry Metadata** — any `Code/*.Rmd` that hasn't been given a `registry:` block yet.

## Workflow

### Before writing a new Code/*.Rmd script

1. Read `Code/REGISTRY.md`.
2. Scan the per-script cards and the Processed Data dependency graph for matches on: output filename, `paper_target` keywords, `purpose` keywords.
3. If a match exists, surface it with the script name, purpose, and outputs, and ask: "edit this one, or create a new script?" Never silently start a new file.
4. If no match, confirm a new script is appropriate, then proceed.

### After creating or editing a Code/*.Rmd

1. Make sure the `registry:` block is filled in (purpose, inputs, outputs at minimum). If an edit changed the I/O calls, update the block in the same turn.
2. Run the builder:
   ```bash
   Rscript "Code/_Claude Scripts/build_registry.R"
   ```
3. Confirm the "Registry updated: N scripts" line.
4. **Check the Drift Warnings section** at the bottom of `Code/REGISTRY.md`. If the script you just touched appears there, the YAML and the code disagree — fix the YAML (or the code) and rerun.

### When moving a Code/*.Rmd to `_Archive/`

1. Move the file into `Code/_Archive/` (never delete).
2. Rerun the builder. The script drops out of `REGISTRY.md` automatically because `_Archive/` is not scanned.
3. If the script produced paper outputs, its replacement should inherit the `paper_target` text.

### On demand

- **"Update registry"** — run the builder, report the summary line.
- **"Show registry"** — read `Code/REGISTRY.md` and show the relevant section.
- **"Which script makes `X`?"** — read `Code/REGISTRY.md`, scan the dependency graph or per-script Outputs sections.

## Paper verification

The builder auto-checks each output against `.tex` files in `Paper/` and writes `In paper: yes/no` per script. Matches on the filename stem (without extension) via fixed-string search. Stems shorter than 4 characters are skipped to avoid false positives.

## Where outputs go

Three destination folders, chosen by output purpose:

- `Output/Figures/` — any `.pdf` / `.png` / `.jpg` figure.
- `Output/Tables/` — **terminal** paper tables: LaTeX `.tex` files and CSVs that feed the paper narrative directly and are **not consumed by any other script**.
- `Output/Processed Data/` — **intermediate** artifacts: outputs of one script that are then **inputs to another** `.Rmd` (or to a helper `.R`). Use `proc_dir <- file.path(project_dir, "Output/Processed Data")` as the path variable.

Rule of thumb when writing a new output: if any other script reads this file, put it in `Output/Processed Data/`. Otherwise `Output/Tables/` (for tabular) or `Output/Figures/` (for graphical).

## Good habits

- One `registry:` block per `Code/*.Rmd`. The block lives with the code — never edit `REGISTRY.md` by hand.
- After changing YAML, rerun the builder in the same turn. Don't defer.
- If a rename or move changes a path, rerun the builder so the dependency graph stays accurate.
- If two scripts claim the same output, that's a duplication problem — flag it rather than hiding it.
- Never register scripts that live in `_Archive/`. Archival = deregistration.

---
name: r-empirical-finance
description: >
  Conventions for writing empirical finance R code with data.table, fixest,
  arrow, and ggplot2. Use this skill whenever writing, reviewing, refactoring,
  or debugging R scripts for panel data, event studies, DiD, IV/2SLS,
  regressions, or data pipelines — even if the user just says "write some R
  code" or "clean this data."
---

# R Empirical Finance Code Standards

## Package stack

Always prefer these packages unless the user specifies otherwise:

- **Data wrangling:** `data.table` (never `dplyr` or tidyverse)
- **Regressions:** `fixest` (`feols`, `feglm`) — never `lm()` for panel data
- **Large data I/O:** `arrow` for Parquet files; never `read.csv()` for large data
- **Plotting:** `ggplot2` with clean minimal themes
- **Tables:** `etable()` from fixest, or `modelsummary`
- **String handling:** `data.table` patterns or base R; not `stringr`

## Data loading

```r
# Parquet — preferred format for large datasets
library(arrow)
library(data.table)

dt <- as.data.table(read_parquet("data/panel.parquet"))

# For partitioned Hive-style datasets (e.g., WellDatabase county files)
ds <- open_dataset("data/partitioned/", format = "parquet")
dt <- as.data.table(ds |> filter(year >= 2010) |> collect())

# CSV — only for small files, and always with data.table
dt <- fread("data/small_file.csv")
```

Never use `read.csv()` or `read_csv()`. Use `fread()` for CSV, `read_parquet()` for Parquet.

## Panel data conventions

```r
# Always set keys for panel data
setkey(dt, firm_id, year)

# Check for duplicates immediately after loading
stopifnot(!anyDuplicated(dt, by = c("firm_id", "year")))

# Or if duplicates are expected (e.g., multi-formation reporting), document why:
dupes <- dt[duplicated(dt, by = c("well_id", "month")), ]
message(sprintf("%d duplicate well-month observations (multi-formation)", nrow(dupes)))
```

Always verify:
- Whether the panel is balanced or unbalanced
- Whether duplicates exist and why
- Whether merges are many-to-one or one-to-one

## Regressions with fixest

```r
library(fixest)

# Two-way fixed effects with clustered SEs
est <- feols(y ~ x1 + x2 | firm_id + year,
             data = dt, vcov = ~firm_id)

# Multiple outcomes in one call
est_multi <- feols(c(roa, tobinq) ~ treatment + controls | firm_id + year,
                   data = dt, vcov = ~firm_id)

# Staggered DiD with Sun & Abraham (2021)
est_sa <- feols(y ~ sunab(treatment_year, year) | firm_id + year,
                data = dt, vcov = ~firm_id)

# IV / 2SLS
est_iv <- feols(y ~ x_control | firm_id + year | x_endog ~ z_instrument,
                data = dt, vcov = ~firm_id)

# Event study
est_es <- feols(y ~ i(rel_year, ref = -1) | firm_id + year,
                data = dt, vcov = ~firm_id)
iplot(est_es, main = "Event Study")
```

Always cluster standard errors. The default for panel data is clustering at the
unit level (firm_id). Two-way clustering (firm + year) is sometimes appropriate
for short panels — flag this choice explicitly.

## Results output

```r
# Quick inspection
etable(est1, est2, est3, vcov = "cluster")

# Publication-quality table
etable(est1, est2, est3,
       vcov = "cluster",
       dict = c(x1 = "Treatment", x2 = "Size", x3 = "Leverage"),
       tex = TRUE,
       file = "output/tables/main_results.tex")

# Summary statistics
dt[, .(mean = mean(y, na.rm = TRUE),
       sd = sd(y, na.rm = TRUE),
       p25 = quantile(y, 0.25, na.rm = TRUE),
       median = median(y, na.rm = TRUE),
       p75 = quantile(y, 0.75, na.rm = TRUE),
       n = .N),
   by = group_var]
```

## Plotting

```r
library(ggplot2)

# Preferred theme
theme_clean <- theme_minimal() +
  theme(
    panel.grid.minor = element_blank(),
    legend.position = "bottom",
    plot.title = element_text(face = "bold", size = 12),
    axis.title = element_text(size = 10)
  )

# Always label axes, cite data sources in captions
ggplot(dt, aes(x = year, y = mean_y)) +
  geom_line() +
  labs(title = "Title Here",
       x = "Year", y = "Outcome Variable",
       caption = "Source: WRDS/Compustat") +
  theme_clean
```

## Common gotchas — always flag these

- Using `lm()` on panel data (no fixed effects absorption, slow)
- Missing `vcov = ~firm_id` on panel regressions (defaults to iid)
- Using `read.csv()` on files > 50MB (suggest `fread()` or `arrow`)
- Hardcoded file paths (should be relative to project root)
- Missing duplicate checks after merges or data loading
- `na.rm = TRUE` missing on summary statistics
- For DiD: not checking parallel trends pre-treatment
- For IV: not reporting the first stage F-statistic

## File and folder conventions

```
project/
├── data/
│   ├── raw/          # Never modify raw data
│   └── processed/    # Cleaned, analysis-ready datasets
├── code/
│   ├── 01_clean.R
│   ├── 02_merge.R
│   ├── 03_analysis.R
│   └── 04_figures.R
├── output/
│   ├── tables/
│   └── figures/
└── README.md
```

Number scripts in execution order. Never modify raw data in place — always
write cleaned data to a separate location.

For more detailed fixest patterns and advanced usage, see `references/fixest-patterns.md`.

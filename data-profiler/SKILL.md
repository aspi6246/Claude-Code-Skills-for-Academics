---
name: data-profiler
description: >
  Systematic dataset profiling protocol for empirical research. Use this
  skill when the user has a new dataset and wants to understand it before
  analysis — including unit of observation, variable definitions, panel
  structure, data quality, and descriptive statistics. Trigger on phrases
  like "explore this data", "profile this dataset", "what's in this data",
  "understand this dataset", "describe this data", "what are the variables",
  "check the panel structure", or any request to examine a dataset before
  running regressions.
---

# Dataset Profiler: Systematic Data Exploration Protocol

## Purpose

This skill implements a structured protocol for profiling a dataset before
any analysis begins. The goal is to produce a **dataset profile document**
that records your understanding of the data and becomes permanent reference
material for the project.

Do not skip phases. Do not jump to regressions. The boring profiling work
done here prevents data quality bugs from surfacing three weeks into the
analysis.

## Critical Rules

- Use `tidyverse` for all data manipulation (only `data.table` for large datasets)
- Use `arrow` for reading Parquet files, `fread()` for CSV
- All R code should be shown to the user and explained
- Do NOT modify the raw data files — profiling is read-only
- Ask the user before writing any files
- If a codebook or data dictionary accompanies the dataset, read it first

## Phase 1: Structure Discovery

Before looking at any numbers, understand what you are dealing with.

### 1.1 File-level information
```r
# Format, size, dimensions
file.info("path/to/data")
dt <- fread("path/to/data")  # or read_parquet()
dim(dt)
```

Report: file format, file size, number of rows, number of columns.

### 1.2 Column inventory
```r
# Names, types, first few values
str(dt)
head(dt)
sapply(dt, class)
```

Produce a column inventory table:

| Column | Type | Example Values | Apparent Purpose |
|--------|------|---------------|-----------------|
| ... | ... | ... | ... |

For each column, make an initial guess about what it represents based on
the name and values. Flag any ambiguous names.

### 1.3 Candidate identifiers

Look for columns that might serve as row identifiers or panel keys:
- Columns with "id", "code", "key", "ticker", "permno", "gvkey", "cusip"
  in the name
- Date/time columns
- Columns with high cardinality relative to row count

```r
# Check cardinality of candidate identifiers
dt[, .(n_unique = uniqueN(.SD[[1]])), .SDcols = candidate_cols]
```

## Phase 2: Unit of Observation

This is the most important phase. Get this wrong and every subsequent
analysis is built on sand.

### 2.1 Identify the unit

State a hypothesis: "Each row appears to represent a [firm-year /
well-month / trade / person-quarter / ...]"

### 2.2 Test the hypothesis

```r
# Test whether candidate key is unique
candidate_key <- c("firm_id", "year")
n_total <- nrow(dt)
n_unique <- uniqueN(dt, by = candidate_key)
cat(sprintf("Rows: %d | Unique keys: %d | Duplicates: %d\n",
            n_total, n_unique, n_total - n_unique))
```

If duplicates exist, investigate:
```r
# Show examples of duplicate keys
dupes <- dt[duplicated(dt, by = candidate_key) |
            duplicated(dt, by = candidate_key, fromLast = TRUE)]
head(dupes[order(candidate_key)], 20)
```

### 2.3 Characterise panel structure (if panel data)

```r
# Entities and time periods
n_entities <- uniqueN(dt, by = "firm_id")
n_periods  <- uniqueN(dt, by = "year")
cat(sprintf("Entities: %d | Periods: %d | Expected if balanced: %d | Actual: %d\n",
            n_entities, n_periods, n_entities * n_periods, nrow(dt)))

# Entry and exit
entity_spans <- dt[, .(first = min(year), last = max(year), n_obs = .N),
                   by = firm_id]
summary(entity_spans)
```

Report:
- Is the panel balanced or unbalanced?
- What is the time range?
- What is the distribution of observations per entity?
- Is there entry/exit (entities appearing/disappearing)?

## Phase 3: Variable Profiling

Profile every variable. For datasets with many columns (>30), profile all
identifier and key variables, then ask the user which remaining variables
to profile in detail.

### 3.1 Continuous variables

For each continuous variable, report:

```r
dt[, .(
  n        = .N,
  n_miss   = sum(is.na(var)),
  pct_miss = round(100 * mean(is.na(var)), 1),
  mean     = round(mean(var, na.rm = TRUE), 4),
  sd       = round(sd(var, na.rm = TRUE), 4),
  min      = min(var, na.rm = TRUE),
  p1       = quantile(var, 0.01, na.rm = TRUE),
  p25      = quantile(var, 0.25, na.rm = TRUE),
  median   = median(var, na.rm = TRUE),
  p75      = quantile(var, 0.75, na.rm = TRUE),
  p99      = quantile(var, 0.99, na.rm = TRUE),
  max      = max(var, na.rm = TRUE)
)]
```

Flag:
- Variables with >10% missing values
- Extreme outliers (p1/p99 far from p25/p75)
- Values that suggest coding anomalies (-99, -999, 999999 as missing)
- Variables where min/max suggests wrong units (e.g., percentages
  stored as decimals vs. whole numbers)
- Zero-inflated distributions

### 3.2 Categorical / factor variables

For each categorical variable:

```r
# Frequency table (top values + count)
dt[, .N, by = var][order(-N)][1:min(.N, 15)]
# Number of distinct values
uniqueN(dt$var)
```

Flag:
- Categories with very few observations (<5)
- Suspiciously similar categories (typos, encoding issues)
- Missing value patterns (NA vs. empty string vs. "N/A")

### 3.3 Date / time variables

```r
dt[, .(
  min_date = min(date_var, na.rm = TRUE),
  max_date = max(date_var, na.rm = TRUE),
  n_miss   = sum(is.na(date_var)),
  n_unique = uniqueN(date_var)
)]
```

Flag:
- Gaps in date sequences
- Dates outside plausible range
- Inconsistent date formats within the column

### 3.4 Missingness patterns

```r
# Overall missingness by column
miss <- dt[, lapply(.SD, function(x) round(100 * mean(is.na(x)), 1))]
sort(unlist(miss), decreasing = TRUE)
```

Flag:
- Columns that are entirely or almost entirely missing
- Correlated missingness (variables missing together — may indicate
  the data comes from different sources or vintages)

## Phase 4: Relationships and Red Flags

### 4.1 Identifier consistency

- Are identifier formats consistent (e.g., all CUSIPs 8 characters)?
- Do identifiers match expected formats for standard datasets
  (PERMNO for CRSP, GVKEY for Compustat, API number for wells)?
- Are there identifiers that change over time for the same entity?

### 4.2 Logical consistency checks

```r
# Examples of checks — adapt to the specific dataset
dt[price < 0]                          # Negative prices
dt[percentage > 100 | percentage < 0]  # Out-of-range percentages
dt[start_date > end_date]              # Inverted date ranges
dt[age < 0 | age > 150]               # Impossible ages
```

### 4.3 Cross-variable relationships

For key variable pairs, check whether relationships make sense:
```r
# Correlation matrix for key continuous variables
cor(dt[, .(var1, var2, var3)], use = "pairwise.complete.obs")
```

### 4.4 Merge feasibility

If the data will be merged with standard datasets, check identifier
compatibility:
- CRSP: PERMNO (integer), CUSIP (8-char), date format
- Compustat: GVKEY (6-char), CUSIP (9-char with check digit)
- WellDatabase: API number format
- WRDS: Common linking tables available?

## Phase 5: Profile Document

After completing all phases, produce a structured Markdown profile
document. Read `references/profile-template.md` for the full template.

Save the profile at: `[project_root]/data/processed/dataset_profile.md`
(or wherever the user prefers — ask before writing).

This document becomes institutional memory for the project. It should
be comprehensive enough that someone unfamiliar with the data can read
it and understand what they're working with.

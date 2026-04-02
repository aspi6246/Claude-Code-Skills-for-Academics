# Dataset Profile Template

Use this template to produce the final profile document. Adapt sections
as needed for the specific dataset — not every section will be relevant
to every dataset. Ask the user before writing the file.

Suggested location: `[project_root]/data/processed/dataset_profile.md`

---

```markdown
# Dataset Profile: [Dataset Name]

**Profiled on:** YYYY-MM-DD
**Source:** [Where the data came from — database, provider, web scrape, etc.]
**File(s):** [Filename(s) and format(s)]
**File size:** [On disk]
**Rows:** [N]
**Columns:** [N]

---

## 1. Unit of Observation

**Each row represents:** [e.g., "a firm-year observation"]

**Panel key:** `[var1]` × `[var2]` (e.g., `firm_id` × `year`)

**Key uniqueness:** [Unique / N duplicates found — explain if duplicates]

**Panel structure:**
- Entities: [N unique]
- Time periods: [N unique, range from X to Y]
- Balance: [Balanced / Unbalanced — if unbalanced, describe pattern]
- Obs per entity: [median, min, max]
- Entry/exit: [Description of pattern]

---

## 2. Variable Dictionary

### Identifiers

| Variable | Type | Description | Unique Values | Missing |
|----------|------|-------------|--------------|---------|
| ... | ... | ... | ... | ...% |

### Key Outcome Variables

| Variable | Type | Description | Mean | SD | Min | Median | Max | Missing |
|----------|------|-------------|------|-----|-----|--------|-----|---------|
| ... | ... | ... | ... | ... | ... | ... | ... | ...% |

### Key Explanatory Variables

| Variable | Type | Description | Mean | SD | Min | Median | Max | Missing |
|----------|------|-------------|------|-----|-----|--------|-----|---------|
| ... | ... | ... | ... | ... | ... | ... | ... | ...% |

### Control Variables

| Variable | Type | Description | Mean | SD | Min | Median | Max | Missing |
|----------|------|-------------|------|-----|-----|--------|-----|---------|
| ... | ... | ... | ... | ... | ... | ... | ... | ...% |

### Categorical Variables

| Variable | Type | Description | N Categories | Top Categories | Missing |
|----------|------|-------------|-------------|----------------|---------|
| ... | ... | ... | ... | [list top 3-5] | ...% |

### Date / Time Variables

| Variable | Type | Format | Range | Gaps? | Missing |
|----------|------|--------|-------|-------|---------|
| ... | ... | ... | X to Y | Yes/No | ...% |

---

## 3. Missingness Summary

| Variable | % Missing | Pattern Notes |
|----------|-----------|---------------|
| ... | ... | [e.g., "missing before 2005", "correlated with var_x"] |

**Correlated missingness:** [Note any variables that tend to be missing
together and what this might indicate]

---

## 4. Data Quality Flags

### Outliers and Anomalies

| Variable | Issue | Details | Recommendation |
|----------|-------|---------|----------------|
| ... | [e.g., "extreme outliers"] | [p1=X, p99=Y] | [e.g., "winsorise at 1/99"] |

### Coding Issues

| Variable | Issue | Details | Recommendation |
|----------|-------|---------|----------------|
| ... | [e.g., "-99 used as missing"] | [N instances] | [e.g., "recode to NA"] |

### Logical Inconsistencies

| Check | Violations | Details |
|-------|-----------|---------|
| [e.g., "price >= 0"] | [N rows] | [description] |

---

## 5. Merge Feasibility

### Available identifiers for linking

| Target Dataset | Linking Variable | Format | Coverage | Notes |
|---------------|-----------------|--------|----------|-------|
| [e.g., CRSP] | [e.g., PERMNO] | [format] | [% non-missing] | ... |

### Known linking issues

[Note any identifier format mismatches, time coverage gaps, or
linking table requirements]

---

## 6. Key Descriptive Findings

[2-5 paragraphs summarising the most important things learned from
profiling. What is surprising? What needs attention before analysis?
What assumptions about the data turned out to be wrong?]

---

## 7. Recommendations Before Analysis

In order of priority:

1. [ ] [Most critical data cleaning step]
2. [ ] [Second priority]
3. [ ] [Third priority]
...

---

## 8. Sample Construction Notes

[If the user has discussed sample filters, treatment definitions, or
variable construction during profiling, record those decisions here
so they're not lost. This section may be empty after initial profiling
and filled in during analysis.]
```

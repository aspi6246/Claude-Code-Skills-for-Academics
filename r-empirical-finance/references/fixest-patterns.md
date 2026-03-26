# fixest Advanced Patterns Reference

This file is supplementary reference material for the `r-empirical-finance`
skill. Read this file when the user needs advanced fixest functionality
beyond the basics covered in SKILL.md.

## Multi-way fixed effects

```r
# Three-way FE
est <- feols(y ~ x | firm_id + year + industry_code, data = dt, vcov = ~firm_id)

# Interacted fixed effects (firm x quarter)
est <- feols(y ~ x | firm_id^quarter, data = dt, vcov = ~firm_id)
```

## Stepwise estimation

```r
# Run multiple specifications at once
est_sw <- feols(y ~ x1 + csw(x2, x3, x4) | firm_id + year,
                data = dt, vcov = ~firm_id)
# csw  = cumulative stepwise (adds one variable at a time)
# sw   = non-cumulative stepwise (swaps variables)
etable(est_sw)
```

## Split samples

```r
# Estimate by subgroup
est_split <- feols(y ~ x | firm_id + year,
                   data = dt, vcov = ~firm_id,
                   split = ~size_tercile)
etable(est_split)
```

## Nonlinear models

```r
# Poisson pseudo-maximum likelihood (gravity models, count data)
est_ppml <- fepois(count_y ~ x1 + x2 | firm_id + year,
                   data = dt, vcov = ~firm_id)

# Logit with fixed effects
est_logit <- feglm(binary_y ~ x1 + x2 | firm_id + year,
                   data = dt, family = binomial, vcov = ~firm_id)
```

## Lag and lead operators

```r
# Within-panel lags and leads
est <- feols(y ~ l(x, 1) + l(x, -1) | firm_id + year,
             data = dt, vcov = ~firm_id,
             panel.id = ~firm_id + year)
# l(x, 1)  = one-period lag
# l(x, -1) = one-period lead
# l(x, 1:3) = lags 1 through 3
```

## Two-way clustering

```r
# Cluster by firm and year
est <- feols(y ~ x | firm_id + year,
             data = dt, vcov = ~firm_id + year)

# Conley spatial standard errors (if applicable)
# Use the conley() function with coordinates
```

## Wald tests and coefficient comparisons

```r
# Test linear hypotheses
wald(est, "x1 = x2")

# F-test for joint significance
wald(est, c("x1", "x2"))
```

## First stage diagnostics for IV

```r
est_iv <- feols(y ~ controls | firm_id + year | x_endog ~ z1 + z2,
                data = dt, vcov = ~firm_id)

# First stage F-statistic
summary(est_iv, stage = 1)

# Effective F-statistic (Olea & Pflueger, 2013)
fitstat(est_iv, "ivf")
```

## etable formatting for publication

```r
etable(est1, est2, est3,
       vcov = "cluster",
       # Rename variables for display
       dict = c(x1 = "Treatment",
                x2 = "Firm Size (log)",
                x3 = "Leverage"),
       # Control which stats appear
       fitstat = ~r2 + n + ar2,
       # Drop specific coefficients from display
       drop = "controls_",
       # Add significance note
       signif.code = c("***" = 0.01, "**" = 0.05, "*" = 0.10),
       # Output to LaTeX
       tex = TRUE,
       file = "output/tables/results.tex",
       # Style
       style.tex = style.tex("aer"))
```

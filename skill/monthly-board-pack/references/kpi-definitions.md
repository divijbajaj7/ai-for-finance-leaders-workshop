# KPI definitions

| KPI | Definition (source columns) |
|---|---|
| Revenue | Sum of `Type = Revenue` |
| Total costs | Sum of `Type = Cost` (negative numbers) |
| EBITDA | Sum of all lines except `Type = Below EBITDA` (includes `Other`, e.g. FX) |
| Net result | Sum of all lines |
| Variance | Actual − Budget (positive = favourable for all lines) |
| Variance % | Variance / abs(Budget); "n/a" when Budget = 0 |
| Material | abs(Variance) ≥ absolute threshold OR abs(Variance %) ≥ % threshold |
| YTD | Sum of months from the first month in the file to the reporting month |

## Volume / price split (when volume and price columns exist)
- Volume effect = (Actual volume − Budget volume) × Budget price
- Price effect = (Actual price − Budget price) × Actual volume
- Check: volume effect + price effect = total variance (compute, don't assume).

## Intercompany
Lines containing `(IC)` appear twice, once in each division, with opposite signs. They net to zero at group level.

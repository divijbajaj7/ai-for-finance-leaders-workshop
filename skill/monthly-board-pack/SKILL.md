---
name: monthly-board-pack
description: Turns an uploaded budget-vs-actual workbook into a monthly board pack, with code-calculated variances and KPIs, house-style management commentary, an interactive dashboard artifact and an 8–10 slide .pptx board deck. Use when the user asks for a "board pack", "monthly management pack", "month-end pack", "variance commentary for the board", or uploads budget vs actual / BvA / management accounts data and wants findings, a dashboard or slides.
---

# Monthly Board Pack

Turns one budget-vs-actual file into four outputs: KPI summary, house-style commentary, interactive dashboard, board deck.
Accuracy beats speed. **Every number comes from code run on the source rows. Never do arithmetic in your head.**

## Inputs
- An .xlsx or .csv with columns `Month, Division, Line item, Type, Budget, Actual` (preferably in a sheet named `Monthly_Detail`).
  - `Type` ∈ Revenue / Cost / Other / Below EBITDA. Costs are stored as negatives.
- Optional from the user: reporting month (default = latest month in file), entity name, materiality overrides, audience.

## Workflow

### 1. Validate the input
- Run `python scripts/compute_variances.py <file> --out result.json` (add `--month`, `--pct`, `--abs` if the user gave them).
- If the script reports missing columns, show the user which columns were found and ask them to map them. Do not guess.
- Tell the user in one line: sheet used, row count, months covered, reporting month.

### 2. Compute variances & KPIs (code only)
- `Variance = Actual − Budget`. Positive = Favourable (F) for every line, because costs are negative.
- KPIs: Revenue, Total costs, EBITDA (all lines except `Below EBITDA`), Net result. Month and YTD.
- Definitions are in `references/kpi-definitions.md`.

### 3. Apply materiality
- Default: material if |variance| ≥ **MUR 5.0m (5,000 in MUR '000)** OR |variance %| ≥ **10%**.
- Zero-budget lines: absolute test only, % shown as "n/a".
- Lines tagged `(IC)` are intercompany. Mention that they eliminate on consolidation and don't count them as group drivers.

### 4. Write the commentary in house style
Follow `references/house-style.md` exactly. In short:
- **Headline** (1 sentence, group EBITDA vs budget and the top 2–3 drivers).
- **By division:** each material item as **Driver → Impact → Action**.
- **Watch list:** 2–4 items that are not yet material but are trending (use the monthly trend).
- MUR m to 1 decimal; favourable `MUR 12.0m F`, adverse `(MUR 26.7m) A`; ≤ 250 words.
- **No speculation beyond the data.** If the cause is not in the file, write "driver to confirm with <division>".
- Where volume and price data exist (e.g. an Operational_KPIs sheet), split revenue/cost variances into volume and price effects **in code** before writing.

### 5. Build the interactive dashboard (artifact)
Single-page HTML artifact with: KPI cards (budget, actual, variance, %), EBITDA bridge/waterfall (material lines + "Other"), monthly EBITDA budget-vs-actual trend, flagged-variance table with RAG pills, and the commentary.
Embed the computed numbers from `result.json`. Do not recompute in prose.

### 6. Build the board deck (.pptx)
- Write the commentary pieces to `commentary.json` (`headline`, `divisions{name:[bullets]}`, `risks[]`, `next_steps[]`).
- Run `python scripts/build_deck.py result.json commentary.json board_pack.pptx --entity "<name>"`.
- The slide structure (8–10 slides: one divisional slide per division with a material item) and styling are in `references/slide-spec.md` (navy #1E3A5F, blue #2563EB, Arial).
- Render the deck to images if a converter is available and check for overflow before handing it over.

### 7. Self-check before replying
- [ ] Group totals in the commentary equal `result.json` KPIs (Month and YTD).
- [ ] Every number in the commentary, dashboard and deck traces to a source row or a script output.
- [ ] Each material item appears exactly once, with F/(A) correct.
- [ ] Intercompany lines are flagged, not presented as group drivers.
- [ ] No driver is stated that the data does not support. Unknowns are marked "to confirm".
- [ ] Word count ≤ 250 for the commentary.

## Output to the user
1. 3-line summary (EBITDA vs budget, top drivers, number of material items).
2. The commentary (house style).
3. Dashboard artifact link.
4. The .pptx file.
5. "Open questions for divisions": the list of "to confirm" items.

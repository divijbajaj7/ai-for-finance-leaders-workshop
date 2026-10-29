# AI for Finance Leaders: Learner Prompt Pack

All examples use **ICE Group**, a fictional sugar, energy and property group. Every figure is synthetic, and nothing in it is confidential. Figures are MUR '000.

**Workshop files:** [INSERT SHARED FOLDER LINK]
- `ICE_Group_Budget_vs_Actual_Sep2026.xlsx`: budget vs actual, monthly detail, KPIs, Q4 drivers
- `ICE_Past_Commentaries.docx`: two approved commentaries (house style)
- `ICE_Sugar_Trial_Balance_Sep2026.xlsx`: trial balance + target balance sheet format
- `ICE_Intercompany_Sep2026.xlsx`: intercompany ledgers + policy notes

**The 6-part prompt formula:** Role · Task · Context · Constraints · Format · Examples

**The 4 token habits:** ① New chat per topic ② Edit, don't append ③ Right model for the job ④ Batch your questions

## ★ BUILD-ALONG: Variance Analyzer app

**Step 1.** Open a new chat in Claude.

**Step 2.** Copy the whole prompt below and paste it in.

```
Build me an interactive web app (React artifact) called "Variance Analyzer" for a finance team.

CONTEXT
Users are FP&A analysts. They upload a monthly budget-vs-actual Excel file with a sheet "Monthly_Detail" and the columns: Month, Division, Line item, Type, Budget, Actual. Figures are MUR '000; revenue positive, costs negative; Type is Revenue / Cost / Other / Below EBITDA.

FEATURES
1. Upload .xlsx or .csv (use SheetJS). Show a clear error if columns are missing.
2. Controls: Month dropdown (default latest), Month vs Year-to-date toggle, Division filter, and two materiality thresholds: % (default 10) and absolute MUR '000 (default 5,000). A line is material if it breaches EITHER. For zero-budget lines, use only the absolute test and show % as "n/a".
3. Calculate everything in JavaScript, never estimate: Variance = Actual − Budget (positive = favourable for revenue and cost). Var % = Variance / |Budget|.
4. KPI cards: Revenue, Total costs, EBITDA (exclude "Below EBITDA" rows), Net result. Each shows budget, actual, variance and %.
5. Variance table: sortable, with a RAG flag (red = material adverse, green = material favourable, grey = immaterial). Tag lines containing "(IC)" as "eliminates on consolidation".
6. Charts (Recharts): an EBITDA bridge (waterfall) from budget EBITDA through each material variance to actual EBITDA, grouping the rest as "Other"; and a monthly EBITDA budget-vs-actual line chart.
7. A "Draft commentary" button that uses Claude to write Driver → Impact → Action bullets for each material line, max 200 words, using only the numbers in the table and writing "driver to confirm" where the cause isn't in the data. Show it in a text box with a Copy button.
8. Export flagged items to CSV.

DESIGN
Clean and professional, navy and white. Numbers right-aligned with thousand separators and negatives in brackets. Fits a laptop screen.
```
**Step 3.** When the app appears, upload `ICE_Group_Budget_vs_Actual_Sep2026.xlsx` into it, select Sep-26, and check the results. Your Sep-26 EBITDA should show **418,600 budget vs 321,990 actual**.
**Follow-up prompts to try** (one at a time, using **Edit** if it breaks):
```
Add a price/volume split for Sugar sales and Coal costs using the Operational_KPIs sheet.
```
```
The waterfall is hard to read. Sort the bars from largest adverse to largest favourable and label each bar in MUR m.
```

---


# All prompts from today, in order

## Demo 1: Variance commentary, weak vs strong (the 6-part formula)

**Upload:** `ICE_Group_Budget_vs_Actual_Sep2026.xlsx`

### 1A · Weak prompt 
```
Explain the variances in this file.
```

### 1B · Strong prompt 
```
ROLE
You are a senior FP&A analyst at ICE Group, a sugar, energy and property group. You write the monthly variance commentary for the Group Finance Director.

TASK
Write the September 2026 variance commentary using the sheet "BvA_Sep2026" (month columns only).

CONTEXT
- Figures are MUR '000. Revenue is positive, costs are negative. Variance = Actual − Budget; positive = favourable.
- Lines marked (IC) are intercompany and eliminate on consolidation. Mention them in one line only.
- Volume and price drivers are in the sheet "Operational_KPIs".
- The reader is the Group FD: financially expert, short on time.

CONSTRAINTS
- Only comment on variances ≥ MUR 5,000k OR ≥ 10% of budget. For zero-budget lines, use the absolute test only.
- Use only the data provided. If the cause is not in the data, write "Driver: to confirm with division". Do not guess.
- Where volume and price data exist, split the variance into a volume effect and a price effect and show the calculation.
- Do the arithmetic with code, not in your head.
- Maximum 300 words, excluding the table.

FORMAT
1. Headline: one sentence on Group EBITDA vs budget (MUR m, 1 decimal, %).
2. By division: EBITDA actual vs budget, then each material line as Driver → Impact → Action.
3. Watch list: 3 bullets.
4. Table of material variances: Line | Budget | Actual | Var | Var % | F/(A).

EXAMPLE OF ONE BULLET
- Coal costs: MUR 8.1m (A). Driver: coal price MUR 6,950/t vs 6,600/t budget. Impact: margin pressure on fixed-tariff exports. Action: Procurement to review hedging for Q4 cargoes.
```

### 1C · Three audiences (follow-up in the same chat)
```
Using the analysis above, write three versions. Do not change any number.
A) Board of Directors: 5 bullets, max 120 words, strategic, no accounting jargon. Focus on full-year impact and decisions needed.
B) Head of Energy: only the Energy lines, operational detail, specific actions with owners, max 150 words.
C) Audit & Risk Committee: judgements, one-offs, timing differences, FX exposure and control points. Neutral tone, max 150 words.
Put each under a heading.
```
---


## Demo 2: Few-shot prompting (show, don't describe)

### 2A · House-style commentary
**Upload:** `ICE_Group_Budget_vs_Actual_Sep2026.xlsx` + `ICE_Past_Commentaries.docx` (new chat)

Weak:
```
Write the September management commentary in our usual style.
```
Strong:
```
The attached document contains two approved management commentaries (July and August 2026). They are examples of our house style.

Write the September 2026 commentary in exactly the same style, using the sheets BvA_Sep2026 and Operational_KPIs. Match:
- the structure (Headline → divisions → Watch list → sign-off),
- the materiality rule stated in the examples,
- the tone, length and number formatting (MUR m, 1 decimal, F/(A)).
Where the driver is not in the data, write "Driver: to confirm with division".
```
### 2B · "Put my balance sheet in this format"
**Upload:** `ICE_Sugar_Trial_Balance_Sep2026.xlsx` (new chat)

Weak:
```
Make a balance sheet from this trial balance.
```
Strong:
```
Attached is the trial balance of ICE Sugar Ltd at 30 Sep 2026 (sheet "Trial_Balance"). The sheet "Target_BS_Format" contains our approved balance sheet layout with the Dec-2025 figures as an example.

Task: produce the 30 Sep 2026 Statement of Financial Position in exactly the Target_BS_Format layout, with Dec-2025 as the comparative column.
Rules:
- Follow the HOUSE RULES listed at the bottom of Target_BS_Format.
- The TB still contains YTD P&L accounts (codes 4xxx–7xxx). Calculate profit for the period and add it to retained earnings brought forward.
- Show a mapping table: every TB account → balance sheet line. No account may be left unmapped.
- Show the balance check (Total assets − Total equity & liabilities = 0).
- Do all arithmetic with code.
```
---


## Demo 3: Chain of thought (intercompany reconciliation), run step by step

**Upload:** `ICE_Intercompany_Sep2026.xlsx` (new chat)

Weak:
```
Why don't these intercompany balances match?
```

### Option A: one step per message
Send these one at a time and pause after each to discuss with the room.
```
You are a group consolidation accountant. The attached file has September 2026 ledgers for two ICE Group subsidiaries, an extract of ICE Energy's third-party payables, and group policy notes. We will reconcile the intercompany balance step by step. Do only Step 1 now, and show your working.

Step 1: State both closing balances and the difference.
```
```
Step 2: Match the transactions across the two ledgers by reference. List the matched items and the unmatched items.
```
```
Step 3: For each unmatched item or amount difference, classify the cause as Timing, FX, Mis-coding or Other. Cite the ledger row and the policy note that applies. Check the third-party payables extract too.
```
```
Step 4: Prove it. Show that the unmatched items add up exactly to the difference. If they don't, say so.
```
```
Step 5: Propose the correcting journal entries (entity, Dr/Cr, account, amount) and 3 control checks to stop this recurring. Finish with a summary table: Item | Amount (MUR '000) | Cause | Entity to correct | Entry.
```

### Option B: the same thing as one chain-of-thought prompt
```
You are a group consolidation accountant. Attached are September 2026 ledgers for two ICE Group subsidiaries, an extract of ICE Energy's third-party payables, and group policy notes.

Reconcile the intercompany balance step by step. Show your working at each step before moving on:
Step 1: State both closing balances and the difference.
Step 2: Match transactions across the two ledgers by reference.
Step 3: Classify each unmatched item as Timing, FX, Mis-coding or Other, citing the ledger row and the policy note.
Step 4: Prove that the unmatched items add up exactly to the difference. If they don't, say so.
Step 5: Propose correcting journal entries (entity, Dr/Cr, account, amount) and 3 control checks.
Finish with a summary table: Item | Amount (MUR '000) | Cause | Entity to correct | Entry.
```
---


## Demo 4: Tree of thought (Q4 cash scenarios)

**Upload:** `ICE_Group_Budget_vs_Actual_Sep2026.xlsx` (sheet `Q4_Forecast_Drivers`)

Weak:
```
Give me a Q4 forecast with best and worst case.
```
Strong:
```
I need a Q4 2026 cash outlook for ICE Group, using the sheet "Q4_Forecast_Drivers" (base budget, opening cash, minimum buffer, overdraft, driver ranges). Treat the P&L lines as cash flows and ignore working capital. State this as an assumption.

Use a Tree of Thought approach:
1. Three independent analysts each build one branch:
   - Analyst A: Base case
   - Analyst B: Downside (drought continues, coal and USD stay high)
   - Analyst C: Upside (prices hold, crop recovers)
   Each lists EVERY assumption explicitly (sugar price, cane crushed, coal price, USD/MUR, GWh, land-sale timing), using only the ranges in the sheet, and calculates closing cash for Oct, Nov and Dec.
2. Each analyst critiques the other two branches: which assumption is weakest, and why?
3. As CFO, compare the branches. Recommend which case to plan on, and say whether the MUR 75m minimum buffer or the overdraft is at risk in any month.
4. Sensitivity table: effect on Dec closing cash of ±10% sugar price, ±10% coal price, ±1.0 USD/MUR, and the land sale slipping to Jan-27.
Do all calculations in code. Label clearly what is data and what is assumption.
```
---


## Demo 5: Verification and reviewer prompts

### 5A · Technical accounting + "least certain" follow-up
```
Two of our subsidiaries both have MUR as their functional currency. One invoiced the other a USD 150,000 management fee. The issuer recorded it at the invoice-date rate (45.20). The receiver recorded it at the month-end rate (46.10). Under IFRS (IAS 21), what is the correct treatment at month-end in each entity's books, and what happens on consolidation?
```
Then:
```
Which parts of your answer are you least certain about? List the specific IAS 21 paragraphs I should verify, and anything that depends on facts you don't have.
```
### 5B · Reviewer mode (anomaly review)
```
Act as a sceptical financial controller reviewing the sheet "Monthly_Detail" (Jan–Sep 2026). Flag up to 5 unusual movements or trends. For each one:
- cite the exact rows (Month, Line item),
- quantify the movement,
- rate your confidence (High / Medium / Low),
- give the question you would ask the division.
If something cannot be explained from the data, write "Not enough information". Do not flag anything you cannot point to in the data.
```
### 5C · Safe prompting
Before pasting bid or tender data: replace names with placeholders (Bidder A, Project X), scale or round the figures (×0.8, or index to 100), and remove contract IDs. Check the workspace data settings: is training on your data off? Is this the company-approved tenant?

---


## Demo 6: Token economics (rambling vs tight)

**Rambling (chat 1), then three follow-ups:**
```
Hi! Hope you're well. So I've got this file, it's our budget vs actual stuff for the group, there's a lot in there, sugar, energy, property and so on. Could you maybe have a look and tell me what's going on? My boss wants to know about the variances I think, mostly September but maybe also year to date, not sure. Also can you make it look nice? And maybe mention coal because I think coal is a problem. Actually also FX. Thanks so much!!
```
```
Actually only September please.
```
```
Shorter.
```
```
Use MUR millions.
```
**Tight (chat 2), one message:**
```
Using BvA_Sep2026 (Sep-26 month columns only): list the 5 largest adverse variances as a table (Line | Var MUR m | Var %), then one sentence each on the driver, using only data in the file. Max 150 words.
```
**The 4 habits:** ① New chat per topic ② Edit, don't append ③ Right model for the job ④ Batch your questions.

---


## Demo 7: Build your own Claude project

1. Claude → **Projects → New project** → name: `ICE Group – Month-end Close`
2. **Project instructions:** paste this:
```
You support the Group Finance team of ICE Group (sugar, energy, property). Figures are MUR '000 unless stated.

Always:
- Materiality: comment only on variances ≥ MUR 5m or ≥ 10% of budget. Zero-budget lines use the absolute test only.
- Do all arithmetic with code and show that totals tie back to the source.
- Never speculate beyond the data. Write "to confirm with division" or "not enough information".
- Write commentary in the house style shown in ICE_Past_Commentaries.
- Intercompany reconciliations: follow the 5 steps: (1) balances and difference (2) match by reference (3) classify unmatched items as Timing / FX / Mis-coding / Other, citing the row and policy (4) prove the difference (5) correcting entries + 3 control checks. End with a summary table.
- Balance sheets: use the layout and house rules in the Target_BS_Format sheet.
- Apply the group policy notes in the knowledge files.
```
3. **Knowledge:** upload `ICE_Past_Commentaries.docx`, `ICE_Sugar_Trial_Balance_Sep2026.xlsx` (for the template), and `ICE_Intercompany_Sep2026.xlsx` (it contains the policy notes).
4. New chat inside the project, upload the IC ledger, and type only:
```
Reconcile the September intercompany balances.
```
---


## Demo 9: Skills
A skill packages your house style, rules and steps so Claude can use them in any chat. Ask your facilitator for the `monthly-board-pack` example, then open a new chat, upload the data, and type:
```
Prepare the September 2026 board pack.
```


---
**Your one next step:** pick one task you do every month. Write it as a 6-part prompt, test it on anonymised data, and save it as a project.

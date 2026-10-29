# Prompt Run-Sheet: AI for Finance Leaders (3 hours)

Copy and paste these live, in this order. Each block lists **what to upload**, the prompts, and **what to point out**.
The data is for the fictional company ICE Group. All files are in `datasets/`.

| Time | Block | Demo | Tool |
|---|---|---|---|
| 0:00 | Opening | Hook: weak vs strong (Demo 1, outputs only) | Claude |
| 0:10 | 1 · LLMs | Slides only | — |
| 0:30 | 2 · Prompting | Demo 1 6-part formula → 1b three audiences | Claude + Copilot |
| 0:50 | | Demo 2 few-shot house style → 2b balance sheet in my format | Claude |
| 1:00 | | Demo 3 chain of thought: intercompany recon, step by step | Claude |
| 1:10 | | Demo 4 tree of thought: Q4 cash scenarios | Claude |
| 1:20 | | Demo 5 verification (IFRS) + reviewer mode | Claude / Copilot |
| 1:30 | Break | | |
| 1:40 | 3 · Tokens | Demo 6 rambling vs tight, model choice | Claude + Copilot |
| 2:00 | 4 · Projects | Demo 7 the chain-of-thought prompt becomes a project | Claude |
| 2:10 | Artifacts | Demo 8 build-along Variance Analyzer | Claude (everyone) |
| 2:25 | Skills | Demo 9 board-pack skill: data → dashboard + deck | Claude |
| 2:50 | Wrap | Playbook + Q&A | — |

> **Before the session:** open fresh chats in **Claude** and **Copilot**. Upload `ICE_Group_Budget_vs_Actual_Sep2026.xlsx` once per chat. Have the backup outputs ready (see the Facilitator Guide, section 9).

---

## Demo 1: Variance commentary, weak vs strong (the 6-part formula)

**Upload:** `ICE_Group_Budget_vs_Actual_Sep2026.xlsx`

### 1A · Weak prompt (run in chat 1)
```
Explain the variances in this file.
```

### 1B · Strong prompt (run in chat 2; keep both visible side by side)
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

**Point out:**
- Each block maps to one letter of the formula: **R**ole, **T**ask, **C**ontext, **C**onstraints, **F**ormat, **E**xample.
- Sugar sales look small (−2.9%) but hide **−51.6m volume and +36.7m price**. The weak prompt usually misses this.
- Harvest & transport: the data doesn't explain the overrun. A good output says *"to confirm with division"* instead of inventing a reason.
- FX has a zero budget, so the % is meaningless. The rule we wrote handles it.
- **Run 1B in Copilot too**, the same prompt, and compare. *"The prompt is the skill, not the tool."*

### 1C · Three audiences (follow-up in chat 2)
```
Using the analysis above, write three versions. Do not change any number.
A) Board of Directors: 5 bullets, max 120 words, strategic, no accounting jargon. Focus on full-year impact and decisions needed.
B) Head of Energy: only the Energy lines, operational detail, specific actions with owners, max 150 words.
C) Audit & Risk Committee: judgements, one-offs, timing differences, FX exposure and control points. Neutral tone, max 150 words.
Put each under a heading.
```
**Point out:** only the *audience* line changed, and the content, length and vocabulary changed with it. This removes the "rewrite the pack three times" pain from board prep.

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
**Point out:** we never *described* the style ("concise, professional…"). We *showed* it, and two examples beat a paragraph of adjectives. This is also exactly what a **skill** stores later.

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
**Answer key:** total assets **6,681,000**; profit for the period **506,600**; retained earnings **598,000** (91,400 b/f + 506,600); total equity **3,718,000**. See Facilitator Guide §8 for every line.
**Point out:** the weak version usually forgets that P&L accounts must roll into retained earnings, so the balance sheet doesn't balance. The example plus the house rules fix it.

---

## Demo 3: Chain of thought (intercompany reconciliation), run step by step

**Upload:** `ICE_Intercompany_Sep2026.xlsx` (new chat)

Weak:
```
Why don't these intercompany balances match?
```

### Option A (recommended live): one step per message
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

### Option B: the same thing as one chain-of-thought prompt (this becomes the project instruction in Demo 7)
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
**Answer key:** difference **10,165** = **7,100** mis-coding (INV-S-0927 posted to third-party AP) + **3,200** timing (INV-S-0941 received 2 Oct) − **135** FX (USD 150k at 45.20 vs 46.10). After the corrections both sides show **48,735**.

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
**Point out:**
- Chain of thought is **one path** done carefully. Tree of thought is **several paths**, critiqued, then a choice.
- Every assumption is on the table, so the finance team can **challenge it**. That matters for energy and commodity forecasting.
- The base case closes December at **MUR 80.4m, only MUR 5.4m above the MUR 75m buffer** (Oct 111.4m → Nov 101.4m → Dec 80.4m). Almost any downside breaches the buffer, and that's the "aha".

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
**Point out:** make verification a habit, and keep the accountant as the reviewer. Ask in Copilot as well and compare the two answers.

### 5B · Reviewer mode (anomaly review), if time allows
```
Act as a sceptical financial controller reviewing the sheet "Monthly_Detail" (Jan–Sep 2026). Flag up to 5 unusual movements or trends. For each one:
- cite the exact rows (Month, Line item),
- quantify the movement,
- rate your confidence (High / Medium / Low),
- give the question you would ask the division.
If something cannot be explained from the data, write "Not enough information". Do not flag anything you cannot point to in the data.
```
**Expected:** coal cost overrun widening (Jul +6% → Aug +11% → Sep +19%); IT/ERP overrun growing (+20% → +40% → +77%); FX losses growing every month since June; the September land sale missing; sugar price rising while volume falls; the September maintenance spike.

### 5C · Safe prompting (just talk it through, 1 minute)
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
**Point out:**
- Chat 1 re-sent the whole file and conversation **four times**. Chat 2 sent it once, and the answer is better.
- Then show **Edit**: edit the first rambling message into the tight one, and the follow-ups disappear.
- Model choice: run the tight prompt on a lighter model (Haiku or Sonnet in Claude; quick mode in Copilot), then the final board version on the top model.

**The 4 habits:** ① New chat per topic ② Edit, don't append ③ Right model for the job ④ Batch your questions.

---

## Demo 7: From the chain-of-thought prompt to a Claude project

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
**Point out:** the 5-step method now runs from a one-line request, and next month you only upload new ledgers. *"A project is a pre-briefed analyst."*

---

## Demo 8: Artifact build-along (Variance Analyzer)

Share the Google Doc link (it contains the prompt below) and the dataset. Everyone pastes it into a new Claude chat.
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
Then upload `ICE_Group_Budget_vs_Actual_Sep2026.xlsx` **into the app** and check against the answer key: Sep-26 EBITDA **418,600 budget vs 321,990 actual**, **11 material lines**.
**Follow-up prompts to try** (one at a time, using **Edit** if it breaks):
```
Add a price/volume split for Sugar sales and Coal costs using the Operational_KPIs sheet.
```
```
The waterfall is hard to read. Sort the bars from largest adverse to largest favourable and label each bar in MUR m.
```

---

## Demo 9: Skill (monthly board pack)

1. Show the skill (`skill/monthly-board-pack/SKILL.md`): explain it is the house style + KPI rules + slide spec, written down once.
2. Claude → Settings → Capabilities → Skills → upload `monthly-board-pack.zip` (code execution must be on).
3. New chat (no project), upload `ICE_Group_Budget_vs_Actual_Sep2026.xlsx`, type:
```
Prepare the September 2026 board pack.
```
4. Show the dashboard artifact and the .pptx deck it produces.
**Point out:** the **project** gave Claude the *context* for one workspace. The **skill** gives Claude a *procedure* it can use in any chat. The **artifact** is the *output* you share.

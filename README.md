# AI for Finance Leaders: Workshop Materials

Hands-on materials for the 3-hour **AI for Finance Leaders** workshop. Every example uses **ICE Group**, a fictional sugar, energy and property group. All data is synthetic, and figures are in MUR '000.

## What's here

| Path | What it is |
|---|---|
| `Learner_Prompt_Pack.docx` / `.md` | **Start here.** The Variance Analyzer build-along prompt, plus every prompt from the session |
| `Prompt_RunSheet.md` | All demo prompts in session order, weak vs strong, with notes |
| `datasets/ICE_Group_Budget_vs_Actual_Sep2026.xlsx` | Budget vs actual (Sep-26 + YTD), monthly detail, operational KPIs, Q4 forecast drivers |
| `datasets/ICE_Past_Commentaries.docx` | Two approved management commentaries (house style, for few-shot prompting) |
| `datasets/ICE_Sugar_Trial_Balance_Sep2026.xlsx` | Trial balance + target balance sheet format |
| `datasets/ICE_Intercompany_Sep2026.xlsx` | Intercompany ledgers + group policy notes (chain-of-thought reconciliation) |
| `skill/monthly-board-pack.zip` | Claude skill: upload monthly data and get a dashboard and a board deck back |
| `skill/monthly-board-pack/` | The same skill, unzipped so you can read it |
| `backup_artifact/variance_analyzer.html` | A finished Variance Analyzer app. Open it in a browser and click "Load sample data" |

## Using the skill
In Claude, go to **Settings → Capabilities → Skills**, upload `skill/monthly-board-pack.zip` (code execution must be on), then upload the budget-vs-actual file in a new chat and type: *"Prepare the September 2026 board pack."*

## Session flow
1. Understanding LLMs: the 5 steps from tokenisation to response
2. Prompting for finance: the 6-part formula, few-shot, chain of thought, tree of thought
3. Token economics: 4 habits for better answers at lower cost
4. Projects, Artifacts & Skills

# Monthly Budget Planner

A PySide6 desktop application for tracking planned versus actual spending across
budget categories, with live summary totals.

## Running the application

```
uv run budget-planner
```
This launches the `BudgetPlannerWindow`, which displays four budget category
panels (Housing, Food, Transportation, Savings) along with an **Update summary**
button and summary cards for total planned, total actual, and remaining amounts.

Two standalone test entry points are also available for the individual widgets:

```
uv run single-panel
uv run single-card
```

## Data persistence

All budget data entered into the application exists **only in memory** for the
duration of the running program. Nothing is written to disk, so planned amounts,
actual amounts, and checkbox/combo-box selections are reset each time the
application is restarted.

## Branches

- `m2/human/budget-ui` — the frozen, student-only baseline. All application
  code and documentation on this branch were written without generative-AI
  assistance.
- `m2/ai/budget-finalization` — the AI-assisted finalization branch, built on
  top of the human baseline. AI assistance on this branch is scoped to visual
  styling (`style.qss`), this README, and narrowly-requested, targeted fixes,
  as defined in `CLAUDE.md`.

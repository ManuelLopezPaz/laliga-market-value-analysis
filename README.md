# Does the Football Transfer Market Reward Performance or Potential?
### A La Liga Analysis Using Expected Goals and Market Valuations (2014–2024)
**Manuel López Paz** | 2026
Performance data from understat.com · Market valuations from Transfermarkt (Kaggle)
---
## Research Questions
1. Which performance metrics best predict player market value in La Liga?
2. Does xG predict market value better than raw goals — has the transfer
   market shifted toward valuing underlying performance over results?
---
## Key Findings
- **xG and goals predict market value almost equally well**: Model 1
  (traditional metrics) achieves R² = 0.268 and Model 2 (xG/xA) achieves
  R² = 0.266 — the market has not clearly shifted toward rewarding
  underlying performance over results
- **xA per 90 is the strongest performance predictor** (β = 2.57 in
  Model 4) — creative players who generate chances for teammates are
  valued more highly than pure finishers
- **Age is the most important variable overall**: adding age and age²
  raised R² from 0.278 to 0.406 — a jump of 12.8 percentage points
- **Peak market value occurs at around 19-20 years old**, suggesting
  the transfer market prices in future potential more than current form
- When goals and xG are in the same model, xG loses significance
  (correlation = 0.88) — the two variables are too similar to separate
---
## Dataset
| Field | Detail |
|---|---|
| Performance source | understat.com (scraped via POST API) |
| Valuation source | Transfermarkt — davidcariboo/player-scores (Kaggle) |
| League | La Liga (ES1) |
| Period | 2014/15 – 2024/25 (11 seasons) |
| Observations | 2,679 player-seasons (after filters) |
| Filters applied | Market value >= €500,000 · Minutes >= 450 · No goalkeepers |
---
## Methods
- Data scraping (requests + json) and dataset merge (exact + fuzzy name matching)
- Log transformation of market value (dependent variable)
- Four progressive OLS regression models
- Per-90 performance metrics (xG, xA, goals, assists)
- Quadratic age term to capture non-linear relationship with market value
---
## Repository Structure
---
## Limitations
- R² = 0.406 — 60% of market value variance is unexplained (injury
  history, contract length, and media profile are not in the dataset)
- Transfermarkt valuations are community estimates, not actual transfer fees
- Name matching between understat and Transfermarkt relies on fuzzy
  string matching — some players may be incorrectly matched or excluded
- Goalkeepers excluded entirely (xG/xA do not capture their performance)
---
## Tools & Libraries
Python 3 · pandas · numpy · matplotlib · seaborn · statsmodels ·
requests · json · rapidfuzz

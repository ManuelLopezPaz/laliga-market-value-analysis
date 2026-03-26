# La Liga Market Value Analysis (2014–2024)

**ManuelLopezPaz**

---

## Questions

1. Which performance metrics best predict player market value in La Liga?
2. Does xG predict market value better than raw goals?

---

## Main Findings

- xG and goals predict market value almost equally well (R² = 0.268 vs 0.266)
- xA per 90 is the strongest performance predictor in the full model (β = 2.57)
- Adding age raised R² from 0.278 to 0.406 — bigger jump than any performance metric
- Market value peaks at around 19–20 years old
- When goals and xG are both in the model, xG loses significance (r = 0.88 between them)

---

## Data

- Performance: understat.com, scraped via POST API
- Market values: Transfermarkt dataset on Kaggle (davidcariboo/player-scores, CC0)
- La Liga, 2014/15 to 2024/25, 2,679 player-seasons after filters

---

## Files
```
01_data_cleaning.ipynb       data loading, merge, and feature engineering
02_analysis.ipynb            EDA, regression models, and results
01_scrape_understat.py       script used to scrape understat.com
understat_laliga_2014_2024.csv    raw scraped data (6,192 rows)
laliga_cleaned.csv           final dataset (2,679 rows)
figures/                     all charts
```

---

## Limitations

- 60% of market value variance unexplained — contract length, injuries, 
  and media profile are not in the data
- Transfermarkt values are community estimates, not real transfer fees
- Goalkeepers excluded

---

## Tools

Python · pandas · numpy · matplotlib · seaborn · statsmodels · requests

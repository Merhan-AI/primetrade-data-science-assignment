# Crypto Sentiment & Trader Performance Analysis

## 📌 Objective
This repository contains my submission for the Primetrade.ai / Anything.ai Data Science assignment. The objective of this project is to explore the relationship between individual trader performance (via Hyperliquid historical data) and macroeconomic market sentiment (via the Bitcoin Fear & Greed Index).

The core script cleans, aligns, and merges time-series data to uncover hidden behavioral patterns, specifically isolating elite traders to analyze their risk adjustments during extreme market conditions.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas (Data manipulation, Time-series alignment, Aggregation)

## 📊 Key Actionable Insights

Based on the data processing and cohort analysis, here are the primary findings regarding trader behavior:

1. **Market State vs. Win Rate:** The analysis reveals that the overall trader win rate is [Insert %] during "Fear" states, compared to [Insert %] during "Greed" states, indicating that traders generally [struggle/succeed] more when the market is euphoric.

2. **Elite Trader Risk Management (Top 10%):** When analyzing the top 10% most profitable accounts, a distinct behavioral pattern emerges. During "Fear" classifications, elite traders [increase/decrease] their average trade size to $[Insert Number], compared to standard retail traders who average $[Insert Number]. This suggests the most profitable accounts are actively [scaling into / reducing] risk during market downturns.

3. **Overall Profitability Skew:**
   The average PnL across all cohorts is significantly impacted by sentiment, with "Greed" days resulting in an average PnL of $[Insert Number], contrasting heavily with "Fear" days at $[Insert Number]. This data can directly inform automated risk-scaling strategies for algorithmic execution.

## 🚀 How to Run the Code
1. Clone this repository.
2. Ensure you have `pandas` installed (`pip install pandas`).
3. Place `historical_data.csv` and `sentiment_data.csv` in the root directory.
4. Run `python analysis.py` to output the dataframes and metrics to the terminal or generate the summary CSVs.

---
*Author: Mohammed Mehran Imtiyaz Ahmed Shaikh*

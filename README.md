# Crypto Sentiment & Trader Performance Analysis

## 📌 Objective
This repository contains my submission for the Primetrade.ai / Anything.ai Data Science assignment. The objective of this project is to explore the relationship between individual trader performance (via Hyperliquid historical data) and macroeconomic market sentiment (via the Bitcoin Fear & Greed Index).

The core script cleans, aligns, and merges time-series data to uncover hidden behavioral patterns, specifically isolating elite traders to analyze their risk adjustments during extreme market conditions.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas (Data manipulation, Time-series alignment, Aggregation)

## 📊 Key Actionable Insights

Based on the data processing and cohort analysis, here are the primary findings regarding trader behavior:

1. **Market State vs. Win Rate:** The analysis reveals that the overall trader win rate is 42.08% during standard "Fear" states, compared to 38.48% during "Greed" states. Interestingly, extreme market euphoria ("Extreme Greed") pushes the overall average win rate to its peak at 46.49%.

2. **Elite Trader Risk Management (Top 10%):** When analyzing the top 10% most profitable accounts, a distinct behavioral pattern emerges regarding position sizing. During "Fear" classifications, elite traders increase their average trade size to $12,968.25, compared to standard retail traders (the other 90%) who average just $4,722.24. This suggests the most profitable accounts are actively scaling into risk and buying with high conviction during market downturns.

3. **Asymmetric Profitability in Extreme Greed:**
   The top 10% of traders exhibit a massive profitability skew during "Extreme Greed." While their win rate actually drops to 32.05% in this state, their average PnL skyrockets to $378.88 per trade (compared to the other 90% who average just $44.38). This indicates that elite traders do not win more often during euphoric markets; rather, they utilize asymmetric risk management—cutting losers quickly and letting winning trades run significantly further.

## 🚀 How to Run the Code
1. Clone this repository.
2. Ensure you have `pandas` installed (`pip install pandas`).
3. Place `historical_data.csv` and `sentiment_data.csv` in the root directory.
4. Run `python analysis.py` to output the dataframes and metrics to the terminal.

---
*Author: Mohammed Mehran Imtiyaz Ahmed Shaikh*

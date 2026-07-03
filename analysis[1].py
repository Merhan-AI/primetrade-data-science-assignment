import pandas as pd

print("1. Loading datasets...")
df_trader = pd.read_csv('historical_data.csv')
df_sentiment = pd.read_csv('sentiment_data.csv')

print("2. Formatting dates and merging...")
# Use Timestamp IST directly - it's already a readable date string (DD-MM-YYYY HH:MM),
# avoiding any epoch-unit ambiguity in the raw 'Timestamp' column
df_trader['merge_date'] = pd.to_datetime(
    df_trader['Timestamp IST'], format='%d-%m-%Y %H:%M'
).dt.strftime('%Y-%m-%d')

# Sentiment 'date' column is already clean YYYY-MM-DD strings
df_sentiment['merge_date'] = pd.to_datetime(df_sentiment['date']).dt.strftime('%Y-%m-%d')

# Sanity check before merging - confirms the two date ranges actually overlap
print("Trader date range:", df_trader['merge_date'].min(), "to", df_trader['merge_date'].max())
print("Sentiment date range:", df_sentiment['merge_date'].min(), "to", df_sentiment['merge_date'].max())

# Glue the datasets together based on the date
df_merged = pd.merge(df_trader, df_sentiment, on='merge_date', how='left')
print("Merged rows:", len(df_merged), "| Unmatched classification:", df_merged['classification'].isna().sum())

print("3. Cleaning Data...")
# Ensure PnL and Size are numbers, not text, so we can do math on them
df_merged['Closed PnL'] = pd.to_numeric(df_merged['Closed PnL'], errors='coerce').fillna(0)
df_merged['Size USD'] = pd.to_numeric(df_merged['Size USD'], errors='coerce').fillna(0)

# Define a "Win" as any trade that made a profit greater than 0
df_merged['Is_Win'] = df_merged['Closed PnL'] > 0

print("\n=======================================================")
print("  PHASE 2: OVERALL PERFORMANCE BY MARKET SENTIMENT")
print("=======================================================\n")

# Group all data by the market classification (Fear vs Greed)
sentiment_group = df_merged.groupby('classification').agg(
    Total_Trades=('Closed PnL', 'count'),
    Avg_PnL=('Closed PnL', 'mean'),
    Avg_Trade_Size=('Size USD', 'mean'),
    Win_Rate=('Is_Win', 'mean')
).reset_index()

sentiment_group['Win_Rate'] = (sentiment_group['Win_Rate'] * 100).round(2)
sentiment_group['Avg_PnL'] = sentiment_group['Avg_PnL'].round(2)
sentiment_group['Avg_Trade_Size'] = sentiment_group['Avg_Trade_Size'].round(2)

print(sentiment_group.to_string(index=False))
sentiment_group.to_csv('sentiment_performance_summary.csv', index=False)

print("\n=======================================================")
print("  PHASE 3: ELITE TRADERS (TOP 10%) VS. THE REST")
print("=======================================================\n")

# Calculate Total PnL for each unique account to find the best traders
account_pnl = df_merged.groupby('Account')['Closed PnL'].sum().reset_index()

# Find the cutoff number for the top 10%
top_10_threshold = account_pnl['Closed PnL'].quantile(0.90)

# Get a list of those top accounts
top_traders = account_pnl[account_pnl['Closed PnL'] >= top_10_threshold]['Account']

# Label each trade in the main dataset based on who made it
df_merged['Trader_Tier'] = df_merged['Account'].apply(
    lambda x: 'Top 10%' if x in top_traders.values else 'Other 90%'
)

# Analyze how the Elite perform in Fear vs Greed compared to everyone else
cohort_group = df_merged.groupby(['Trader_Tier', 'classification']).agg(
    Avg_PnL=('Closed PnL', 'mean'),
    Avg_Trade_Size=('Size USD', 'mean'),
    Win_Rate=('Is_Win', 'mean')
).reset_index()

cohort_group['Win_Rate'] = (cohort_group['Win_Rate'] * 100).round(2)
cohort_group['Avg_PnL'] = cohort_group['Avg_PnL'].round(2)
cohort_group['Avg_Trade_Size'] = cohort_group['Avg_Trade_Size'].round(2)

print(cohort_group.to_string(index=False))
cohort_group.to_csv('elite_vs_rest_summary.csv', index=False)

print("\nAnalysis Complete! Summary CSVs saved to disk.")

import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Numeric validation
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct",
    "sharpe_ratio"
]

for col in cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Negative Sharpe
negative_sharpe = df[
    df["sharpe_ratio"] < 0
]

print(
    "Negative Sharpe:",
    len(negative_sharpe)
)

# Expense ratio range
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Saved")

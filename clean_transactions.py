import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Standardize text
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Amount validation
df = df[df["amount_inr"] > 0]

# Convert dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Remove duplicates
df = df.drop_duplicates()

# KYC check
print(
    df["kyc_status"].unique()
)

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("Saved")
import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV
df = df[df["nav"] > 0]

# Save
df.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)

print(df.shape)
print("Clean NAV saved")
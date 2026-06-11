import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

funds = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/processed/clean_nav.csv"
)

transactions = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

performance = pd.read_csv(
    "data/processed/clean_performance.csv"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

funds.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

benchmark.to_sql(
    "dim_benchmark",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded")
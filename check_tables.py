import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print(tables)

for table in tables["name"]:
    print(f"\n--- {table} ---")
    cols = pd.read_sql(
        f"PRAGMA table_info({table});",
        conn
    )
    print(cols[["name","type"]])

conn.close()
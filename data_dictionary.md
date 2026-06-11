# Data Dictionary

## dim_fund

| Column        | Type    | Description             |
| ------------- | ------- | ----------------------- |
| amfi_code     | INTEGER | Unique AMFI scheme code |
| fund_house    | TEXT    | Mutual fund company     |
| scheme_name   | TEXT    | Scheme name             |
| category      | TEXT    | Fund category           |
| sub_category  | TEXT    | Fund sub category       |
| risk_category | TEXT    | Risk classification     |

## fact_nav

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | INTEGER | Scheme code     |
| date      | DATE    | NAV date        |
| nav       | REAL    | Net Asset Value |

## fact_transactions

| Column           | Type | Description            |
| ---------------- | ---- | ---------------------- |
| investor_id      | TEXT | Investor identifier    |
| transaction_date | DATE | Transaction date       |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr       | REAL | Transaction amount     |

## fact_performance

| Column            | Type | Description          |
| ----------------- | ---- | -------------------- |
| return_1yr_pct    | REAL | 1 Year Return        |
| return_3yr_pct    | REAL | 3 Year Return        |
| return_5yr_pct    | REAL | 5 Year Return        |
| sharpe_ratio      | REAL | Risk adjusted return |
| expense_ratio_pct | REAL | Expense ratio        |

## dim_benchmark

| Column      | Type | Description     |
| ----------- | ---- | --------------- |
| index_name  | TEXT | Benchmark index |
| date        | DATE | Trading date    |
| close_value | REAL | Closing value   |

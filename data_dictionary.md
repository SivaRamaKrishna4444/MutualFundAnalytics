# Data Dictionary

## dim_fund

Source: `01_fund_master.csv`

| Column             | Type    | Description                         |
| ------------------ | ------- | ----------------------------------- |
| amfi_code          | INTEGER | Unique AMFI scheme code             |
| fund_house         | TEXT    | Mutual fund company name            |
| scheme_name        | TEXT    | Name of the mutual fund scheme      |
| category           | TEXT    | Fund category (Equity, Debt, etc.)  |
| sub_category       | TEXT    | Fund sub-category                   |
| plan               | TEXT    | Direct or Regular plan              |
| launch_date        | TEXT    | Scheme launch date                  |
| benchmark          | TEXT    | Benchmark index used for comparison |
| expense_ratio_pct  | REAL    | Expense ratio percentage            |
| exit_load_pct      | REAL    | Exit load percentage                |
| min_sip_amount     | INTEGER | Minimum SIP investment amount       |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment amount  |
| fund_manager       | TEXT    | Fund manager name                   |
| risk_category      | TEXT    | Risk classification                 |
| sebi_category_code | TEXT    | SEBI category code                  |

---

## fact_nav

Source: `02_nav_history.csv` / `clean_nav.csv`

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | INTEGER | Scheme code     |
| date      | DATE    | NAV date        |
| nav       | REAL    | Net Asset Value |

---

## fact_transactions

Source: `08_investor_transactions.csv` / `clean_transactions.csv`

| Column             | Type    | Description                                |
| ------------------ | ------- | ------------------------------------------ |
| investor_id        | TEXT    | Unique investor identifier                 |
| transaction_date   | DATE    | Transaction date                           |
| amfi_code          | INTEGER | Mutual fund scheme code                    |
| transaction_type   | TEXT    | SIP, Lumpsum, or Redemption                |
| amount_inr         | INTEGER | Transaction amount in INR                  |
| state              | TEXT    | Investor state                             |
| city               | TEXT    | Investor city                              |
| city_tier          | TEXT    | City classification (Tier 1, Tier 2, etc.) |
| age_group          | TEXT    | Investor age group                         |
| gender             | TEXT    | Investor gender                            |
| annual_income_lakh | REAL    | Annual income in lakhs                     |
| payment_mode       | TEXT    | Mode of payment                            |
| kyc_status         | TEXT    | KYC verification status                    |

---

## fact_performance

Source: `07_scheme_performance.csv` / `clean_performance.csv`

| Column             | Type    | Description                           |
| ------------------ | ------- | ------------------------------------- |
| amfi_code          | INTEGER | Scheme code                           |
| scheme_name        | TEXT    | Scheme name                           |
| fund_house         | TEXT    | Fund house name                       |
| category           | TEXT    | Fund category                         |
| plan               | TEXT    | Fund plan type                        |
| return_1yr_pct     | REAL    | One-year return percentage            |
| return_3yr_pct     | REAL    | Three-year return percentage          |
| return_5yr_pct     | REAL    | Five-year return percentage           |
| benchmark_3yr_pct  | REAL    | Benchmark three-year return           |
| alpha              | REAL    | Alpha performance metric              |
| beta               | REAL    | Beta risk metric                      |
| sharpe_ratio       | REAL    | Risk-adjusted return measure          |
| sortino_ratio      | REAL    | Downside-risk-adjusted return measure |
| std_dev_ann_pct    | REAL    | Annualized standard deviation         |
| max_drawdown_pct   | REAL    | Maximum drawdown percentage           |
| aum_crore          | INTEGER | Assets Under Management (Crore INR)   |
| expense_ratio_pct  | REAL    | Expense ratio percentage              |
| morningstar_rating | INTEGER | Morningstar rating                    |
| risk_grade         | TEXT    | Risk grade classification             |

---

## dim_benchmark

Source: `10_benchmark_indices.csv`

| Column      | Type | Description          |
| ----------- | ---- | -------------------- |
| date        | DATE | Trading date         |
| index_name  | TEXT | Benchmark index name |
| close_value | REAL | Closing index value  |

---

## Database Information

Database Name: `bluestock_mf.db`

Tables:

1. dim_fund
2. fact_nav
3. fact_transactions
4. fact_performance
5. dim_benchmark

Purpose:
This database supports mutual fund analytics including NAV trend analysis, investor transaction analysis, scheme performance evaluation, benchmark comparison, and risk-return analytics.

-- 1. Top 5 Funds by AUM

SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV Across All Funds

SELECT ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav;

-- 3. Monthly Average NAV

SELECT SUBSTR(date,1,7) AS month,
ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 4. Transactions by State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio Below 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Average 3-Year Return by Category

SELECT category,
ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY category;

-- 7. Total Transaction Amount

SELECT SUM(amount_inr) AS total_transaction_amount
FROM fact_transactions;

-- 8. Transaction Type Distribution

SELECT transaction_type,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Highest NAV Recorded

SELECT amfi_code,
date,
nav
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;

-- 10. Fund Count by Risk Grade

SELECT risk_grade,
COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;

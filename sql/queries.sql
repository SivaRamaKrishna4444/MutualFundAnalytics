-- 1. Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV

SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Monthly Average NAV

SELECT substr(nav_date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Transactions by State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1

SELECT amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Return by Category

SELECT category,
AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;

-- 7. Total Transaction Amount

SELECT SUM(amount_inr)
FROM fact_transactions;

-- 8. Transaction Type Distribution

SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Highest NAV Recorded

SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;

-- 10. Fund Count by Risk Grade

SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;
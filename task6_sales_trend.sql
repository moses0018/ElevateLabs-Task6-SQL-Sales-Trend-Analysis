SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM superstore_sales
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY YEAR(order_date), MONTH(order_date);


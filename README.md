# Task 6: Sales Trend Analysis Using SQL (Superstore Dataset)

## 📌 Objective
Analyze monthly revenue and order volume using SQL aggregations as part of the Elevate Labs Internship Program (Task 6).

---

## 🛠 Tools & Technologies
- **MySQL**
- **Python (for data import into MySQL)**
- **Superstore Sales Dataset (CSV)**

---

## 📂 Dataset Columns Used
- `order_id`
- `order_date`
- `sales`
- `product_id` (not used directly in calculation, but part of dataset)

---

## 📊 SQL Query: Monthly Revenue & Order Volume

```sql
SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM superstore_sales
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY YEAR(order_date), MONTH(order_date);

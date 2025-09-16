-- Example Derived Metrics
CREATE VIEW vw_customer_lifetime_value AS
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(t.amount) AS lifetime_value
FROM dim_customer c
LEFT JOIN fact_transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;

-- Churn Analysis (Customers with no txn in last 90 days)
CREATE VIEW vw_churned_customers AS
SELECT c.customer_id, c.first_name, c.last_name
FROM dim_customer c
LEFT JOIN fact_transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING MAX(t.txn_date) < DATEADD(DAY, -90, GETDATE());
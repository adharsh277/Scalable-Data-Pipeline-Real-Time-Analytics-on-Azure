-- Transactions Fact
CREATE TABLE fact_transactions (
    txn_id NVARCHAR(50) PRIMARY KEY,
    customer_id NVARCHAR(50) REFERENCES dim_customer(customer_id),
    txn_date DATE,
    product NVARCHAR(100),
    amount DECIMAL(18,2),
    status NVARCHAR(20)
);
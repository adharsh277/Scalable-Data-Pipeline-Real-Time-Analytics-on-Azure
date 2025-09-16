-- Customer Dimension
CREATE TABLE dim_customer (
    customer_id NVARCHAR(50) PRIMARY KEY,
    first_name NVARCHAR(100),
    last_name NVARCHAR(100),
    email NVARCHAR(150),
    phone NVARCHAR(20),
    gender NVARCHAR(10),
    dob_day INT,
    dob_month INT,
    dob_year INT,
    region NVARCHAR(100)
);
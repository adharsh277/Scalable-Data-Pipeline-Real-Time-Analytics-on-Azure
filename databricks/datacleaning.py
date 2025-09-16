# Trim spaces, normalize emails, phone numbers
df_clean = (df_raw
    .withColumn("customer_id", trim(col("customer_id")))
    .withColumn("email", lower(trim(col("email"))))
    .withColumn("phone", regexp_replace(col("phone"), "[^0-9]", ""))  # keep only digits
)

# Handle DOB – split into day, month, year
df_dob = (df_clean
    .withColumn("dob_year", year(col("dob").cast("date")))
    .withColumn("dob_month", month(col("dob").cast("date")))
    .withColumn("dob_day", dayofmonth(col("dob").cast("date")))
)

# Normalize Gender column
df_transformed = (df_dob
    .withColumn("gender", when(col("gender") == "M", "Male")
                         .when(col("gender") == "F", "Female")
                         .otherwise("Other"))
)

# Example Join with Transactions dataset
transactions_raw_path = "abfss://raw@<datalake_name>.dfs.core.windows.net/transactions/"
df_txn = spark.read.format("csv").option("header", "true").load(transactions_raw_path)

df_joined = df_transformed.join(df_txn, "customer_id", "left")

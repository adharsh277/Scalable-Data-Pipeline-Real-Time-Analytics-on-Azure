# Databricks PySpark Transformation Script
# ----------------------------------------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, year, month, dayofmonth, trim, lower, upper, when, regexp_replace

# Initialize Spark
spark = SparkSession.builder.appName("CRM_Transformations").getOrCreate()

# -----------------------
# 1️⃣ Read Raw Data
# -----------------------
crm_raw_path = "abfss://raw@<datalake_name>.dfs.core.windows.net/crm/"
df_raw = spark.read.format("csv").option("header", "true").load(crm_raw_path)
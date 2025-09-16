df_joined.write \
    .format("com.databricks.spark.sqldw") \
    .option("url", "jdbc:sqlserver://<synapse_server>.database.windows.net:1433;database=<synapse_db>") \
    .option("forwardSparkAzureStorageCredentials", "true") \
    .option("dbtable", "fact_crm") \
    .option("tempDir", "abfss://temp@<datalake_name>.dfs.core.windows.net/") \
    .save()

print(" Transformation & Load completed successfully!")
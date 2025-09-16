curated_path = "abfss://curated@<datalake_name>.dfs.core.windows.net/crm/"
(df_joined.write.mode("overwrite")
    .parquet(curated_path)
)
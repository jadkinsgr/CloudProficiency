# Databricks notebook source
import dlt
import pyspark.sql.functions as F
import pyspark.sql
from delta.tables import DeltaTable

# COMMAND ----------

#set your variables
container = 'landing'
product = 'ClinicalData'
account = 'adkinsstorage'
directory = 'Encounters'
initials = 'JTA' ## CHANGE THIS TO YOUR INITIALS

# Define the location of your file
fileLocation = f"abfss://{container}@{account}.dfs.core.windows.net/{product}/{directory}/"
print(fileLocation)

# COMMAND ----------

@dlt.table(
    name = f"{initials}_python_bronze_encounters",
    comment = "Raw data from encounters feed"
)
def ingest_file():
        df = (spark.readStream
              .format("cloudFiles")
              .option("cloudFiles.format", "csv")
              .option("cloudFiles.inferColumnTypes", 'true') # infer datatypes
              .load(fileLocation)
              .selectExpr("*", "_metadata as source_metadata")
        )

        df_transformed = (
            df.withColumn("SourceFileName", F.element_at(F.split(F.col("source_metadata")["file_path"], "/"), -1))
              .drop("source_metadata")
              .withColumn("EtlStartDate", F.current_timestamp())
        )

        return df_transformed

# COMMAND ----------

@dlt.table(
    name = f"{initials}_python_silver_encounters",
    comment = "clean data from encounters feed"
)
@dlt.expect_or_fail("valid_description", "reasondescription IS NOT NULL")
def python_silver_encounters_clean():
    return (
        dlt.read_stream(f"{initials}_python_bronze_encounters")
    )

# COMMAND ----------

@dlt.table(
    name = f"{initials}_python_gold_encounters",
    comment = "gold level data from encounters feed"
)
def python_gold_encounters():
  return spark.sql(f"SELECT * FROM LIVE.{initials}_python_silver_encounters")

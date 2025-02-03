# Databricks notebook source
# MAGIC %md
# MAGIC ###Welcome! 🚀
# MAGIC ####Full Pipeline Tutorial
# MAGIC
# MAGIC 1. Creating a bronze table
# MAGIC 2. Creating a quality catch (silver prep data quality enforcement step)
# MAGIC 3. Creating a silver type 1 SCD table
# MAGIC 4. Creating a silver type 2 SCD table
# MAGIC 5. Creating a final gold level reporting table
# MAGIC 6. Creating the Pipeline - wrapping steps 1-5 together
# MAGIC
# MAGIC Example Scenarios I have prepared:
# MAGIC
# MAGIC 1. Loading the initial set of values
# MAGIC 2. Adding new values, but not the ones from step 1.
# MAGIC 3. Correcting a value from step 2
# MAGIC 4. Running the pipeline with “bad” data - quality check enforcement
# MAGIC 5. Illustrating schema drift
# MAGIC 6. Illustrating what happens when we receive unexpected value (for example a string, when we expect a integer)

# COMMAND ----------

#import libraries
import dlt
import pyspark.sql.functions as F
import pyspark.sql
from delta.tables import DeltaTable


# COMMAND ----------

#set your variables
container = 'landing'
product = 'fullprocess'
account = 'adkinsstorage'
directory = 'Developers_FullPipeline'
initials = 'jta' ## CHANGE THIS TO YOUR INITIALS

# Define the location of your file
fileLocation = f"abfss://{container}@{account}.dfs.core.windows.net/{product}/"
print(fileLocation)

# COMMAND ----------

#Create Bronze - this is a 1:1 raw copy of the ingestion files
@dlt.table(
    name = f"{initials}bronze_developers_python",
    comment = "Raw data from developers feed"
)
def ingest_encounters():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("cloudFiles.inferColumnTypes", 'true') #infer datatypes
        .load(fileLocation)
        .select(
            "*",
            F.current_timestamp().alias("ETLStartDate"),
            F.lit('Developers').alias("SourceFileName") #optional - if dealing with many files you can dynamically get the filename
        )
    )

# COMMAND ----------

#Quality Check - Valid Year (no missing values)
@dlt.table(
    name = f"{initials}quality_catch_developers_prep_python",
    comment = "Raw data from developers feed"
)
@dlt.expect_or_drop("valid_year", "Year IS NOT NULL")
def silver_developers_prep_python():
    return (
        dlt.read_stream(f"{initials}bronze_developers_python")
    )

# COMMAND ----------

#Silver Table Example 1 - SCD Type 1
dlt.create_streaming_table(
    name = f"{initials}silver_developers_type1_python",
    comment="Clean, merged developers - Type 1 SCD Table"
)

dlt.apply_changes(
    target = f"{initials}silver_developers_type1_python",
    source = f"{initials}quality_catch_developers_prep_python",
    keys = ["Id"],
    sequence_by = F.col("ETLStartDate"),
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = "1"
    #track_history_column_list = None,
    #track_history_except_column_list = ["processing_time"]

)

# COMMAND ----------

#Silver Table Example 2 - SCD Type 2
dlt.create_streaming_table(
    name = f"{initials}silver_developers_type2_python",
    comment="Clean, merged developers Type 2 SCD Table"
)

dlt.apply_changes(
    target = f"{initials}silver_developers_type2_python",
    source = f"{initials}quality_catch_developers_prep_python",
    keys = ["Id"],
    sequence_by = F.col("ETLStartDate"),
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = "2",
    track_history_column_list = None,
    track_history_except_column_list = ["ETLStartDate"]

)

# COMMAND ----------

#Gold Table Example (materilized view) - Materialized views are often faster, developers preference based on context - its also recreated, not appended.
@dlt.table(
    name = f"{initials}gold_developers_python",
    comment = "Fully Transformed Data Thats Clean from developers feed"
)
def gold_developers_python():
  return spark.sql(f"SELECT * FROM LIVE.{initials}silver_developers_type1_python")


# COMMAND ----------

# Collect bad data that fails the quality check
@dlt.table(
    name = f"{initials}Bad_Data_Collection",
    comment = "Collecting the data that fails the quality check"
)
def bad_data_collection():
    return (
        dlt.read_stream(f"{initials}bronze_developers_python")
        .filter("Year IS NULL")  # Capture only bad data
    )

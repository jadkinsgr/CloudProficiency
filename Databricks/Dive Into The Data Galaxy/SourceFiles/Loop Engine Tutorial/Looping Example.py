# Databricks notebook source
import dlt
import requests

from   datetime              import datetime  as DT
from   pyspark.sql           import functions as F
from   pyspark.sql.functions import col, when, from_json, explode
from   pyspark.sql.types     import StructType, StructField, StringType, IntegerType, ArrayType, BooleanType, LongType, ShortType, DecimalType, TimestampType


# COMMAND ----------

#functions
#Adkins Functions Additional
def blank_as_null(x):
    return when(col(x) != "", col(x)).otherwise(None)
  
def blank_as_null_for_string_columns(df):
    string_columns = [field.name for field in df.schema.fields if field.dataType.simpleString() == 'string']
    exprs = [blank_as_null(col_name).alias(col_name) if col_name in string_columns else col_name for col_name in df.columns]
    return df.select(*exprs)
  
# Function to convert uppercase with underscores to PascalCase
def to_pascal_case(name):
    return ''.join(word.capitalize() for word in name.lower().split('_'))

def stringToPascal( convertString ) :
    # function doc string
    """Accepts a string, and converts it to a PascalCaseString.
    """

    # replace _ with - for uniform splits
    tempString  = convertString.replace("_", "-")
    stringParts = tempString.split("-")

    # capitalize
    for i in range( 1, len(stringParts) ):
      stringParts[i] = stringParts[i].capitalize()

    # recombine
    combinedString   = "".join(stringParts)
    pascalCaseString = combinedString[0].upper() + combinedString[1:]

    return pascalCaseString


# COMMAND ----------

# Set your variables
container = 'landing'
account = 'adkinsstorage'
product = 'looping'
initials = 'jta'

FileLocation = f"abfss://{container}@{account}.dfs.core.windows.net/{product}"
print(FileLocation)


# COMMAND ----------

def create_bronze_table(landingFolder, table):
    @dlt.table(name=f"{initials}_bronze_{table}")
    def ingest_file():
        df = (spark.readStream
              .format("cloudFiles")
              .option("cloudFiles.format", "csv")
              .option("cloudFiles.inferColumnTypes", 'true') # infer datatypes
              .load(landingFolder)
              .selectExpr("*", "_metadata as source_metadata")
        )

        df_transformed = (
            df.withColumn("SourceFileName", F.element_at(F.split(F.col("source_metadata")["file_path"], "/"), -1))
              .drop("source_metadata")
              .withColumn("EtlStartDate", F.current_timestamp())
        )

        return df_transformed

def create_silver_table(table):
    @dlt.table(name=f"{initials}_silver_{table}")
    def silver_creation():
        df1 = dlt.read_stream(f"{initials}_bronze_{table}").select("*")
        df1_with_nulls = blank_as_null_for_string_columns(df1)
        renamed_columns = [F.col(c).alias(stringToPascal(c)) for c in df1_with_nulls.columns]
        transformed_df = df1_with_nulls.select(*renamed_columns)
        return transformed_df
    
def create_gold_table(table):
    @dlt.table(name=f"{initials}_gold_{table}")
    def gold_creation():
        df1 = dlt.read_stream(f"{initials}_silver_{table}").select("*")
        return df1

# Get a list of subfolders in the root pick up location
landingFolders = [
    folder.path
    for folder in dbutils.fs.ls(FileLocation)
    if folder.isDir()
]


# COMMAND ----------

for landingFolder in landingFolders:
    tableName = [part for part in landingFolder.split("/") if part][-1]
    create_bronze_table(landingFolder, tableName)
    create_silver_table(tableName)
    create_gold_table(tableName)


# COMMAND ----------

# MAGIC %md
# MAGIC Drop database looping_example.developers CASCADE;

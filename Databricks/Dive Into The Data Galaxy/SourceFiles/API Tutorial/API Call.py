# Databricks notebook source
import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType
import dlt
##API Documentation##
#https://openweathermap.org/api/one-call-3#data


# COMMAND ----------

kv = "AdkinsOpenWeatherAPI"
api_key = dbutils.secrets.get(scope = kv, key ="AdkinsOpenWeatherAPIKey")
print(api_key)


# COMMAND ----------

# List of cities for which we want to get the weather data
cities = [
    "Grand Rapids,MI,US", 
    "Charleston,SC,US", 
    "Chicago,IL,US", 
    "Johnson City,TN,US", 
    "New Orleans,LA,US", 
    "Asheville,SC,US"
]

# COMMAND ----------

# Define the schema for the Spark DataFrame
schema = StructType([
    StructField("city", StringType(), True),
    StructField("temperature", FloatType(), True),  # Temperature in Fahrenheit (imperial units)
    StructField("humidity", IntegerType(), True),
    StructField("weather", StringType(), True)
])

# COMMAND ----------

# Initialize an empty list to hold the data for each city
all_city_data = []

# COMMAND ----------

# Loop through each city and make the API request
for city in cities:
    # Construct the API URL with units set to 'imperial'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
    
    # Make the API call and extract the data
    response = requests.get(url)
    data = response.json()
    
    # Extract fields from the JSON response and add them to the list
    city_data = (
        data.get("name"),  # City name
        data["main"].get("temp"),  # Temperature in Fahrenheit
        data["main"].get("humidity"),  # Humidity
        data["weather"][0].get("description")  # Weather description
    )
    
    all_city_data.append(city_data)

# Create a Spark DataFrame using the collected data and schema
weather_df = spark.createDataFrame(all_city_data, schema)

# Show the Spark DataFrame with weather data for all cities
weather_df.show()

# COMMAND ----------

# Create a DLT table based on weather_df
import dlt

@dlt.table
def weather_data():
    return weather_df

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from weather.conditions.weather_data order by city asc

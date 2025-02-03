-- Databricks notebook source
-- MAGIC %md 
-- MAGIC #Step 1: Create your Bronze Table
-- MAGIC #### Use SparkSQL to create your Bronze Table

-- COMMAND ----------

--Creating a LIVE table tells databricks we are using delta live tables
--Make sure to create your table in hive_metastore.default.xxxxx where xxxxx is your table name.

CREATE LIVE TABLE JTA_Bronze_Patient
(
  Id String COMMENT 'This is the primary key column',
  BIRTHDATE STRING,
  DEATHDATE STRING,
  SSN STRING,
  DRIVERS STRING,
  PASSPORT STRING,
  PREFIX STRING,
  FIRST STRING,
  LAST STRING,
  SUFFIX STRING,
  MAIDEN STRING,
  MARITAL STRING,
  RACE STRING,
  ETHNICITY STRING,
  GENDER STRING,
  BIRTHPLACE STRING,
  ADDRESS STRING,
  CITY STRING,
  STATE STRING,
  COUNTY STRING,
  ZIP STRING,
  LAT STRING,
  LON STRING,
  HEALTHCARE_EXPENSES STRING,
  HEALTHCARE_COVERAGE STRING,
  FileName STRING,
  CreatedOn TIMESTAMP
)
--- Fake patient data for tutorial
USING DELTA 
COMMENT "Bronze Table for Patient"

AS

Select * 
,INPUT_FILE_NAME() as FileName
,CURRENT_TIMESTAMP() AS CreatedOn
FROM jtapatients --if using azure this might be From [INSERT AZURE LOCATION]

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC #Step 2: Create your Silver Table
-- MAGIC #### Use SparkSQL to create your Silver Table. We do three things here: Data Type Changes, Generate new columns, and add constraints to control for data errors.

-- COMMAND ----------

--Creating a LIVE table tells databricks we are using delta live tables

CREATE LIVE TABLE JTA_Silver_Patient
(
  Id STRING COMMENT 'This is the primary key column',
  BIRTHDATE DATE,
  DEATHDATE DATE,
  SSN STRING,
  ZIP STRING,
  LAT DECIMAL(9,6),
  LON DECIMAL(9,6),
  FileName STRING,
  CreatedOn TIMESTAMP,
  
  --Add some custom calculations
  BirthYear INT Generated always as (YEAR (BIRTHDATE)),
  BirthMonth INT Generated always as (MONTH (BIRTHDATE)),
  BirthDay INT Generated always as (DAY (BIRTHDATE)),

  --add constraints-- this is us cleaning up the silver table, these are our requirements
  CONSTRAINT Valid_Zip Expect (ZIP is not null) ON VIOLATION DROP ROW,
  CONSTRAINT Valid_ID Expect (ID IS NOT NULL) ON VIOLATION DROP ROW
  )
--- Fake patient data for tutorial
USING DELTA 
COMMENT "Silver Table for Patient"

AS

SELECT
ID,
cast(BIRTHDATE as DATE),
cast(DEATHDATE as DATE),
SSN,
ZIP,
cast(LAT as DECIMAL(9,6)) LAT,
cast(LON as DECIMAL(9,6)) LON,
FileName,
CreatedOn
FROM live.JTA_Bronze_Patient --check that this dataset exists

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC #Step 3: Optional - but you can catch your contraints from your bronze table. This is a good way to do it.
-- MAGIC

-- COMMAND ----------

--Creating a LIVE table tells databricks we are using delta live tables

CREATE LIVE TABLE JTA_ErrorLogging
(
  Id STRING COMMENT 'This is the primary key column',
  BIRTHDATE DATE,
  DEATHDATE DATE,
  SSN STRING,
  ZIP STRING,
  LAT DECIMAL(9,6),
  LON DECIMAL(9,6),
  FileName STRING,
  CreatedOn TIMESTAMP,
  
  --Add some custom calculations
  BirthYear INT Generated always as (YEAR (BIRTHDATE)),
  BirthMonth INT Generated always as (MONTH (BIRTHDATE)),
  BirthDay INT Generated always as (DAY (BIRTHDATE))

  --add constraints-- this is us cleaning up the silver table, these are our requirements
  --CONSTRAINT Valid_Zip Expect (ZIP is not null) ON VIOLATION DROP ROW,
  --CONSTRAINT Valid_ID Expect (ID IS NOT NULL) ON VIOLATION DROP ROW
  )
--- Fake patient data for tutorial
USING DELTA 
COMMENT "ErrorLogging Table"

AS

SELECT
ID,
cast(BIRTHDATE as DATE),
cast(DEATHDATE as DATE),
SSN,
ZIP,
cast(LAT as DECIMAL(9,6)) LAT,
cast(LON as DECIMAL(9,6)) LON,
FileName,
CreatedOn
FROM live.JTA_Bronze_Patient --check that this dataset exists
Where 
ZIP is Null 
or 
ID is null

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC #Step 4: Create your Gold Table
-- MAGIC #### Use SparkSQL to create your Gold Table - This is any data we want curated for visualization or reporting. We will be using a very simple version - just 10 rows. But you could group records by birth month or zip code as well.

-- COMMAND ----------

CREATE LIVE TABLE JTA_Gold_Patient
AS
(
Select * from live.JTA_Silver_Patient limit 10
)

# **🚀 Dive into the Data Galaxy: Quick Follow Along Options**

Welcome to the exciting world of databricks! We've got some fantastic quick lessons that will turn you into a Databricks maestro in no time. Let the data adventure begin!

- *Special note: at the conclusion of each work session - make sure to stop or terminate your clusters. This will save the company cloud computing costs. Cluster creation is covered below and if you have any questions feel free to reach out to [joshua.adkins@tegria.com](mailto:joshua.adkins@tegria.com).
- *Special note two: Databricks is case sensitive. So if you hit an error check out the case styling!

## **📊 Lesson Highlights:**

1. [**Cluster Creation:**](https://scribehow.com/shared/Creating_a_Cluster_on_Databricks__e7x8x4iERZOquCQijQMy2g) Join the guide to create your first cluster on Databricks.
2. [**Create a Table:**](https://scribehow.com/shared/A_Guide_to_Creating_a_Table_in_Databricks_local_file_store__BtwzHwXJRJiucuOGQTzQnw) Learn the art of creating tables in Databricks' local file store. Unleash the power of data organization with this step-by-step guide.
3. [**View DBFS:**](https://scribehow.com/shared/How_to_view_DBFS_inside_of_Databricks__3SSx0fA_Qd6rsuVUOiTmRg) By default, DBFS (Databricks File System)is hidden, lets add the option to see it. After this step - you can view the table you created in step 2!
4. [**Write your first Python Notebook:**](https://scribehow.com/shared/Creating_a_Notebook_and_Printing_Hello_World_on_Databricks_Community_Cloud__gzmpctt4TYO6gczAC2zL6w) Launch your data journey with a bang! Create a notebook and print "Hello World" on Databricks Community Cloud.
5. [Setting up user security](https://scribehow.com/shared/Azure_Databricks__User_Security_Setup__wRL9rRwjR_6LGx5FWWiCLg) - so developers have all rights, and end-users can only see or interact with silver or gold layer tables.
6. **Import or export a notebook from a .dbc file:** With this approach (also in option 2: unity catalog) you can import a notebook from another user or export yours for someone else.

[**Import**](https://scribehow.com/shared/Import_a_notebook_within_Databricks_from_an_existing_file__8pC4pSM4Q9C_QpTEKEzYyg?referrer=documents) 

[**Export**](https://scribehow.com/shared/Export_a_notebook_to_share_with_others__7YN5mDp3SwCZTFFoJOh8xg?referrer=documents)

---

# **🎥 Videos Tutorials**

These quick lessons are designed for speed - breaking up the individual tasks into bite sized components that are 5 minutes or less, but don't worry if something is missing - we are adding to it all the time.

Also keep in mind - this is an illustration on the Hive Metastore - not Unity Catalog (UC). UC as of 1/1/2024 - is still in private preview. However as of this moment one notebook = one catalog. If Bronze, Silver, Gold is in different catalogs you cannot use one notebook to publish to all three. However, the workaround to this is to place the medallion architecture at the table level which is recommended by Databricks. A example is placed below in Extras.

[**Welcome Start Here:**](https://www.loom.com/share/2fa9b495cc2e4424a7a3b380be060c25?sid=f3e16844-a2b6-4537-88af-52e5d0d3a5e7) There are two training pathways - both are valuable but you can chose which to follow or do both.

**Option 1**: Hive Metastore (Legacy) - This creates bronze/silver/gold tables assuming no schema inference and shows you how to convert datatypes in the pipeline.

**Option2**: This is the Unity Catalog Approach (future): Where we inherit datatypes from the source and ingest data from ADLS Gen2 storage rather than DBFS (Databricks File System)

## **Setup Videos:**

1. [**Cluster Creation Video:**](https://www.loom.com/share/81b5029002a24f38a1163bee9979f7d9) Join the guide to create your first cluster on Databricks.
2. [**Table Creation Video:**](https://www.loom.com/share/f3efcbe9174144c189a6bbbf2bdd3882?sid=381ce194-ca44-4453-beb2-3ee03640044e)  Create a fake source file for us to create our pipeline.


## **Hive MetaStore (Legacy) - Option 1:**

1. [**Create your Bronze Table:**](https://www.loom.com/share/1e1027e2c983402c801cea5d52cca01f?sid=63964baa-775f-4b1e-9e66-84f0dff9d44e) Create your starter table that contains everything
    

    
2. [**Create your Silver Table:**](https://www.loom.com/share/26913daf73cd4cf19e511f05c4746c34?sid=70046655-2607-481f-8f44-1dea0e10b540) : Create your table that possibly has some data type changes, column generation and constraints.
    
 
    
3. [**Create your Gold Table:**](https://www.loom.com/share/12faed2c0e9241f18ed4dad811716dd0?sid=d3476169-d2da-4499-8001-f4ab7aed5bdf) Create your reporting table - this is what data scientists, business intelligence analysts would use.
    
    
    
4. [**Create your Delta Lake Pipeline:**](https://www.loom.com/share/7c48139e6fe447bca9d7b58f708e1807?sid=e06f9b54-48dc-4933-90be-3402aac1960b) This runs the data through the pipeline from source, to bronze, to silver and to gold.
5. [**View your data created in step 6 (Create your Delta Lake Pipeline):**](https://www.loom.com/share/aea6db61df404af3b909b156f9ee9789?sid=076fccab-1532-417d-8531-a27eb605cd00) Take a look and see the output of all your hard work by browsing the bronze, silver and gold layer tables.

## **Unity Catalog (future)- Option 2:**

1. [**Unity Catalog Overview:**](https://www.loom.com/share/e6ed5b53f0194af28069e671c0d328b1?sid=6244def6-7760-4147-bc7f-88db5d134300) Get an overview of Unity Catalog.
    
    This repository file contains the entire notebook - you may use it if you like, to do so import the notebook into your own databricks account: [repo](https://dev.azure.com/tegria-technical-services/AnalyticsDojo/_wiki/wikis/AnalyticsDojo.wiki/44/Dive-into-the-Databricks-Galaxy-Quick-Follow-Along-Options)
    
2. [**Unity Catalog - Bronze Table:**](https://www.loom.com/share/b572f22d58624c39b6835baa5a703e57?sid=1f34250f-5dbd-412d-af2a-b2f1a8ae6d79) Learn about creating the Bronze Table in Spark SQL.
3. [**Unity Catalog - Silver Table:**](https://www.loom.com/share/8d1e7158677a4522b214bfba4d37eaf0?sid=12eac752-4bed-4f8f-85d7-591439187339) Learn about creating the Silver Table in Spark SQL.
4. [**Unity Catalog - Gold Table:**](https://www.loom.com/share/021bbae9cafd4547aa5954373c1753af?sid=49ab2c7d-6828-4773-af5d-38402bd49083) Learn about creating the Gold Table in Spark SQL.
5. [**Unity Catalog: DLT Pipeline Orchestration:**](https://www.loom.com/share/47dd8388203c4e389aa710e1aad66a06?sid=ce8dbeaf-7170-4d75-8867-8e13b32d8a7d) Understand DLT Pipeline Orchestration. Using our tables created in Steps 2-3.
6. [**Unity Catalog - Python Variation:**](https://www.loom.com/share/b978a87e2783444da9e77d5155206974?sid=93cc4473-2133-423f-8229-c7ca0a964166) Explore the Python Variation of these steps within Unity Catalog.
    

    

---

## **Extras!**

1. [**EngineLoop**](https://www.loom.com/share/c704db3fa16244409506b54bba5cecb6?sid=9af423c9-b83d-4d07-825a-93476c26f64a) - Ever needed to process a large amount of files into various tables with minimal coding - check out this engine loop video which will explore our options. 
2. [**Full Pipeline Tutorial**](https://www.loom.com/share/2b1d8f36cfc44307ab132c57944304f3)
    1. Creating a bronze table
    2. Creating a silver prep (data quality enforcement step)
    3. Creating a silver type 1 SCD table
    4. Creating a silver type 2 SCD table
    5. Creating a final gold level reporting table
    6. Creating the Pipeline - wrapping steps 1-5 together
    
    Example scenarios I have prepared that you will most likely encounter:
    
    1. Loading the initial set of values
    2. Adding new values, but not the ones from step 1.
    3. Correcting a value from step 2
    4. Running the pipeline with “bad” data - quality check enforcement
    5. Illustrating schema drift
    6. Illustrating what happens when we receive unexpected value (for example a string, when we expect a integer)
    
    
3. [**Incorporating Secrets from Key Vault to Databricks**](https://www.loom.com/share/98992b960f924b918033dfcb2a3452c1?sid=f4307f58-ee75-4883-9bfe-05c87c7a41ed) 🗝️

4. **[Leveraging a Databricks notebook to connect directly to a API Endpoint](https://www.loom.com/share/39f437c70f244234838652d0e34752a7?sid=7cda4501-ae02-447a-a010-06760d2d1297) 💽**
    
    Bypass the need to retrieve data from Azure Data Factory or AWS Glue and connect directly from databricks!

    
    Create your Key Vault secret, set up a Databricks secret scope using Key Vault properties, and then pull everything together by assigning the secret to a variable.

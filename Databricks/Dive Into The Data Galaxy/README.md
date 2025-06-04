# **🚀 Dive into the Data Galaxy: Quick Follow Along Options**

Welcome to the exciting world of databricks! We've got some fantastic quick lessons that will turn you into a Databricks maestro in no time. Let the data adventure begin!

- *Special note: at the conclusion of each work session - make sure to stop or terminate your clusters. This will save the company cloud computing costs. Cluster creation is covered below and if you have any questions feel free to reach out to [business.joshadkins@gmail.com](mailto:business.joshadkins@gmail.com).
- *Special note two: Databricks is case sensitive. So if you hit an error check out the case styling!

## **📊 Lesson Highlights:**

1. [**Cluster Creation:**](https://scribehow.com/shared/Creating_a_Cluster_on_Databricks__e7x8x4iERZOquCQijQMy2g) Join the guide to create your first cluster on Databricks.
2. [**Create a Table:**](https://scribehow.com/shared/A_Guide_to_Creating_a_Table_in_Databricks_local_file_store__BtwzHwXJRJiucuOGQTzQnw) Learn the art of creating tables in Databricks' local file store. Unleash the power of data organization with this step-by-step guide.
3. [**View DBFS:**](https://scribehow.com/shared/How_to_view_DBFS_inside_of_Databricks__3SSx0fA_Qd6rsuVUOiTmRg) By default, DBFS (Databricks File System)is hidden, lets add the option to see it. After this step - you can view the table you created in step 2!
4. [**Write your first Python Notebook:**](https://scribehow.com/shared/Creating_a_Notebook_and_Printing_Hello_World_on_Databricks_Community_Cloud__gzmpctt4TYO6gczAC2zL6w) Launch your data journey with a bang! Create a notebook and print "Hello World" on Databricks Community Cloud.
5. [**Setting up user security**](https://scribehow.com/shared/Azure_Databricks__User_Security_Setup__wRL9rRwjR_6LGx5FWWiCLg) - so developers have all rights, and end-users can only see or interact with silver or gold layer tables.
6. [**Import Notebooks**](https://scribehow.com/shared/Import_a_notebook_within_Databricks_from_an_existing_file__8pC4pSM4Q9C_QpTEKEzYyg?referrer=documents) - Import notebooks at a click of a button rather then manually writing them.
7. [**Export Notebooks**](https://scribehow.com/shared/Export_a_notebook_to_share_with_others__7YN5mDp3SwCZTFFoJOh8xg?referrer=documents) - share your notebook with others by exporting its contents

---

# **🎥 Videos Tutorials**

These quick lessons are designed for speed - breaking up the individual tasks into bite sized components that are 5 minutes or less, but don't worry if something is missing - we are adding to it all the time.

Also keep in mind - this is an illustration on the Hive Metastore - not Unity Catalog (UC). UC as of 1/1/2024 - is still in private preview. However as of this moment one notebook = one catalog. If Bronze, Silver, Gold is in different catalogs you cannot use one notebook to publish to all three. However, the workaround to this is to place the medallion architecture at the table level which is recommended by Databricks. A example is placed below in Extras.

[**Welcome Start Here:**](https://youtu.be/rRABFbz8wbw) There are two training pathways - both are valuable but you can chose which to follow or do both.

**Option 1**: Hive Metastore (Legacy) - This creates bronze/silver/gold tables assuming no schema inference and shows you how to convert datatypes in the pipeline.

**Option2**: This is the Unity Catalog Approach (future): Where we inherit datatypes from the source and ingest data from ADLS Gen2 storage rather than DBFS (Databricks File System)

## **Setup Videos:**

1. [**Cluster/Compute Creation Video:**](https://youtu.be/Uz3z9bT73iI) Join the guide to create your first cluster on Databricks.

2. [**Table Creation Video:**](https://youtu.be/3As9Zdi09gU)  Create a fake source file for us to create our pipeline. - [**Synthea Patient File**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SyntheaFiles/patients.csv)



## **Hive MetaStore (Legacy) - Option 1:**
### Source Creation Files can be found here:
[**Synthea Patient Files**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SyntheaFiles/patients.csv)

[**Notebook - Hive Metastore**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/Hive%20Metastore%20Tutorial/PatientTutorial.sql)

1. [**Create your Bronze Table:**](https://youtu.be/TvWr-3RIons) Create your starter table that contains everything
2. [**Create your Silver Table:**](https://youtu.be/fXZzzZLe4Lk) : Create your table that possibly has some data type changes, column generation and constraints. 
3. [**Create your Error Logging Table:**](https://youtu.be/fiOnB1nBJnk): At the silver level we had a constraint that would catch data quality issues and drop the row. In this example we are collecting those issues in one location for easy UAT or quality review.  
4. [**Create your Gold Table:**](https://youtu.be/PmxK9MF5wq0) Create your reporting table - this is what data scientists, business intelligence analysts would use.
5. [**Create your Delta Live Pipeline:**](https://youtu.be/lBriuE3urhE) This runs the data through the pipeline from source, to bronze, to silver and to gold.


## **Unity Catalog (future)- Option 2:**
[**Synthea Encounter Files**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SyntheaFiles/encounters.csv)

[**Notebook - Unity Catalog**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/Unity%20Catalog%20Tutorial/EncountersPipeline_Python.py)

1. [**Unity Catalog Overview:**](https://youtu.be/1IGMwHfzrh4) Get an overview of Unity Catalog.
2. [**Unity Catalog - Bronze Table:**](https://youtu.be/m_b8DKHTZUM) Learn about creating the Bronze Table in Python.
3. [**Unity Catalog - Silver Table:**](https://youtu.be/Giyyih8FPNE) Learn about creating the Silver Table in Python.
4. [**Unity Catalog - Gold Table:**](https://youtu.be/NF5V4enM370) Learn about creating the Gold Table in Python.
5. [**Unity Catalog: DLT Pipeline Orchestration:**](https://youtu.be/iF2MCuJ19wY) Understand DLT Pipeline Orchestration. Using our tables created in the prior steps.
6. [**Unity Catalog: Viewing our date output:**](https://youtu.be/d7SgtCbRLYg) We built our date, we build our pipeline - now lets take a look at its output.


## **Extras!**  

1. [**EngineLoop**](https://youtu.be/mO3HOkuvVgs) – Ever needed to process a large amount of files into various tables with minimal coding? Check out this Engine Loop video, which explores our options. 
    
    [**Notebook Link**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/Loop%20Engine%20Tutorial/Looping%20Example.py)  

2. **Full Pipeline Tutorial**: 
    
    [**Notebook Link**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/Full%20Pipeline%20Tutorial/FullDeveloperPipeline_Python%20(SCD%20Type%201%20and%202).py)  


    **Pipeline Steps:**  
    - **1.** Creating a bronze table  
    - **2.** Creating a silver prep (data quality enforcement step)  
    - **3.** Creating a silver Type 1 SCD table  
    - **4.** Creating a silver Type 2 SCD table  
    - **5.** Creating a final gold-level reporting table  
    - **6.** Creating the pipeline – wrapping steps 1-5 together  

    **Example Scenarios You’ll Encounter:**  
    - Loading the initial set of values  
    - Adding new values (but not ones from step 1)  
    - Correcting a value from step 2  
    - Running the pipeline with "bad" data (quality check enforcement)  
    - Illustrating schema drift  
    - Handling unexpected values (e.g., a string when an integer is expected)  

    **Full Pipeline Example – Bronze to Gold:**  
    - [**Part 1 - High level overview of everything including the notebook, workflow, and cloud storage items**](https://youtu.be/qJu3DDnJUQE)  
    - [**Part 2 - Running through each scenario in the pipeline**](https://youtu.be/pNFUYyKW8ts)  
    - [**Part 3 - Review and Recap, lets review the data**](https://youtu.be/0yxXuggG9hk)  

3. [**Incorporating Secrets from Key Vault to Databricks**](https://youtu.be/au6baQbMSh4): 

    [**Notebook Link**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/API%20Tutorial/Creating%20and%20Connecting%20to%20vs%20APIs%20in%20KeyVault.ipynb)  🗝️  

4. **[Leveraging a Databricks Notebook to Connect Directly to an API Endpoint](https://youtu.be/kKiCjv7b5_c) 💽**  

    [**Notebook Link**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/API%20Tutorial/API%20Call.py)
    
    Bypass the need to retrieve data from Azure Data Factory or AWS Glue—connect directly from Databricks!  

    - Create your Key Vault secret  
    - Set up a Databricks secret scope using Key Vault properties  
    - Assign the secret to a variable to bring everything together  

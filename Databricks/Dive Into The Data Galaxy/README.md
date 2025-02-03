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

[**Welcome Start Here:**](https://www.loom.com/share/cdcbe440ceae472f9e2ff4424626561c) There are two training pathways - both are valuable but you can chose which to follow or do both.

**Option 1**: Hive Metastore (Legacy) - This creates bronze/silver/gold tables assuming no schema inference and shows you how to convert datatypes in the pipeline.

**Option2**: This is the Unity Catalog Approach (future): Where we inherit datatypes from the source and ingest data from ADLS Gen2 storage rather than DBFS (Databricks File System)

## **Setup Videos:**

1. [**Cluster Creation Video:**](https://www.loom.com/share/f06ece936b1741c5944d0de7408d7c1f?sid=137520f6-ac81-47d5-ad32-4928005fb6b9) Join the guide to create your first cluster on Databricks.

2. [**Table Creation Video:**](https://www.loom.com/share/b38b2c75f3ff4880a4297a49b6e029bb)  Create a fake source file for us to create our pipeline. - [**Synthea Patient File**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SyntheaFiles/patients.csv)



## **Hive MetaStore (Legacy) - Option 1:**
### Source Creation Files can be found here:
[**Synthea Patient Files**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SyntheaFiles/patients.csv)

[**Notebook - Hive Metastore**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/Hive%20Metastore%20Tutorial/PatientTutorial.sql)

1. [**Create your Bronze Table:**](https://www.loom.com/share/8017eb20012e4078a31bea115033c98c) Create your starter table that contains everything
2. [**Create your Silver Table:**](https://www.loom.com/share/539b3ae60cc3426cb31b0eba14f289c7?sid=cb55687d-3cd1-46cc-8998-c4020f159c63) : Create your table that possibly has some data type changes, column generation and constraints. 
3. [**Create your Error Logging Table:**](https://www.loom.com/share/40dbde43d2b9478aa199d3ff69f4f5e5?sid=61792ded-4749-44db-9662-f956cea67cb0): At the silver level we had a constraint that would catch data quality issues and drop the row. In this example we are collecting those issues in one location for easy UAT or quality review.  
4. [**Create your Gold Table:**](https://www.loom.com/share/dbffb0b1badb4138aeeacd9277603c5e?sid=50f4c758-c826-46e2-81fd-49ca700af80b) Create your reporting table - this is what data scientists, business intelligence analysts would use.
5. [**Create your Delta Live Pipeline:**](https://www.loom.com/share/9e2fad182df44f6caeef9c79e0f0377c?sid=c6cc3d40-e2e3-4b89-933d-3a3742504a82) This runs the data through the pipeline from source, to bronze, to silver and to gold.


## **Unity Catalog (future)- Option 2:**
[**Synthea Encounter Files**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SyntheaFiles/encounters.csv)

[**Notebook - Unity Catalog**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/Unity%20Catalog%20Tutorial/EncountersPipeline_Python.py)

1. [**Unity Catalog Overview:**](https://www.loom.com/share/b0f1c5b4782d4db08de41fb453ae0a95?sid=9c223c8e-49aa-49a2-869c-eead90e02876) Get an overview of Unity Catalog.
2. [**Unity Catalog - Bronze Table:**](https://www.loom.com/share/4d9f1fadb29946068e909431369f0eec?sid=e914209f-52fa-47d2-b15c-1ac998a90449) Learn about creating the Bronze Table in Python.
3. [**Unity Catalog - Silver Table:**](https://www.loom.com/share/3d18375f7d9a4794aea852f321f53e05?sid=31a17223-f5b3-4410-b1e4-540c30ecd35a) Learn about creating the Silver Table in Python.
4. [**Unity Catalog - Gold Table:**](https://www.loom.com/share/8316ffc602664678aab20cddc5aa2922?sid=1495b19d-8999-46da-98f6-3002fa683063) Learn about creating the Gold Table in Python.
5. [**Unity Catalog: DLT Pipeline Orchestration:**](https://www.loom.com/share/a3b3c5c0b53143699a8a2a432f6d856b?sid=460329ff-4329-4a03-9526-3c96dc67d845) Understand DLT Pipeline Orchestration. Using our tables created in the prior steps.
6. [**Unity Catalog: Viewing our date output:**](https://www.loom.com/share/7cacc898a3494ce085e7b47fe9d1dc70?sid=037b62e4-f6b3-41de-9113-1fee2632e465) We built our date, we build our pipeline - now lets take a look at its output.


## **Extras!**  

1. [**EngineLoop**](https://www.loom.com/share/0f154ad256f34b709646ef52e6ef1a71?sid=3251a2d6-c33d-41c6-9258-f8c013f67cc1) – Ever needed to process a large amount of files into various tables with minimal coding? Check out this Engine Loop video, which explores our options. 
    
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
    - [**Part 1 - High level overview of everything including the notebook, workflow, and cloud storage items**](https://www.loom.com/share/33f66f16b5de4bf485b82bdd6d316c38)  
    - [**Part 2 - Running through each scenario in the pipeline**](https://www.loom.com/share/82ff5b64c3c548c4bae2b992bf58f546?sid=2bd0829c-3411-468c-a8db-f527e1b679e5)  
    - [**Part 3 - Review and Recap, lets review the data**](https://www.loom.com/share/d8107c3c38814a45975b97d14a43e880?sid=d5971d38-8fa4-4149-8c34-92f5438fb0eb)  

3. [**Incorporating Secrets from Key Vault to Databricks**](https://www.loom.com/share/f4cd82e3530c4b56927b253d05bbffc2?sid=275380ab-02c8-45c1-b26c-f8f43d016586): 

    [**Notebook Link**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/API%20Tutorial/Creating%20and%20Connecting%20to%20vs%20APIs%20in%20KeyVault.ipynb)  🗝️  

4. **[Leveraging a Databricks Notebook to Connect Directly to an API Endpoint](https://www.loom.com/share/22b0f5eaf8874d3ba59833369d139188?sid=390a2479-0f49-450d-8635-ede0bb44154a) 💽**  

    [**Notebook Link**](https://github.com/jadkinsgr/CloudProficiency/blob/main/Databricks/Dive%20Into%20The%20Data%20Galaxy/SourceFiles/API%20Tutorial/API%20Call.py)
    
    Bypass the need to retrieve data from Azure Data Factory or AWS Glue—connect directly from Databricks!  

    - Create your Key Vault secret  
    - Set up a Databricks secret scope using Key Vault properties  
    - Assign the secret to a variable to bring everything together  

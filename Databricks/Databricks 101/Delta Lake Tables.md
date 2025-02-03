# Delta Tables

### Delta Lake Tables (High Level) by Databricks 🌟

Not to be confused with Data Lake, Delta Lake is a powerful storage layer offered by Databricks that brings reliability to data lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Simply put its more comprehensive and offers  several benefits over traditional data storage. Below are the key aspects and benefits of Delta Lake Tables:

1. **Reliability**: Delta Lake provides ACID transactions on Spark, ensuring data integrity and consistency. This enables concurrent reads and writes, making data operations reliable and robust.
2. **Scalability**: Delta Lake is highly scalable, allowing seamless handling of large data sets. It supports petabyte-scale data lakes, making it suitable for organizations with extensive data storage requirements.
3. **Streaming and Batch Unification**: Delta Lake unifies streaming and batch processing, providing a single source of truth for data ingestion and processing. This simplifies data pipelines and enables real-time analytics alongside batch processing.
4. **Schema Enforcement**: Delta Lake enforces schema on write, ensuring that incoming data adheres to predefined schema, thus enhancing data quality and consistency.
5. **Time Travel**: Delta Lake offers built-in data versioning, allowing users to access and revert to earlier versions of data, providing historical data snapshots and audit capabilities.
6. **Data Lake Optimization**: Delta Lake optimizes data storage by using advanced indexing and compaction techniques, resulting in efficient storage and improved query performance.
7. **Unified Analytics**: Delta Lake seamlessly integrates with the Databricks Unified Data Analytics Platform, providing a unified environment for data engineering, data science, and business analytics.
8. **Compatibility**: Delta Lake is fully compatible with Apache Spark APIs, making it easy for existing Spark users to transition to Delta Lake without major changes to their codebase.

# Databricks Lakehouse Fundamentals

# What is a delta lakehouse? - A environment to tie all your data lake resources together securely and centralized.

## Problems with data lakes

*   No Transactional Support
*   Poor Data Reliability
*   Slow Analysis Performance
*   Data Governance Concerns
*   Data Warehouses still needed
*   32% of companies said their data value was lossed or of no value

[https://customer-academy.databricks.com/learn/course/1325/fundamentals-of-the-databricks-lakehouse-platform?generated\_by=574087&hash=a0d059de069908c9d3ff81a6ec32e6b091203033](https://customer-academy.databricks.com/learn/course/1325/fundamentals-of-the-databricks-lakehouse-platform?generated_by=574087&hash=a0d059de069908c9d3ff81a6ec32e6b091203033)

## Businesses needed disparate incompatible platforms to function

![](https://t14110920.p.clickup-attachments.com/t14110920/fcebf58f-6845-4337-b428-000f11188538/image.png)

## Data Lakehouses provide both bi and ai together becoming a source of truth

  

![](https://t14110920.p.clickup-attachments.com/t14110920/c2b7df84-f403-419f-93df-2245a0eeffd3/image.png)

Other benefits include:

*   Transaction support (ACID)
*   Schema enforcement and governance
*   data governance
*   bi support
*   decoupled storage from compute
*   open storage formats
*   support for diverse data type and workloads

  

LAKE HOUSE = Today's Data warehouse

  

# What is the databricks Lakehouse platform

![](https://t14110920.p.clickup-attachments.com/t14110920/2f3d818e-05a3-43a9-981d-e37759713c93/image.png)

![](https://t14110920.p.clickup-attachments.com/t14110920/8bbb4f15-3c8d-4557-9966-221ac3cec08c/image.png)

  

# Databricks Lakehouse Platform Architecture and Security Fundamentals

## Data Reliability

*   Delta Lake and Photon provide optimal data reliability

### Delta Lake:

![](https://t14110920.p.clickup-attachments.com/t14110920/b7dc6851-212c-4b4f-a6a4-31d13ab1dfb4/image.png)

*   Compatible with Apache Spark
*   Uses Delta Tables
*   Has a Transaction log (allows for a multi transaction environment with history)!!
*   The ability to use so many sources:

![](https://t14110920.p.clickup-attachments.com/t14110920/91ba2ffd-abc3-48e3-8038-d79226f9130f/image.png)

### Photon:

Photon is the next generation query engine - it provides over 80% cost savings from traditional systems through efficiency. Its built on top of apache spark.

  

![](https://t14110920.p.clickup-attachments.com/t14110920/db5d0006-7f87-4aad-a60d-b724bb2dfa95/image.png)

  

![](https://t14110920.p.clickup-attachments.com/t14110920/4c71e9a4-530e-4de9-ac3c-03b87d98b639/image.png)

  

![](https://t14110920.p.clickup-attachments.com/t14110920/e3532d7c-c53b-4160-8fc7-655f6816e4d3/image.png)

  

![](https://t14110920.p.clickup-attachments.com/t14110920/f0647e85-e5e4-491a-8334-a0f058481d81/image.png)

  

Photon is compatible with SQL, Dataframes and Koalas

![](https://t14110920.p.clickup-attachments.com/t14110920/8d700e0c-6995-4de3-b8df-3cdd46e57344/image.png)

## Unified governance and security

### The importance of unified governance and security to platform architecture

Unity Catalog

1.     1. Unified data governance solution for all data assets
    2. Healthcare specific - columns can be tagged as PHI and then we can create one rule to manage all of PHI (viewable by whom etc)
    3. ![](https://t14110920.p.clickup-attachments.com/t14110920/29cab184-5c2c-4cd4-b202-b1c2dd31a5ae/image.png)

### Explain how unity catalog and delta sharing are used

1. Delta Sharing - data sharing - What we have typically had

![](https://t14110920.p.clickup-attachments.com/t14110920/a3b0be54-7c24-45d8-b96c-1e4093002d92/image.png)

What delta sharing provides: - users do not have to even be on the cloud or databricks system to view sharing of the data.

![](https://t14110920.p.clickup-attachments.com/t14110920/b81d5567-42cd-4b77-8a42-ae63045d4146/image.png)

  

Delta sharing offers many benefits including:

![](https://t14110920.p.clickup-attachments.com/t14110920/771841d9-5848-4fa3-b341-457504f0816a/image.png)

  

### Differentiate between the control plane and the data plane in the Databricks Lakehouse platform architecture

In Databricks, the control plane and the data plane serve distinct purposes:

*   **Control Plane**: This is responsible for managing the Databricks environment, including tasks such as creating and managing clusters, configuring access control, and monitoring the overall health and performance of the environment. The control plane handles administrative and management functions, allowing users to control the configuration and settings of their Databricks environment.
*   **Data Plane**: This is the component of Databricks that handles the actual data processing and storage tasks. It is where data is ingested, processed, and analyzed using tools like Apache Spark, Delta Lake, and other data processing frameworks. The data plane is where the computational and storage resources are utilized to perform data operations and run workloads.

In summary, the control plane deals with the management and configuration of the Databricks environment, while the data plane is responsible for the actual data processing and analysis tasks.

  

  

![](https://t14110920.p.clickup-attachments.com/t14110920/9c4018f0-978c-4ea6-9f78-fb7d7484165a/image.png)

  

User Identity and access

![](https://t14110920.p.clickup-attachments.com/t14110920/7b2406f2-2178-4469-a713-fbc64cddd4ef/image.png)

![](https://t14110920.p.clickup-attachments.com/t14110920/b6667cc2-6245-403c-8fd0-0dbf90ec92f8/image.png)

###   

* * *

## Instant compute and serverless

Creating data clusters (computes) for many users is difficult - its hard to balance the needs with the resources pool while maintaining a delicate balance with budget.

  

Thats why Databricks offers Serverless Data Planes

Serverless computes - puts the bill within the databricks account rather then the cloud account like AWS and Azure - its also substantially cheaper.

![](https://t14110920.p.clickup-attachments.com/t14110920/085db27e-5e33-45c6-b392-b3b55504e3c7/image.png)

  

![](https://t14110920.p.clickup-attachments.com/t14110920/fbdeb36b-479a-493a-9cbb-fbf9cd0849ee/image.png)

  

The clusters are cheaper because it grabs always running - server fleet instances that are are always on and at the ready to be allocated to your workspace.

![](https://t14110920.p.clickup-attachments.com/t14110920/d7abc556-3980-4c28-92fc-417297520ed3/image.png)

  

## Intro to lakehouse data management - Terms to know

*   **Delta Lake**: Delta Lake is an open-source storage layer that brings reliability to data lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of your existing data lake and is fully compatible with Apache Spark APIs.
*   **Unity Catalog**: Unity Catalog is a feature of Databricks that provides a unified metadata service for managing data and objects across different Databricks workspaces and accounts. It allows users to access and manipulate metadata across workspaces and accounts without having to switch between them.
*   **Metastore**: A metastore is a repository of metadata such as the schema structure and partitioned columns of tables in a data warehouse. In Databricks, the metastore is used to store and manage metadata related to tables and views, making it easier to query and analyze the data.
*   **Schema**: In the context of Databricks, a schema refers to the organization or structure of a dataset. It defines the columns, data types, and other properties of the data within a table or file.
*   **Table**: A table in Databricks refers to a structured set of data, organized into rows and columns. Tables can be created from various data sources and are used for querying and analyzing data using SQL or other programming languages. (these can be managed tables or external tables)
*   **View**: In Databricks, a view is a virtual table based on the result set of a SQL query. It does not store the data itself but provides a way to present the results of a query as a table.
*   **Function**: In Databricks, a function refers to a reusable piece of code that performs a specific task. Functions can be defined and used in SQL, Python, Scala, or other supported languages for data processing and analysis.
*   **Storage Credential**: A storage credential in Databricks is used to securely access external data storage systems such as Azure Blob Storage, AWS S3, or Google Cloud Storage. It includes the necessary authentication information (e.g., access keys, secrets) to connect to the external storage. These are created by admins.
*   **External Location**: In Databricks, an external location refers to a storage location outside of the Databricks environment, such as Azure Blob Storage, AWS S3, or Google Cloud Storage. It can be used to access and query data stored in these external locations from within Databricks.
*   **Share**: In Databricks, a share is a feature that allows users to share data, notebooks, and other resources with specific individuals or groups within the Databricks workspace.
*   **Recipient**: A recipient refers to the individual or group who is intended to receive a shared resource or communication within the Databricks environment. This could include shared data, reports, or other information.

# Supported Workloads on the Databricks Lakehouse Platform

![](https://t14110920.p.clickup-attachments.com/t14110920/7fa8dd75-f529-4480-8a56-3931e2cdc519/image.png)

*   Best price for performance - greater scale and elasticity
*   Built in governance
    *   Single copy in your datalakes - unity catalog controls it all
*   Rich ecosystem of tools all under the databricks lakehouse platform to work with tools like DBT or tableau
*   Breakdown of silos - by centralizing tools
*   **Cost savings are 24-40%!**

## Data Engineering

![](https://t14110920.p.clickup-attachments.com/t14110920/a0bed8a6-f36b-4cb8-b104-5877963ecbd7/image.png)

### Data Engineering Challenges we face everyday:

*   complex data ingestion methods
*   support for data engineering principles
*   third party orchestration tools
*   pipeline and architecture performance tuning
*   inconsistencies between data warehouse and data lake providers

Databricks provides:

![](https://t14110920.p.clickup-attachments.com/t14110920/49513b92-d5b8-4d55-88f1-61dc57e71fe6/image.png)

### **Databricks lakehouse platform benefits a data engineer**

*   **Easy Data Ingestion (petabytes of data made easy)**
*   **Automated ETL Pipelines**
*   **Data Quality Checks**
*   **Batch and Streaming tuning with cost controls**
*   **Automatic recovery**
*   **Data Pipeline observability**
*   **Simplified operations**
*   **Scheduling and orchestration**

### Delta Live Tables

![](https://t14110920.p.clickup-attachments.com/t14110920/d9e50979-3c2d-4241-bea3-ef0d473d02dc/image.png)

*   Auto loader will process new data files as they arrive in the cloud platform without hitting the old files.

![](https://t14110920.p.clickup-attachments.com/t14110920/caed5704-cf86-45cc-b27e-15b1a7ec6cbb/image.png)

Data Transformation (through medallion architecture) is key - Delta Live Tables are incredibly valuable.

*   DLT is the first ETL process that is declarative and can scale automatically. DLT can support python and sql.
*   Dev and Prod environments are also supported.

  

### Databricks workflows support for data orchestration

*   Workflows enables built in data orchestration pipelines regardless of source or platform.

## Streaming Data (Real-Time) - ex: ADT Data

*   Databricks supports:
    *   Realtime analytics
    *   Realtime machine learning
    *   Realtime applications
*   Industry uses:
    *   Retail (point of sale software)
    *   Industrial automation (automated process handling)
    *   Healthcare: (ADT)
    *   financial institutions (fraud alerts)

![](https://t14110920.p.clickup-attachments.com/t14110920/fad69d90-35ef-4d2a-8d3f-2a046b034b4d/image.png)

![](https://t14110920.p.clickup-attachments.com/t14110920/6ed06f32-1cc9-4774-b202-0a370201fa15/image.png)

FAQ ⁉️

In Databricks, Delta Live Tables and Spark Structured Streaming are both technologies for real-time data processing, but they have different functionalities and use cases:

*   **Delta Live Tables**: This is a feature within the Databricks Lakehouse Platform that provides continuous data processing for real-time analytics and applications. It is built on Delta Lake and enables real-time data ingestion, processing, and analytics with ACID transactions, schema enforcement, and time travel capabilities. Delta Live Tables is designed to handle both streaming and batch data with unified APIs, enabling consistent processing for both types of data.
*   **Spark Structured Streaming**: This is a component of Apache Spark that provides a high-level API for stream processing. It allows for the processing of live data streams with the same DataFrame and SQL APIs provided for batch processing. Spark Structured Streaming enables continuous computation and output updates as new data arrives, making it suitable for real-time analytics, event processing, and data integration scenarios.

In summary, Delta Live Tables is a feature of the Databricks Lakehouse Platform that provides real-time data processing capabilities with features specific to Delta Lake, while Spark Structured Streaming is a component of Apache Spark that enables continuous processing of live data streams using familiar DataFrame and SQL APIs.

## Supported workflows for data science and machine learning

![](https://t14110920.p.clickup-attachments.com/t14110920/0c1d42c2-1b55-4232-b4e9-b48d11933852/image.png)

Data Science Example:

![](https://t14110920.p.clickup-attachments.com/t14110920/4d30e361-1e84-4040-ae04-6c5f1458cfbf/image.png)

  

ML FLOW - Allow you to train and score models

![](https://t14110920.p.clickup-attachments.com/t14110920/4e09f240-0b84-4cc1-bd50-014715b9e9f0/image.png)

![](https://t14110920.p.clickup-attachments.com/t14110920/2eebc604-6a7f-49c4-a0ec-7c4d11a6ab55/image.png)

![](https://t14110920.p.clickup-attachments.com/t14110920/c67aa605-1adb-4c94-911e-aeb79d31f9ba/image.png)
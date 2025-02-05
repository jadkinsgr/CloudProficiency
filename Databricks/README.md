# Welcome!

# Databricks Introduction 101

## Introduction to Databricks 🚀

Databricks is a unified data analytics platform designed to be a collaborative environment for data science, engineering, and business analytics. It provides a workspace for users to create and manage data science projects, collaborate with peers, and deploy models into production. 

### [Trials Offered by Databricks](https://www.databricks.com/try-databricks#account) 🧱
1. Databricks offers a community edition that lasts for 6 months and is free for learning (recommended). 
2. A more extensive free 14 day trial is offered as well with an integration with cloud storage providers (AWS, Azure, Google Cloud Storage). (I **do not** recommend this one unless you are very comfortable already - you can quickly and easily rack up personal server charges).
---
## Native Connections to Cloud Storage ☁️

Databricks provides native connections to major cloud storage platforms, including AWS, Azure, and Google Cloud Storage. These connections allow seamless integration with data stored in these cloud platforms, enabling data engineers and data scientists to easily access, process, and analyze data without having to move it to a different location.

### Partner Connections

*   **AWS**: Databricks can directly connect to Amazon S3 for storing and accessing data.
*   **Azure**: Databricks has native integration with Azure Blob Storage for seamless data access.
*   **Google Cloud**: Databricks provides native connections to Google Cloud Storage for efficient data processing.

### Medallion Structure within Databricks 🥇

Databricks provides a structured approach to managing data, commonly referred to as the "Medallion Structure." This approach involves organizing data into three main categories: bronze, silver, and gold, each serving a specific purpose in the data lifecycle.

<IMG  src="https://www.databricks.com/wp-content/uploads/2019/08/Delta-Lake-Multi-Hop-Architecture-Bronze.png"/>

### **Bronze Data** (Raw Data)

*   **Description**:
    *   Bronze data represents the raw, unprocessed data ingested into the system. This data is often ingested from various sources such as databases, streaming platforms, or files.
*   **Characteristics**:
    *   Raw, untransformed data
    *   Minimal processing or cleansing
    *   Often includes duplicates, errors, and inconsistencies
    *   Usually stored in its original form
*   **Processing Steps**:
    *   Ingestion from source systems
    *   Basic schema enforcement
    *   Minimal data cleaning (e.g., removing irrelevant fields)

### **Silver Data** (Cleaned Data)

*   **Description**:
    *   Silver data is the intermediate stage where data has undergone processing and cleansing to make it suitable for analysis and modeling.
*   **Characteristics**:
    *   Processed and cleansed data
    *   Standardized schema
    *   De-duplication and error correction
    *   May include derived or aggregated data
*   **Processing Steps**:
    *   Data transformation (e.g., normalization, standardization)
    *   Quality checks and error handling
    *   Aggregations, enrichments, and feature engineering

### **Gold Data** (Report Quality Data)

*   **Description**:
    *   Gold data represents the highest quality of data, refined for use in reporting, visualization, and advanced analytics.
*   **Characteristics**:
    *   Highly refined, quality-assured data
    *   Optimized for reporting and analytics
    *   Well-documented and governed
    *   Typically used for business intelligence and decision-making
*   **Processing Steps**:
    *   Advanced data quality checks
    *   Optimization for query performance
    *   Documentation and metadata management
    *   Implementation of access control and governance
---
  

## Introduction to Serverless Data Warehouses 💡

Databricks provides the capability to create a serverless data warehouse using its Unified Data Analytics platform. By leveraging Databricks for data warehousing, users can benefit from the scalability, flexibility, and cost-efficiency of serverless computing for their data storage and analytics needs. 
(**TL;DR**: It saves the organization a lot of money.)

### Benefits of Serverless Data Warehouse

*   Scalability: Databricks allows the serverless data warehouse to scale automatically based on the workload, ensuring optimal performance.
*   Cost-efficiency: With serverless computing, users only pay for the resources they use, leading to cost savings.
*   Flexibility: Serverless data warehousing in Databricks offers flexibility in managing and analyzing data without the overhead of infrastructure management.
*   Fast and easy to spin up a serverless data warehouse. (10 seconds or so) with the ability to spin it back down after X minutes of inactivity.

### Creating a Cluster in Databricks 🧱

Databricks enables users to create clusters for distributed data processing and computation. Here's a high-level overview of creating a cluster in Databricks:

1. **Cluster Creation**: Users can create clusters in Databricks through the web interface or programmatically using the Databricks API.
2. **Usage and Management**: Utilize the cluster for data processing, analytics, and machine learning tasks, and manage the cluster's lifecycle as needed.
3. **Clusters** can be scaled on demand and you can create as many clusters that you want for various use- cases.
---
### Knowledge check! 💡

1. **Databricks:** Unified data analytics platform for collaborative data science, engineering, and business analytics. Partner connections to AWS, Azure, and Google Cloud Storage.
2. **Medallion Structure:** Organizes data into Bronze (raw), Silver (cleaned), and Gold (report-quality) categories for various stages in the data lifecycle.
3. **Serverless Data Warehouse:** Databricks enables a serverless data warehouse for scalable, flexible, and cost-efficient data storage and analytics. Quick to spin up and down based on usage.
4. **Cluster Creation:** Databricks allows users to create clusters for distributed data processing and computation, scalable on demand for diverse use-cases.
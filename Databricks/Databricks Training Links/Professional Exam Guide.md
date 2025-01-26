# Databricks Professional Training Guide

### Assumption:

This guide assumes that the user has already taken the Databricks Associate level exam.

### Link to Course Materials:

- **Primary Link**: Course+Materials.dbc
- **If the link above doesn’t work**:
    - Navigate to `devops > AnalyticsDojo > Repos > AnalyticsDojo > DatabricksTrainingMaterials`
    - Download: `Course_Materials.dbc`

---

## Overview:

The course covers the following key topics:

- **Data Modeling**
- **Data Processing**
- **Improving Performance**
- **Databricks Tooling**
- **Security Governance**
- **Testing and Deployment**

The `Course + Material dbs` file contains 7 folders, each with notebooks for following along. The **"includes"** notebook is used to load the course data into each of the other notebooks.

---

### 1) Modeling Data Management Solutions

### 1.1 Ingestion Patterns

- **Singleplex**: One-to-one mapping (e.g., one table to one bronze table).
- **Multiplex**: Many-to-one mapping (e.g., stream multiple tables into one table).
    - **Topic Column**: This column represents the name of the table from which the row came, and each row’s value is a JSON object containing the table’s columns.

### 1.2 Streaming from Multiplex Bronze

- Initial data connection via mounting a storage account containing Kafka files.
- Use **Autoloader** to read in the files and define columns such as `timestamp` and `year-month`.
- **Trigger** (`availableNow=True`) is used for batch execution, reading everything available before stopping.

### 1.3 Quality Enforcement

- Constraints can be added to tables to enforce data rules (e.g., `timestamp > '2020-01-01'`).
- Violations will fail the insertion process and not add the problematic rows.

### 1.4 Streaming Deduplication

- **Deduplication** is performed at the **silver** level, not on the original **bronze** table.
- Use `dropDuplicates()` in static data and structured streaming.
- **Watermarking** (`.withWatermark()`) is used to limit the state that is tracked.

### 1.5 Slowly Changing Dimensions (SCD)

- **SCD Type 2**: Adds a new row for each change and marks the old row as obsolete.
    - **Fields**: `current`, `effective_date`, `end_date`.

---

### 2) Data Processing

### 2.1 Change Data Capture (CDC)

- Tracks changes (insert, update, delete) in source data.
- **For Streaming**: Use `foreachBatch` to handle CDC in streaming data.

### 2.2 Delta Lake CDF (Change Data Feed)

- Automatically generates CDC feeds for Delta tables, tracking row-level changes.
- **_change_type**: Indicates changes like `update_preimage` (before) and `update_postimage` (after).

### 2.3 Stream-Stream Joins

- Spark buffers past input streams to join them with future inputs. The join syntax is the same as for static tables.

### 2.4 Stream-Static Joins

- Static tables are not stateful and do not trigger join operations when new records are added.
    - Use `writeStream` in append mode for streaming joins.
    - To handle unmatched records, create a separate method for them.

### 2.5 Materialized Gold Tables

- Using **views** for memory and cost efficiency.
- **Materialized Views** store the results and persist them, unlike regular views that are cached.

---

### 3) Improving Performance

### 3.1 Partitioning Delta Lake Tables

- Partition by a meaningful column (e.g., `year`, `date`, `IDs`).
- Aim for partitions of around 1GB in size to optimize performance and reduce costs.

### 3.2 Delta Lake Transaction Log

- Each commit to a table writes a transaction log.
- Checkpoints are created every 10 commits to optimize table reads.
- File statistics track column data (e.g., `max`, `min`, `null count`).

### 3.3 Auto-Optimizing Delta Lake

- Delta automatically compacts small files to optimize storage.
- Use the properties:`delta.autoOptimize.optimizeWrite = Truedelta.autoOptimize.autoCompact = True`

---

### 4) Databricks Tooling

### 4.1 Configuring Multi-Task Jobs

- Create a job and configure multiple tasks (e.g., "Land new data").
- Add parameters for task orchestration (e.g., `number_of_files`).

### 4.2 CLI (Command Line Interface)

- Generate a **Personal Access Token (PAT)** from the settings menu.
- Install and configure the Databricks CLI via terminal.

---

### 5) Propagating Deletes

### 5.1 Propagating Deletes in Delta

- Deletes can be propagated from the bronze table by using the `DELETE` function in SQL.
- Compare deleted versions using the `EXCEPT` keyword.

### 5.2 Dynamic Views for Access Control

- Use **Access Control Lists (ACLs)** to restrict access to specific columns or rows of a table based on user roles.

---

### 6) Testing and Deployment

### 6.1 Relative Imports – Notebooks

- Import code from other notebooks using `%run` or `.py` scripts.
- Handle **clear state** errors by resetting the notebook state.

### 6.2 Data Pipeline Testing

- **Unit Testing**: Ensures code functions as expected by testing individual pieces of code.
- **Integration Testing**: Tests how subsystems interact.
- **End-to-End Testing**: Tests the entire pipeline in development, mimicking production data.

---

### 7) Monitoring Clusters

### 7.1 Cluster Permissions and Access

- Manage permissions via the **admin console** to control who can create clusters.
- Create user groups and assign permissions for cluster access.

### 7.2 Debugging Clusters

- Use the **Event Log** and **Metrics** tabs to monitor cluster events and resource usage (e.g., CPU, memory).
- Check cluster **library** installations to ensure consistency.

### 7.3 Cluster Configuration

- Choose appropriate **node types** and **driver types** to balance cost and performance.
- Review cluster policies to manage access control and functions.

---

### Exam Question Breakdown

- **18/60** – Data Processing
- **12/60** – Data Modeling
- **12/60** – Data Tooling
- **6/60** – Security and Governance
- **6/60** – Testing / Deployment
- **6/60** – Monitoring and Logging


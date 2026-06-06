# Databricks-Genie-Medallion-Pipeline

## AI Assisted Medallion Data Pipeline using Databricks Genie

### Overview

This project demonstrated the implementation of Medallion Architecture (Bronze, Silver and Gold layers) using Databricks Genie for AI Assisted Data Engineering.

The pipeline processes synthetic order data generated in JSON format and automatically creates structured data layers to support business analytics.

### Flow diagram of ETL pipeline

![image_alt](https://github.com/BhaskarKosala/Databricks-Genie-Medallion-Pipeline/blob/93ade16df788ad297ab020db3e3fe38ede01e7c4/Databrics%20Genie%20Flowchart.drawio.png)

### Technologies Used

- Databricks
- Databricks Genie
- Python
- SQL
- Delta Tables
- Medallion Architecture

### Business Requirements

The pipeline was designed to:

1. Ingest JSON Order data.
2. Filter records where order status is 'cancelled'.
3. Implement Bronze, Silver and Gold layers.
4. Generate business metrics:
   - Total sales by city
   - Total orders by status

### Architecture

```mermaid
flowchart TD
    A[JSON Files] --> B[Bronze Layer<br/>Raw Data]
    B --> C[Silver Layer<br/>Cleaned Data]
    C --> D[Gold Layer<br/>Business Metrics]
```

### Implementation Steps

#### Data Generation

A Python script was used to generate synthetic order data.

#### Databricks Setup

- Created Catalog
- Created Schema
- Created Volume
- Uploaded JSON data generation script in python workspace

#### AI Assisted Pipeline Creation

Databricks Genie was provided business requirements and generated the pipeline workflow.

#### Validation

The generated Bronze, Silver and Gold layers were validated to ensure:
- Correct filtering logic
- Accurate Metric calculations
- Proper Medallion Architecture implementation

### Business Metrics

#### Metric 1

Total Sales by City

#### Metric 2

Total Orders by Status

### ETL Pipeline in Databricks

![image_alt](https://github.com/BhaskarKosala/Databricks-Genie-Medallion-Pipeline/blob/418b86a976476c63dd977ea6d3ec1469dab76078/%20pipeline.png)

### Key Learnings

- Medallion Architecture
- AI Assisted Data Engineering
- Databricks Data Organization
- Data Validation Techniques
- Conversational Analytics using Databricks Genie

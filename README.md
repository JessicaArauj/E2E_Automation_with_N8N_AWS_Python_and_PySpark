# E2E Automation with N8N, AWS, Python and PySpark

This project implements an **end-to-end automation workflow** for collecting, processing, and exposing **broadband access data in Brazil**. It allows automated extraction, transformation and storage in a **Data Lake on AWS S3**, and provides access via a **REST API** as well as **natural language queries** through a user-friendly interface.

## Features

- **Automated Data Collection**  
  - Retrieves broadband access datasets from `dados.gov.br`.  
  - Downloads and extracts ZIP files containing CSVs.  

- **Data Transformation and Processing**  
  - Cleans and standardizes data using **Python** and **PySpark**.  
  - Handles multiple CSV formats including wide, density and total datasets.  
  - Maps months to names and states (`UF`) to regions.  

- **Data Lake Integration**  
  - Stores processed CSVs on **AWS S3**.  
  - Organizes files in a structured hierarchy (`processed_data/`).  

- **Workflow Orchestration**  
  - Automates ETL and data upload via **N8N** workflows.  
  - Allows scheduling and monitoring of data pipelines.  

- **Data Access**  
  - Provides a **REST API** to query processed datasets.  
  - Supports **natural language queries** with optional LLM integration via Firebase Studio.  

## Installation

The project can run on **Google Colab** or a local Python environment. Required libraries:

```bash
!pip install boto3
!pip install pyspark
!pip install pandas
!pip install tqdm
````
Ensure AWS credentials are set either in the environment or through userdata in Colab:

```python
from google.colab import userdata

AWS_ACCESS_KEY_ID = userdata.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = userdata.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = userdata.get('AWS_REGION')
BUCKET_NAME = userdata.get('BUCKET_NAME')
````

## Main Structure

- **S3 Client**: Handles downloads and uploads of raw and processed datasets.
- **Spark ETL Pipelines**: Processes CSV files in different formats (`normal`, `colunas`, `densidade`, `total`).
- **UDFs**: Maps month numbers to names and states to regions.
- **N8N Workflow**: Orchestrates the entire ETL pipeline, from download to S3 upload.
- **REST API Integration**: Allows querying processed data and supports natural language interaction.

## Configuration

- Configure AWS credentials in **environment variables** or via **Colab userdata**.
- Ensure the **S3 bucket** exists and is accessible.
- Schedule the workflow in **N8N** for automated execution.
- Optionally, configure **Firebase Studio** for LLM-based queries on the processed datasets.

## Notes

- This project is designed as a **prototype** and should be adapted for production with security and performance optimizations.
- Large datasets may require sufficient **memory and Spark resources** to process efficiently.
- Proper **AWS IAM permissions** are required for S3 access.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as needed.



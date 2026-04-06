# 🚀 LTA AWS Data Pipeline 

## 📌 Overview

This project demonstrates a complete **cloud-based data engineering pipeline** built using **Python, AWS S3, and Athena**.

The pipeline ingests real-time transport data from Singapore’s LTA API, stores it in a cloud data lake, transforms it into structured format, and enables SQL-based analytics using Athena.

---

## 🎯 Problem Statement

Transport data from APIs is often unstructured and not stored for historical analysis. This project solves that by:

- Ingesting real-time API data
- Storing raw data in a scalable cloud storage (S3)
- Transforming nested JSON into structured tabular data
- Enabling analytics using SQL without managing infrastructure

---

## 🏗️ Architecture

      +-------------------------+
      |   LTA API / Source Data |
      +-------------------------+
                  │
                  ▼
      +-------------------------+
      |   Python Ingestion      |
      |   (requests)            |
      +-------------------------+
                  │
                  ▼
      +-------------------------+
      |   Amazon S3 Raw Layer   |
      |   (JSON Storage)        |
      +-------------------------+
                  │
                  ▼
      +-------------------------+
      |   Python Transform      |
      |   (pandas)              |
      +-------------------------+
                  │
                  ▼
      +-------------------------+
      | Amazon S3 Processed     |
      | Layer (CSV KPI Ready)   |
      +-------------------------+
                  │
                  ▼
      +-------------------------+
      |   Amazon Athena         |
      |   (SQL Analytics)       |
      +-------------------------+
                  │
                  ▼
      +-------------------------+
      | Query Results / Reports |
      | Stored in S3            |
      +-------------------------+
---

## 🔄 Pipeline Flow

1. Fetch bus arrival data from LTA API
2. Store raw JSON data locally and upload to S3
3. Transform nested JSON into structured tabular format
4. Upload processed data to S3
5. Query data using Athena

---

## 📊 Sample Queries

- Count total records
- Service frequency analysis
- Load distribution
- Data completeness checks

---

## 📂 Project Structure

```
│
├── data/                     
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   │   ├── fetch_lta_data.py
│   │   └── upload_to_s3.py
│   │
│   ├── transformation/
│   │   ├── transform_data.py
│   │   └── upload_processed_to_s3.py
│   │
│   ├── utils/
│   │   └── aws_helper.py
│
├── config/
│   └── config.py
│
├── screenshots/             
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env                   

```

---
## 🚀 Key Features

- Modular pipeline design
- Secure credential handling using `.env`
- Partitioned S3 storage structure
- Serverless querying with Athena
- Cost-efficient cloud architecture

---

## 💡 Future Improvements

- Convert CSV to Parquet for better performance
- Add partitioning for Athena optimization
- Automate pipeline using AWS Lambda or Airflow
- Build dashboard using Power BI or QuickSight

---

## 🧠 Learnings

- Built end-to-end cloud data pipeline
- Designed S3-based data lake
- Integrated Python with AWS services
- Implemented serverless analytics using Athena

---

## 👨‍💻 Author

Vamsi Krishna

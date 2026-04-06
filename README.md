# lta-aws-data-pipeline

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

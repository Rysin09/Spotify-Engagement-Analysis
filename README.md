<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg" width="180" />
</p>

<h1 align="center">Spotify Engagement Analysis 🎧📊</h1>

<p align="center">
A complete Data Engineering + Analytics pipeline built using <b>AWS S3, Glue, Athena, and Power BI</b>.
</p>

---

## 🚀 Project Overview

This project builds an **end-to-end cloud analytics pipeline** that ingests Spotify listening history, transforms it using AWS Glue (PySpark), optimizes storage using Parquet, queries data using Athena, and visualizes insights using Power BI.

You learn & demonstrate **real industry-level data engineering**.

---

## 🏗️ Architecture (Concise Flow)
<pre style="background:#f8f8f8; padding:18px; border-radius:6px;">
S3 (Raw CSV)
↓
Glue Crawler (Auto Schema Detection)
↓
Glue Data Catalog (RAW Table)
↓
Glue ETL Job (Transform → Parquet)
↓
S3 (Processed Parquet)
↓
Glue Data Catalog (Processed Table)
↓
Amazon Athena (Query Engine)
↓
Power BI (Visualization)
  </pre>


---

## 🔧 Tech Stack

| Tool / Service | Purpose |
|----------------|---------|
| **Amazon S3** | Data Lake (Raw + Processed zones) |
| **AWS Glue Crawler** | Detect schema from CSV and build metadata |
| **AWS Glue ETL (PySpark)** | Transform → clean → convert to Parquet |
| **AWS Glue Data Catalog** | Central metadata store for Athena |
| **Amazon Athena** | Serverless SQL engine querying S3 parquet |
| **Power BI** | Dashboards & visual analytics |
| **Python / PySpark** | ETL logic |

---

## 📁 Repository Structure
<pre style="background:#f8f8f8; padding:18px; border-radius:6px;">
  /
├── architecture/
│ └── aws_spotify_architecture.png
│
├── assets/
│ ├── s3_raw.png
│ ├── s3_processed.png
│ ├── glue_crawler.png
│ ├── glue_job_success.png
│ ├── athena_query.png
│ └── powerbi_dashboard.png
│
├── code/
│ └── glue_etl_script.py
│
├── sql/
│ └── athena_queries.sql
│
├── docs/
│ ├── project_flow.md
│ └── powerbi_connection_guide.md
│
├── data/
│ └── sample_spotify_history.csv
│
└── README.md
</pre>


---

## 🧠 What This Pipeline Does

- Converts raw Spotify history into clean, analysis-ready data  
- Generates optimized **Parquet** + **partitioned** data  
- Enables fast SQL analytics through Athena  
- Creates an automated, scalable **data lake → warehouse → BI** workflow  
- Produces a Power BI dashboard with listening insights  

---

## 📊 Insights Generated

- Total listening time (daily / monthly / yearly)  
- Top artists, top tracks  
- Listening trends over time  
- Skip rate, shuffle behavior  
- Time-of-day analytics  
- Heatmaps for weekday × hour patterns  

---

## 🛠️ How It Works (Short Explanation)

**1. Upload Raw CSV → S3**  
Your Spotify history file is added to the data lake (raw zone).

**2. Glue Crawler → Detect Schema**  
Automatically identifies CSV columns & types.  
Creates a RAW table inside Glue Data Catalog.

**3. Glue ETL Job → Transform**  
PySpark script:  
- Cleans timestamps  
- Adds useful columns (year, month, hour, weekday, etc.)  
- Converts CSV → Parquet  
- Writes to S3 processed zone

**4. Athena → Query Layer**  
Athena reads processed Parquet files via the catalog.  
Provides SQL analytics.

**5. Power BI → Dashboard**  
Power BI connects to Athena via ODBC.  
Data is imported and visualized.

---

## 🖼️ Architecture Diagram

*(Add your AWS dark-theme diagram here)*



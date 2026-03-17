Sales Analytics Data Pipeline

Overview

This project implements an end-to-end data engineering pipeline that processes sales data, stores aggregated results in a relational database, and exposes analytics through a REST API and dashboard.

The pipeline demonstrates how raw transactional data can be transformed into analytical insights using modern data engineering tools.

Architecture

CSV Dataset
     │
     ▼
Python Data Generation
     │
     ▼
PySpark ETL Processing
     │
     ▼
PostgreSQL Database
     │
     ▼
Node.js REST API
     │
     ▼
React Dashboard

Dataset

A synthetic dataset containing 50,000 sales transactions was generated using Python.

Dataset fields:

- order_id
- product
- category
- price
- quantity
- revenue

ETL Pipeline

1. Data Generation

A Python script generates the dataset and stores it as a CSV file.

Location:

etl/clean_data.py

Output:

data/sales.csv

2. Data Processing

PySpark processes the dataset and performs aggregation operations such as:

- total revenue by product
- sales distribution
- price statistics

Location:

etl/spark_process.ipynb

Output:

data/product_revenue/product_revenue.csv

3. Data Storage

Processed analytics data is loaded into a PostgreSQL database.

Database table:

product_revenue

Backend API

A Node.js Express API exposes the analytics data.

Endpoint:

GET /revenue

Example response:

[
  { "product": "Laptop", "revenue": 12450000 },
  { "product": "Phone", "revenue": 10320000 },
  { "product": "Tablet", "revenue": 8760000 },
  { "product": "Monitor", "revenue": 6450000 }
]

Backend location:

backend/server.js

Frontend Dashboard

A React dashboard visualizes revenue analytics using Chart.js.

Features:

- revenue distribution by product
- interactive bar chart visualization
- API integration with backend service

Frontend location:

frontend/react-dashboard

Technology Stack

Data Processing

- Python
- PySpark
- Pandas

Database

- PostgreSQL

Backend

- Node.js
- Express

Frontend

- React
- Chart.js
- Axios

Dev Tools

- Git
- Docker (basic setup)

Project Structure

sales-data-pipeline
│
├── backend
│   └── server.js
│
├── data
│   ├── sales.csv
│   └── product_revenue
│
├── docker
│
├── etl
│   ├── clean_data.py
│   └── spark_process.ipynb
│
├── frontend
│   └── react-dashboard
│
└── README.md

Running the Project

Start Backend

cd backend
node server.js

Server runs at:

http://localhost:5000

Start Frontend

cd frontend/react-dashboard
npm start

Dashboard runs at:

http://localhost:3000

Key Learning Outcomes

- Building a batch data pipeline using PySpark
- Designing ETL workflows for structured data
- Integrating PostgreSQL with backend APIs
- Creating data visualization dashboards
- Structuring full-stack analytics projects

Future Improvements

- Automate ETL pipeline with Airflow
- Containerize services using Docker
- Deploy pipeline on cloud infrastructure
- Add streaming ingestion with Kafka
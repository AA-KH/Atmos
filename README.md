# Atmos 🌍

> A production-inspired Data Engineering platform for collecting, processing, monitoring, analyzing, and visualizing real-time environmental intelligence for cities worldwide.

---

# Overview

Atmos is an end-to-end Data Engineering project that demonstrates how modern data systems ingest, validate, transform, store, analyze, monitor, and visualize real-world data.

The platform gathers live weather and air-quality information from external APIs, processes the incoming data through a structured ETL pipeline, stores the results in a relational database, generates analytical metrics, tracks pipeline performance, exports datasets, and presents insights through an interactive dashboard.

The project was intentionally built around practical Data Engineering concepts and workflows commonly found in industry environments rather than purely academic exercises.

---

# Core Features

## Data Ingestion

- Global city search
- Geocoding integration
- Weather data ingestion
- Air quality ingestion
- Dynamic city onboarding

## ETL Pipeline

- Extract data from external APIs
- Transform raw responses into structured records
- Validate records before storage
- Load validated data into a database

## Data Validation

- Schema validation using Pydantic
- Type enforcement
- Data quality checks
- Invalid record protection

## Storage Layer

- SQLite database
- SQLAlchemy ORM
- Relational modeling
- Foreign-key relationships

## Analytics Engine

- Weather scoring
- AQI scoring
- Readiness scoring
- Risk classification

## Monitoring

- Pipeline execution tracking
- Runtime measurement
- Success/failure tracking
- Historical execution logs

## Dashboard

- City readiness rankings
- City explorer
- Pipeline monitoring
- Dataset explorer
- Dynamic city search

## Deployment

- Dockerized application
- Docker Compose support
- Portable deployment workflow

---

# Architecture

```text
User
 │
 ▼
Streamlit Dashboard
 │
 ▼
Pipeline Layer
 │
 ├── Geocoding API
 ├── Weather API
 └── Air Quality API
 │
 ▼
Validation Layer
 │
 ▼
Transformation Layer
 │
 ▼
SQLite Database
 │
 ├── Cities
 ├── Weather
 ├── Air Quality
 ├── Daily Metrics
 └── Pipeline Runs
 │
 ▼
Analytics Layer
 │
 ▼
CSV Export Layer
 │
 ▼
Dashboard Visualizations
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.13 |
| Dashboard | Streamlit |
| Database | SQLite |
| ORM | SQLAlchemy |
| Data Processing | Pandas |
| Validation | Pydantic |
| API Communication | Requests |
| CLI | Typer |
| Containerization | Docker |
| Orchestration | Docker Compose |

---

# Project Structure

```text
Atmos/
│
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── data/
│   └── exports/
│
├── src/
│   ├── analytics/
│   ├── clients/
│   ├── dashboard/
│   ├── monitoring/
│   ├── pipeline/
│   ├── transformers/
│   ├── validators/
│   ├── database.py
│   ├── models.py
│   ├── config.py
│   └── create_database.py
│
└── README.md
```

---

# Data Pipeline

Atmos follows a traditional ETL architecture.

## Extract

The system retrieves:

- City metadata
- Geographic coordinates
- Weather information
- Air quality information

from the Open-Meteo ecosystem.

## Transform

Raw API responses are normalized into a consistent internal structure.

Typical transformations include:

- Datetime conversion
- Field renaming
- Type conversion
- Score generation
- Data cleaning

## Validate

All transformed records pass through Pydantic validation before entering the database.

Validation ensures:

- Correct datatypes
- Required fields
- Consistent schemas
- Reliable downstream analytics

## Load

Validated records are stored using SQLAlchemy ORM and persisted in SQLite.

---

# Database Design

## Cities

Stores metadata about every city processed by the system.

| Field | Description |
|---------|---------|
| id | Primary Key |
| city_name | City Name |
| country | Country Code |
| latitude | Latitude |
| longitude | Longitude |
| population | Population |
| timezone | Timezone |

## Weather

Stores weather observations.

| Field | Description |
|---------|---------|
| city_id | City Reference |
| date | Observation Date |
| temperature | Temperature |
| humidity | Humidity |
| wind_speed | Wind Speed |
| precipitation | Rainfall |
| condition | Weather Condition |

## Air Quality

Stores environmental pollution measurements.

| Field | Description |
|---------|---------|
| city_id | City Reference |
| date | Observation Date |
| aqi | Air Quality Index |
| pm25 | PM2.5 |
| pm10 | PM10 |
| o3 | Ozone |
| no2 | Nitrogen Dioxide |

## Daily Metrics

Stores generated analytics.

| Field | Description |
|---------|---------|
| weather_score | Weather Quality Score |
| aqi_score | Air Quality Score |
| readiness_score | Final Composite Score |
| risk_level | Risk Classification |

## Pipeline Runs

Stores monitoring information.

| Field | Description |
|---------|---------|
| city_name | Processed City |
| start_time | Pipeline Start |
| end_time | Pipeline End |
| duration_seconds | Runtime |
| status | Success/Failure |
| records_processed | Processed Records |
| error_message | Failure Reason |

---

# Analytics Engine

Atmos generates several derived metrics.

## Weather Score

Measures environmental favorability using weather conditions.

## AQI Score

Evaluates pollution conditions using AQI and pollutant measurements.

## Readiness Score

Combines environmental indicators into a single city readiness metric.

## Risk Classification

Cities are categorized into:

- LOW
- MODERATE
- HIGH

based on their environmental conditions.

---

# Monitoring System

Every pipeline execution is tracked.

Recorded information includes:

- City processed
- Start time
- End time
- Runtime
- Success status
- Failure status
- Records processed
- Error messages

This monitoring data powers the Pipeline Monitoring dashboard page.

---

# Dashboard

## Overview

Displays:

- Active cities
- Weather records
- AQI records
- Analytics records
- Readiness rankings
- Risk distribution
- Weather comparisons
- AQI comparisons

## City Explorer

Provides city-specific analytics including:

- Readiness score
- Weather score
- AQI score
- Risk classification
- Historical metrics
- Environmental measurements

## Pipeline Monitoring

Displays:

- Total runs
- Success rate
- Average runtime
- Historical executions

## Data Explorer

Provides direct access to exported datasets.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/AA-KH/Atmos
cd Atmos
```

## Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Create all database tables:

```bash
python -m src.create_database
```

---

# Running The Pipeline

Populate the system with the default city set:

```bash
python main.py run-all
```

Export datasets:

```bash
python main.py export
```

View generated metrics:

```bash
python main.py metrics
```

View pipeline statistics:

```bash
python main.py stats
```

View pipeline history:

```bash
python main.py history
```

---

# Launching The Dashboard

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# Dynamic City Search

Atmos allows users to search and ingest cities directly from the dashboard.

Workflow:

1. Enter city name
2. Fetch coordinates
3. Retrieve weather data
4. Retrieve air-quality data
5. Validate records
6. Store data
7. Generate analytics
8. Export datasets
9. Refresh dashboard

---

# Docker Deployment

## Build Image

```bash
docker build -t atmos .
```

## Run Container

```bash
docker run -p 8501:8501 atmos
```

## Docker Compose

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

---

# CLI Commands

Run default pipeline:

```bash
python main.py run-all
```

Run single city:

```bash
python main.py run-city Delhi
```

Export datasets:

```bash
python main.py export
```

View metrics:

```bash
python main.py metrics
```

View pipeline statistics:

```bash
python main.py stats
```

View pipeline history:

```bash
python main.py history
```

---

# Data Sources

Atmos uses Open-Meteo APIs.

- Geocoding API
- Weather Forecast API
- Air Quality API

---

# Data Engineering Concepts Demonstrated

- ETL Pipelines
- Data Validation
- Data Quality Enforcement
- API Integration
- Data Modeling
- SQLAlchemy ORM
- Relational Databases
- Monitoring Systems
- Analytics Generation
- Dashboard Development
- Docker Deployment
- Production-Oriented Architecture

---

# End-To-End Workflow

```text
User Searches City
        │
        ▼
Geocoding API
        │
        ▼
Weather API + AQI API
        │
        ▼
Transformation Layer
        │
        ▼
Validation Layer
        │
        ▼
SQLite Database
        │
        ▼
Analytics Generation
        │
        ▼
CSV Export Layer
        │
        ▼
Streamlit Dashboard
```

---

# Atmos

A complete Data Engineering platform demonstrating practical ETL pipelines, data validation, monitoring, analytics, dashboarding, and Dockerized deployment using real-world environmental intelligence data.

# Stock Pipeline

## Overview

This project implements a data pipeline to fetch stock market data, process it, and store it in a PostgreSQL database. The pipeline is orchestrated using Dagster and is containerized using Docker Compose for easy deployment and scalability.

## Deliverables

* **docker-compose.yml**: Defines the services for PostgreSQL, Dagster, and any other dependencies.
* **Orchestrator Logic**: A Dagster job that orchestrates the data fetching and processing tasks.
* **Data Fetching Script**: A Python script that fetches stock market data and updates the PostgreSQL database.
* **README.md**: Provides instructions on how to build and run the pipeline.

## Project Structure

```
stock_pipeline/
│
├── .env                  # Environment variables for configuration
├── .gitignore            # Git ignore file
├── docker-compose.yml    # Docker Compose configuration
├── stock_pipeline/jobs.py           # Dagster orchestrator logic, Script to fetch and store stock data
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Prerequisites

* Docker & Docker Compose installed
* Python 3.10+
* Alpha Vantage API key

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/jdesai05/stock_pipeline.git
cd stock_pipeline
```

2. **Create a `.env` file**

In the root directory, create a `.env` file with the following content:

```
ALPHA_VANTAGE_KEY=your_alpha_vantage_api_key
POSTGRES_USER=dagster
POSTGRES_PASSWORD=dagster
POSTGRES_DB=market_data
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

3. **Build and start the services**

```bash
docker-compose up --build
```

This command will build the Docker images and start the containers as defined in `docker-compose.yml`.

## Usage

* **Dagster UI**: Once the services are up, you can access the Dagster UI at `http://localhost:3000` to monitor and manage the pipeline.

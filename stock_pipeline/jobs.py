import os
import requests
import psycopg2
from datetime import datetime
from dagster import job, op, schedule

@op
def fetch_stock_data():
    api_key = os.getenv("ALPHA_VANTAGE_KEY")
    symbol = "NVDA"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

    req = requests.get(url, timeout=10)
    data = req.json().get("Global Quote", {})
    price = data.get("05. price")
    return {"symbol": symbol, "price": price, "timestamp": datetime.now()}

@op
def store_in_postgres(stock_data):
    if not stock_data["price"]:
        raise ValueError("No price data available to store.")
    
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST","localhost"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT",5432),
    )

    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS stock_prices ( id SERIAL PRIMARY KEY, symbol VARCHAR(10), price NUMEriC, timestamp TIMESTAMP)"
    )
    cur.execute(
        "INSERT INTO stock_prices (symbol, price, timestamp) VALUES (%s, %s, %s)",
        (stock_data["symbol"], stock_data["price"], stock_data["timestamp"]),
    )

    conn.commit()
    cur.close()
    conn.close()


@job
def stock_pipeline():
    data = fetch_stock_data()
    store_in_postgres(data)


@schedule(
        cron_schedule="35 9 * * *",
        job=stock_pipeline,
        execution_timezone="Asia/Kolkata",
)
def daily_stock_schedule(_context):
    return {}


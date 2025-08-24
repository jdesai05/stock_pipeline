import psycopg2
import os

# load environment variables (if you’re using .env)
from dotenv import load_dotenv
load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        dbname=os.getenv("POSTGRES_DB", "market_data"),
        user=os.getenv("POSTGRES_USER", "dagster"),
        password=os.getenv("POSTGRES_PASSWORD", "dagster"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )
    print("✅ Connected to Postgres successfully!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

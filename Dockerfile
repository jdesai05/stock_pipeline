# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Install system packages required for psycopg2 (Postgres driver)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first (for caching layers)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose Dagster webserver port
EXPOSE 3000

# Set PYTHONPATH so Python can find your stock_pipeline package
ENV PYTHONPATH=/app

# Start Dagster dev server
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000"]




from dagster import Definitions
from .jobs import stock_pipeline, daily_stock_schedule

defs = Definitions(
    jobs=[stock_pipeline],
    schedules=[daily_stock_schedule]
)

from src.pipeline.load_city_data import run_pipeline
from src.analytics.export_manager import export_all
from src.analytics.report_generator import generate_daily_report
from src.logging_config import logger
from src.config import DEFAULT_CITIES

def run_all_cities(cities):
    logger.info("Starting batch pipeline")
    for city in cities:
        try:
            run_pipeline(city)

        except Exception as e:
            logger.exception(f"Failed city: {city} | {e}")

    export_all()
    generate_daily_report()
    logger.info("Batch pipeline completed")

def run_default_pipeline():
    run_all_cities(DEFAULT_CITIES)
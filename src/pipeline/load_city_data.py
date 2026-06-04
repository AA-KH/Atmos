from src.clients.geocoding_client import GeocodingClient
from src.clients.weather_client import WeatherClient
from src.clients.air_quality_client import AirQualityClient
from src.transforms.city_transform import transform_city
from src.transforms.weather_transform import transform_weather
from src.transforms.aqi_transform import transform_aqi
from src.storage.db_store import insert_city, insert_weather, insert_aqi
from src.logging_config import logger
from src.analytics.metric_generator import generate_metrics
from src.monitoring.run_tracker import start_run, finish_run
from src.monitoring.quality_checks import validate_weather_quality, validate_aqi_quality

def run_pipeline(city_name):

    run_id = start_run(city_name)
    records_processed = 0

    try:
        geo = GeocodingClient()
        weather_client = WeatherClient()
        aqi_client = AirQualityClient()

        city_info = geo.get_city_info(city_name)
        if not city_info:
            logger.error(f"Could not fetch city information for {city_name}")
            finish_run(run_id, "FAILED", records_processed, "Could not fetch city information")
            return

        city_record = transform_city(city_info)
        if not city_record:
            logger.error("City validation failed")
            finish_run(run_id, "FAILED", records_processed, "City validation failed")
            return

        city_id = insert_city(city_record)

        weather_data = weather_client.get_weather(
            city_info["latitude"],
            city_info["longitude"]
        )
        if not weather_data:
            logger.error("Weather API request failed")
            finish_run(run_id, "FAILED", records_processed, "Weather API request failed")
            return

        if not validate_weather_quality(weather_data):
            logger.error("Weather quality check failed")
            finish_run(run_id, "FAILED", records_processed, "Weather quality check failed")
            return

        weather_record = transform_weather(weather_data, city_id)
        if not weather_record:
            logger.error("Weather transformation failed")
            finish_run(run_id, "FAILED", records_processed, "Weather transformation failed")
            return

        insert_weather(weather_record.model_dump())
        records_processed += 1

        aqi_data = aqi_client.get_air_quality(
            city_info["latitude"],
            city_info["longitude"]
        )
        if not aqi_data:
            logger.error("AQI API request failed")
            finish_run(run_id, "FAILED", records_processed, "AQI API request failed")
            return

        if not validate_aqi_quality(aqi_data):
            logger.error("AQI quality check failed")
            finish_run(run_id, "FAILED", records_processed, "AQI quality check failed")
            return

        aqi_record = transform_aqi(aqi_data, city_id)
        if not aqi_record:
            logger.error("AQI transformation failed")
            finish_run(run_id, "FAILED", records_processed, "AQI transformation failed")
            return

        insert_aqi(aqi_record.model_dump())
        records_processed += 1
        generate_metrics(city_id)
        records_processed += 1

        logger.info(f"Pipeline completed successfully for {city_name}")
        finish_run(
            run_id,
            "SUCCESS",
            records_processed
        )

    except Exception as e:

        logger.exception(f"Unexpected pipeline failure: {e}")
        finish_run(
            run_id,
            "FAILED",
            records_processed,
            str(e)
        )
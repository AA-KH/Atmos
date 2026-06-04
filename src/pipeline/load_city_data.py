from src.clients.geocoding_client import GeocodingClient
from src.clients.weather_client import WeatherClient
from src.clients.air_quality_client import AirQualityClient
from src.transforms.city_transform import transform_city
from src.transforms.weather_transform import transform_weather
from src.transforms.aqi_transform import transform_aqi
from src.storage.db_store import insert_city, insert_weather, insert_aqi
from src.logging_config import logger
from src.analytics.metric_generator import generate_metrics

def run_pipeline(city_name):

    try:

        geo = GeocodingClient()
        weather_client = WeatherClient()
        aqi_client = AirQualityClient()
        city_info = geo.get_city_info(city_name)
        if not city_info:
            logger.error(f"Could not fetch city information for {city_name}")
            return

        city_record = transform_city(city_info)
        if not city_record:
            logger.error("City validation failed")
            return

        city_id = insert_city(city_record)
        weather_data = weather_client.get_weather(city_info["latitude"], city_info["longitude"])
        if not weather_data:
            logger.error("Weather API request failed")
            return

        weather_record = transform_weather(weather_data, city_id)
        if not weather_record:
            logger.error("Weather transformation failed")
            return

        insert_weather(weather_record.model_dump())
        aqi_data = aqi_client.get_air_quality(city_info["latitude"], city_info["longitude"])
        if not aqi_data:
            logger.error("AQI API request failed")
            return

        aqi_record = transform_aqi(aqi_data, city_id)
        if not aqi_record:
            logger.error("AQI transformation failed")
            return

        insert_aqi(aqi_record.model_dump())
        generate_metrics(city_id)
        logger.info(f"Pipeline completed successfully for {city_name}")

    except Exception as e:
        logger.exception(f"Unexpected pipeline failure: {e}")
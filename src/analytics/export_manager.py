import pandas as pd
from src.database import SessionLocal
from src.models import City, Weather, AirQuality, DailyMetric
from src.logging_config import logger

def export_cities():
    session = SessionLocal()

    try:
        cities = session.query(City).all()
        data = []
        for city in cities:
            data.append({
                "id": city.id,
                "city_name": city.city_name,
                "country": city.country,
                "latitude": city.latitude,
                "longitude": city.longitude,
                "population": city.population,
                "timezone": city.timezone
            })

        df = pd.DataFrame(data)
        df.to_csv("data/exports/cities.csv", index=False)
        logger.info("cities.csv exported")

    finally:
        session.close()

def export_weather():
    session = SessionLocal()

    try:
        weather_records = session.query(Weather).all()
        data = []

        for weather in weather_records:
            city = session.query(City).filter_by(id=weather.city_id).first()
            data.append({
                "city_name": city.city_name if city else "Unknown",
                "date": weather.date,
                "temperature": weather.temperature,
                "humidity": weather.humidity,
                "wind_speed": weather.wind_speed,
                "precipitation": weather.precipitation,
                "condition": weather.condition
            })

        df = pd.DataFrame(data)
        df.to_csv("data/exports/weather.csv", index=False)
        logger.info("weather.csv exported")

    finally:
        session.close()

def export_aqi():
    session = SessionLocal()

    try:
        records = session.query(AirQuality).all()
        data = []
        for record in records:
            city = session.query(City).filter_by(id=record.city_id).first()
            data.append({
                "city_name": city.city_name if city else "Unknown",
                "date": record.date,
                "aqi": record.aqi,
                "pm25": record.pm25,
                "pm10": record.pm10,
                "o3": record.o3,
                "no2": record.no2
            })

        df = pd.DataFrame(data)
        df.to_csv("data/exports/aqi.csv", index=False)
        logger.info("aqi.csv exported")

    finally:
        session.close()

def export_metrics():
    session = SessionLocal()

    try:
        metrics = session.query(DailyMetric).all()
        data = []
        for metric in metrics:
            city = session.query(City).filter_by(id=metric.city_id).first()
            data.append({
                "city_name": city.city_name if city else "Unknown",
                "date": metric.date,
                "weather_score": metric.weather_score,
                "aqi_score": metric.aqi_score,
                "readiness_score": metric.readiness_score,
                "risk_level": metric.risk_level
            })

        df = pd.DataFrame(data)
        df.to_csv("data/exports/metrics.csv", index=False)
        logger.info("metrics.csv exported")

    finally:
        session.close()

def export_all():

    export_cities()
    export_weather()
    export_aqi()
    export_metrics()

    logger.info("All exports completed")
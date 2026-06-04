from src.database import SessionLocal
from src.models import Weather, AirQuality, DailyMetric
from src.analytics.metrics import calculate_weather_score, calculate_aqi_score, calculate_readiness_score, determine_risk_level
from src.logging_config import logger

def generate_metrics(city_id):
    session = SessionLocal()

    try:
        weather = session.query(Weather).filter_by(city_id=city_id).order_by(Weather.date.desc()).first()
        aqi = session.query(AirQuality).filter_by(city_id=city_id).order_by(AirQuality.date.desc()).first()

        if not weather or not aqi:
            logger.error("Missing weather or AQI data")
            return

        weather_score = calculate_weather_score(weather)
        aqi_score = calculate_aqi_score(aqi)
        readiness_score = calculate_readiness_score(weather_score,aqi_score)
        risk_level = determine_risk_level(readiness_score)

        existing = session.query(DailyMetric).filter_by(city_id=city_id,date=weather.date).first()

        if existing:
            logger.info("Metrics already exist")
            return

        metric = DailyMetric(
            city_id=city_id,
            date=weather.date,
            weather_score=weather_score,
            aqi_score=aqi_score,
            readiness_score=readiness_score,
            risk_level=risk_level
        )

        session.add(metric)
        session.commit()

        logger.info(f"Metrics generated for city_id={city_id}")

    except Exception as e:
        session.rollback()
        logger.exception(f"Metric generation failed: {e}")

    finally:
        session.close()
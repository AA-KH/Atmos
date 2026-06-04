from src.database import SessionLocal
from src.models import City,Weather, AirQuality
from src.logging_config import logger

def insert_city(city_data):
    session = SessionLocal()

    try:
        existing = session.query(City).filter_by(city_name= city_data["city_name"]).first()
        if existing:
            logger.info(f"City exists: {existing.city_name}")
            return existing.id

        city = City(**city_data)
        session.add(city)
        session.commit()
        session.refresh(city)
        return city.id
    
    except Exception as e:
        session.rollback()
        logger.error(f"City insert failed: {e}")

    finally:
        session.close()

def insert_weather(weather_data):
    session = SessionLocal()

    try:
        existing = session.query(Weather).filter_by(city_id=weather_data["city_id"],date=weather_data["date"]).first()
        if existing:
            logger.info("Weather already exists")
            return

        weather = Weather(**weather_data)
        session.add(weather)
        session.commit()
    
    except  Exception as e:
        session.rollback()
        logger.error(f"Weather insert failed: {e}")

    finally:
        session.close()

def insert_aqi(aqi_data):
    session = SessionLocal()

    try:
        existing = session.query(AirQuality).filter_by(city_id=aqi_data["city_id"],date=aqi_data["date"]).first()
        if existing:
            return
        aqi = AirQuality(**aqi_data)
        session.add(aqi)
        session.commit()

    except Exception as e:
        session.rollback()
        logger.error(f"AQI insert failed: {e}")

    finally:
        session.close()
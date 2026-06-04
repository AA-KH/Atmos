from src.schemas import CitySchema, WeatherSchema, AQISchema, HolidaySchema, DailyMetricSchema
from pydantic import ValidationError
from src.logging_config import logger

def validate_city(data):
    try:
        return CitySchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None

def validate_weather(data):
    try:
        return WeatherSchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None

def validate_aqi(data):
    try:
        return AQISchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None

def validate_holiday(data):
    try:
        return HolidaySchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None
    
def validate_metric(data):
    try:
        return DailyMetricSchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None
from src.schemas import CitySchema, RawWeatherSchema, RawAQISchema, HolidaySchema, WeatherSchema, AQISchema, DailyMetricSchema
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
        return RawWeatherSchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None

def validate_aqi(data):
    try:
        return RawAQISchema(**data)
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
    
def validate_weather_record(data):
    try:
        return WeatherSchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None

def validate_aqi_record(data):
    try:
        return AQISchema(**data)
    except ValidationError as e:
        logger.error(e)
        return None
from src.logging_config import logger

def validate_weather_quality(weather_data):

    if weather_data["temperature"] < -100:
        return False

    if weather_data["temperature"] > 70:
        return False

    if weather_data["humidity"] < 0:
        return False

    if weather_data["humidity"] > 100:
        return False

    return True

def validate_aqi_quality(aqi_data):

    if aqi_data["pm25"] < 0:
        return False

    if aqi_data["pm10"] < 0:
        return False

    return True
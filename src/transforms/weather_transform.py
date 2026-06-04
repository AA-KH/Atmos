from datetime import datetime
from src.validators.data_validator import validate_weather_record

def transform_weather(weather_data,city_id):

    transformed = {
        "city_id": city_id,
        "date": datetime.fromisoformat(weather_data["observation_time"]).date(),
        "temperature": weather_data["temperature"],
        "humidity": weather_data["humidity"],
        "wind_speed": weather_data["wind_speed"],
        "precipitation": weather_data["precipitation"],
        "condition": "UNKNOWN"
    }

    return validate_weather_record(transformed)
from datetime import datetime
from src.validators.data_validator import validate_aqi_record

def transform_aqi(aqi_data, city_id):

    transformed = {
        "city_id": city_id,
        "date": datetime.fromisoformat(aqi_data["observation_time"]).date(),
        "aqi": aqi_data["aqi"],
        "pm25": aqi_data["pm25"],
        "pm10": aqi_data["pm10"],
        "o3": aqi_data["o3"],
        "no2": aqi_data["no2"]
    }

    return validate_aqi_record(transformed)
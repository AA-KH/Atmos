from pydantic import BaseModel
from pydantic import field_validator
from datetime import date

class CitySchema(BaseModel):
    city_name: str
    country: str
    latitude: float
    longitude: float
    population: int | None = None
    timezone: str | None = None

class RawWeatherSchema(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    precipitation: float

    @field_validator("humidity")
    def validate_humidity(cls, value):
        if value < 0 or value > 100:
            raise ValueError("Humidity must be between 0 and 100")
        return value
    
    @field_validator("temperature")
    def validate_temperature(cls, value):
        if value < -100 or value > 70:
            raise ValueError("Unrealistic temperature")
        return value

class RawAQISchema(BaseModel):
    pm25: float
    pm10: float
    o3: float
    no2: float

    @field_validator(
        "pm25",
        "pm10",
        "o3",
        "no2"
    )
    def validate_pollution(cls, value):
        if value < 0:
            raise ValueError("Pollution values cannot be negative")
        return value
    
class HolidaySchema(BaseModel):
    date: date
    country: str
    holiday_name: str
    is_national: bool

class WeatherSchema(BaseModel):
    city_id: int
    date: date
    temperature: float
    humidity: float
    wind_speed: float
    precipitation: float
    condition: str | None = None

class AQISchema(BaseModel):
    city_id: int
    date: date
    aqi: int | None = None
    pm25: float
    pm10: float
    o3: float
    no2: float

class DailyMetricSchema(BaseModel):
    city_id: int
    date: date
    weather_score: float
    aqi_score: float
    readiness_score: float
    risk_level: str

    @field_validator("readiness_score")
    def validate_score(cls, value):
        if value < 0 or value > 100:
            raise ValueError("Score must be between 0 and 100")
        return value
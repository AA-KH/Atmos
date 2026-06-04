from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
from sqlalchemy import DateTime
from datetime import datetime

class City(Base):
    __tablename__ = "cities"

    def __repr__(self):
        return (
            f"City("
            f"id={self.id}, "
            f"name='{self.city_name}', "
            f"country='{self.country}'"
            f")"
        )

    id = Column(Integer, primary_key=True)
    city_name = Column(String, nullable=False)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    population = Column(Integer)
    timezone = Column(String)

    weather_records = relationship("Weather", back_populates="city")
    aqi_records = relationship("AirQuality",back_populates="city")
    metrics = relationship("DailyMetric",back_populates="city")

class Weather(Base):
    __tablename__ = "weather"

    def __repr__(self):
        return (
        f"Weather("
        f"city_id={self.city_id}, "
        f"date={self.date}, "
        f"temp={self.temperature}"
        f")"
        )

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    date = Column(Date)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    precipitation = Column(Float)
    condition = Column(String)
    city = relationship("City", back_populates="weather_records")

class AirQuality(Base):
    __tablename__ = "air_quality"

    def __repr__(self):

        return (
        f"AirQuality("
        f"city_id={self.city_id}, "
        f"date={self.date}, "
        f"aqi={self.aqi}"
        f")"
    )

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    date = Column(Date)
    aqi = Column(Integer)
    pm25 = Column(Float)
    pm10 = Column(Float)
    o3 = Column(Float)
    no2 = Column(Float)
    city = relationship("City", back_populates="aqi_records")

class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(Integer, primary_key=True)
    country = Column(String)
    date = Column(Date)
    holiday_name = Column(String)
    is_national = Column(Boolean)

class DailyMetric(Base):
    __tablename__ = "daily_metrics"

    def __repr__(self):

        return (
        f"DailyMetric("
        f"city_id={self.city_id}, "
        f"score={self.readiness_score}"
        f")"
        )

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    date = Column(Date)
    weather_score = Column(Float)
    aqi_score = Column(Float)
    readiness_score = Column(Float)
    risk_level = Column(String)
    city = relationship("City", back_populates="metrics")

class PipelineRun(Base):
    __tablename__ = "pipeline_runs"
    id = Column(Integer, primary_key=True)
    city_name = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    duration_seconds = Column(Float)
    status = Column(String)
    records_processed = Column(Integer)
    error_message = Column(String, nullable=True)
    
    def __repr__(self):
        return f"PipelineRun(city='{self.city_name}', status='{self.status}')"
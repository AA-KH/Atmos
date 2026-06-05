import pandas as pd

def load_metrics():
    return pd.read_csv("data/exports/metrics.csv")

def load_weather():
    return pd.read_csv("data/exports/weather.csv")

def load_aqi():
    return pd.read_csv("data/exports/aqi.csv")

def load_cities():
    return pd.read_csv("data/exports/cities.csv")
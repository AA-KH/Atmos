def calculate_weather_score(weather):
    score = 100

    if weather.temperature > 40:
        score -= 30
    elif weather.temperature > 35:
        score -= 15

    if weather.wind_speed > 30:
        score -= 20

    if weather.precipitation > 20:
        score -= 25

    return max(score, 0)

def calculate_aqi_score(aqi):
    score = 100

    if aqi.pm25 > 100:
        score -= 50
    elif aqi.pm25 > 50:
        score -= 30
    elif aqi.pm25 > 25:
        score -= 15

    if aqi.pm10 > 150:
        score -= 25

    return max(score, 0)

def calculate_readiness_score(weather_score, aqi_score):
    return round((weather_score * 0.6) + (aqi_score * 0.4), 2)

def determine_risk_level(score):

    if score >= 80:
        return "LOW"

    elif score >= 60:
        return "MODERATE"

    elif score >= 40:
        return "HIGH"

    return "CRITICAL"
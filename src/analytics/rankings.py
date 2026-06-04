from src.repositories.city_repository import CityRepository
from src.repositories.metric_repository import MetricRepository

def get_city_rankings():
    rankings = []
    cities = CityRepository.get_all()

    for city in cities:
        metric = MetricRepository.get_latest_by_city(city.id)
        
        if not metric:
            continue

        rankings.append({
            "city": city.city_name,
            "score": metric.readiness_score,
            "risk": metric.risk_level
        })

    rankings.sort(key=lambda x: x["score"],reverse=True)

    return rankings
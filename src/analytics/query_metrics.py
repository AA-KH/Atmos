from src.database import SessionLocal
from src.models import DailyMetric, City

def get_latest_metrics():
    session = SessionLocal()

    try:
        results = []
        metrics = session.query(DailyMetric).all()
        for metric in metrics:
            city = session.query(City).filter_by(id=metric.city_id).first()
            results.append({
                "city_name": city.city_name if city else "Unknown",
                "date": metric.date,
                "readiness_score": metric.readiness_score,
                "risk_level": metric.risk_level
            })

        return results

    finally:
        session.close()
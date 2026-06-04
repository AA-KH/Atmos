from src.database import SessionLocal
from src.models import DailyMetric, City

def generate_daily_report():
    session = SessionLocal()

    try:
        metrics = session.query(DailyMetric).all()
        with open("data/exports/daily_report.txt", "w") as report:
            report.write("=== DATAPULSE DAILY REPORT ===\n\n")

            for metric in metrics:
                city = session.query(City).filter_by(id=metric.city_id).first()
                report.write(f"City: {city.city_name}\n")
                report.write(f"Readiness Score: {metric.readiness_score}\n")
                report.write(f"Risk Level: {metric.risk_level}\n\n")

    finally:
        session.close()
from src.database import SessionLocal
from src.models import DailyMetric

def get_latest_metrics():
    session = SessionLocal()

    try:
        return session.query(DailyMetric).all()

    finally:
        session.close()
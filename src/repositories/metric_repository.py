from src.database import SessionLocal
from src.models import DailyMetric

class MetricRepository:

    @staticmethod
    def get_all():
        session = SessionLocal()

        try:
            return session.query(DailyMetric).all()

        finally:
            session.close()

    @staticmethod
    def get_latest_by_city(city_id):
        session = SessionLocal()

        try:

            return session.query(DailyMetric)\
                .filter_by(city_id=city_id)\
                .order_by(DailyMetric.date.desc())\
                .first()

        finally:
            session.close()
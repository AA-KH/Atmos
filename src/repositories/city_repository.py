from src.database import SessionLocal
from src.models import City

class CityRepository:

    @staticmethod
    def get_by_id(city_id):
        session = SessionLocal()

        try:
            return session.query(City).filter_by(id=city_id).first()

        finally:
            session.close()

    @staticmethod
    def get_by_name(city_name):
        session = SessionLocal()

        try:
            return session.query(City).filter_by(city_name=city_name).first()

        finally:
            session.close()

    @staticmethod
    def get_all():
        session = SessionLocal()

        try:
            return session.query(City).all()

        finally:
            session.close()
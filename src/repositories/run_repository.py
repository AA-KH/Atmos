from src.database import SessionLocal
from src.models import PipelineRun

class RunRepository:

    @staticmethod
    def get_all():
        session = SessionLocal()

        try:
            return session.query(PipelineRun).all()

        finally:
            session.close()

    @staticmethod
    def get_recent(limit=10):
        session = SessionLocal()

        try:

            return session.query(PipelineRun)\
                .order_by(PipelineRun.start_time.desc())\
                .limit(limit)\
                .all()

        finally:
            session.close()
from src.database import SessionLocal
from src.models import PipelineRun

def get_recent_runs(limit=10):
    session = SessionLocal()

    try:
        return session.query(PipelineRun).order_by(PipelineRun.start_time.desc()).limit(limit).all()

    finally:
        session.close()
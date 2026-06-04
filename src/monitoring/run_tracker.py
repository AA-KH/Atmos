from datetime import datetime
from src.database import SessionLocal
from src.models import PipelineRun

def start_run(city_name):
    session = SessionLocal()

    try:
        run = PipelineRun(
            city_name=city_name,
            start_time=datetime.now(),
            status="RUNNING",
            records_processed=0
        )

        session.add(run)
        session.commit()
        session.refresh(run)

        return run.id

    finally:
        session.close()

def finish_run(run_id, status, records_processed, error_message=None):
    session = SessionLocal()

    try:
        run = session.query(PipelineRun).filter_by(id=run_id).first()

        if not run:
            return

        run.end_time = datetime.now()
        run.duration_seconds = (run.end_time - run.start_time).total_seconds()
        run.status = status
        run.records_processed = records_processed
        run.error_message = error_message
        session.commit()

    finally:
        session.close()
from src.database import SessionLocal
from src.models import PipelineRun

def get_pipeline_stats():
    session = SessionLocal()

    try:
        runs = session.query(PipelineRun).all()
        total_runs = len(runs)

        successful_runs = len([
            run for run in runs
            if run.status == "SUCCESS"
        ])

        failed_runs = len([
            run for run in runs
            if run.status == "FAILED"
        ])

        return {
            "total_runs": total_runs,
            "successful_runs": successful_runs,
            "failed_runs": failed_runs
        }

    finally:
        session.close()
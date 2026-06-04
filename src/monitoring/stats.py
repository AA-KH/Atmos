from src.repositories.run_repository import RunRepository

def get_pipeline_stats():

    runs = RunRepository.get_all()
    total_runs = len(runs)
    successful_runs = len([run for run in runs if run.status == "SUCCESS"])
    failed_runs = len([run for run in runs if run.status == "FAILED"])

    success_rate = 0

    if total_runs > 0:
        success_rate = round(successful_runs / total_runs * 100,2)

    avg_duration = 0

    durations = [run.duration_seconds for run in runs if run.duration_seconds]

    if durations:
        avg_duration = round(sum(durations) / len(durations),2)

    total_records = sum(run.records_processed for run in runs)

    return {
        "total_runs": total_runs,
        "successful_runs": successful_runs,
        "failed_runs": failed_runs,
        "success_rate": success_rate,
        "avg_duration": avg_duration,
        "total_records": total_records
    }
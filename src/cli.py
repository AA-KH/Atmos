import typer
from src.pipeline.load_city_data import run_pipeline
from src.pipeline.pipeline_manager import run_default_pipeline
from src.analytics.export_manager import export_all
from src.analytics.report_generator import generate_daily_report
from src.analytics.query_metrics import get_latest_metrics
from src.monitoring.stats import get_pipeline_stats
from src.monitoring.history import get_recent_runs
from src.analytics.rankings import get_city_rankings
from src.analytics.summary import get_summary

app = typer.Typer()
@app.command()
def run_city(city: str):
    run_pipeline(city)
    print(f"Pipeline completed for {city}")

@app.command()
def run_all():
    run_default_pipeline()
    print("Default pipeline completed")

@app.command()
def export():
    export_all()
    print("Exports completed")

@app.command()
def report():
    generate_daily_report()
    print("Report generated")

@app.command()
def metrics():
    metrics_data = get_latest_metrics()
    print()
    for metric in metrics_data:
        print(
            f"{metric['city_name']} | "
            f"{metric['date']} | "
            f"Readiness: {metric['readiness_score']} | "
            f"Risk: {metric['risk_level']}"
        )
    print()

@app.command()
def health():
    print("DataPulse Operational")

@app.command()
def stats():
    stats = get_pipeline_stats()

    print(f"Total Runs: {stats['total_runs']}")
    print(f"Successful Runs: {stats['successful_runs']}")
    print(f"Failed Runs: {stats['failed_runs']}")
    print(f"Success Rate: {stats['success_rate']}%")
    print(f"Average Duration: {stats['avg_duration']}s")
    print(f"Records Processed: {stats['total_records']}")


@app.command()
def history():
    runs = get_recent_runs()

    for run in runs:
        print(
            f"{run.city_name} | "
            f"{run.status} | "
            f"{round(run.duration_seconds, 2)}s"
        )

@app.command()
def rankings():
    rankings = get_city_rankings()

    for index, city in enumerate(rankings, start=1):
        print(
            f"{index}. "
            f"{city['city']} | "
            f"Score: {city['score']} | "
            f"Risk: {city['risk']}"
        )

@app.command()
def summary():
    summary = get_summary()

    if not summary:
        print("No analytics available")
        return

    print(f"Average Readiness Score: {summary['avg_score']}")
    print(f"Low Risk Cities: {summary['low_risk']}")
    print(f"Moderate Risk Cities: {summary['moderate_risk']}")
    print(f"High Risk Cities: {summary['high_risk']}")
    print(f"Critical Risk Cities: {summary['critical_risk']}")
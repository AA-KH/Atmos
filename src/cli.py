import typer
from src.pipeline.load_city_data import run_pipeline
from src.pipeline.pipeline_manager import run_default_pipeline
from src.analytics.export_manager import export_all
from src.analytics.report_generator import generate_daily_report
from src.analytics.query_metrics import get_latest_metrics

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
from src.repositories.metric_repository import MetricRepository

def get_summary():
    metrics = MetricRepository.get_all()

    if not metrics:
        return None

    avg_score = round(sum(metric.readiness_score for metric in metrics) / len(metrics),2)
    low_risk = len([metric for metric in metrics if metric.risk_level == "LOW"])
    moderate_risk = len([metric for metric in metrics if metric.risk_level == "MODERATE"])
    high_risk = len([metric for metric in metrics if metric.risk_level == "HIGH"])
    critical_risk = len([metric for metric in metrics if metric.risk_level == "CRITICAL"])

    return {
        "avg_score": avg_score,
        "low_risk": low_risk,
        "moderate_risk": moderate_risk,
        "high_risk": high_risk,
        "critical_risk": critical_risk
    }
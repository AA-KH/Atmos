import streamlit as st
import pandas as pd
from src.dashboard.data_loader import load_metrics, load_weather, load_aqi, load_cities
from src.monitoring.stats import get_pipeline_stats
from src.monitoring.history import get_recent_runs
from src.pipeline.load_city_data import run_pipeline
from src.analytics.export_manager import export_all
from src.dashboard.data_loader import load_all_data

st.set_page_config(
    page_title="DataPulse",
    page_icon="🌍",
    layout="wide"
)

data = load_all_data()
metrics_df = data["metrics"]
weather_df = data["weather"]
aqi_df = data["aqi"]
cities_df = data["cities"]

st.sidebar.title("🌍 DataPulse")
st.sidebar.caption("City Intelligence Platform")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Overview",
        "City Explorer",
        "Pipeline Monitoring",
        "Data Explorer"
    ]
)

st.sidebar.divider()
st.sidebar.subheader("🔍 Search City")

city_search = st.sidebar.text_input("City Name", placeholder="Berlin")

if st.sidebar.button("Fetch City Data"):

    city_search = city_search.strip()

    if city_search:

        with st.spinner(f"Fetching data for {city_search}..."):

            try:
                run_pipeline(city_search)
                export_all()
                st.success(f"{city_search} updated successfully")
                st.rerun()

            except Exception as e:

                st.error(f"Failed to fetch city: {e}")

if page == "Overview":

    st.title("🌍 DataPulse")
    st.subheader("Global City Intelligence Dashboard")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Cities", len(cities_df))
    with col2:
        st.metric("Weather Records", len(weather_df))
    with col3:
        st.metric("AQI Records", len(aqi_df))
    with col4:
        st.metric("Metrics", len(metrics_df))

    st.divider()
    left, right = st.columns([2, 1])

    with left:

        st.subheader("🏆 City Readiness Rankings")

        latest_metrics = (metrics_df.sort_values("date").groupby("city_name").tail(1))

        rankings = latest_metrics.sort_values(by="readiness_score",ascending=False).reset_index(drop=True)
        rankings.index = rankings.index + 1

        st.dataframe(
            rankings[
                [
                    "city_name",
                    "readiness_score",
                    "weather_score",
                    "aqi_score",
                    "risk_level"
                ]
            ],
            use_container_width=True
        )

    with right:

        st.subheader("⚠ Risk Distribution")
        risk_counts = metrics_df["risk_level"].value_counts()
        st.bar_chart(risk_counts)

    st.divider()
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🌤 Weather Score Comparison")
        weather_chart = latest_metrics.set_index("city_name")["weather_score"]
        st.bar_chart(weather_chart)

    with col2:

        st.subheader("🌫 AQI Score Comparison")
        aqi_chart = latest_metrics.set_index("city_name")["aqi_score"]
        st.bar_chart(aqi_chart)

elif page == "City Explorer":

    st.title("🏙 City Explorer")
    cities = sorted(cities_df["city_name"].unique())
    selected_city = st.selectbox("Select City", cities)

    city_metric = metrics_df[metrics_df["city_name"] == selected_city]
    city_weather = weather_df[weather_df["city_name"] == selected_city]
    city_aqi = aqi_df[aqi_df["city_name"] == selected_city]
    latest = city_metric.iloc[-1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Readiness Score", latest["readiness_score"])

    with col2:
        st.metric("Weather Score",latest["weather_score"])

    with col3:
        st.metric("AQI Score",latest["aqi_score"])

    st.divider()
    risk = latest["risk_level"]

    if risk == "LOW":
        st.success(f"Risk Level: {risk}")

    elif risk == "MODERATE":
        st.warning(f"Risk Level: {risk}")

    else:
        st.error(f"Risk Level: {risk}")


    st.subheader("City Metrics")
    st.dataframe(city_metric,use_container_width=True)

elif page == "Pipeline Monitoring":

    st.title("⚙ Pipeline Monitoring")
    stats = get_pipeline_stats()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Runs", stats["total_runs"])

    with col2:
        st.metric("Success Rate",f"{stats['success_rate']}%")

    with col3:
        st.metric("Average Runtime",f"{stats['avg_duration']}s")

    st.divider()
    st.subheader("Pipeline Statistics")

    stats_df = pd.DataFrame(
        {
            "Metric": [
                "Successful Runs",
                "Failed Runs",
                "Records Processed"
            ],
            "Value": [
                stats["successful_runs"],
                stats["failed_runs"],
                stats["total_records"]
            ]
        }
    )

    st.dataframe(stats_df,use_container_width=True)
    st.subheader("Recent Pipeline Runs")
    runs = get_recent_runs()

    run_data = []

    for run in runs:
        run_data.append(
            {
                "City": run.city_name,
                "Status": run.status,
                "Duration (s)": round(run.duration_seconds or 0,2),
                "Records": run.records_processed
            }
        )

    st.dataframe(run_data, use_container_width=True)

elif page == "Data Explorer":

    st.title("📊 Data Explorer")
    dataset = st.selectbox(
        "Select Dataset",
        [
            "Cities",
            "Weather",
            "AQI",
            "Metrics"
        ]
    )

    if dataset == "Cities":
        st.dataframe(cities_df,use_container_width=True)

    elif dataset == "Weather":
        st.dataframe(weather_df,use_container_width=True)

    elif dataset == "AQI":
        st.dataframe(aqi_df,use_container_width=True)

    else:
        st.dataframe(metrics_df,use_container_width=True)
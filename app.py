import streamlit as st

from src.dashboard.data_loader import load_metrics, load_weather, load_aqi, load_cities
from src.dashboard.components import render_header, render_metric_card

st.set_page_config(
    page_title="DataPulse",
    page_icon="🌍",
    layout="wide"
)

render_header()

metrics_df = load_metrics()
weather_df = load_weather()
aqi_df = load_aqi()
cities_df = load_cities()

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric_card("Cities", len(cities_df))

with col2:
    render_metric_card("Weather Records", len(weather_df))

with col3:
    render_metric_card("AQI Records", len(aqi_df))

with col4:
    render_metric_card("Metrics", len(metrics_df))

st.markdown("---")
st.subheader("City Readiness Rankings")

rankings = metrics_df.sort_values(by="readiness_score", ascending=False)
st.dataframe(rankings, use_container_width=True)

st.markdown("---")
st.subheader("Risk Distribution")

risk_counts = (metrics_df["risk_level"].value_counts())
st.bar_chart(risk_counts)

st.markdown("---")
st.subheader("Weather Data")

st.dataframe(weather_df, use_container_width=True)

st.markdown("---")
st.subheader("Air Quality Data")

st.dataframe(aqi_df,use_container_width=True) 

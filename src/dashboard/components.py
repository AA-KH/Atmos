import streamlit as st

def render_header():
    st.title("🌍 DataPulse")
    st.subheader("City Intelligence Dashboard")

def render_metric_card(label, value):
    st.metric(label=label, value=value)
import streamlit as st
import heatmap
import trendanalysis
import trend_30days

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Main Dashboard", "Predictive Analysis", "30-Day Trend Analysis"])

# Main Dashboard Section
if section == "Main Dashboard":
    st.title("Enhanced Patient Data Dashboard")
    st.subheader("Heatmap Correlation")
    heatmap.show_heatmap()

# Predictive Analysis Section
elif section == "Predictive Analysis":
    st.title("Predictive Analysis: Health Improvement")
    trendanalysis.predictive_analysis()

# 30-Day Trend Analysis Section
elif section == "30-Day Trend Analysis":
    st.title("30-Day Trend Analysis")
    trend_30days.show_30day_trend()

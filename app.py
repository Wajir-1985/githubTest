import streamlit as st
import heatmap
import trendanalysis
import trend_30days
import glob
import os
from time_series_analysis import time_series_analysis  # Assuming the function is defined or imported

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Main Dashboard", "Heatmap Correlation", "Predictive Analysis", "30-Day Trend Analysis", "Time Series Analysis"])

# Main Dashboard Section
if section == "Main Dashboard":
    st.title("Welcome to the Patient Data Analysis Dashboard")
    st.markdown("""
    This dashboard provides various tools for analyzing patient data, including:
    - **Heatmap Correlation**: Visualize the correlation between different health metrics.
    - **Predictive Analysis**: Predict outcomes based on patient data.
    - **30-Day Trend Analysis**: View trends in health metrics over a 30-day period for individual patients.
    - **Time Series Analysis**: Analyze and forecast trends in patient health data over time.
    
    Use the navigation menu on the left to access different sections.
    """)

# Heatmap Correlation Section
elif section == "Heatmap Correlation":
    st.title("Heatmap Correlation")
    st.subheader("Visualize the Correlation between Health Metrics")
    heatmap.show_heatmap()

# Predictive Analysis Section
elif section == "Predictive Analysis":
    st.title("Predictive Analysis: Health Improvement")
    trendanalysis.predictive_analysis()

# 30-Day Trend Analysis Section
elif section == "30-Day Trend Analysis":
    st.title("30-Day Trend Analysis")
    trend_30days.show_30day_trend()

# Time Series Analysis Section
elif section == "Time Series Analysis":
    st.title("Time Series Analysis")

    # Allow the user to select a patient file
    patient_data_dir = 'Patient-Data'
    patient_files = glob.glob(os.path.join(patient_data_dir, '*_data_with_date.xlsx'))
    
    if not patient_files:
        st.error("No patient data files found.")
    else:
        patient_file = st.selectbox("Select a patient file:", patient_files)
        if patient_file:
            time_series_analysis(patient_file)

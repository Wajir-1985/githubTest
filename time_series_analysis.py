import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import streamlit as st

def time_series_analysis(file_path):
    # Load the data
    df = pd.read_excel(file_path, parse_dates=['Date'])
    
    # Ensure the data is sorted by date
    df = df.sort_values(by='Date')
    
    # Choose a metric to analyze (e.g., 'Systolic_pressure')
    metric = 'Systolic_pressure'
    
    # Check if the metric exists in the data
    if metric not in df.columns:
        st.error(f"The column '{metric}' is not found in the data.")
        return
    
    # Set the date as the index
    df.set_index('Date', inplace=True)
    
    # Plot the time series data
    plt.figure(figsize=(10, 5))
    plt.plot(df[metric], marker='o', linestyle='-')
    plt.title(f'Time Series for {metric}')
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.grid(True)
    st.pyplot(plt)
    
    # Train an ARIMA model
    model = ARIMA(df[metric], order=(5, 1, 0))  # (p,d,q) order - can be tuned
    model_fit = model.fit()
    
    # Forecast for the next 7 days
    forecast = model_fit.forecast(steps=7)
    
    # Plot the forecast
    plt.figure(figsize=(10, 5))
    plt.plot(df[metric], label='Observed', marker='o')
    plt.plot(forecast, label='Forecast', marker='o', linestyle='--')
    plt.title(f'ARIMA Forecast for {metric}')
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    st.subheader("Forecasted Values")
    st.write(forecast)

# Example usage: time_series_analysis('Patient-Data/P001_data_with_date.xlsx')

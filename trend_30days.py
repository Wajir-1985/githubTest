import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

def show_30day_trend():
    # Define the directory containing the patient files
    patient_data_dir = 'Patient-Data'
    
    # Get all patient data files in the specified directory
    patient_files = glob.glob(os.path.join(patient_data_dir, '*_data_with_date.xlsx'))
    
    if not patient_files:
        st.error("No patient data files found.")
        return
    
    # Dropdown to select a patient
    patient_file = st.selectbox("Select a patient file:", patient_files)
    
    if not patient_file:
        return
    
    # Load the selected patient data
    df = pd.read_excel(patient_file)
    
    # Debugging: Print out the column names
    st.write("Columns in the data:", df.columns.tolist())
    
    if 'Date' not in df.columns:
        st.error("The 'Date' column is missing from the data.")
        return
    
    # Extracting Patient ID from the filename for the title
    patient_id = os.path.basename(patient_file).split('_')[0]
    st.title(f"30-Day Trend Analysis for Patient {patient_id}")
    
    # Columns to analyze
    metrics = ['Systolic_pressure', 'Diastolic_pressure', 'Pulse_pressure', 'SpO2', 
               'Estimated_DO2', 'Estimated_VO2']
    
    for metric in metrics:
        if metric not in df.columns:
            st.error(f"The '{metric}' column is missing from the data.")
            continue
        
        st.subheader(f"Trend Analysis for {metric}")
        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df[metric], marker='o')
        plt.xlabel('Date')
        plt.ylabel(metric)
        plt.title(f'Trend Analysis for {metric} over 30 Days')
        plt.xticks(rotation=45)
        plt.grid(True)
        st.pyplot(plt)

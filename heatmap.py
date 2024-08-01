import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def show_heatmap():
    # Load the data
    df = pd.read_excel('enhanced_patient_data.xlsx')
    
    # Define the default and optional parameters
    default_parameters = ['Systolic_pressure', 'Diastolic_pressure', 'Pulse_pressure', 'Stress_index', 'Exercise_Frequency', 'Rehab_attendance']
    all_parameters = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Ensure default parameters are in the dataset
    default_parameters = [param for param in default_parameters if param in all_parameters]
    
    # User selection with default parameters pre-selected
    selected_columns = st.multiselect(
        "Select parameters to include in the heatmap:",
        options=all_parameters,
        default=default_parameters
    )
    
    if not selected_columns:
        st.warning("Please select at least one parameter.")
        return
    
    # Filter the dataframe to include only the selected columns
    df_selected = df[selected_columns]
    
    # Calculate the correlation matrix
    correlation_matrix = df_selected.corr()

    # Plotting the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    st.pyplot(plt)

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def show_heatmap():
    # Load the data
    df = pd.read_excel('enhanced_patient_data.xlsx')
    
    # Select only numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Allow user to select which parameters to include in the heatmap
    selected_columns = st.multiselect("Select parameters to include in the heatmap:", numeric_columns, default=numeric_columns)
    
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

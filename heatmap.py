import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def show_heatmap():
    # Load the data
    try:
        df = pd.read_excel('enhanced_patient_data.xlsx')
    except FileNotFoundError:
        st.error("The data file was not found. Please check the file path.")
        return
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return

    # Select only numeric columns for correlation calculation
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        st.error("No numeric data found to compute correlation.")
        return

    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()

    # Plotting the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    st.pyplot(plt)

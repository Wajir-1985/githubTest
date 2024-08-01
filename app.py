import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_excel('enhanced_patient_data.xlsx')

# Streamlit app title
st.title("Enhanced Patient Data Dashboard")

# Display the raw data
st.subheader("Raw Patient Data")
st.write(df)

# Calculate and display the correlation matrix
st.subheader("Correlation Heatmap")

# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
st.pyplot(plt)

# Trend Analysis
st.subheader("Trend Analysis for Key Parameters")

# Select parameters for trend analysis
parameters = ['Systolic_pressure', 'Diastolic_pressure', 'Pulse_pressure', 'SpO2', 
              'Estimated_DO2', 'Estimated_VO2', 'Exercise_Frequency', 'Rehab_Attendance']

for parameter in parameters:
    st.subheader(f"Trend Analysis for {parameter}")
    plt.figure(figsize=(10, 5))
    plt.plot(df['Patient_ID'], df[parameter], marker='o')
    plt.xlabel('Patient ID')
    plt.ylabel(parameter)
    plt.title(f'Trend Analysis for {parameter}')
    plt.grid(True)
    st.pyplot(plt)

# Additional plot for Exercise Type and Rehab Type counts
st.subheader("Distribution of Exercise and Rehab Types")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.countplot(x='Exercise_Type', data=df, ax=axes[0])
axes[0].set_title('Exercise Type Distribution')
axes[0].set_xlabel('Exercise Type')
axes[0].set_ylabel('Count')

sns.countplot(x='Rehab_Type', data=df, ax=axes[1])
axes[1].set_title('Rehab Type Distribution')
axes[1].set_xlabel('Rehab Type')
axes[1].set_ylabel('Count')

st.pyplot(fig)

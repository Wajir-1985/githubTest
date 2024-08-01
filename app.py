import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('enhanced_patient_data.xlsx')

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Main Dashboard", "Predictive Analysis"])

# Main Dashboard Section
if section == "Main Dashboard":
    st.title("Enhanced Patient Data Dashboard")

    st.subheader("Raw Patient Data")
    st.write(df)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    st.pyplot(plt)

    # Trend Analysis
    st.subheader("Trend Analysis for Key Parameters")
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

    # Distribution of Exercise and Rehab Types
    st.subheader("Distribution of Exercise and Rehab Types")
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.countplot(x='Exercise_Type', data=df, ax=axes[0])
    axes[0].set_title('Exercise Type Distribution')
    sns.countplot(x='Rehab_Type', data=df, ax=axes[1])
    axes[1].set_title('Rehab Type Distribution')
    st.pyplot(fig)

# Predictive Analysis Section
if section == "Predictive Analysis":
    st.title("Predictive Analysis: Health Improvement")

    st.subheader("Data for Prediction")
    st.write(df)

    # Feature selection and target definition
    features = df[['Systolic_pressure', 'Diastolic_pressure', 'Pulse_pressure', 'SpO2', 
                  'Estimated_DO2', 'Estimated_VO2', 'Exercise_Frequency', 'Rehab_Attendance']]
    df['Improvement'] = (df['SpO2'] > 95).astype(int)  # Example criteria for improvement
    X = features
    y = df['Improvement']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Display metrics
    st.subheader("Model Performance")
    st.write(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    st.write("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred))
    st.write("Classification Report:")
    st.text(classification_report(y_test, y_pred))

import streamlit as st
import pandas as pd
import numpy as np  # Add this line if numpy is used in this file
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def show_trend_analysis():
    df = pd.read_excel('enhanced_patient_data.xlsx')
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

def predictive_analysis():
    df = pd.read_excel('enhanced_patient_data.xlsx')

    st.subheader("Data for Prediction")
    st.write(df)

    features = df[['Systolic_pressure', 'Diastolic_pressure', 'Pulse_pressure', 'SpO2', 
                  'Estimated_DO2', 'Estimated_VO2', 'Exercise_Frequency', 'Rehab_Attendance']]
    df['Improvement'] = (df['SpO2'] > 95).astype(int)  # Example criteria for improvement
    X = features
    y = df['Improvement']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    st.subheader("Model Performance")
    st.write(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    st.write("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred))
    st.write("Classification Report:")
    st.text(classification_report(y_test, y_pred))

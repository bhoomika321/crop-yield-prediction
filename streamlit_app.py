import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None

st.title("Crop Yield Analysis")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

df = load_data(uploaded_file)
if df is not None:
    st.write("### Dataset Preview")
    st.write(df.head())
    
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    
    st.write("### Summary Statistics")
    st.write(df.describe())
    
    st.write("### Data Visualization")
    st.write("#### Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
else:
    st.warning("Please upload a CSV file to proceed.")

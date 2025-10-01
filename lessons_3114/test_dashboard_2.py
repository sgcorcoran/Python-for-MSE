import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Materials Science Dashboard",
    page_icon="🔬",
    layout="wide"
)

# Title and header
st.title("🔬 Materials Science Data Dashboard")
st.header("Interactive Data Exploration")

# Load your processed data from Step 1
@st.cache_data
def load_data():
    return pd.read_csv("dashboard_data.csv")

data = load_data()

# Display basic info
st.subheader("Dataset Overview")
st.write(f"Dataset shape: {data.shape}")
st.write(f"Columns: {list(data.columns)}")

# Sidebar for controls
st.sidebar.header("Dashboard Controls")

# Main dashboard area
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Overview")
    # Display first few rows using PyArrow-safe method
    st.write("First 5 rows:")
    for i, row in data.head(5).iterrows():
        st.write(f"Row {i}: {row.to_dict()}")

with col2:
    st.subheader("Basic Statistics")
    st.write(data.describe())

# Footer
st.markdown("---")
st.markdown("Built with Streamlit for MSE 3114")
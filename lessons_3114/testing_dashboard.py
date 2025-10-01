import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="My Materials Science Dashboard",
    page_icon="🔬",
    layout="wide"
)

# Title and header
st.title("🔬 My Materials Science Dashboard")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("dashboard_data.csv")

data = load_data()

# Data overview section
st.header("📊 Data Overview")
col_info1, col_info2 = st.columns(2)
with col_info1:
    st.metric("Total Records", len(data))
with col_info2:
    st.metric("Number of Columns", len(data.columns))

# TODO: Add your data preview table here
st.subheader("📋 Data Preview")
st.write("**Your data preview table will go here**")

# TODO: Add your statistics table here
st.subheader("📈 Data Statistics")
st.write("**Your statistics table will go here**")

# Visualizations section
st.header("📊 Data Visualizations")

# Create visualization grid
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Visualization 1")
    st.write("**Your first plot will go here**")

with col2:
    st.subheader("📊 Visualization 2")
    st.write("**Your second plot will go here**")

col3, col4 = st.columns(2)

with col3:
    st.subheader("📊 Visualization 3")
    st.write("**Your third plot will go here**")

with col4:
    st.subheader("📊 Visualization 4")
    st.write("**Your fourth plot will go here**")

# Full-width visualization
st.header("📊 Advanced Visualization")
st.write("**Your full-width plot will go here**")

# Footer
st.markdown("---")
st.markdown("**Built with Streamlit for MSE 3114**")
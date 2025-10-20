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

# Data preview table
st.subheader("📋 Data Preview")

# Create data preview table
fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(data.columns),
        fill_color='lightblue',
        align='left',
        font=dict(size=12, color='black')
    ),
    cells=dict(
        values=[data[col].head(5) for col in data.columns],
        fill_color='lightgray',
        align='left',
        font=dict(size=11, color='black')
    )
)])

fig.update_layout(
    title='Data Preview (First 5 Rows)',
    height=300
)

st.plotly_chart(fig, use_container_width=True)

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
    st.subheader("📊 Composition Length Distribution")
    
    # Create histogram
    fig = px.histogram(
        data, 
        x='Composition_Length',
        nbins=20,
        title='Distribution of Composition Length',
        color_discrete_sequence=['skyblue']
    )

    # Update bar edges to black
    fig.update_traces(
        marker=dict(
            line=dict(color='black', width=1)
        )
    )

    fig.update_layout(
        xaxis_title='Composition Length',
        yaxis_title='Count',
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

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
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
    # Convert to dict and display row by row to avoid PyArrow issues
    display_data = data.head(5).to_dict('records')
    for i, row in enumerate(display_data):
        st.write(f"Row {i}: {row}")

with col2:
    st.subheader("Basic Statistics")
    # Use st.dataframe for better compatibility with PyArrow
    st.dataframe(data.describe())

# Add some visualizations
st.subheader("Data Visualizations")

# Create a histogram of composition length
fig = px.histogram(
    data, 
    x='composition_length', 
    nbins=20,
    title="Distribution: Composition String Length",
    labels={'composition_length': 'Number of Characters'}
)

# Customize colors
fig.update_traces(marker_color='skyblue', marker_line_color='black')
st.plotly_chart(fig, use_container_width=True)

# Add glass forming analysis
col3, col4 = st.columns(2)

with col3:
    # Glass forming pie chart
    glass_counts = data['Glass_Forming'].value_counts()
    fig_pie = px.pie(
        values=glass_counts.values,
        names=glass_counts.index,
        title="Glass Forming Distribution"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col4:
    # Element count distribution
    fig_elements = px.histogram(
        data,
        x='num_elements',
        nbins=15,
        title="Number of Elements Distribution"
    )
    st.plotly_chart(fig_elements, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit for MSE 3114")

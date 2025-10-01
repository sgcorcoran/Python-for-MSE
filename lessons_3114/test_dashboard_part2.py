
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

# Display first 5 rows using Plotly table
st.subheader("Data Preview")
st.write("**First 5 rows:**")

fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(data.head().columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[data.head()[col] for col in data.head().columns],
               fill_color='lavender',
               align='left'))
])
st.plotly_chart(fig_table, use_container_width=True)

# Display basic statistics using Plotly table
st.subheader("Basic Statistics")
stats = data.describe()
fig_stats = go.Figure(data=[go.Table(
    header=dict(values=['Statistic'] + list(stats.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[stats.index] + [stats[col] for col in stats.columns],
               fill_color='lavender',
               align='left'))
])
st.plotly_chart(fig_stats, use_container_width=True)

# Add some visualizations
st.subheader("Data Visualizations")

# Create a histogram of composition length
fig = px.histogram(
    data, 
    x='Composition_Length', 
    nbins=20,
    title="Distribution: Composition String Length",
    labels={'Composition_Length': 'Number of Characters'}
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

# Add correlation analysis
st.subheader("Correlation Analysis")
numeric_cols = ['Composition_Length', 'num_elements']
if len(numeric_cols) > 1:
    corr_data = data[numeric_cols].corr()
    fig_corr = px.imshow(
        corr_data,
        text_auto=True,
        aspect="auto",
        title="Correlation Matrix"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit for MSE 3114")
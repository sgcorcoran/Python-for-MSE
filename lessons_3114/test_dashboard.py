"""
Materials Science Dashboard - Student Template
=============================================

This is a template for students to build their own dashboard.
Replace the placeholder sections with your own visualizations and data displays.

Author: MSE 3114 Course
"""

# =============================================================================
# STEP 1: IMPORTS AND PAGE CONFIGURATION
# =============================================================================

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

# =============================================================================
# STEP 2: TITLE AND SIDEBAR
# =============================================================================

# Title
st.title("🔬 My Materials Science Dashboard")
st.markdown("---")

# Sidebar controls
st.sidebar.header("🎛️ Dashboard Controls")
st.sidebar.write("Add your filters and controls here")
# TODO: Add sidebar controls here
# Examples:
# - Filter by category: st.sidebar.selectbox("Category", options)
# - Range slider: st.sidebar.slider("Range", min_val, max_val)
# - Checkbox: st.sidebar.checkbox("Show only...")

# =============================================================================
# STEP 3: DATA LOADING
# =============================================================================

@st.cache_data
def load_data():
    """Load and cache the dashboard data"""
    return pd.read_csv("dashboard_data.csv")

data = load_data()

# =============================================================================
# STEP 4: DATA OVERVIEW
# =============================================================================

st.header("📊 Data Overview")

# Display basic dataset information
col_info1, col_info2 = st.columns(2)
with col_info1:
    st.metric("Total Records", len(data))
with col_info2:
    st.metric("Number of Columns", len(data.columns))

st.write(f"**Columns:** {', '.join(data.columns)}")

# =============================================================================
# STEP 5: DATA PREVIEW SECTION
# =============================================================================

st.header("📋 Data Preview")
st.write("**Your data display goes here**")

# TODO: Replace this placeholder with your data preview
# Examples:
# - Show first 5 rows: st.write(data.head())
# - Create a Plotly table: st.plotly_chart(fig_table, use_container_width=True)
# - Display specific columns: st.write(data[['Composition', 'Glass_Forming']].head())
# - Use Streamlit dataframe: st.dataframe(data.head())  # Note: requires PyArrow

st.info("💡 **Tip:** Choose how you want to display your data. Consider what information would be most useful for your audience.")

# =============================================================================
# STEP 6: STATISTICS SECTION
# =============================================================================

st.header("📈 Data Statistics")
st.write("**Your statistics display goes here**")

# TODO: Replace this placeholder with your statistics
# Examples:
# - Basic descriptive stats: st.write(data.describe())
# - Create a Plotly stats table: st.plotly_chart(fig_stats, use_container_width=True)
# - Custom statistics: st.write(data['Glass_Forming'].value_counts())
# - Summary by category: st.write(data.groupby('Glass_Forming').describe())

st.info("💡 **Tip:** Show key statistics that help users understand your data patterns.")

# =============================================================================
# STEP 7: VISUALIZATIONS
# =============================================================================

st.header("📊 Data Visualizations")

# Create first row of visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Visualization 1")
    st.write("**Your first plot goes here**")
    # TODO: Add your first visualization
    # Examples:
    # - Histogram: fig = px.histogram(data, x='Composition_Length')
    # - Pie chart: fig = px.pie(data, names='Glass_Forming')
    # - Bar chart: fig = px.bar(data, x='category', y='value')
    # st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Visualization 2")
    st.write("**Your second plot goes here**")
    # TODO: Add your second visualization
    # Examples:
    # - Scatter plot: fig = px.scatter(data, x='x_col', y='y_col')
    # - Box plot: fig = px.box(data, x='category', y='value')
    # - Violin plot: fig = px.violin(data, x='category', y='value')
    # st.plotly_chart(fig, use_container_width=True)

# Create second row of visualizations
col3, col4 = st.columns(2)

with col3:
    st.subheader("📊 Visualization 3")
    st.write("**Your third plot goes here**")
    # TODO: Add your third visualization
    # Examples:
    # - Correlation heatmap: fig = px.imshow(data.corr())
    # - Line plot: fig = px.line(data, x='x_col', y='y_col')
    # - Area plot: fig = px.area(data, x='x_col', y='y_col')
    # st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader("📊 Visualization 4")
    st.write("**Your fourth plot goes here**")
    # TODO: Add your fourth visualization
    # Examples:
    # - Sunburst: fig = px.sunburst(data, path=['level1', 'level2'])
    # - Treemap: fig = px.treemap(data, path=['category'])
    # - Scatter matrix: fig = px.scatter_matrix(data, dimensions=['col1', 'col2'])
    # st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# STEP 8: FULL-WIDTH VISUALIZATION
# =============================================================================

st.header("📊 Advanced Visualization")
st.write("**Your full-width plot goes here**")

# TODO: Add your full-width visualization
# Examples:
# - Large scatter plot: fig = px.scatter(data, x='x', y='y', size='size', color='category')
# - Complex dashboard: fig = px.density_heatmap(data, x='x', y='y', facet_col='category')
# - 3D plot: fig = px.scatter_3d(data, x='x', y='y', z='z')
# st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# STEP 9: CONCLUSIONS AND INSIGHTS
# =============================================================================

st.header("💡 Key Insights")
st.write("**Your insights and conclusions go here**")

# TODO: Add your analysis conclusions
# Examples:
# - Key findings: st.write("The data shows...")
# - Recommendations: st.write("Based on this analysis...")
# - Next steps: st.write("Future work should focus on...")

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.markdown("**Built with Streamlit for MSE 3114** | *Replace placeholders with your own analysis*")
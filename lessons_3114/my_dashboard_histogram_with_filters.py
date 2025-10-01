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

# ===== FILTERING SECTION =====
st.sidebar.header("🔍 Data Filters")

# Composition Length Filter
st.sidebar.subheader("Composition Length Range")
composition_min = int(data['Composition_Length'].min())
composition_max = int(data['Composition_Length'].max())

composition_range = st.sidebar.slider(
    "Select Composition Length Range",
    min_value=composition_min,
    max_value=composition_max,
    value=(composition_min, composition_max),
    step=1
)

# Glass Forming Filter
st.sidebar.subheader("Glass Forming")
glass_options = st.sidebar.multiselect(
    "Select Glass Forming Options",
    options=data['Glass_Forming'].unique(),
    default=data['Glass_Forming'].unique()
)

# Number of Elements Filter
st.sidebar.subheader("Number of Elements")
num_elements_min = int(data['num_elements'].min())
num_elements_max = int(data['num_elements'].max())

elements_range = st.sidebar.slider(
    "Select Number of Elements Range",
    min_value=num_elements_min,
    max_value=num_elements_max,
    value=(num_elements_min, num_elements_max),
    step=1
)

# Reset Filters Button
if st.sidebar.button("🔄 Reset All Filters"):
    st.rerun()

# Apply Filters
filtered_data = data[
    (data['Composition_Length'] >= composition_range[0]) &
    (data['Composition_Length'] <= composition_range[1]) &
    (data['Glass_Forming'].isin(glass_options)) &
    (data['num_elements'] >= elements_range[0]) &
    (data['num_elements'] <= elements_range[1])
]

# ===== MAIN DASHBOARD =====

# Data overview section
st.header("📊 Data Overview")
col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.metric("Total Records", len(data))
with col_info2:
    st.metric("Filtered Records", len(filtered_data))
with col_info3:
    st.metric("Filter Reduction", f"{len(data) - len(filtered_data)} ({((len(data) - len(filtered_data))/len(data)*100):.1f}%)")

# Data preview table
st.subheader("📋 Data Preview")
fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(filtered_data.head(10).columns),
                fill_color='lightblue',
                align='center'),
    cells=dict(values=[filtered_data.head(10)[col] for col in filtered_data.head(10).columns],
               fill_color='lightgray',
               align='center'))
])
fig_table.update_layout(title="First 10 Rows of Filtered Data")
st.plotly_chart(fig_table, use_container_width=True)

# Statistics table
st.subheader("📈 Data Statistics")
numeric_cols = filtered_data.select_dtypes(include=['int64', 'float64']).columns
if len(numeric_cols) > 0:
    stats_data = filtered_data[numeric_cols].describe()
    
    fig_stats = go.Figure(data=[go.Table(
        header=dict(values=['Statistic'] + list(stats_data.columns),
                    fill_color='lightblue',
                    align='center'),
        cells=dict(values=[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']] + 
                          [stats_data[col].round(2).tolist() for col in stats_data.columns],
                   fill_color='lightgray',
                   align='center'))
    ])
    fig_stats.update_layout(title="Statistical Summary of Filtered Data")
    st.plotly_chart(fig_stats, use_container_width=True)

# Visualizations section
st.header("📊 Data Visualizations")

# Create visualization grid
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Composition Length Distribution")
    fig = px.histogram(
        filtered_data, 
        x='Composition_Length', 
        nbins=25, 
        title='Distribution of Composition Length (Filtered)'
    )
    fig.update_traces(marker=dict(color='skyblue', line=dict(color='black', width=1)))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Number of Elements Distribution")
    fig = px.histogram(
        filtered_data,
        x='num_elements',
        nbins=10,
        title='Distribution of Number of Elements (Filtered)'
    )
    fig.update_traces(marker=dict(color='lightgreen', line=dict(color='black', width=1)))
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("📊 Glass Forming Distribution")
    fig = px.pie(
        filtered_data,
        names="Glass_Forming",
        title="Glass Forming Distribution (Filtered)"
    )
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader("📊 Composition Length vs Elements")
    fig = px.scatter(
        filtered_data,
        x='Composition_Length',
        y='num_elements',
        color='Glass_Forming',
        title='Composition Length vs Number of Elements (Filtered)'
    )
    st.plotly_chart(fig, use_container_width=True)

# Full-width visualization
st.header("📊 Advanced Visualization")
fig = px.box(
    filtered_data,
    x='Glass_Forming',
    y='Composition_Length',
    title='Composition Length Distribution by Glass Forming (Filtered)'
)
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Built with Streamlit for MSE 3114**")

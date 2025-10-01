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

# Main dashboard area - use full width for better table display
st.subheader("Data Overview")
# Display first 5 rows as a formatted table
st.write("**First 5 rows:**")

# Create a responsive HTML table with horizontal scrolling
html_table = "<div style='overflow-x: auto;'>"
html_table += "<table style='border-collapse: collapse; width: 100%; font-size: 14px; min-width: 600px;'>"
html_table += "<tr style='background-color: #f2f2f2;'>"
for col in data.columns:
    html_table += f"<th style='border: 1px solid #ddd; padding: 6px; text-align: left; font-size: 12px;'>{col}</th>"
html_table += "</tr>"

for i in range(min(5, len(data))):
    row_data = data.iloc[i]
    html_table += "<tr>"
    for col in data.columns:
        html_table += f"<td style='border: 1px solid #ddd; padding: 6px; font-size: 12px;'>{row_data[col]}</td>"
    html_table += "</tr>"

html_table += "</table>"
html_table += "</div>"
st.markdown(html_table, unsafe_allow_html=True)

# Display statistics as a responsive HTML table to avoid PyArrow
stats = data.describe()

# Create responsive HTML table for statistics with horizontal scrolling if needed
stats_html = "<div style='overflow-x: auto;'>"
stats_html += "<table style='border-collapse: collapse; width: 100%; font-size: 14px; min-width: 600px;'>"
stats_html += "<tr style='background-color: #f2f2f2;'>"
stats_html += "<th style='border: 1px solid #ddd; padding: 6px; text-align: left; font-size: 12px;'>Statistic</th>"
for col in stats.columns:
    stats_html += f"<th style='border: 1px solid #ddd; padding: 6px; text-align: left; font-size: 12px;'>{col}</th>"
stats_html += "</tr>"

for stat in stats.index:
    stats_html += "<tr>"
    stats_html += f"<td style='border: 1px solid #ddd; padding: 6px; font-weight: bold; font-size: 12px;'>{stat}</td>"
    for col in stats.columns:
        value = stats.loc[stat, col]
        if pd.isna(value):
            stats_html += "<td style='border: 1px solid #ddd; padding: 6px; font-size: 12px;'>-</td>"
        else:
            stats_html += f"<td style='border: 1px solid #ddd; padding: 6px; font-size: 12px;'>{value:.4f}</td>"
    stats_html += "</tr>"

stats_html += "</table>"
stats_html += "</div>"
st.markdown(stats_html, unsafe_allow_html=True)

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

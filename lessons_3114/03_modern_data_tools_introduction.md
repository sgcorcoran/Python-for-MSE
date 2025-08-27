# Lesson 3: Modern Data Tools Introduction
## Beyond Pandas: Fast Data Processing and Interactive Dashboards

**Duration**: 2 weeks (Weeks 5-6)  
**Weekly Workload**: 3-4 hours  
**Learning Focus**: Modern data processing tools and basic dashboard creation

---

## Learning Objectives

By the end of this lesson, you will be able to:
- **Understand limitations** of traditional pandas for large datasets
- **Implement Polars** for fast data processing
- **Create basic Streamlit dashboards** for materials science data
- **Compare performance** between different data processing tools
- **Apply modern tools** to materials science problems

---

## Week 5: Understanding Data Processing Limitations

### Why Move Beyond Pandas?

Pandas has been the go-to data processing library for years, but it has limitations that become apparent with larger datasets:

#### Traditional Pandas Limitations
- **Memory Usage**: Creates copies of data during operations
- **Speed**: Single-threaded operations on large datasets
- **Memory Layout**: Not optimized for modern CPU architectures
- **Lazy Evaluation**: No built-in lazy processing capabilities

#### When You Need Modern Tools
- **Large Datasets**: >100MB files or >1M rows
- **Real-time Processing**: Interactive dashboards and live data
- **Memory Constraints**: Limited RAM on your system
- **Performance Requirements**: Need faster processing times

### Performance Comparison: Pandas vs. Modern Alternatives

Let's create a simple benchmark to see the difference:

```python
import pandas as pd
import polars as pl
import numpy as np
import time
import psutil
import matplotlib.pyplot as plt

def create_large_dataset(size=1000000):
    """Create a large materials science dataset for testing"""
    np.random.seed(42)
    
    # Generate realistic materials data
    compositions = np.random.uniform(0, 10, (size, 5))  # 5 alloying elements
    temperatures = np.random.uniform(20, 800, size)      # Processing temperatures
    times = np.random.uniform(1, 24, size)              # Processing times
    properties = np.random.uniform(100, 600, size)      # Mechanical properties
    
    # Create DataFrame structure
    data_dict = {
        'Al_content': compositions[:, 0],
        'Cu_content': compositions[:, 1],
        'Mg_content': compositions[:, 2],
        'Si_content': compositions[:, 3],
        'Fe_content': compositions[:, 4],
        'Temperature_C': temperatures,
        'Time_hours': times,
        'Tensile_Strength_MPa': properties
    }
    
    return data_dict

def benchmark_pandas(data_dict):
    """Benchmark pandas operations"""
    print("=== PANDAS BENCHMARK ===")
    
    # Memory before
    memory_before = psutil.Process().memory_info().rss / 1024 / 1024  # MB
    
    start_time = time.time()
    
    # Create DataFrame
    df_pandas = pd.DataFrame(data_dict)
    create_time = time.time() - start_time
    
    # Memory after creation
    memory_after_create = psutil.Process().memory_info().rss / 1024 / 1024
    
    # Perform operations
    start_time = time.time()
    
    # Group by temperature ranges and calculate statistics
    df_pandas['Temp_Range'] = pd.cut(df_pandas['Temperature_C'], 
                                    bins=[0, 200, 400, 600, 800], 
                                    labels=['Low', 'Medium', 'High', 'Very High'])
    
    grouped_stats = df_pandas.groupby('Temp_Range').agg({
        'Tensile_Strength_MPa': ['mean', 'std', 'count'],
        'Cu_content': 'mean',
        'Mg_content': 'mean'
    }).round(2)
    
    # Filter high-strength alloys
    high_strength = df_pandas[df_pandas['Tensile_Strength_MPa'] > 400]
    
    # Calculate correlations
    correlations = df_pandas[['Al_content', 'Cu_content', 'Mg_content', 
                             'Tensile_Strength_MPa']].corr()
    
    operation_time = time.time() - start_time
    
    # Memory after operations
    memory_after_ops = psutil.Process().memory_info().rss / 1024 / 1024
    
    total_time = create_time + operation_time
    
    print(f"DataFrame creation: {create_time:.3f}s")
    print(f"Operations: {operation_time:.3f}s")
    print(f"Total time: {total_time:.3f}s")
    print(f"Memory usage: {memory_after_ops:.1f} MB")
    print(f"Dataset shape: {df_pandas.shape}")
    
    return {
        'create_time': create_time,
        'operation_time': operation_time,
        'total_time': total_time,
        'memory_usage': memory_after_ops,
        'shape': df_pandas.shape
    }

def benchmark_polars(data_dict):
    """Benchmark polars operations"""
    print("\n=== POLARS BENCHMARK ===")
    
    # Memory before
    memory_before = psutil.Process().memory_info().rss / 1024 / 1024
    
    start_time = time.time()
    
    # Create DataFrame
    df_polars = pl.DataFrame(data_dict)
    create_time = time.time() - start_time
    
    # Memory after creation
    memory_after_create = psutil.Process().memory_info().rss / 1024 / 1024
    
    # Perform operations
    start_time = time.time()
    
    # Group by temperature ranges and calculate statistics
    df_polars = df_polars.with_columns([
        pl.when(pl.col('Temperature_C') <= 200).then(pl.lit('Low'))
        .when(pl.col('Temperature_C') <= 400).then(pl.lit('Medium'))
        .when(pl.col('Temperature_C') <= 600).then(pl.lit('High'))
        .otherwise(pl.lit('Very High')).alias('Temp_Range')
    ])
    
    grouped_stats = df_polars.group_by('Temp_Range').agg([
        pl.col('Tensile_Strength_MPa').mean().alias('mean_strength'),
        pl.col('Tensile_Strength_MPa').std().alias('std_strength'),
        pl.col('Tensile_Strength_MPa').count().alias('count'),
        pl.col('Cu_content').mean().alias('mean_cu'),
        pl.col('Mg_content').mean().alias('mean_mg')
    ])
    
    # Filter high-strength alloys
    high_strength = df_polars.filter(pl.col('Tensile_Strength_MPa') > 400)
    
    # Calculate correlations
    correlations = df_polars.select([
        pl.col('Al_content'), pl.col('Cu_content'), 
        pl.col('Mg_content'), pl.col('Tensile_Strength_MPa')
    ]).corr()
    
    operation_time = time.time() - start_time
    
    # Memory after operations
    memory_after_ops = psutil.Process().memory_info().rss / 1024 / 1024
    
    total_time = create_time + operation_time
    
    print(f"DataFrame creation: {create_time:.3f}s")
    print(f"Operations: {operation_time:.3f}s")
    print(f"Total time: {total_time:.3f}s")
    print(f"Memory usage: {memory_after_ops:.1f} MB")
    print(f"Dataset shape: {df_polars.shape}")
    
    return {
        'create_time': create_time,
        'operation_time': operation_time,
        'total_time': total_time,
        'memory_usage': memory_after_ops,
        'shape': df_polars.shape
    }

# Run benchmarks
print("Creating large dataset...")
data_dict = create_large_dataset(1000000)  # 1M rows

pandas_results = benchmark_pandas(data_dict)
polars_results = benchmark_polars(data_dict)

# Performance comparison
print("\n=== PERFORMANCE COMPARISON ===")
print(f"Pandas total time: {pandas_results['total_time']:.3f}s")
print(f"Polars total time: {polars_results['total_time']:.3f}s")
speedup = pandas_results['total_time'] / polars_results['total_time']
print(f"Polars is {speedup:.1f}x faster than pandas")

print(f"\nPandas memory: {pandas_results['memory_usage']:.1f} MB")
print(f"Polars memory: {polars_results['memory_usage']:.1f} MB")
memory_ratio = pandas_results['memory_usage'] / polars_results['memory_usage']
print(f"Polars uses {memory_ratio:.1f}x less memory than pandas")
```

### Understanding the Results

The benchmark should show that Polars is significantly faster and more memory-efficient than pandas for large datasets. This is because:

1. **Rust Backend**: Polars is written in Rust, which is faster than Python
2. **Lazy Evaluation**: Operations are optimized before execution
3. **Memory Layout**: Data is stored in columnar format for better CPU cache utilization
4. **Parallel Processing**: Many operations can run on multiple CPU cores

### Week 5 Assignment: Performance Benchmarking

**Due**: End of Week 5  
**Points**: 10 points  
**Deliverables**:
1. **Complete benchmark code** comparing pandas and polars
2. **Performance analysis** with visualizations
3. **Memory usage comparison** charts
4. **Dataset size scaling** analysis (test with different sizes)
5. **Benchmark report** summarizing findings

**Code Requirements**:
- Clean benchmarking functions
- Error handling and validation
- Professional visualizations
- Comprehensive documentation

**Analysis Requirements**:
- Test with datasets of 100K, 500K, and 1M rows
- Compare creation time, operation time, and memory usage
- Create performance vs. dataset size plots
- Document any system-specific variations

---

## Week 6: Building Your First Streamlit Dashboard

### Introduction to Streamlit

Streamlit is a Python library that makes it easy to create interactive web applications for data science. It's perfect for creating dashboards that showcase your materials science analysis.

### Why Streamlit for Materials Science?

- **Quick Development**: Turn Python scripts into web apps in minutes
- **Interactive Elements**: Sliders, dropdowns, and file uploads
- **Real-time Updates**: Changes to code automatically update the app
- **Easy Deployment**: Simple deployment to cloud platforms
- **Python Native**: Works seamlessly with your existing code

### Basic Streamlit Dashboard Structure

#### 1. Simple Materials Properties Dashboard
```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Materials Science Dashboard",
    page_icon="🔬",
    layout="wide"
)

# Title and description
st.title("🔬 Materials Science Properties Dashboard")
st.markdown("Interactive dashboard for exploring materials properties and compositions")

# Sidebar for controls
st.sidebar.header("Dashboard Controls")

# File upload
uploaded_file = st.sidebar.file_uploader(
    "Upload your materials data (CSV)",
    type=['csv'],
    help="Upload a CSV file with materials properties"
)

# Sample data if no file uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success(f"Data loaded: {data.shape[0]} rows, {data.shape[1]} columns")
else:
    # Generate sample data
    st.info("Using sample data. Upload your own CSV file to analyze your data.")
    data = generate_sample_materials_data()

# Display basic data info
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Samples", len(data))
with col2:
    st.metric("Properties Measured", len(data.select_dtypes(include=[np.number]).columns))
with col3:
    st.metric("Composition Elements", len([col for col in data.columns if 'content' in col.lower()]))

# Data preview
st.subheader("📊 Data Preview")
st.dataframe(data.head(10))

# Interactive visualizations
st.subheader("📈 Interactive Visualizations")

# Property distribution
col1, col2 = st.columns(2)

with col1:
    st.write("**Property Distribution**")
    property_col = st.selectbox(
        "Select property to visualize:",
        options=data.select_dtypes(include=[np.number]).columns.tolist()
    )
    
    if property_col:
        fig = px.histogram(data, x=property_col, nbins=20, 
                          title=f"Distribution of {property_col}")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("**Composition Analysis**")
    composition_cols = [col for col in data.columns if 'content' in col.lower()]
    
    if composition_cols:
        selected_composition = st.selectbox(
            "Select composition element:",
            options=composition_cols
        )
        
        if selected_composition:
            fig = px.box(data, y=selected_composition, 
                        title=f"{selected_composition} Distribution")
            st.plotly_chart(fig, use_container_width=True)

# Correlation analysis
st.subheader("🔗 Property Correlations")
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()

if len(numeric_cols) > 1:
    # Calculate correlations
    corr_matrix = data[numeric_cols].corr()
    
    # Create heatmap
    fig = px.imshow(corr_matrix, 
                    text_auto=True, 
                    aspect="auto",
                    title="Property Correlation Matrix",
                    color_continuous_scale='RdBu')
    st.plotly_chart(fig, use_container_width=True)

# Interactive filtering
st.subheader("🔍 Data Filtering")
col1, col2 = st.columns(2)

with col1:
    if 'Tensile_Strength_MPa' in data.columns:
        min_strength = st.slider(
            "Minimum Tensile Strength (MPa):",
            min_value=float(data['Tensile_Strength_MPa'].min()),
            max_value=float(data['Tensile_Strength_MPa'].max()),
            value=float(data['Tensile_Strength_MPa'].min())
        )
        
        filtered_data = data[data['Tensile_Strength_MPa'] >= min_strength]
        st.write(f"**Filtered Results**: {len(filtered_data)} samples meet criteria")

with col2:
    if 'Density_g_cm3' in data.columns:
        max_density = st.slider(
            "Maximum Density (g/cm³):",
            min_value=float(data['Density_g_cm3'].min()),
            max_value=float(data['Density_g_cm3'].max()),
            value=float(data['Density_g_cm3'].max())
        )
        
        density_filtered = data[data['Density_g_cm3'] <= max_density]
        st.write(f"**Density Filtered**: {len(density_filtered)} samples meet criteria")

# Display filtered results
if 'filtered_data' in locals():
    st.subheader("📋 Filtered Data Results")
    st.dataframe(filtered_data)

# Download filtered data
if 'filtered_data' in locals():
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_materials_data.csv",
        mime="text/csv"
    )

# Helper function for sample data
def generate_sample_materials_data():
    """Generate sample materials science data"""
    np.random.seed(42)
    n_samples = 100
    
    # Generate realistic materials data
    data = {
        'Sample_ID': [f'Sample_{i:03d}' for i in range(1, n_samples + 1)],
        'Al_content': np.random.uniform(85, 99, n_samples),
        'Cu_content': np.random.uniform(0, 5, n_samples),
        'Mg_content': np.random.uniform(0, 3, n_samples),
        'Si_content': np.random.uniform(0, 2, n_samples),
        'Fe_content': np.random.uniform(0, 1, n_samples),
        'Tensile_Strength_MPa': np.random.uniform(100, 600, n_samples),
        'Yield_Strength_MPa': np.random.uniform(80, 500, n_samples),
        'Elongation_Percent': np.random.uniform(2, 25, n_samples),
        'Hardness_HV': np.random.uniform(50, 200, n_samples),
        'Density_g_cm3': np.random.uniform(2.6, 2.9, n_samples)
    }
    
    return pd.DataFrame(data)
```

#### 2. Running Your Dashboard
```bash
# Save the code as app.py
# Run the dashboard
streamlit run app.py
```

### Advanced Dashboard Features

#### Interactive Parameter Exploration
```python
# Add to your dashboard
st.subheader("🎛️ Parameter Exploration")

# Composition sliders
st.write("**Adjust Composition Parameters**")
col1, col2, col3 = st.columns(3)

with col1:
    cu_target = st.slider("Target Cu Content (%)", 0.0, 5.0, 2.0, 0.1)
with col2:
    mg_target = st.slider("Target Mg Content (%)", 0.0, 3.0, 1.0, 0.1)
with col3:
    si_target = st.slider("Target Si Content (%)", 0.0, 2.0, 0.5, 0.1)

# Find similar compositions
if 'data' in locals():
    tolerance = 0.5
    similar_compositions = data[
        (abs(data['Cu_content'] - cu_target) <= tolerance) &
        (abs(data['Mg_content'] - mg_target) <= tolerance) &
        (abs(data['Si_content'] - si_target) <= tolerance)
    ]
    
    st.write(f"**Similar Compositions Found**: {len(similar_compositions)} samples")
    
    if len(similar_compositions) > 0:
        st.dataframe(similar_compositions)
        
        # Plot similar compositions
        fig = px.scatter_3d(
            similar_compositions,
            x='Cu_content', y='Mg_content', z='Si_content',
            color='Tensile_Strength_MPa',
            title="Similar Compositions in 3D Space"
        )
        st.plotly_chart(fig, use_container_width=True)
```

### Week 6 Assignment: Interactive Materials Dashboard

**Due**: End of Week 6  
**Points**: 15 points  
**Deliverables**:
1. **Complete Streamlit dashboard** with interactive features
2. **Data processing functions** using Polars for efficiency
3. **Interactive visualizations** with Plotly
4. **User controls** (sliders, dropdowns, file uploads)
5. **Dashboard documentation** and user guide

**Code Requirements**:
- Clean, modular dashboard structure
- Efficient data processing with Polars
- Professional visualizations
- Error handling and user feedback
- Comprehensive documentation

**Dashboard Requirements**:
- File upload capability for CSV data
- Interactive property exploration
- Composition-property relationships
- Data filtering and export
- Professional appearance and layout

---

## Key Concepts Summary

### Modern Data Processing
- **Polars**: Fast, memory-efficient alternative to pandas
- **Performance Benefits**: Significant speed and memory improvements
- **Use Cases**: Large datasets, real-time processing, memory-constrained systems

### Interactive Dashboards
- **Streamlit**: Quick web app development for data science
- **Interactive Elements**: Sliders, dropdowns, file uploads
- **Real-time Updates**: Live code changes reflected in the app
- **Easy Deployment**: Simple cloud deployment process

### Best Practices
- **Choose the Right Tool**: Use pandas for small datasets, Polars for large ones
- **Benchmark Performance**: Always test performance with your specific data
- **Modular Design**: Build dashboards with reusable components
- **User Experience**: Focus on intuitive controls and clear visualizations
- **Documentation**: Provide clear instructions for dashboard users

---

## Next Steps

In the next lesson, we'll learn about **basic statistical analysis with AI assistance**, including hypothesis testing and automated reporting for materials science data.

**Remember**: Modern data tools aren't just about speed - they're about enabling new types of analysis and making your research more accessible to others through interactive dashboards.

---

## Resources and References

### Modern Data Tools
- [Polars Documentation](https://pola.rs/python/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)

### Performance Optimization
- [Python Performance Profiling](https://docs.python.org/3/library/profile.html)
- [Memory Profiling in Python](https://pypi.org/project/memory-profiler/)
- [Benchmarking Best Practices](https://pythonhosted.org/pyperf/)

### Dashboard Design
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Plotly Chart Types](https://plotly.com/python/plotly-express/)
- [Interactive Visualization Best Practices](https://www.interaction-design.org/literature/topics/data-visualization)

---

**Happy dashboard building!** 🚀


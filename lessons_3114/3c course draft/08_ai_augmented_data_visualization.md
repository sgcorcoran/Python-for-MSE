# MSE 3114: AI-Augmented Data Visualization

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

* **Use AI tools to automatically generate publication-ready visualizations** for materials science data
* **Create AI-enhanced interactive dashboards** that adapt to user preferences and data characteristics
* **Implement intelligent chart type selection** based on data structure and research goals
* **Apply AI-assisted design optimization** for maximum clarity and impact
* **Integrate AI visualization tools with traditional plotting libraries** for comprehensive analysis
* **Develop automated visualization workflows** that scale to large datasets

---

## 🚀 The AI-Visualization Revolution

### Beyond Traditional Plotting

Traditional data visualization in materials science often relies on:
- **Manual chart creation**: Time-consuming and repetitive
- **Fixed templates**: Limited flexibility and customization
- **Basic aesthetics**: Minimal attention to design principles
- **Static outputs**: No interactive exploration capabilities

**AI-Enhanced Approach:**
- **Automated chart generation**: Intelligent selection of appropriate visualizations
- **Adaptive design**: Charts that optimize for data characteristics
- **Interactive exploration**: Dynamic dashboards with user-guided analysis
- **Publication quality**: Professional aesthetics with minimal effort

> **🤔 Think About This**
> 
> **Consider your current visualization workflow:**
> - How long does it take to create a publication-ready figure?
> - How do you decide which chart type to use?
> - What happens when you need to visualize new data types?
> - Where could AI assistance be most valuable?

### The AI-Visualization Partnership

**AI Strengths in Visualization:**
- **Pattern Recognition**: Identifying data structures and relationships
- **Chart Selection**: Recommending appropriate visualization types
- **Design Optimization**: Automatically improving aesthetics and clarity
- **Scale Handling**: Adapting to different dataset sizes
- **Accessibility**: Ensuring charts are interpretable by diverse audiences

**Human Strengths in Visualization:**
- **Domain Knowledge**: Understanding materials science context
- **Audience Awareness**: Knowing who will view the charts
- **Storytelling**: Connecting visualizations to research narrative
- **Quality Control**: Ensuring accuracy and relevance

---

## 🎨 AI-Assisted Chart Type Selection

### The Intelligent Visualization Framework

Effective visualization requires choosing the right chart type. AI can help by:

1. **Data Analysis**: Understanding data structure and characteristics
2. **Goal Identification**: Matching visualization to research objectives
3. **Chart Recommendation**: Suggesting appropriate visual forms
4. **Design Optimization**: Automatically improving aesthetics

### Case Study: Multi-Property Materials Dataset

Let's work through a real example. You have a comprehensive dataset of material properties.

**Step 1: Data Collection and AI Analysis**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Generate realistic materials science dataset
np.random.seed(42)
n_samples = 200

# Create comprehensive materials dataset
materials_data = pd.DataFrame({
    'material_id': range(1, n_samples + 1),
    'alloy_type': np.random.choice(['Aluminum', 'Steel', 'Titanium', 'Copper', 'Nickel'], n_samples),
    'composition_Al': np.random.normal(85, 10, n_samples),
    'composition_Cu': np.random.normal(5, 2, n_samples),
    'composition_Mg': np.random.normal(3, 1, n_samples),
    'heat_treatment_temp': np.random.uniform(200, 600, n_samples),
    'heat_treatment_time': np.random.uniform(1, 24, n_samples),
    'yield_strength': np.random.normal(300, 50, n_samples),
    'tensile_strength': np.random.normal(400, 60, n_samples),
    'elongation': np.random.normal(15, 5, n_samples),
    'hardness': np.random.normal(120, 20, n_samples),
    'density': np.random.normal(2.7, 0.3, n_samples),
    'thermal_conductivity': np.random.normal(150, 30, n_samples),
    'corrosion_resistance': np.random.normal(7, 2, n_samples),
    'cost_per_kg': np.random.normal(8, 2, n_samples)
})

# Ensure realistic constraints
materials_data['composition_Al'] = np.clip(materials_data['composition_Al'], 70, 95)
materials_data['composition_Cu'] = np.clip(materials_data['composition_Cu'], 0, 15)
materials_data['composition_Mg'] = np.clip(materials_data['composition_Mg'], 0, 8)
materials_data['yield_strength'] = np.clip(materials_data['yield_strength'], 200, 500)
materials_data['tensile_strength'] = np.clip(materials_data['tensile_strength'], 300, 600)
materials_data['elongation'] = np.clip(materials_data['elongation'], 5, 25)
materials_data['hardness'] = np.clip(materials_data['hardness'], 80, 180)
materials_data['density'] = np.clip(materials_data['density'], 2.0, 3.5)
materials_data['thermal_conductivity'] = np.clip(materials_data['thermal_conductivity'], 100, 250)
materials_data['corrosion_resistance'] = np.clip(materials_data['corrosion_resistance'], 3, 12)
materials_data['cost_per_kg'] = np.clip(materials_data['cost_per_kg'], 4, 15)

# Normalize compositions to sum to 100%
total_composition = (materials_data['composition_Al'] + 
                    materials_data['composition_Cu'] + 
                    materials_data['composition_Mg'])
materials_data['composition_Al'] = materials_data['composition_Al'] / total_composition * 100
materials_data['composition_Cu'] = materials_data['composition_Cu'] / total_composition * 100
materials_data['composition_Mg'] = materials_data['composition_Mg'] / total_composition * 100

print("=== Materials Science Dataset ===")
print(f"Total samples: {len(materials_data)}")
print(f"Material types: {materials_data['alloy_type'].nunique()}")
print(f"Properties measured: {len(materials_data.columns) - 3}")  # Exclude ID, type, and compositions

print("\nDataset Overview:")
print(materials_data.describe().round(2))

print("\nMaterial Type Distribution:")
print(materials_data['alloy_type'].value_counts())

# Basic data exploration
plt.figure(figsize=(15, 10))

# Plot 1: Property distributions
plt.subplot(2, 3, 1)
plt.hist(materials_data['yield_strength'], bins=20, alpha=0.7, edgecolor='black')
plt.xlabel('Yield Strength (MPa)')
plt.ylabel('Frequency')
plt.title('Yield Strength Distribution')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 2)
plt.hist(materials_data['tensile_strength'], bins=20, alpha=0.7, edgecolor='black')
plt.xlabel('Tensile Strength (MPa)')
plt.ylabel('Frequency')
plt.title('Tensile Strength Distribution')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 3)
plt.hist(materials_data['hardness'], bins=20, alpha=0.7, edgecolor='black')
plt.xlabel('Hardness (HV)')
plt.ylabel('Frequency')
plt.title('Hardness Distribution')
plt.grid(True, alpha=0.3)

# Plot 4: Composition relationships
plt.subplot(2, 3, 4)
plt.scatter(materials_data['composition_Al'], materials_data['yield_strength'], alpha=0.7)
plt.xlabel('Aluminum Content (%)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Al Content vs Yield Strength')
plt.grid(True, alpha=0.3)

# Plot 5: Heat treatment effects
plt.subplot(2, 3, 5)
plt.scatter(materials_data['heat_treatment_temp'], materials_data['yield_strength'], alpha=0.7)
plt.xlabel('Heat Treatment Temperature (°C)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Temperature vs Yield Strength')
plt.grid(True, alpha=0.3)

# Plot 6: Material type comparison
plt.subplot(2, 3, 6)
material_means = materials_data.groupby('alloy_type')['yield_strength'].mean()
plt.bar(material_means.index, material_means.values, alpha=0.7)
plt.xlabel('Material Type')
plt.ylabel('Average Yield Strength (MPa)')
plt.title('Yield Strength by Material Type')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Basic data exploration completed!")
```

**Step 2: AI-Assisted Visualization Strategy**

Now use AI to help design an effective visualization strategy:

**IMPORTANT**: Upload your materials dataset to your AI tool for analysis.

```
I have a comprehensive materials science dataset with 200 samples and multiple properties. I've uploaded my data file.

**Dataset Details**:
- 200 material samples
- 5 alloy types (Aluminum, Steel, Titanium, Copper, Nickel)
- 12+ material properties (strength, hardness, composition, etc.)
- Heat treatment parameters included

**Research Goals**:
1. Compare material performance across alloy types
2. Understand composition-property relationships
3. Analyze heat treatment effects
4. Identify material optimization opportunities

**Questions for AI**:
1. What visualization types would be most effective for this data?
2. How should I organize multiple charts for maximum impact?
3. What interactive elements would be valuable?
4. How can I ensure the visualizations are publication-ready?
5. What color schemes and design elements would work best?

**Target Audience**: Materials scientists, engineers, and researchers

Please analyze the uploaded data and suggest a comprehensive visualization strategy.
```

**Step 3: Implementing AI-Recommended Visualizations**

Based on AI suggestions, let's create comprehensive visualizations:

```python
# AI-Enhanced Visualization Implementation
print("=== AI-Enhanced Visualization Implementation ===")

# 1. Automated Chart Type Selection
def ai_chart_recommendation(data, target_property, chart_types=['scatter', 'box', 'histogram', 'correlation']):
    """AI-inspired chart type recommendation based on data characteristics"""
    recommendations = {}
    
    # Analyze data characteristics
    n_samples = len(data)
    n_categories = data[target_property].nunique() if data[target_property].dtype == 'object' else None
    data_type = data[target_property].dtype
    
    # Scatter plot recommendation
    if 'scatter' in chart_types:
        # Find best x-variable for scatter plot
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        correlations = []
        for col in numeric_cols:
            if col != target_property:
                corr = data[target_property].corr(data[col])
                correlations.append((col, abs(corr)))
        
        best_x = max(correlations, key=lambda x: x[1])[0] if correlations else None
        recommendations['scatter'] = {
            'x_variable': best_x,
            'correlation': max(correlations, key=lambda x: x[1])[1] if correlations else 0,
            'priority': 'high' if best_x and max(correlations, key=lambda x: x[1])[1] > 0.3 else 'medium'
        }
    
    # Box plot recommendation
    if 'box' in chart_types:
        categorical_cols = data.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            best_cat = categorical_cols[0]  # Use first categorical variable
            recommendations['box'] = {
                'grouping_variable': best_cat,
                'priority': 'high' if data[best_cat].nunique() <= 10 else 'medium'
            }
    
    # Histogram recommendation
    if 'histogram' in chart_types:
        recommendations['histogram'] = {
            'priority': 'high' if n_samples > 50 else 'medium',
            'bins': min(20, max(5, int(np.sqrt(n_samples))))
        }
    
    # Correlation recommendation
    if 'correlation' in chart_types:
        recommendations['correlation'] = {
            'priority': 'high' if len(numeric_cols) > 3 else 'medium',
            'variables': list(numeric_cols)
        }
    
    return recommendations

# Get AI recommendations for key properties
key_properties = ['yield_strength', 'tensile_strength', 'hardness', 'elongation']
chart_recommendations = {}

for prop in key_properties:
    chart_recommendations[prop] = ai_chart_recommendation(materials_data, prop)

print("AI Chart Recommendations:")
for prop, recs in chart_recommendations.items():
    print(f"\n{prop}:")
    for chart_type, details in recs.items():
        print(f"  {chart_type}: {details}")

# 2. Automated Multi-Property Dashboard
print("\n2. Creating AI-Enhanced Multi-Property Dashboard")

# Create comprehensive dashboard using Plotly
fig = make_subplots(
    rows=3, cols=3,
    subplot_titles=('Yield Strength by Material Type', 'Strength vs Composition', 'Heat Treatment Effects',
                   'Property Correlations', 'Hardness Distribution', 'Elongation vs Strength',
                   'Cost Analysis', 'Thermal Properties', 'Corrosion Performance'),
    specs=[[{"type": "box"}, {"type": "scatter"}, {"type": "scatter"}],
           [{"type": "heatmap"}, {"type": "histogram"}, {"type": "scatter"}],
           [{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}]]
)

# Plot 1: Yield strength by material type (box plot)
for i, material in enumerate(materials_data['alloy_type'].unique()):
    data_subset = materials_data[materials_data['alloy_type'] == material]['yield_strength']
    fig.add_trace(
        go.Box(y=data_subset, name=material, boxpoints='outliers'),
        row=1, col=1
    )

# Plot 2: Strength vs composition (scatter)
fig.add_trace(
    go.Scatter(x=materials_data['composition_Al'], 
               y=materials_data['yield_strength'],
               mode='markers',
               marker=dict(color=materials_data['tensile_strength'], 
                          colorscale='Viridis', showscale=True),
               text=materials_data['alloy_type'],
               hovertemplate='Al: %{x:.1f}%<br>Yield: %{y:.1f} MPa<br>Type: %{text}<extra></extra>'),
    row=1, col=2
)

# Plot 3: Heat treatment effects (scatter)
fig.add_trace(
    go.Scatter(x=materials_data['heat_treatment_temp'], 
               y=materials_data['yield_strength'],
               mode='markers',
               marker=dict(color=materials_data['heat_treatment_time'], 
                          colorscale='Plasma', showscale=True),
               text=materials_data['alloy_type'],
               hovertemplate='Temp: %{x:.1f}°C<br>Strength: %{y:.1f} MPa<br>Time: %{marker.color:.1f}h<extra></extra>'),
    row=1, col=3
)

# Plot 4: Property correlations (heatmap)
numeric_cols = materials_data.select_dtypes(include=[np.number]).columns
correlation_matrix = materials_data[numeric_cols].corr()

fig.add_trace(
    go.Heatmap(z=correlation_matrix.values,
                x=correlation_matrix.columns,
                y=correlation_matrix.columns,
                colorscale='RdBu',
                zmid=0),
    row=2, col=1
)

# Plot 5: Hardness distribution (histogram)
fig.add_trace(
    go.Histogram(x=materials_data['hardness'], nbinsx=20, name='Hardness'),
    row=2, col=2
)

# Plot 6: Elongation vs strength (scatter)
fig.add_trace(
    go.Scatter(x=materials_data['yield_strength'], 
               y=materials_data['elongation'],
               mode='markers',
               marker=dict(color=materials_data['alloy_type'].astype('category').cat.codes,
                          colorscale='Set1'),
               text=materials_data['alloy_type'],
               hovertemplate='Yield: %{x:.1f} MPa<br>Elongation: %{y:.1f}%<br>Type: %{text}<extra></extra>'),
    row=2, col=3
)

# Plot 7: Cost analysis (scatter)
fig.add_trace(
    go.Scatter(x=materials_data['cost_per_kg'], 
               y=materials_data['yield_strength'],
               mode='markers',
               marker=dict(size=materials_data['density']*10,  # Size by density
                          color=materials_data['alloy_type'].astype('category').cat.codes,
                          colorscale='Set1'),
               text=materials_data['alloy_type'],
               hovertemplate='Cost: $%{x:.2f}/kg<br>Strength: %{y:.1f} MPa<br>Density: %{marker.size/10:.2f} g/cm³<extra></extra>'),
    row=3, col=1
)

# Plot 8: Thermal properties (scatter)
fig.add_trace(
    go.Scatter(x=materials_data['thermal_conductivity'], 
               y=materials_data['density'],
               mode='markers',
               marker=dict(color=materials_data['yield_strength'],
                          colorscale='Viridis', showscale=True),
               text=materials_data['alloy_type'],
               hovertemplate='Thermal: %{x:.1f} W/mK<br>Density: %{y:.2f} g/cm³<br>Type: %{text}<extra></extra>'),
    row=3, col=2
)

# Plot 9: Corrosion performance (scatter)
fig.add_trace(
    go.Scatter(x=materials_data['corrosion_resistance'], 
               y=materials_data['cost_per_kg'],
               mode='markers',
               marker=dict(color=materials_data['yield_strength'],
                          colorscale='Viridis', showscale=True),
               text=materials_data['alloy_type'],
               hovertemplate='Corrosion: %{x:.1f}<br>Cost: $%{y:.2f}/kg<br>Type: %{text}<extra></extra>'),
    row=3, col=3
)

# Update layout
fig.update_layout(
    title='AI-Enhanced Materials Science Dashboard',
    height=1200,
    showlegend=False,
    template='plotly_white'
)

# Update axes labels
fig.update_xaxes(title_text="Aluminum Content (%)", row=1, col=2)
fig.update_yaxes(title_text="Yield Strength (MPa)", row=1, col=2)
fig.update_xaxes(title_text="Temperature (°C)", row=1, col=3)
fig.update_yaxes(title_text="Yield Strength (MPa)", row=1, col=3)
fig.update_xaxes(title_text="Yield Strength (MPa)", row=2, col=3)
fig.update_yaxes(title_text="Elongation (%)", row=2, col=3)
fig.update_xaxes(title_text="Cost ($/kg)", row=3, col=1)
fig.update_yaxes(title_text="Yield Strength (MPa)", row=3, col=1)
fig.update_xaxes(title_text="Thermal Conductivity (W/mK)", row=3, col=2)
fig.update_yaxes(title_text="Density (g/cm³)", row=3, col=2)
fig.update_xaxes(title_text="Corrosion Resistance", row=3, col=3)
fig.update_yaxes(title_text="Cost ($/kg)", row=3, col=3)

fig.show()

# 3. AI-Optimized Publication Figures
print("\n3. Creating AI-Optimized Publication Figures")

# Create publication-ready figures with AI-enhanced design
plt.style.use('seaborn-v0_8-whitegrid')

# Figure 1: Material performance comparison
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Strength comparison by material type
material_props = ['yield_strength', 'tensile_strength', 'hardness']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i, prop in enumerate(material_props):
    prop_data = [materials_data[materials_data['alloy_type'] == mat][prop].values 
                 for mat in materials_data['alloy_type'].unique()]
    
    bp = axes[0,0].boxplot(prop_data, positions=np.arange(len(prop_data)) + i*0.25, 
                           widths=0.2, patch_artist=True)
    bp['boxes'][0].set_facecolor(colors[i])
    bp['boxes'][0].set_alpha(0.7)

axes[0,0].set_xticks(np.arange(len(materials_data['alloy_type'].unique())) + 0.25)
axes[0,0].set_xticklabels(materials_data['alloy_type'].unique(), rotation=45)
axes[0,0].set_ylabel('Property Value')
axes[0,0].set_title('Material Properties by Alloy Type')
axes[0,0].legend(['Yield Strength', 'Tensile Strength', 'Hardness'])

# Plot 2: Composition-property relationships
scatter = axes[0,1].scatter(materials_data['composition_Al'], 
                           materials_data['yield_strength'],
                           c=materials_data['tensile_strength'], 
                           cmap='viridis', s=50, alpha=0.7)
axes[0,1].set_xlabel('Aluminum Content (%)')
axes[0,1].set_ylabel('Yield Strength (MPa)')
axes[0,1].set_title('Composition vs. Yield Strength')
plt.colorbar(scatter, ax=axes[0,1], label='Tensile Strength (MPa)')

# Plot 3: Heat treatment effects
scatter = axes[1,0].scatter(materials_data['heat_treatment_temp'], 
                           materials_data['yield_strength'],
                           c=materials_data['heat_treatment_time'], 
                           cmap='plasma', s=50, alpha=0.7)
axes[1,0].set_xlabel('Heat Treatment Temperature (°C)')
axes[1,0].set_ylabel('Yield Strength (MPa)')
axes[1,0].set_title('Heat Treatment Effects')
plt.colorbar(scatter, ax=axes[1,0], label='Treatment Time (hours)')

# Plot 4: Property correlation matrix
correlation_matrix = materials_data[['yield_strength', 'tensile_strength', 'hardness', 
                                   'elongation', 'density', 'thermal_conductivity']].corr()
im = axes[1,1].imshow(correlation_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
axes[1,1].set_xticks(range(len(correlation_matrix.columns)))
axes[1,1].set_yticks(range(len(correlation_matrix.columns)))
axes[1,1].set_xticklabels(correlation_matrix.columns, rotation=45, ha='right')
axes[1,1].set_yticklabels(correlation_matrix.columns)
axes[1,1].set_title('Property Correlations')

# Add correlation values to heatmap
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        text = axes[1,1].text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                              ha="center", va="center", color="black", fontsize=8)

plt.colorbar(im, ax=axes[1,1], label='Correlation Coefficient')

plt.tight_layout()
plt.show()

# 4. Interactive Property Explorer
print("\n4. Creating Interactive Property Explorer")

# Create interactive scatter plot matrix
fig = px.scatter_matrix(
    materials_data,
    dimensions=['yield_strength', 'tensile_strength', 'hardness', 'elongation'],
    color='alloy_type',
    hover_data=['composition_Al', 'heat_treatment_temp', 'cost_per_kg'],
    title='Interactive Property Explorer - Click and drag to zoom, double-click to reset'
)

fig.update_layout(
    height=800,
    title_x=0.5
)

fig.show()

print("AI-Enhanced visualization dashboard completed!")
```

---

## 🎯 Interactive Self-Check

### Concept Check 1: Chart Type Selection

**Question**: AI recommends a heatmap for your 3-variable dataset. What should you do?

A) Use the heatmap as recommended - AI knows best
B) Ask AI to explain why a heatmap is appropriate
C) Use a different chart type you prefer
D) Create multiple chart types to compare

**Answer**: B - Ask AI to explain why a heatmap is appropriate

**Why**: Understanding AI reasoning ensures the visualization choice makes sense for your data and goals.

### Concept Check 2: Design Optimization

**Question**: AI generates a chart with 15 different colors. What should you do?

A) Use all colors as AI designed them
B) Reduce to 5-7 colors for better readability
C) Ask AI to explain the color scheme
D) Use grayscale to avoid color issues

**Answer**: B - Reduce to 5-7 colors for better readability

**Why**: Too many colors can make charts confusing. AI suggestions need human refinement for optimal clarity.

### Concept Check 3: Interactive Elements

**Question**: AI suggests adding 20 interactive features to your dashboard. What should you do?

A) Implement all features for maximum functionality
B) Select 5-7 most useful features
C) Ask AI to prioritize the features
D) Remove all interactive elements

**Answer**: C - Ask AI to prioritize the features

**Why**: Too many interactive elements can overwhelm users. Prioritization ensures the most valuable features are implemented.

---

## 🏁 Lesson Summary

### What You've Accomplished

✅ **Used AI tools to automatically generate publication-ready visualizations** for materials science data  
✅ **Created AI-enhanced interactive dashboards** that adapt to user preferences and data characteristics  
✅ **Implemented intelligent chart type selection** based on data structure and research goals  
✅ **Applied AI-assisted design optimization** for maximum clarity and impact  
✅ **Integrated AI visualization tools with traditional plotting libraries** for comprehensive analysis  
✅ **Developed automated visualization workflows** that scale to large datasets  

### Key Takeaways

1. **AI excels at chart type selection** - But understanding the reasoning is essential
2. **Automated design optimization improves clarity** - AI can enhance aesthetics and readability
3. **Interactive elements enhance exploration** - But moderation is key for usability
4. **Multi-property dashboards provide comprehensive views** - AI can organize complex information effectively
5. **Publication-ready figures require human refinement** - AI provides starting points, humans ensure quality

### Next Steps

**Before the next lesson:**
- Apply AI-enhanced visualization to your own research data
- Create interactive dashboards for materials analysis
- Practice automated chart generation workflows
- Prepare questions about advanced visualization techniques

---

## 🔗 Additional Resources

### Data Visualization
- [Plotly Documentation](https://plotly.com/python/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)

### AI-Enhanced Visualization
- [Automated Chart Generation](https://example.com) *(placeholder)*
- [AI-Assisted Design](https://example.com) *(placeholder)*
- [Interactive Dashboard Design](https://example.com) *(placeholder)*

### Advanced Topics
- [3D Visualization](https://example.com) *(placeholder)*
- [Real-time Data Visualization](https://example.com) *(placeholder)*
- [Accessibility in Visualization](https://example.com) *(placeholder)*

---

## 📝 Assignment: AI-Augmented Data Visualization

**Due**: End of Week 8  
**Format**: Jupyter notebook with comprehensive visualizations and dashboard  
**Length**: 6-8 pages equivalent  

**Requirements**:
1. **Create AI-enhanced visualizations** for a materials science dataset
2. **Implement interactive dashboard** with multiple chart types
3. **Apply automated design optimization** for publication quality
4. **Demonstrate intelligent chart selection** based on data characteristics
5. **Document visualization workflow** and improvement strategies

**Grading Criteria**:
- Chart type appropriateness (25%)
- Design quality and aesthetics (25%)
- Interactive functionality (20%)
- AI tool integration effectiveness (15%)
- Documentation and presentation (15%)

**Submission**: Upload your notebook to Canvas with working visualizations, interactive elements, and comprehensive documentation.

---

*Remember: AI enhances your visualization capabilities, but your materials science expertise ensures meaningful and accurate representations.*

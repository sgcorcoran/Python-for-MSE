# Lesson 1: AI Tools Setup and Basic Analysis
## AI-Augmented Materials Science Fundamentals

**Duration**: 2 weeks (Weeks 1-2)  
**Weekly Workload**: 3-4 hours  
**Learning Focus**: AI tool configuration and first stress-strain analysis

---

## Learning Objectives

By the end of this lesson, you will be able to:
- **Configure AI tools** for materials science research
- **Load and validate** stress-strain data using Python
- **Perform basic analysis** with AI assistance
- **Create simple visualizations** of mechanical properties
- **Understand AI tool limitations** and best practices

---

## Week 1: AI Tools Setup and Environment Configuration

### Introduction to AI-Augmented Materials Science

Welcome to MSE 3114! This course will teach you how to use artificial intelligence tools to enhance your materials science research. We'll start by setting up the essential AI tools and then apply them to a classic materials science problem: stress-strain analysis.

### Why AI-Augmented Materials Science?

Traditional materials science research involves:
- Manual data analysis and interpretation
- Time-consuming literature reviews
- Limited experimental design optimization
- Basic statistical analysis

AI augmentation provides:
- **Accelerated Analysis**: Faster data processing and interpretation
- **Enhanced Insights**: Pattern recognition beyond human capability
- **Optimized Design**: AI-assisted experimental planning
- **Automated Reporting**: Quick generation of analysis summaries

### Essential AI Tools Setup

#### 1. ChatGPT Plus or Claude Pro
**Purpose**: AI research assistant for analysis planning and interpretation
**Setup Steps**:
1. Visit [chat.openai.com](https://chat.openai.com) or [claude.ai](https://claude.ai)
2. Create account and subscribe to Plus/Pro tier
3. Verify access to advanced features

**Alternative**: If you can't access these tools, we'll provide local LLM alternatives

#### 2. GitHub Copilot
**Purpose**: AI-powered code completion and generation
**Setup Steps**:
1. Install VS Code with Python extension
2. Sign up for [GitHub Student Developer Pack](https://education.github.com/pack)
3. Install GitHub Copilot extension
4. Authenticate with your GitHub account

#### 3. Local LLM Setup (Optional Alternative)
**Purpose**: Offline AI assistance for data privacy
**Setup Steps**:
1. Install [Ollama](https://ollama.ai)
2. Download Llama 3.1 8B model: `ollama pull llama3.1:8b`
3. Test with simple queries

### Python Environment Setup

#### Anaconda Installation
```bash
# Download and install Anaconda from https://www.anaconda.com/
# Create course environment
conda create -n mse3114 python=3.9
conda activate mse3114

# Install required packages
conda install pandas numpy matplotlib scipy scikit-learn
pip install opencv-python plotly streamlit polars duckdb
```

#### Verify Installation
```python
# Test your environment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import plotly.express as px
import streamlit as st
import polars as pl
import duckdb

print("All packages imported successfully!")
print(f"Pandas version: {pd.__version__}")
print(f"OpenCV version: {cv2.__version__}")
```

### First AI Interaction: Stress-Strain Analysis Planning

Let's use AI to help plan our first analysis. This demonstrates how AI can assist in research planning.

#### AI Prompt Template
```
**Context**: I'm a materials science student analyzing aluminum 7075-T6 tensile test data
**Data**: CSV file with columns for load, displacement, time, and cross-sectional area
**Goal**: Perform stress-strain analysis to determine mechanical properties
**Questions**: 
1. What steps should I follow for this analysis?
2. What mechanical properties can I extract?
3. What potential issues should I watch for?
4. How should I validate my results?
```

#### Expected AI Response
The AI should provide:
- Step-by-step analysis workflow
- List of mechanical properties to calculate
- Common data quality issues to check
- Validation methods for results

### Week 1 Assignment: Environment Setup

**Due**: End of Week 1  
**Points**: 10 points  
**Deliverables**:
1. **Screenshot** of working AI tool (ChatGPT/Claude or local LLM)
2. **Code verification** showing all packages imported successfully
3. **AI interaction log** with your first stress-strain analysis prompt
4. **Environment summary** listing your setup configuration

**Submission Format**: GitHub repository with README.md documenting your setup

---

## Week 2: Basic Stress-Strain Analysis with AI Assistance

### Data Loading and Validation

#### Sample Dataset
We'll use a simulated aluminum 7075-T6 tensile test dataset to practice our analysis.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load sample data (you'll get the actual file)
# data = pd.read_csv('aluminum_7075_tensile_data.csv')

# For now, let's create sample data to practice with
np.random.seed(42)
n_points = 1000

# Simulate realistic tensile test data
strain = np.linspace(0, 0.15, n_points)  # Engineering strain
noise = np.random.normal(0, 0.002, n_points)

# Simulate stress-strain curve with realistic properties
E = 71.7e3  # MPa (Young's modulus for Al 7075)
sigma_y = 503  # MPa (yield strength)
sigma_u = 572  # MPa (ultimate tensile strength)

# Create realistic stress-strain curve
stress = E * strain * (1 + 50 * strain) + noise * E
stress = np.maximum(stress, 0)  # No negative stress

# Create DataFrame
data = pd.DataFrame({
    'Strain': strain,
    'Stress_MPa': stress,
    'Load_N': stress * 100,  # Assuming 100 mm² cross-section
    'Displacement_mm': strain * 50  # Assuming 50 mm gauge length
})

print("Dataset shape:", data.shape)
print("Columns:", data.columns.tolist())
print("\nFirst few rows:")
print(data.head())
```

#### Data Quality Check
```python
def check_data_quality(data):
    """Basic data quality assessment"""
    print("=== DATA QUALITY CHECK ===")
    print(f"Dataset shape: {data.shape}")
    print(f"Missing values: {data.isnull().sum().sum()}")
    print(f"Data types:\n{data.dtypes}")
    
    # Check for physical constraints
    print(f"\nStress range: {data['Stress_MPa'].min():.1f} - {data['Stress_MPa'].max():.1f} MPa")
    print(f"Strain range: {data['Strain'].min():.4f} - {data['Strain'].max():.4f}")
    
    # Check for negative values where inappropriate
    negative_stress = (data['Stress_MPa'] < 0).sum()
    if negative_stress > 0:
        print(f"Warning: {negative_stress} negative stress values found")
    
    return data

# Run quality check
data = check_data_quality(data)
```

### Basic Stress-Strain Analysis

#### 1. Calculate Engineering Properties
```python
def calculate_mechanical_properties(data):
    """Calculate basic mechanical properties"""
    stress = data['Stress_MPa'].values
    strain = data['Strain'].values
    
    # Young's Modulus (slope of linear region)
    # Use first 20% of data for linear region
    linear_end = int(len(strain) * 0.2)
    slope, intercept = np.polyfit(strain[:linear_end], stress[:linear_end], 1)
    E = slope
    
    # Yield Strength (0.2% offset method)
    offset_strain = strain + 0.002
    offset_stress = E * offset_strain
    yield_idx = np.argmin(np.abs(stress - offset_stress))
    sigma_y = stress[yield_idx]
    
    # Ultimate Tensile Strength
    sigma_u = np.max(stress)
    
    # Elongation at break
    elongation = strain[-1] * 100
    
    return {
        'Young_Modulus_MPa': E,
        'Yield_Strength_MPa': sigma_y,
        'Ultimate_Strength_MPa': sigma_u,
        'Elongation_Percent': elongation
    }

# Calculate properties
properties = calculate_mechanical_properties(data)
print("\n=== MECHANICAL PROPERTIES ===")
for prop, value in properties.items():
    print(f"{prop}: {value:.1f}")
```

#### 2. Create Basic Visualizations
```python
def create_stress_strain_plot(data, properties):
    """Create publication-ready stress-strain plot"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Main stress-strain curve
    ax1.plot(data['Strain'], data['Stress_MPa'], 'b-', linewidth=2, label='Experimental Data')
    
    # Add linear region line
    linear_end = int(len(data) * 0.2)
    strain_linear = data['Strain'].iloc[:linear_end]
    stress_linear = properties['Young_Modulus_MPa'] * strain_linear
    ax1.plot(strain_linear, stress_linear, 'r--', linewidth=2, label=f"E = {properties['Young_Modulus_MPa']:.0f} MPa")
    
    # Add yield point
    ax1.axhline(y=properties['Yield_Strength_MPa'], color='g', linestyle=':', 
                label=f'σy = {properties["Yield_Strength_MPa"]:.0f} MPa')
    
    ax1.set_xlabel('Engineering Strain')
    ax1.set_ylabel('Engineering Stress (MPa)')
    ax1.set_title('Aluminum 7075-T6 Stress-Strain Curve')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Zoom on elastic region
    ax2.plot(data['Strain'], data['Stress_MPa'], 'b-', linewidth=2)
    ax2.plot(strain_linear, stress_linear, 'r--', linewidth=2)
    ax2.set_xlim(0, 0.01)
    ax2.set_ylim(0, 800)
    ax2.set_xlabel('Engineering Strain')
    ax2.set_ylabel('Engineering Stress (MPa)')
    ax2.set_title('Elastic Region (Zoom)')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Create plots
create_stress_strain_plot(data, properties)
```

### AI-Assisted Analysis Enhancement

#### Using AI for Interpretation
Now let's use our AI tools to enhance our analysis:

**Prompt for AI**:
```
I've analyzed aluminum 7075-T6 tensile test data and found:
- Young's Modulus: 71,700 MPa
- Yield Strength: 503 MPa  
- Ultimate Strength: 572 MPa
- Elongation: 15%

The data shows some noise in the stress measurements. Can you help me:
1. Interpret these results compared to typical Al 7075-T6 properties?
2. Suggest ways to reduce noise in future measurements?
3. Identify any potential issues with my analysis method?
4. Recommend additional properties I should calculate?
```

#### AI Response Analysis
The AI should provide:
- Comparison with literature values
- Noise reduction strategies
- Analysis validation suggestions
- Additional property calculations

### Week 2 Assignment: Complete Stress-Strain Analysis

**Due**: End of Week 2  
**Points**: 15 points  
**Deliverables**:
1. **Complete analysis code** with all mechanical property calculations
2. **Publication-ready stress-strain plot** with proper labels and formatting
3. **AI interaction summary** showing how AI enhanced your analysis
4. **Results validation** comparing your values with literature
5. **Error analysis** identifying potential sources of uncertainty

**Code Requirements**:
- Clean, well-documented functions
- Error handling for edge cases
- Clear variable naming
- Comprehensive comments

**Analysis Requirements**:
- Calculate Young's modulus, yield strength, ultimate strength, elongation
- Create professional stress-strain plots
- Validate results against literature values
- Document any data quality issues

---

## Key Concepts Summary

### AI Tool Integration
- **ChatGPT/Claude**: Research planning and interpretation assistance
- **GitHub Copilot**: Code completion and generation
- **Local LLMs**: Privacy-focused alternative for sensitive data

### Data Analysis Workflow
1. **Data Loading**: Import and validate data quality
2. **Property Calculation**: Implement mechanical property algorithms
3. **Visualization**: Create publication-ready plots
4. **AI Enhancement**: Use AI for interpretation and validation
5. **Documentation**: Record analysis process and results

### Best Practices
- **Always validate AI suggestions** with domain knowledge
- **Test code incrementally** to catch errors early
- **Document your analysis process** for reproducibility
- **Compare results with literature** to validate findings
- **Consider data quality issues** before drawing conclusions

---

## Next Steps

In the next lesson, we'll learn **prompt engineering** techniques to get better results from AI tools, and apply them to a more complex **alloy optimization case study**.

**Remember**: AI tools are assistants, not replacements for your materials science expertise. Use them to enhance your analysis, not to replace critical thinking.

---

## Resources and References

### AI Tools
- [ChatGPT Plus](https://chat.openai.com)
- [Claude Pro](https://claude.ai)
- [GitHub Copilot](https://github.com/features/copilot)
- [Ollama (Local LLMs)](https://ollama.ai)

### Materials Science References
- ASM Handbook Volume 2: Properties and Selection of Aluminum Alloys
- ASTM E8: Standard Test Methods for Tension Testing of Metallic Materials
- Typical Al 7075-T6 properties: E ≈ 71.7 GPa, σy ≈ 503 MPa, σu ≈ 572 MPa

### Python Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)

---

**Good luck with your first AI-augmented materials science analysis!** 🚀


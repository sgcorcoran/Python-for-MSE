# Lesson 5: Basic Experimental Design with AI Assistance
## Planning Efficient Materials Science Experiments

**Duration**: 2 weeks (Weeks 9-10)  
**Weekly Workload**: 3-4 hours  
**Learning Focus**: Basic DOE principles and AI-assisted experimental planning

---

## Learning Objectives

By the end of this lesson, you will be able to:
- **Understand basic DOE principles** for materials science experiments
- **Design simple factorial experiments** with AI assistance
- **Use Latin Hypercube Sampling** for parameter space exploration
- **Implement basic optimization** algorithms for materials processing
- **Create AI-enhanced experimental workflows** for research planning

---

## Week 9: Experimental Design Fundamentals

### Introduction to Design of Experiments (DOE)

Design of Experiments is a systematic approach to planning experiments that allows researchers to efficiently explore the effects of multiple variables on material properties. In materials science, this is crucial for:
- **Process Optimization**: Finding optimal processing conditions
- **Parameter Screening**: Identifying which factors matter most
- **Response Modeling**: Understanding relationships between inputs and outputs
- **Resource Efficiency**: Maximizing information from limited experiments

### Why DOE Matters in Materials Science

#### Traditional Approach Problems
- **One-Factor-at-a-Time**: Misses interactions between variables
- **Inefficient**: Many experiments needed for limited information
- **No Optimization**: Can't find optimal conditions systematically
- **Poor Understanding**: Limited insight into factor relationships

#### DOE Benefits
- **Efficient**: Fewer experiments for more information
- **Comprehensive**: Captures factor interactions
- **Optimized**: Systematic approach to finding best conditions
- **Statistical**: Results have statistical validity

### Basic DOE Concepts

#### 1. Factors and Levels
- **Factors**: Variables you can control (temperature, time, composition)
- **Levels**: Specific values for each factor (low, medium, high)
- **Response**: What you measure (strength, hardness, conductivity)

#### 2. Experimental Designs
- **Full Factorial**: All combinations of factor levels
- **Fractional Factorial**: Subset of full factorial (screening designs)
- **Response Surface**: Focused on optimization region
- **Latin Hypercube**: Space-filling design for complex spaces

#### 3. Design Efficiency
- **Resolution**: Ability to estimate main effects and interactions
- **Aliasing**: Confounding of effects in fractional designs
- **Randomization**: Reducing systematic bias

### AI-Assisted Experimental Planning

Let's use AI to help plan our experiments:

#### AI Prompt Template for Experimental Design
```
**Context**: I'm designing experiments to optimize [material property] for [application]
**Factors**: [List the variables I can control and their ranges]
**Constraints**: [Budget, time, equipment limitations]
**Objectives**: [What I want to achieve - maximize, minimize, or target]
**Current Knowledge**: [What I already know about factor effects]

**Output**: 
1. Recommended experimental design type
2. Number of experiments needed
3. Factor level combinations
4. Analysis plan
5. Success criteria
```

### Basic Factorial Design Implementation

Let's implement a simple 2³ factorial design for materials processing:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product
from scipy.stats import linregress
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

def create_factorial_design(factors, levels):
    """
    Create a full factorial experimental design
    
    Parameters:
    factors: List of factor names
    levels: Dictionary of factor levels {factor: [low, high]}
    
    Returns:
    DataFrame with experimental design matrix
    """
    
    print("=== FACTORIAL EXPERIMENTAL DESIGN ===")
    print(f"Factors: {factors}")
    print(f"Levels: {levels}")
    
    # Generate all combinations
    factor_combinations = list(product(*[levels[factor] for factor in factors]))
    
    # Create design matrix
    design_matrix = pd.DataFrame(factor_combinations, columns=factors)
    
    # Add standard order and run order
    design_matrix['Standard_Order'] = range(1, len(design_matrix) + 1)
    design_matrix['Run_Order'] = np.random.permutation(len(design_matrix)) + 1
    
    # Add center points if requested
    center_points = 3  # Number of center point replicates
    center_run = pd.DataFrame([{factor: np.mean(levels[factor]) for factor in factors} 
                             for _ in range(center_points)])
    center_run['Standard_Order'] = ['Center'] * center_points
    center_run['Run_Order'] = np.random.permutation(center_run.index) + len(design_matrix) + 1
    
    # Combine factorial and center points
    full_design = pd.concat([design_matrix, center_run], ignore_index=True)
    
    print(f"\nDesign Matrix Created:")
    print(f"Factorial runs: {len(design_matrix)}")
    print(f"Center points: {len(center_run)}")
    print(f"Total runs: {len(full_design)}")
    
    return full_design

def analyze_factorial_results(design_matrix, responses):
    """
    Analyze factorial experiment results
    
    Parameters:
    design_matrix: DataFrame with factor levels
    responses: List of response values corresponding to each run
    """
    
    print("\n=== FACTORIAL ANALYSIS ===")
    
    # Add responses to design matrix
    analysis_data = design_matrix.copy()
    analysis_data['Response'] = responses
    
    # Calculate main effects
    main_effects = {}
    for factor in [col for col in design_matrix.columns if col not in ['Standard_Order', 'Run_Order']]:
        high_level = analysis_data[analysis_data[factor] == analysis_data[factor].max()]['Response'].mean()
        low_level = analysis_data[analysis_data[factor] == analysis_data[factor].min()]['Response'].mean()
        main_effects[factor] = high_level - low_level
    
    print("\nMain Effects:")
    for factor, effect in main_effects.items():
        print(f"{factor}: {effect:.3f}")
    
    # Calculate two-factor interactions
    interactions = {}
    factors_list = [col for col in design_matrix.columns if col not in ['Standard_Order', 'Run_Order']]
    
    for i, factor1 in enumerate(factors_list):
        for factor2 in factors_list[i+1:]:
            # Calculate interaction effect
            interaction_effect = calculate_interaction_effect(analysis_data, factor1, factor2)
            interactions[f"{factor1}×{factor2}"] = interaction_effect
    
    print("\nTwo-Factor Interactions:")
    for interaction, effect in interactions.items():
        print(f"{interaction}: {effect:.3f}")
    
    # Create main effects plot
    create_effects_plots(main_effects, interactions)
    
    return main_effects, interactions

def calculate_interaction_effect(data, factor1, factor2):
    """Calculate two-factor interaction effect"""
    
    # Get all combinations of the two factors
    f1_levels = sorted(data[factor1].unique())
    f2_levels = sorted(data[factor2].unique())
    
    # Calculate interaction effect
    effect = ((data[(data[factor1] == f1_levels[1]) & (data[factor2] == f2_levels[1])]['Response'].mean() +
               data[(data[factor1] == f1_levels[0]) & (data[factor2] == f2_levels[0])]['Response'].mean()) -
              (data[(data[factor1] == f1_levels[1]) & (data[factor2] == f2_levels[0])]['Response'].mean() +
               data[(data[factor1] == f1_levels[0]) & (data[factor2] == f2_levels[1])]['Response'].mean()) / 2
    
    return effect

def create_effects_plots(main_effects, interactions):
    """Create visualization of main effects and interactions"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Main effects plot
    factors = list(main_effects.keys())
    effects = list(main_effects.values())
    
    bars = ax1.bar(factors, effects, color=['blue' if e > 0 else 'red' for e in effects])
    ax1.set_title('Main Effects')
    ax1.set_ylabel('Effect Size')
    ax1.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    
    # Add value labels on bars
    for bar, effect in zip(bars, effects):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + (0.01 if height > 0 else -0.01),
                f'{effect:.3f}', ha='center', va='bottom' if height > 0 else 'top')
    
    # Interactions plot
    interaction_names = list(interactions.keys())
    interaction_effects = list(interactions.values())
    
    bars = ax2.bar(interaction_names, interaction_effects, 
                   color=['blue' if e > 0 else 'red' for e in interaction_effects])
    ax2.set_title('Two-Factor Interactions')
    ax2.set_ylabel('Effect Size')
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, effect in zip(bars, interaction_effects):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + (0.01 if height > 0 else -0.01),
                f'{effect:.3f}', ha='center', va='bottom' if height > 0 else 'top')
    
    plt.tight_layout()
    plt.show()

# Example: Heat treatment optimization
def heat_treatment_example():
    """Example: Heat treatment optimization for aluminum alloy"""
    
    print("=== HEAT TREATMENT OPTIMIZATION EXAMPLE ===")
    
    # Define factors and levels
    factors = ['Temperature_C', 'Time_hours', 'Quench_Rate']
    levels = {
        'Temperature_C': [400, 500],      # Low, High
        'Time_hours': [2, 6],            # Short, Long
        'Quench_Rate': ['Slow', 'Fast']  # Slow, Fast
    }
    
    # Create factorial design
    design = create_factorial_design(factors, levels)
    
    print("\nExperimental Design Matrix:")
    print(design)
    
    # Simulate responses (in practice, these would be actual measurements)
    np.random.seed(42)
    simulated_responses = []
    
    for _, row in design.iterrows():
        if row['Standard_Order'] == 'Center':
            # Center point response
            response = 75 + np.random.normal(0, 2)
        else:
            # Factorial point responses based on factor effects
            base_response = 70
            
            # Temperature effect
            temp_effect = 15 if row['Temperature_C'] == 500 else 0
            
            # Time effect
            time_effect = 8 if row['Time_hours'] == 6 else 0
            
            # Quench rate effect
            quench_effect = 12 if row['Quench_Rate'] == 'Fast' else 0
            
            # Interaction effects
            temp_time_interaction = 5 if (row['Temperature_C'] == 500 and row['Time_hours'] == 6) else 0
            
            response = base_response + temp_effect + time_effect + quench_effect + temp_time_interaction
            response += np.random.normal(0, 3)  # Add noise
        
        simulated_responses.append(response)
    
    # Analyze results
    main_effects, interactions = analyze_factorial_results(design, simulated_responses)
    
    return design, main_effects, interactions

# Run the example
if __name__ == "__main__":
    design, main_effects, interactions = heat_treatment_example()
```

### Week 9 Assignment: Factorial Design Implementation

**Due**: End of Week 9  
**Points**: 10 points  
**Deliverables**:
1. **Complete factorial design system** with design generation
2. **Main effects and interaction analysis** functions
3. **Visualization tools** for effects plots
4. **AI integration** for experimental planning assistance
5. **Documentation** explaining the DOE process

**Code Requirements**:
- Clean factorial design generation
- Comprehensive effects analysis
- Professional visualizations
- Error handling and validation
- Clear documentation

**Analysis Requirements**:
- Handle 2³ factorial designs
- Calculate main effects and interactions
- Generate publication-ready plots
- Include center point analysis
- Provide clear interpretation guidance

---

## Week 10: Latin Hypercube Sampling and Basic Optimization

### Introduction to Latin Hypercube Sampling (LHS)

Latin Hypercube Sampling is a space-filling experimental design that's particularly useful for:
- **Complex Parameter Spaces**: Many factors with continuous ranges
- **Nonlinear Relationships**: When factor interactions are complex
- **Computational Experiments**: Simulation-based optimization
- **Screening Studies**: Initial exploration of large parameter spaces

### Why LHS for Materials Science?

#### Advantages
- **Efficient**: Good coverage with fewer experiments
- **Flexible**: Works with any number of factors and levels
- **Robust**: Less sensitive to factor correlations
- **Scalable**: Easy to add more experiments

#### Applications
- **Process Optimization**: Heat treatment, alloy composition
- **Material Selection**: Property optimization
- **Computational Design**: Simulation parameter tuning
- **Quality Control**: Process parameter screening

### Implementing Latin Hypercube Sampling

```python
def create_latin_hypercube_design(factors, n_samples, bounds):
    """
    Create Latin Hypercube experimental design
    
    Parameters:
    factors: List of factor names
    n_samples: Number of experiments to run
    bounds: Dictionary of factor bounds {factor: (min, max)}
    
    Returns:
    DataFrame with LHS design matrix
    """
    
    print("=== LATIN HYPERCUBE SAMPLING DESIGN ===")
    print(f"Factors: {factors}")
    print(f"Number of samples: {n_samples}")
    print(f"Bounds: {bounds}")
    
    # Create LHS design
    from scipy.stats.qmc import LatinHypercube
    
    # Initialize LHS
    lhs = LatinHypercube(d=len(factors), seed=42)
    
    # Generate samples in [0, 1] space
    samples_01 = lhs.random(n=n_samples)
    
    # Scale to actual factor ranges
    design_matrix = pd.DataFrame(samples_01, columns=factors)
    
    for factor in factors:
        min_val, max_val = bounds[factor]
        design_matrix[factor] = min_val + (max_val - min_val) * design_matrix[factor]
    
    # Add run order
    design_matrix['Run_Order'] = np.random.permutation(n_samples) + 1
    
    print(f"\nLHS Design Matrix Created:")
    print(f"Total runs: {len(design_matrix)}")
    print(f"Factor ranges covered:")
    for factor in factors:
        min_val, max_val = bounds[factor]
        actual_min = design_matrix[factor].min()
        actual_max = design_matrix[factor].max()
        print(f"  {factor}: {min_val:.2f} to {max_val:.2f} (actual: {actual_min:.2f} to {actual_max:.2f})")
    
    return design_matrix

def analyze_lhs_results(design_matrix, responses):
    """
    Analyze LHS experiment results
    
    Parameters:
    design_matrix: DataFrame with factor levels
    responses: List of response values corresponding to each run
    """
    
    print("\n=== LHS ANALYSIS ===")
    
    # Add responses to design matrix
    analysis_data = design_matrix.copy()
    analysis_data['Response'] = responses
    
    # Basic statistics
    print(f"Response Statistics:")
    print(f"  Mean: {np.mean(responses):.3f}")
    print(f"  Std: {np.std(responses):.3f}")
    print(f"  Min: {np.min(responses):.3f}")
    print(f"  Max: {np.max(responses):.3f}")
    
    # Factor importance using Random Forest
    factor_cols = [col for col in design_matrix.columns if col != 'Run_Order']
    X = analysis_data[factor_cols]
    y = analysis_data['Response']
    
    # Train Random Forest to assess factor importance
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X, y)
    
    # Get feature importance
    feature_importance = pd.DataFrame({
        'Factor': factor_cols,
        'Importance': rf_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print(f"\nFactor Importance (Random Forest):")
    for _, row in feature_importance.iterrows():
        print(f"  {row['Factor']}: {row['Importance']:.3f}")
    
    # Create factor importance plot
    create_factor_importance_plot(feature_importance)
    
    # Create response surface plots for top factors
    top_factors = feature_importance.head(2)['Factor'].tolist()
    if len(top_factors) >= 2:
        create_response_surface_plot(analysis_data, top_factors[0], top_factors[1])
    
    return feature_importance

def create_factor_importance_plot(feature_importance):
    """Create factor importance visualization"""
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(feature_importance['Factor'], feature_importance['Importance'], 
                   color='skyblue', edgecolor='navy')
    
    plt.title('Factor Importance in LHS Experiment')
    plt.xlabel('Factors')
    plt.ylabel('Importance Score')
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar, importance in zip(bars, feature_importance['Importance']):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{importance:.3f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def create_response_surface_plot(data, factor1, factor2):
    """Create 2D response surface plot for two factors"""
    
    # Create grid for surface plot
    x1_min, x1_max = data[factor1].min(), data[factor1].max()
    x2_min, x2_max = data[factor2].min(), data[factor2].max()
    
    x1_grid = np.linspace(x1_min, x1_max, 50)
    x2_grid = np.linspace(x2_min, x2_max, 50)
    X1_grid, X2_grid = np.meshgrid(x1_grid, x2_grid)
    
    # Fit simple polynomial model for visualization
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    
    X_poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(
        data[[factor1, factor2]]
    )
    model = LinearRegression()
    model.fit(X_poly, data['Response'])
    
    # Predict on grid
    X_grid_poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(
        np.column_stack([X1_grid.ravel(), X2_grid.ravel()])
    )
    Z_grid = model.predict(X_grid_poly).reshape(X1_grid.shape)
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Contour plot
    contour = ax1.contourf(X1_grid, X2_grid, Z_grid, levels=20, cmap='viridis')
    ax1.scatter(data[factor1], data[factor2], c=data['Response'], 
                s=50, edgecolors='white', linewidth=1)
    ax1.set_xlabel(factor1)
    ax1.set_ylabel(factor2)
    ax1.set_title(f'Response Surface: {factor1} vs {factor2}')
    plt.colorbar(contour, ax=ax1, label='Response')
    
    # 3D surface plot
    from mpl_toolkits.mplot3d import Axes3D
    ax2 = fig.add_subplot(122, projection='3d')
    surf = ax2.plot_surface(X1_grid, X2_grid, Z_grid, cmap='viridis', alpha=0.8)
    ax2.scatter(data[factor1], data[factor2], data['Response'], 
                c=data['Response'], s=50, edgecolors='white', linewidth=1)
    ax2.set_xlabel(factor1)
    ax2.set_ylabel(factor2)
    ax2.set_zlabel('Response')
    ax2.set_title(f'3D Response Surface')
    
    plt.tight_layout()
    plt.show()

# Example: Alloy composition optimization
def alloy_composition_example():
    """Example: Alloy composition optimization using LHS"""
    
    print("=== ALLOY COMPOSITION OPTIMIZATION EXAMPLE ===")
    
    # Define factors and bounds
    factors = ['Cu_content', 'Mg_content', 'Si_content', 'Heat_Temp', 'Heat_Time']
    bounds = {
        'Cu_content': (2.0, 6.0),      # wt%
        'Mg_content': (0.5, 2.5),      # wt%
        'Si_content': (0.2, 1.5),      # wt%
        'Heat_Temp': (400, 550),        # °C
        'Heat_Time': (2, 8)             # hours
    }
    
    # Create LHS design
    n_samples = 20
    design = create_latin_hypercube_design(factors, n_samples, bounds)
    
    print("\nLHS Design Matrix:")
    print(design.head(10))
    
    # Simulate responses (in practice, these would be actual measurements)
    np.random.seed(42)
    simulated_responses = []
    
    for _, row in design.iterrows():
        # Simulate tensile strength based on composition and heat treatment
        base_strength = 300  # MPa
        
        # Composition effects
        cu_effect = 25 * row['Cu_content']
        mg_effect = 15 * row['Mg_content']
        si_effect = 10 * row['Si_content']
        
        # Heat treatment effects
        temp_effect = 0.2 * row['Heat_Temp'] - 80
        time_effect = 5 * np.log(row['Heat_Time'])
        
        # Interaction effects
        cu_mg_interaction = 5 * row['Cu_content'] * row['Mg_content']
        temp_time_interaction = 0.1 * row['Heat_Temp'] * row['Heat_Time']
        
        # Calculate total strength
        strength = (base_strength + cu_effect + mg_effect + si_effect + 
                   temp_effect + time_effect + cu_mg_interaction + temp_time_interaction)
        
        # Add realistic noise
        strength += np.random.normal(0, 15)
        
        # Ensure physical constraints
        strength = np.maximum(strength, 200)
        strength = np.minimum(strength, 600)
        
        simulated_responses.append(strength)
    
    # Analyze results
    feature_importance = analyze_lhs_results(design, simulated_responses)
    
    return design, feature_importance

# Run the example
if __name__ == "__main__":
    design, feature_importance = alloy_composition_example()
```

### Week 10 Assignment: LHS Design and Analysis

**Due**: End of Week 10  
**Points**: 15 points  
**Deliverables**:
1. **Complete LHS design system** with design generation
2. **Factor importance analysis** using Random Forest
3. **Response surface visualization** tools
4. **AI integration** for experimental optimization
5. **Comprehensive documentation** of the LHS process

**Code Requirements**:
- Clean LHS design generation
- Comprehensive factor analysis
- Professional visualizations
- Error handling and validation
- Clear documentation

**Analysis Requirements**:
- Handle continuous factor ranges
- Implement factor importance assessment
- Create response surface plots
- Include 3D visualization
- Provide optimization insights

---

## Key Concepts Summary

### Experimental Design Principles
- **Factorial Designs**: Systematic exploration of factor combinations
- **Latin Hypercube Sampling**: Space-filling design for complex spaces
- **Factor Interactions**: Understanding how factors work together
- **Design Efficiency**: Maximizing information from limited experiments

### AI-Assisted Planning
- **Design Selection**: Use AI to choose appropriate experimental designs
- **Factor Screening**: AI helps identify important variables
- **Optimization Guidance**: AI suggests optimal factor combinations
- **Analysis Planning**: AI assists with experimental workflow design

### Best Practices
- **Start Simple**: Begin with factorial designs for screening
- **Use LHS**: For complex, continuous parameter spaces
- **Include Center Points**: For curvature detection and validation
- **Randomize**: Reduce systematic bias in experiments
- **Document Everything**: Record design decisions and results

---

## Next Steps

In the next lesson, we'll learn about **basic machine learning applications** in materials science, including property prediction and classification using AI-assisted model selection.

**Remember**: Good experimental design is about more than just running experiments - it's about planning efficiently, analyzing systematically, and learning from every data point.

---

## Resources and References

### Experimental Design
- [SciPy Latin Hypercube Sampling](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.LatinHypercube.html)
- [Design of Experiments for Engineers](https://www.jmp.com/en_us/statistics-knowledge-portal/design-of-experiments.html)
- [DOE in Materials Science](https://www.asminternational.org/)

### Materials Science Applications
- "Design and Analysis of Experiments" by Douglas C. Montgomery
- ASTM Standards for Experimental Design
- Journal of Materials Engineering and Performance: DOE applications

### AI Integration
- [AI for Experimental Design](https://www.nature.com/articles/s41524-020-00387-3)
- [Machine Learning in Materials Science](https://www.sciencedirect.com/science/article/pii/S0927025618303127)

---

**Happy experimental designing!** 🚀


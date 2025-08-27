# MSE 3114: AI-Enhanced Optimization for Materials Science

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

* **Use AI tools to automatically optimize materials processing parameters** for desired properties
* **Implement AI-assisted multi-objective optimization** balancing multiple conflicting objectives
* **Apply automated experimental design strategies** using AI-guided sampling and optimization
* **Create comprehensive optimization workflows** that integrate with materials science research
* **Develop AI-enhanced parameter space exploration** for discovery of optimal conditions
* **Build interactive optimization dashboards** for real-time process control and decision making

---

## 🚀 The AI-Optimization Revolution

### Beyond Traditional Optimization

Traditional materials optimization often relies on:
- **Trial-and-error approaches**: Time-consuming and inefficient
- **Single-objective optimization**: Limited to one property at a time
- **Fixed experimental designs**: No adaptation based on results
- **Manual parameter selection**: Subjective and potentially suboptimal

**AI-Enhanced Approach:**
- **Automated parameter optimization**: Intelligent search through parameter space
- **Multi-objective optimization**: Balancing multiple conflicting objectives
- **Adaptive experimental design**: Learning from results to guide future experiments
- **Intelligent sampling**: Efficient exploration of high-dimensional parameter spaces

> **🤔 Think About This**
> 
> **Consider your current optimization approach:**
> - How do you choose which parameters to vary in your experiments?
> - What happens when you need to optimize multiple properties simultaneously?
> - How do you know if you've found the global optimum?
> - Where could AI assistance be most valuable?

### The AI-Optimization Partnership

**AI Strengths in Optimization:**
- **Parameter Space Exploration**: Efficiently searching high-dimensional spaces
- **Multi-Objective Balancing**: Finding Pareto-optimal solutions
- **Adaptive Sampling**: Learning from results to guide future experiments
- **Global Optimization**: Avoiding local optima through intelligent search
- **Constraint Handling**: Managing complex physical and practical constraints

**Human Strengths in Optimization:**
- **Domain Knowledge**: Understanding materials science principles and constraints
- **Objective Definition**: Defining meaningful optimization goals
- **Validation**: Ensuring solutions are physically realistic
- **Implementation**: Applying optimization results in practice

---

## 🎯 AI-Assisted Parameter Optimization

### The Intelligent Optimization Framework

Effective optimization requires intelligent parameter selection. AI can help by:

1. **Parameter Space Analysis**: Understanding relationships between variables
2. **Objective Function Design**: Creating meaningful optimization targets
3. **Constraint Definition**: Identifying physical and practical limitations
4. **Search Strategy Selection**: Choosing appropriate optimization algorithms

### Case Study: Heat Treatment Optimization

Let's work through a real example. You want to optimize heat treatment parameters for maximum alloy strength and ductility.

**Step 1: Problem Definition and AI Analysis**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize, differential_evolution
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Generate comprehensive heat treatment dataset
np.random.seed(42)
n_samples = 300

# Create realistic heat treatment parameter space
heat_treatment_data = pd.DataFrame({
    'sample_id': range(1, n_samples + 1),
    'alloy_type': np.random.choice(['Aluminum', 'Steel', 'Titanium'], n_samples),
    'temperature': np.random.uniform(200, 800, n_samples),
    'time': np.random.uniform(0.5, 48, n_samples),
    'cooling_rate': np.random.uniform(0.1, 100, n_samples),
    'aging_temp': np.random.uniform(100, 250, n_samples),
    'aging_time': np.random.uniform(1, 168, n_samples),
    'quench_medium': np.random.choice(['Air', 'Oil', 'Water'], n_samples),
    'precipitation_temp': np.random.uniform(150, 400, n_samples),
    'strain_rate': np.random.uniform(0.001, 0.1, n_samples)
})

# Generate realistic mechanical properties based on processing parameters
def calculate_properties(row):
    """Calculate realistic mechanical properties based on heat treatment"""
    
    # Base properties from temperature and time
    temp_factor = (row['temperature'] - 200) / 600  # Normalized temperature effect
    time_factor = np.log(row['time']) / np.log(48)  # Normalized time effect
    
    # Cooling rate effects
    cooling_factor = np.exp(-row['cooling_rate'] / 50)  # Faster cooling = higher strength
    
    # Aging effects
    aging_factor = (row['aging_temp'] - 100) / 150 * np.log(row['aging_time']) / np.log(168)
    
    # Precipitation effects
    precip_factor = np.exp(-((row['precipitation_temp'] - 275) / 100)**2)  # Optimal around 275°C
    
    # Strain rate effects
    strain_factor = 1 + np.log(row['strain_rate'] / 0.001) * 0.1
    
    # Calculate final properties with realistic relationships
    yield_strength = (200 + temp_factor * 300 + time_factor * 100 + 
                     cooling_factor * 150 + aging_factor * 50 + 
                     precip_factor * 100) * strain_factor
    
    tensile_strength = yield_strength * (1.1 + np.random.normal(0, 0.05))
    
    # Ductility inversely related to strength
    elongation = np.clip(25 - (yield_strength - 200) / 20 + np.random.normal(0, 3), 2, 30)
    
    # Hardness related to strength
    hardness = np.clip(yield_strength / 3 + np.random.normal(0, 5), 60, 200)
    
    # Toughness (impact resistance)
    toughness = np.clip(50 - (yield_strength - 200) / 15 + np.random.normal(0, 8), 10, 80)
    
    return pd.Series({
        'yield_strength': yield_strength,
        'tensile_strength': tensile_strength,
        'elongation': elongation,
        'hardness': hardness,
        'toughness': toughness
    })

# Calculate properties
properties = heat_treatment_data.apply(calculate_properties, axis=1)
heat_treatment_data = pd.concat([heat_treatment_data, properties], axis=1)

# Add categorical encoding for quench medium
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
heat_treatment_data['quench_medium_encoded'] = le.fit_transform(heat_treatment_data['quench_medium'])

print("=== Heat Treatment Optimization Dataset ===")
print(f"Total samples: {len(heat_treatment_data)}")
print(f"Alloy types: {heat_treatment_data['alloy_type'].nunique()}")
print(f"Processing parameters: {len(heat_treatment_data.columns) - 7}")  # Exclude ID, type, and properties
print(f"Target properties: 5 (yield_strength, tensile_strength, elongation, hardness, toughness)")

print("\nDataset Overview:")
print(heat_treatment_data.describe().round(2))

print("\nAlloy Type Distribution:")
print(heat_treatment_data['alloy_type'].value_counts())

# Data exploration and visualization
plt.figure(figsize=(15, 10))

# Plot 1: Temperature effects on yield strength
plt.subplot(2, 3, 1)
for alloy in heat_treatment_data['alloy_type'].unique():
    alloy_data = heat_treatment_data[heat_treatment_data['alloy_type'] == alloy]
    plt.scatter(alloy_data['temperature'], alloy_data['yield_strength'], 
               alpha=0.7, label=alloy, s=30)
plt.xlabel('Temperature (°C)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Temperature vs Yield Strength')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Time effects on yield strength
plt.subplot(2, 3, 2)
for alloy in heat_treatment_data['alloy_type'].unique():
    alloy_data = heat_treatment_data[heat_treatment_data['alloy_type'] == alloy]
    plt.scatter(alloy_data['time'], alloy_data['yield_strength'], 
               alpha=0.7, label=alloy, s=30)
plt.xlabel('Time (hours)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Time vs Yield Strength')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: Cooling rate effects
plt.subplot(2, 3, 3)
for alloy in heat_treatment_data['alloy_type'].unique():
    alloy_data = heat_treatment_data[heat_treatment_data['alloy_type'] == alloy]
    plt.scatter(alloy_data['cooling_rate'], alloy_data['yield_strength'], 
               alpha=0.7, label=alloy, s=30)
plt.xlabel('Cooling Rate (°C/min)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Cooling Rate vs Yield Strength')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 4: Property correlations
plt.subplot(2, 3, 4)
property_cols = ['yield_strength', 'tensile_strength', 'elongation', 'hardness', 'toughness']
correlation_matrix = heat_treatment_data[property_cols].corr()
im = plt.imshow(correlation_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
plt.colorbar(im, label='Correlation Coefficient')
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Property Correlations')

# Plot 5: Aging effects
plt.subplot(2, 3, 5)
for alloy in heat_treatment_data['alloy_type'].unique():
    alloy_data = heat_treatment_data[heat_treatment_data['alloy_type'] == alloy]
    plt.scatter(alloy_data['aging_temp'], alloy_data['yield_strength'], 
               alpha=0.7, label=alloy, s=30)
plt.xlabel('Aging Temperature (°C)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Aging Temperature vs Yield Strength')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 6: Quench medium effects
plt.subplot(2, 3, 6)
quench_means = heat_treatment_data.groupby('quench_medium')['yield_strength'].mean()
plt.bar(quench_means.index, quench_means.values, alpha=0.7)
plt.xlabel('Quench Medium')
plt.ylabel('Average Yield Strength (MPa)')
plt.title('Yield Strength by Quench Medium')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Data exploration completed!")
```

**Step 2: AI-Assisted Optimization Strategy**

Now use AI to help design an effective optimization strategy:

**IMPORTANT**: Upload your heat treatment dataset to your AI tool for analysis.

```
I have a comprehensive heat treatment dataset for optimization. I've uploaded my data file.

**Dataset Details**:
- 300 heat treatment samples with 9+ processing parameters
- 5 target properties (strength, ductility, hardness, toughness)
- Multiple alloy types (Aluminum, Steel, Titanium)
- Various processing conditions (temperature, time, cooling rate, aging, etc.)

**Optimization Goals**:
1. Maximize yield strength while maintaining ductility
2. Optimize heat treatment parameters for different alloy types
3. Balance multiple conflicting objectives (strength vs. ductility)
4. Identify optimal processing windows for specific applications
5. Minimize processing time and energy consumption

**Questions for AI**:
1. What optimization algorithms would be most appropriate for this problem?
2. How should I handle the multi-objective nature of the problem?
3. What constraints should I consider for realistic processing conditions?
4. How can I validate that the optimization results are physically meaningful?
5. What experimental design strategy would be most efficient?

**Target Applications**: Process optimization, alloy development, quality control

Please analyze the uploaded data and suggest a comprehensive optimization strategy.
```

**Step 3: Implementing AI-Recommended Optimization**

Based on AI suggestions, let's create a comprehensive optimization pipeline:

```python
# AI-Enhanced Optimization Implementation
print("=== AI-Enhanced Optimization Implementation ===")

# 1. AI-Assisted Objective Function Design
def ai_objective_function_design(data, target_properties, optimization_type='multi_objective'):
    """AI-inspired objective function design for materials optimization"""
    
    objectives = {}
    
    if optimization_type == 'single_objective':
        # Single objective optimization (e.g., maximize yield strength)
        objectives['primary'] = {
            'property': 'yield_strength',
            'direction': 'maximize',
            'weight': 1.0,
            'reasoning': 'Primary mechanical property of interest'
        }
        
    elif optimization_type == 'multi_objective':
        # Multi-objective optimization
        objectives['yield_strength'] = {
            'property': 'yield_strength',
            'direction': 'maximize',
            'weight': 0.4,
            'reasoning': 'Primary strength requirement'
        }
        
        objectives['elongation'] = {
            'property': 'elongation',
            'direction': 'maximize',
            'weight': 0.3,
            'reasoning': 'Ductility requirement for formability'
        }
        
        objectives['toughness'] = {
            'property': 'toughness',
            'direction': 'maximize',
            'weight': 0.2,
            'reasoning': 'Impact resistance requirement'
        }
        
        objectives['hardness'] = {
            'property': 'hardness',
            'direction': 'maximize',
            'weight': 0.1,
            'reasoning': 'Wear resistance requirement'
        }
    
    # Add composite objective for multi-objective optimization
    if optimization_type == 'multi_objective':
        objectives['composite'] = {
            'type': 'weighted_sum',
            'weights': [obj['weight'] for obj in objectives.values() if 'weight' in obj],
            'reasoning': 'Balanced optimization of all properties'
        }
    
    return objectives

# 2. AI-Enhanced Constraint Definition
def ai_constraint_definition(data, parameter_ranges=None):
    """AI-inspired constraint definition for realistic processing conditions"""
    
    if parameter_ranges is None:
        # Define realistic parameter ranges based on data
        parameter_ranges = {
            'temperature': (200, 800),      # °C
            'time': (0.5, 48),             # hours
            'cooling_rate': (0.1, 100),    # °C/min
            'aging_temp': (100, 250),      # °C
            'aging_time': (1, 168),        # hours
            'precipitation_temp': (150, 400), # °C
            'strain_rate': (0.001, 0.1)    # 1/s
        }
    
    constraints = {}
    
    # Physical constraints
    constraints['physical'] = {
        'temperature_aging_relationship': 'aging_temp < temperature - 50',  # Aging below solution temp
        'time_temperature_relationship': 'time * temperature < 20000',     # Realistic T-t combinations
        'cooling_rate_limits': 'cooling_rate > 0.1',                      # Minimum cooling rate
    }
    
    # Processing constraints
    constraints['processing'] = {
        'total_time_limit': 'time + aging_time < 200',                    # Total processing time
        'temperature_gradient': 'abs(temperature - aging_temp) > 20',     # Minimum temperature difference
        'cooling_efficiency': 'cooling_rate < 100',                       # Maximum cooling rate
    }
    
    # Quality constraints
    constraints['quality'] = {
        'minimum_strength': 'yield_strength > 200',                       # Minimum strength requirement
        'minimum_ductility': 'elongation > 5',                           # Minimum ductility requirement
        'strength_ductility_balance': 'yield_strength / elongation < 20', # Strength-ductility balance
    }
    
    return constraints, parameter_ranges

# 3. AI-Enhanced Multi-Objective Optimization
def ai_multi_objective_optimization(data, alloy_type='Aluminum', n_objectives=4):
    """AI-inspired multi-objective optimization for heat treatment"""
    
    # Filter data for specific alloy type
    alloy_data = data[data['alloy_type'] == alloy_type].copy()
    
    # Prepare features and targets
    feature_cols = ['temperature', 'time', 'cooling_rate', 'aging_temp', 'aging_time', 
                   'precipitation_temp', 'strain_rate', 'quench_medium_encoded']
    
    X = alloy_data[feature_cols]
    y_strength = alloy_data['yield_strength']
    y_ductility = alloy_data['elongation']
    y_toughness = alloy_data['toughness']
    y_hardness = alloy_data['hardness']
    
    # Train Gaussian Process models for each property
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Model for yield strength
    gp_strength = GaussianProcessRegressor(
        kernel=RBF(length_scale=1.0) * ConstantKernel(1.0),
        random_state=42,
        n_restarts_optimizer=10
    )
    gp_strength.fit(X_scaled, y_strength)
    
    # Model for elongation
    gp_ductility = GaussianProcessRegressor(
        kernel=RBF(length_scale=1.0) * ConstantKernel(1.0),
        random_state=42,
        n_restarts_optimizer=10
    )
    gp_ductility.fit(X_scaled, y_ductility)
    
    # Model for toughness
    gp_toughness = GaussianProcessRegressor(
        kernel=RBF(length_scale=1.0) * ConstantKernel(1.0),
        random_state=42,
        n_restarts_optimizer=10
    )
    gp_toughness.fit(X_scaled, y_toughness)
    
    # Model for hardness
    gp_hardness = GaussianProcessRegressor(
        kernel=RBF(length_scale=1.0) * ConstantKernel(1.0),
        random_state=42,
        n_restarts_optimizer=10
    )
    gp_hardness.fit(X_scaled, y_hardness)
    
    # Define multi-objective function
    def multi_objective_function(params):
        """Multi-objective function for optimization"""
        # Normalize parameters to [0, 1] range
        param_ranges = np.array([
            [200, 800],    # temperature
            [0.5, 48],     # time
            [0.1, 100],    # cooling_rate
            [100, 250],    # aging_temp
            [1, 168],      # aging_time
            [150, 400],    # precipitation_temp
            [0.001, 0.1], # strain_rate
            [0, 2]         # quench_medium_encoded
        ])
        
        normalized_params = (params - param_ranges[:, 0]) / (param_ranges[:, 1] - param_ranges[:, 0])
        normalized_params = np.clip(normalized_params, 0, 1)
        
        # Scale parameters
        scaled_params = scaler.transform(normalized_params.reshape(1, -1))
        
        # Predict properties
        strength_pred = gp_strength.predict(scaled_params)[0]
        ductility_pred = gp_ductility.predict(scaled_params)[0]
        toughness_pred = gp_toughness.predict(scaled_params)[0]
        hardness_pred = gp_hardness.predict(scaled_params)[0]
        
        # Normalize objectives to [0, 1] range
        strength_norm = (strength_pred - 200) / (600 - 200)  # Expected range
        ductility_norm = (ductility_pred - 2) / (25 - 2)     # Expected range
        toughness_norm = (toughness_pred - 10) / (70 - 10)   # Expected range
        hardness_norm = (hardness_pred - 60) / (180 - 60)    # Expected range
        
        # Multi-objective function (weighted sum)
        weights = [0.4, 0.3, 0.2, 0.1]  # Strength, ductility, toughness, hardness
        composite_score = (weights[0] * strength_norm + 
                          weights[1] * ductility_norm + 
                          weights[2] * toughness_norm + 
                          weights[3] * hardness_norm)
        
        return -composite_score  # Negative for maximization
    
    # Define parameter bounds
    bounds = [
        (200, 800),    # temperature
        (0.5, 48),     # time
        (0.1, 100),    # cooling_rate
        (100, 250),    # aging_temp
        (1, 168),      # aging_time
        (150, 400),    # precipitation_temp
        (0.001, 0.1), # strain_rate
        (0, 2)         # quench_medium_encoded
    ]
    
    # Run optimization
    print(f"Running multi-objective optimization for {alloy_type}...")
    
    # Use differential evolution for global optimization
    result = differential_evolution(
        multi_objective_function,
        bounds,
        maxiter=1000,
        popsize=20,
        seed=42,
        workers=1
    )
    
    # Get optimal parameters
    optimal_params = result.x
    
    # Predict optimal properties
    param_ranges = np.array(bounds)
    normalized_params = (optimal_params - param_ranges[:, 0]) / (param_ranges[:, 1] - param_ranges[:, 0])
    normalized_params = np.clip(normalized_params, 0, 1)
    scaled_params = scaler.transform(normalized_params.reshape(1, -1))
    
    optimal_strength = gp_strength.predict(scaled_params)[0]
    optimal_ductility = gp_ductility.predict(scaled_params)[0]
    optimal_toughness = gp_toughness.predict(scaled_params)[0]
    optimal_hardness = gp_hardness.predict(scaled_params)[0]
    
    return {
        'optimal_parameters': {
            'temperature': optimal_params[0],
            'time': optimal_params[1],
            'cooling_rate': optimal_params[2],
            'aging_temp': optimal_params[3],
            'aging_time': optimal_params[4],
            'precipitation_temp': optimal_params[5],
            'strain_rate': optimal_params[6],
            'quench_medium': ['Air', 'Oil', 'Water'][int(optimal_params[7])]
        },
        'optimal_properties': {
            'yield_strength': optimal_strength,
            'elongation': optimal_ductility,
            'toughness': optimal_toughness,
            'hardness': optimal_hardness
        },
        'optimization_success': result.success,
        'function_evaluations': result.nfev
    }

# 4. AI-Enhanced Experimental Design
def ai_experimental_design(data, n_new_experiments=20, strategy='adaptive'):
    """AI-inspired experimental design for efficient parameter space exploration"""
    
    if strategy == 'adaptive':
        # Adaptive sampling based on current data
        from sklearn.cluster import KMeans
        
        # Use existing data to identify promising regions
        feature_cols = ['temperature', 'time', 'cooling_rate', 'aging_temp', 'aging_time', 
                       'precipitation_temp', 'strain_rate']
        
        X = data[feature_cols]
        
        # Cluster existing data to identify regions
        kmeans = KMeans(n_clusters=5, random_state=42)
        cluster_labels = kmeans.fit_predict(X)
        
        # Find clusters with best performance
        data['cluster'] = cluster_labels
        cluster_performance = data.groupby('cluster')['yield_strength'].mean()
        best_clusters = cluster_performance.nlargest(3).index
        
        # Generate new experiments in promising regions
        new_experiments = []
        for cluster in best_clusters:
            cluster_center = kmeans.cluster_centers_[cluster]
            cluster_std = X[data['cluster'] == cluster].std()
            
            # Generate experiments around cluster center
            n_cluster_experiments = n_new_experiments // len(best_clusters)
            for _ in range(n_cluster_experiments):
                # Add noise around cluster center
                new_params = cluster_center + np.random.normal(0, cluster_std * 0.5)
                
                # Ensure parameters are within bounds
                new_params = np.clip(new_params, X.min(), X.max())
                
                new_experiments.append(new_params)
        
        # Fill remaining experiments with random sampling
        while len(new_experiments) < n_new_experiments:
            random_params = np.random.uniform(X.min(), X.max())
            new_experiments.append(random_params)
        
        new_experiments = new_experiments[:n_new_experiments]
        
    elif strategy == 'latin_hypercube':
        # Latin Hypercube Sampling for uniform coverage
        from scipy.stats import qmc
        
        sampler = qmc.LatinHypercube(d=len(feature_cols), seed=42)
        sample = sampler.random(n=n_new_experiments)
        
        # Scale to parameter ranges
        param_ranges = np.array([
            [200, 800],    # temperature
            [0.5, 48],     # time
            [0.1, 100],    # cooling_rate
            [100, 250],    # aging_temp
            [1, 168],      # aging_time
            [150, 400],    # precipitation_temp
            [0.001, 0.1]  # strain_rate
        ])
        
        new_experiments = []
        for i in range(n_new_experiments):
            params = sample[i] * (param_ranges[:, 1] - param_ranges[:, 0]) + param_ranges[:, 0]
            new_experiments.append(params)
    
    return np.array(new_experiments)

# 5. Comprehensive Optimization Workflow
print("\n5. Running Comprehensive AI-Enhanced Optimization")

# Run optimization for each alloy type
optimization_results = {}
for alloy_type in heat_treatment_data['alloy_type'].unique():
    print(f"\n=== Optimizing {alloy_type} Heat Treatment ===")
    
    try:
        result = ai_multi_objective_optimization(heat_treatment_data, alloy_type)
        optimization_results[alloy_type] = result
        
        print(f"  Optimization successful: {result['optimization_success']}")
        print(f"  Function evaluations: {result['function_evaluations']}")
        print(f"  Optimal temperature: {result['optimal_parameters']['temperature']:.1f}°C")
        print(f"  Optimal time: {result['optimal_parameters']['time']:.1f} hours")
        print(f"  Optimal cooling rate: {result['optimal_parameters']['cooling_rate']:.1f}°C/min")
        print(f"  Optimal aging temp: {result['optimal_parameters']['aging_temp']:.1f}°C")
        print(f"  Optimal aging time: {result['optimal_parameters']['aging_time']:.1f} hours")
        print(f"  Optimal quench medium: {result['optimal_parameters']['quench_medium']}")
        
        print(f"  Predicted yield strength: {result['optimal_properties']['yield_strength']:.1f} MPa")
        print(f"  Predicted elongation: {result['optimal_properties']['elongation']:.1f}%")
        print(f"  Predicted toughness: {result['optimal_properties']['toughness']:.1f}")
        print(f"  Predicted hardness: {result['optimal_properties']['hardness']:.1f} HV")
        
    except Exception as e:
        print(f"  Optimization failed: {e}")
        optimization_results[alloy_type] = None

# 6. Experimental Design for Validation
print("\n6. AI-Enhanced Experimental Design")

# Generate new experiments for validation
new_experiments = ai_experimental_design(heat_treatment_data, n_new_experiments=30, strategy='adaptive')

print(f"Generated {len(new_experiments)} new experimental designs")
print("New experiment parameters:")
for i, exp in enumerate(new_experiments[:5]):  # Show first 5
    print(f"  Experiment {i+1}: T={exp[0]:.1f}°C, t={exp[1]:.1f}h, CR={exp[2]:.1f}°C/min, "
          f"AT={exp[3]:.1f}°C, ATt={exp[4]:.1f}h, PT={exp[5]:.1f}°C, SR={exp[6]:.3f}")

# 7. Optimization Results Visualization
print("\n7. Creating AI-Enhanced Optimization Visualizations")

# Create comprehensive optimization dashboard
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Plot 1: Optimization results comparison
alloy_types = list(optimization_results.keys())
strengths = [results['optimal_properties']['yield_strength'] if results else 0 
             for results in optimization_results.values()]
ductilities = [results['optimal_properties']['elongation'] if results else 0 
               for results in optimization_results.values()]

x = np.arange(len(alloy_types))
width = 0.35

axes[0,0].bar(x - width/2, strengths, width, label='Yield Strength (MPa)', alpha=0.7)
axes[0,0].bar(x + width/2, ductilities, width, label='Elongation (%)', alpha=0.7)
axes[0,0].set_xlabel('Alloy Type')
axes[0,0].set_ylabel('Property Value')
axes[0,0].set_title('Optimal Properties by Alloy Type')
axes[0,0].set_xticks(x)
axes[0,0].set_xticklabels(alloy_types)
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# Plot 2: Parameter sensitivity analysis
if any(optimization_results.values()):
    # Use first successful optimization for parameter analysis
    successful_optimization = next((r for r in optimization_results.values() if r is not None), None)
    
    if successful_optimization:
        param_names = list(successful_optimization['optimal_parameters'].keys())
        param_values = list(successful_optimization['optimal_parameters'].values())
        
        # Filter numeric parameters
        numeric_params = []
        numeric_values = []
        for name, value in zip(param_names, param_values):
            if isinstance(value, (int, float)):
                numeric_params.append(name)
                numeric_values.append(value)
        
        axes[0,1].bar(range(len(numeric_params)), numeric_values, alpha=0.7)
        axes[0,1].set_xlabel('Processing Parameters')
        axes[0,1].set_ylabel('Optimal Value')
        axes[0,1].set_title('Optimal Parameter Values')
        axes[0,1].set_xticks(range(len(numeric_params)))
        axes[0,1].set_xticklabels(numeric_params, rotation=45, ha='right')
        axes[0,1].grid(True, alpha=0.3)

# Plot 3: Property trade-offs
axes[0,2].scatter(heat_treatment_data['yield_strength'], heat_treatment_data['elongation'], 
                  alpha=0.6, s=30)
axes[0,2].set_xlabel('Yield Strength (MPa)')
axes[0,2].set_ylabel('Elongation (%)')
axes[0,2].set_title('Strength vs Ductility Trade-off')
axes[0,2].grid(True, alpha=0.3)

# Highlight optimal points
if any(optimization_results.values()):
    for alloy_type, result in optimization_results.items():
        if result:
            axes[0,2].scatter(result['optimal_properties']['yield_strength'], 
                             result['optimal_properties']['elongation'], 
                             s=100, marker='*', label=f'{alloy_type} Optimal')
    axes[0,2].legend()

# Plot 4: Temperature-time optimization space
scatter = axes[1,0].scatter(heat_treatment_data['temperature'], heat_treatment_data['time'], 
                           c=heat_treatment_data['yield_strength'], cmap='viridis', s=50, alpha=0.7)
axes[1,0].set_xlabel('Temperature (°C)')
axes[1,0].set_ylabel('Time (hours)')
axes[1,0].set_title('Temperature-Time Optimization Space')
plt.colorbar(scatter, ax=axes[1,0], label='Yield Strength (MPa)')
axes[1,0].grid(True, alpha=0.3)

# Plot 5: Cooling rate effects
axes[1,1].scatter(heat_treatment_data['cooling_rate'], heat_treatment_data['yield_strength'], 
                  alpha=0.6, s=30)
axes[1,1].set_xlabel('Cooling Rate (°C/min)')
axes[1,1].set_ylabel('Yield Strength (MPa)')
axes[1,1].set_title('Cooling Rate vs Yield Strength')
axes[1,1].grid(True, alpha=0.3)

# Plot 6: Aging effects
scatter = axes[1,2].scatter(heat_treatment_data['aging_temp'], heat_treatment_data['aging_time'], 
                           c=heat_treatment_data['yield_strength'], cmap='plasma', s=50, alpha=0.7)
axes[1,2].set_xlabel('Aging Temperature (°C)')
axes[1,2].set_ylabel('Aging Time (hours)')
axes[1,2].set_title('Aging Parameter Optimization Space')
plt.colorbar(scatter, ax=axes[1,2], label='Yield Strength (MPa)')
axes[1,2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 8. Interactive Optimization Dashboard
print("\n8. Creating Interactive Optimization Dashboard")

# Create interactive dashboard using Plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create interactive optimization dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Property Optimization Results', 'Parameter Sensitivity', 
                   'Temperature-Time Space', 'Property Trade-offs'),
    specs=[[{"type": "bar"}, {"type": "bar"}],
           [{"type": "scatter"}, {"type": "scatter"}]]
)

# Plot 1: Optimization results
fig.add_trace(
    go.Bar(x=alloy_types, y=strengths, name='Yield Strength (MPa)'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(x=alloy_types, y=ductilities, name='Elongation (%)'),
    row=1, col=1
)

# Plot 2: Parameter sensitivity
if any(optimization_results.values()):
    successful_optimization = next((r for r in optimization_results.values() if r is not None), None)
    if successful_optimization:
        param_names = list(successful_optimization['optimal_parameters'].keys())
        param_values = list(successful_optimization['optimal_parameters'].values())
        
        numeric_params = []
        numeric_values = []
        for name, value in zip(param_names, param_values):
            if isinstance(value, (int, float)):
                numeric_params.append(name)
                numeric_values.append(value)
        
        fig.add_trace(
            go.Bar(x=numeric_params, y=numeric_values, name='Optimal Values'),
            row=1, col=2
        )

# Plot 3: Temperature-time space
fig.add_trace(
    go.Scatter(x=heat_treatment_data['temperature'], 
               y=heat_treatment_data['time'],
               mode='markers',
               marker=dict(color=heat_treatment_data['yield_strength'], 
                          colorscale='Viridis', showscale=True),
               text=heat_treatment_data['alloy_type'],
               hovertemplate='Temp: %{x:.1f}°C<br>Time: %{y:.1f}h<br>Strength: %{marker.color:.1f} MPa<br>Alloy: %{text}<extra></extra>'),
    row=2, col=1
)

# Plot 4: Property trade-offs
fig.add_trace(
    go.Scatter(x=heat_treatment_data['yield_strength'], 
               y=heat_treatment_data['elongation'],
               mode='markers',
               marker=dict(color=heat_treatment_data['alloy_type'].astype('category').cat.codes,
                          colorscale='Set1'),
               text=heat_treatment_data['alloy_type'],
               hovertemplate='Strength: %{x:.1f} MPa<br>Elongation: %{y:.1f}%<br>Alloy: %{text}<extra></extra>'),
    row=2, col=2
)

# Update layout
fig.update_layout(
    title='AI-Enhanced Heat Treatment Optimization Dashboard',
    height=800,
    showlegend=True
)

fig.show()

print("AI-Enhanced optimization workflow completed!")
```

---

## 🎯 Interactive Self-Check

### Concept Check 1: Multi-Objective Optimization

**Question**: AI suggests optimizing 5 properties simultaneously. What should you do?

A) Optimize all 5 properties as suggested
B) Focus on the 2-3 most important properties
C) Ask AI to explain the optimization strategy
D) Use single-objective optimization instead

**Answer**: B - Focus on the 2-3 most important properties

**Why**: Too many objectives can make optimization complex and may not provide meaningful results. Focus on the most critical properties.

### Concept Check 2: Parameter Bounds

**Question**: AI optimization suggests temperatures above 1000°C. What should you do?

A) Use the AI result as is
B) Check if the temperature is physically realistic
C) Ask AI to explain the reasoning
D) Adjust the parameter bounds

**Answer**: B - Check if the temperature is physically realistic

**Why**: AI may suggest solutions outside physically meaningful ranges. Always validate results against domain knowledge.

### Concept Check 3: Experimental Validation

**Question**: AI optimization achieves 95% improvement. What should you do?

A) Implement the solution immediately
B) Validate the results experimentally
C) Trust the AI prediction
D) Optimize further

**Answer**: B - Validate the results experimentally

**Why**: AI predictions are estimates based on data. Experimental validation ensures the optimization results are reliable and applicable.

---

## 🏁 Lesson Summary

### What You've Accomplished

✅ **Used AI tools to automatically optimize materials processing parameters** for desired properties  
✅ **Implemented AI-assisted multi-objective optimization** balancing multiple conflicting objectives  
✅ **Applied automated experimental design strategies** using AI-guided sampling and optimization  
✅ **Created comprehensive optimization workflows** that integrate with materials science research  
✅ **Developed AI-enhanced parameter space exploration** for discovery of optimal conditions  
✅ **Built interactive optimization dashboards** for real-time process control and decision making  

### Key Takeaways

1. **AI excels at parameter space exploration** - But understanding the optimization strategy is crucial
2. **Multi-objective optimization requires careful design** - Focus on the most important objectives
3. **Constraints ensure physical realism** - Always validate AI suggestions against domain knowledge
4. **Experimental validation is essential** - AI provides predictions, experiments confirm reality
5. **Integration is key** - Optimization tools must fit into existing materials science workflows

### Next Steps

**Before the next lesson:**
- Apply AI-enhanced optimization to your own materials processing problems
- Practice multi-objective optimization workflows
- Experiment with different experimental design strategies
- Prepare questions about advanced optimization techniques

---

## 🔗 Additional Resources

### Optimization
- [Scipy Optimization](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [Multi-Objective Optimization](https://example.com) *(placeholder)*
- [Experimental Design](https://example.com) *(placeholder)*

### AI-Enhanced Optimization
- [Automated Parameter Tuning](https://example.com) *(placeholder)*
- [AI-Guided Sampling](https://example.com) *(placeholder)*
- [Multi-Objective Balancing](https://example.com) *(placeholder)*

### Advanced Topics
- [Bayesian Optimization](https://example.com) *(placeholder)*
- [Genetic Algorithms](https://example.com) *(placeholder)*
- [Real-time Optimization](https://example.com) *(placeholder)*

---

## 📝 Assignment: AI-Enhanced Optimization for Materials

**Due**: End of Week 11  
**Format**: Jupyter notebook with comprehensive optimization pipeline  
**Length**: 8-10 pages equivalent  

**Requirements**:
1. **Implement AI-assisted multi-objective optimization** for a materials processing problem
2. **Create automated experimental design strategy** using AI-guided sampling
3. **Develop comprehensive constraint handling** for realistic processing conditions
4. **Build optimization validation workflow** with experimental design
5. **Document complete optimization pipeline** from problem definition to solution validation

**Grading Criteria**:
- Optimization strategy appropriateness (20%)
- Multi-objective handling effectiveness (25%)
- Constraint implementation (20%)
- Experimental design quality (20%)
- Documentation and presentation (15%)

**Submission**: Upload your notebook to Canvas with working optimization pipeline, comprehensive results, and detailed documentation.

---

*Remember: AI enhances your optimization capabilities, but your materials science expertise ensures physically meaningful and practical solutions.*

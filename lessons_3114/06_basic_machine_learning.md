# Lesson 6: Basic Machine Learning for Materials Science
## Property Prediction and Classification with AI Assistance

**Duration**: 2 weeks (Weeks 11-12)  
**Weekly Workload**: 3-4 hours  
**Learning Focus**: Basic ML applications and AI-assisted model selection

---

## Learning Objectives

By the end of this lesson, you will be able to:
- **Understand basic ML concepts** relevant to materials science
- **Implement property prediction** models using regression algorithms
- **Perform material classification** using classification algorithms
- **Use AI assistance** for model selection and hyperparameter tuning
- **Evaluate model performance** with appropriate metrics

---

## Week 11: Machine Learning Fundamentals for Materials Science

### Introduction to Machine Learning in Materials Science

Machine learning has revolutionized materials science by enabling:
- **Property Prediction**: Predicting mechanical, thermal, and electrical properties
- **Material Classification**: Identifying phases, defects, and material types
- **Process Optimization**: Finding optimal processing conditions
- **Discovery**: Accelerating new material development

### Why Machine Learning for Materials Science?

#### Traditional Approach Limitations
- **Empirical Relationships**: Limited to known correlations
- **Complex Interactions**: Hard to model multiple factor effects
- **Time-Consuming**: Requires extensive experimentation
- **Limited Scope**: Can't handle high-dimensional data

#### Machine Learning Benefits
- **Pattern Recognition**: Discovers hidden relationships in data
- **High-Dimensional Analysis**: Handles many variables simultaneously
- **Nonlinear Modeling**: Captures complex factor interactions
- **Predictive Power**: Makes accurate predictions for new materials

### Key Machine Learning Concepts

#### 1. Supervised vs. Unsupervised Learning
- **Supervised**: Learn from labeled data (regression, classification)
- **Unsupervised**: Find patterns in unlabeled data (clustering, dimensionality reduction)

#### 2. Model Types
- **Regression**: Predict continuous values (strength, conductivity)
- **Classification**: Predict categories (phase type, defect type)
- **Clustering**: Group similar materials together

#### 3. Model Performance
- **Training**: Learning from data
- **Validation**: Testing on unseen data
- **Generalization**: Performance on new, unseen data

### AI-Assisted Model Selection

Let's use AI to help choose the right machine learning approach:

#### AI Prompt Template for Model Selection
```
**Context**: I'm building a machine learning model for [materials science problem]
**Data**: [Describe your dataset - size, features, target variable]
**Problem Type**: [Regression/Classification/Clustering]
**Objectives**: [What you want to predict or classify]
**Constraints**: [Computational, time, interpretability requirements]

**Output**: 
1. Recommended algorithm(s) with justification
2. Feature engineering suggestions
3. Hyperparameter tuning strategy
4. Validation approach
5. Performance metrics to use
```

### Basic Property Prediction: Regression

Let's implement a simple regression model for predicting material properties:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

def create_materials_dataset(n_samples=200):
    """
    Create a realistic materials science dataset for ML training
    
    Parameters:
    n_samples: Number of samples to generate
    
    Returns:
    DataFrame with features and target variable
    """
    
    np.random.seed(42)
    
    # Generate realistic materials features
    data = {
        # Composition features (wt%)
        'Al_content': np.random.uniform(85, 99, n_samples),
        'Cu_content': np.random.uniform(0, 5, n_samples),
        'Mg_content': np.random.uniform(0, 3, n_samples),
        'Si_content': np.random.uniform(0, 2, n_samples),
        'Fe_content': np.random.uniform(0, 1, n_samples),
        
        # Processing features
        'Heat_Temp': np.random.uniform(400, 550, n_samples),
        'Heat_Time': np.random.uniform(2, 8, n_samples),
        'Quench_Rate': np.random.choice(['Slow', 'Medium', 'Fast'], n_samples),
        'Aging_Temp': np.random.uniform(150, 200, n_samples),
        'Aging_Time': np.random.uniform(4, 24, n_samples),
        
        # Microstructural features
        'Grain_Size_um': np.random.uniform(5, 50, n_samples),
        'Precipitate_Size_nm': np.random.uniform(10, 100, n_samples),
        'Precipitate_Density': np.random.uniform(100, 1000, n_samples)
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Encode categorical variables
    df['Quench_Rate_Encoded'] = df['Quench_Rate'].map({'Slow': 1, 'Medium': 2, 'Fast': 3})
    
    # Generate target variable (Tensile Strength) based on realistic relationships
    base_strength = 300  # MPa
    
    # Composition effects
    strength = (base_strength + 
               25 * df['Cu_content'] + 
               15 * df['Mg_content'] + 
               10 * df['Si_content'] - 
               5 * df['Fe_content'])
    
    # Heat treatment effects
    strength += (0.2 * df['Heat_Temp'] - 80 + 
                5 * np.log(df['Heat_Time']) + 
                15 * (df['Quench_Rate_Encoded'] - 1))
    
    # Aging effects
    strength += (0.1 * df['Aging_Temp'] + 
                2 * np.log(df['Aging_Time']))
    
    # Microstructural effects
    strength += (-0.5 * df['Grain_Size_um'] + 
                0.1 * df['Precipitate_Size_nm'] + 
                0.05 * df['Precipitate_Density'])
    
    # Add realistic noise
    strength += np.random.normal(0, 15, n_samples)
    
    # Ensure physical constraints
    strength = np.maximum(strength, 200)
    strength = np.maximum(strength, 600)
    
    # Add target variable
    df['Tensile_Strength_MPa'] = strength
    
    print(f"Dataset created with {n_samples} samples")
    print(f"Features: {len(df.columns) - 1}")
    print(f"Target: Tensile_Strength_MPa")
    print(f"Strength range: {strength.min():.1f} - {strength.max():.1f} MPa")
    
    return df

def prepare_data_for_ml(df, target_col='Tensile_Strength_MPa'):
    """
    Prepare data for machine learning
    
    Parameters:
    df: DataFrame with features and target
    target_col: Name of target variable
    
    Returns:
    X_train, X_test, y_train, y_test, feature_names
    """
    
    # Select numerical features (exclude categorical and target)
    exclude_cols = ['Quench_Rate', target_col]
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    X = df[feature_cols]
    y = df[target_col]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    print(f"Features: {feature_cols}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, feature_cols

def train_regression_models(X_train, X_test, y_train, y_test, feature_names):
    """
    Train multiple regression models and compare performance
    
    Parameters:
    X_train, X_test: Scaled feature matrices
    y_train, y_test: Target variables
    feature_names: List of feature names
    
    Returns:
    Dictionary with model results
    """
    
    print("=== TRAINING REGRESSION MODELS ===")
    
    # Define models to test
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(alpha=1.0),
        'Lasso Regression': Lasso(alpha=0.1),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
        'Support Vector Regression': SVR(kernel='rbf', C=1.0, gamma='scale')
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        # Train model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        # Calculate metrics
        train_r2 = r2_score(y_train, y_pred_train)
        test_r2 = r2_score(y_test, y_pred_test)
        train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
        train_mae = mean_absolute_error(y_train, y_pred_train)
        test_mae = mean_absolute_error(y_test, y_pred_test)
        
        # Cross-validation score
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
        cv_mean = cv_scores.mean()
        cv_std = cv_scores.std()
        
        # Store results
        results[name] = {
            'model': model,
            'train_r2': train_r2,
            'test_r2': test_r2,
            'train_rmse': train_rmse,
            'test_rmse': test_rmse,
            'train_mae': train_mae,
            'test_mae': test_mae,
            'cv_mean': cv_mean,
            'cv_std': cv_std,
            'y_pred_test': y_pred_test
        }
        
        print(f"  Train R²: {train_r2:.3f}")
        print(f"  Test R²: {test_r2:.3f}")
        print(f"  Test RMSE: {test_rmse:.2f} MPa")
        print(f"  CV R²: {cv_mean:.3f} ± {cv_std:.3f}")
    
    return results

def compare_model_performance(results):
    """Compare performance of all models"""
    
    print("\n=== MODEL PERFORMANCE COMPARISON ===")
    
    # Create comparison DataFrame
    comparison_data = []
    for name, result in results.items():
        comparison_data.append({
            'Model': name,
            'Test R²': result['test_r2'],
            'Test RMSE': result['test_rmse'],
            'Test MAE': result['test_mae'],
            'CV R²': result['cv_mean'],
            'CV Std': result['cv_std']
        })
    
    comparison_df = pd.DataFrame(comparison_data)
    comparison_df = comparison_df.sort_values('Test R²', ascending=False)
    
    print(comparison_df.round(3))
    
    # Create performance visualization
    create_performance_comparison_plot(results)
    
    return comparison_df

def create_performance_comparison_plot(results):
    """Create visualization comparing model performance"""
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Test R² comparison
    models = list(results.keys())
    test_r2_scores = [results[model]['test_r2'] for model in models]
    
    bars = axes[0,0].bar(models, test_r2_scores, color='skyblue', edgecolor='navy')
    axes[0,0].set_title('Test R² Scores')
    axes[0,0].set_ylabel('R² Score')
    axes[0,0].tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, score in zip(bars, test_r2_scores):
        height = bar.get_height()
        axes[0,0].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{score:.3f}', ha='center', va='bottom')
    
    # Test RMSE comparison
    test_rmse_scores = [results[model]['test_rmse'] for model in models]
    
    bars = axes[0,1].bar(models, test_rmse_scores, color='lightcoral', edgecolor='darkred')
    axes[0,1].set_title('Test RMSE Scores')
    axes[0,1].set_ylabel('RMSE (MPa)')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, score in zip(bars, test_rmse_scores):
        height = bar.get_height()
        axes[0,1].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                       f'{score:.1f}', ha='center', va='bottom')
    
    # Cross-validation comparison
    cv_means = [results[model]['cv_mean'] for model in models]
    cv_stds = [results[model]['cv_std'] for model in models]
    
    bars = axes[1,0].bar(models, cv_means, yerr=cv_stds, capsize=5, 
                         color='lightgreen', edgecolor='darkgreen')
    axes[1,0].set_title('Cross-Validation R² Scores')
    axes[1,0].set_ylabel('R² Score')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, mean, std in zip(bars, cv_means, cv_stds):
        height = bar.get_height()
        axes[1,0].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{mean:.3f}±{std:.3f}', ha='center', va='bottom')
    
    # Prediction vs Actual for best model
    best_model = max(results.keys(), key=lambda x: results[x]['test_r2'])
    y_pred = results[best_model]['y_pred_test']
    
    # Get actual test values (you'll need to pass these)
    # This is a placeholder - in practice, you'd pass y_test
    y_test_placeholder = np.linspace(200, 600, len(y_pred))
    
    axes[1,1].scatter(y_test_placeholder, y_pred, alpha=0.6, color='purple')
    axes[1,1].plot([200, 600], [200, 600], 'r--', alpha=0.8, label='Perfect Prediction')
    axes[1,1].set_xlabel('Actual Tensile Strength (MPa)')
    axes[1,1].set_ylabel('Predicted Tensile Strength (MPa)')
    axes[1,1].set_title(f'Predictions vs Actual: {best_model}')
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Run the regression example
def run_regression_example():
    """Run complete regression example"""
    
    print("=== MATERIALS PROPERTY PREDICTION EXAMPLE ===")
    
    # Create dataset
    df = create_materials_dataset(200)
    
    # Prepare data for ML
    X_train, X_test, y_train, y_test, feature_names = prepare_data_for_ml(df)
    
    # Train models
    results = train_regression_models(X_train, X_test, y_train, y_test, feature_names)
    
    # Compare performance
    comparison_df = compare_model_performance(results)
    
    return df, results, comparison_df

# Run the example
if __name__ == "__main__":
    df, results, comparison_df = run_regression_example()
```

### Week 11 Assignment: Regression Model Implementation

**Due**: End of Week 11  
**Points**: 10 points  
**Deliverables**:
1. **Complete regression system** with multiple algorithms
2. **Model performance comparison** with visualizations
3. **Cross-validation implementation** for robust evaluation
4. **AI integration** for model selection assistance
5. **Documentation** explaining the ML workflow

**Code Requirements**:
- Clean model training and evaluation
- Comprehensive performance metrics
- Professional visualizations
- Error handling and validation
- Clear documentation

**Analysis Requirements**:
- Implement 5+ regression algorithms
- Compare performance using multiple metrics
- Include cross-validation analysis
- Generate publication-ready plots
- Provide model selection guidance

---

## Week 12: Material Classification and Model Evaluation

### Introduction to Classification in Materials Science

Classification problems in materials science include:
- **Phase Identification**: Identifying different material phases
- **Defect Classification**: Categorizing types of defects
- **Material Type Classification**: Distinguishing between material classes
- **Quality Assessment**: Classifying materials as pass/fail

### Classification Algorithms for Materials Science

#### 1. Logistic Regression
- **Use Case**: Simple binary classification problems
- **Advantages**: Interpretable, fast, good baseline
- **Limitations**: Linear decision boundaries

#### 2. Random Forest
- **Use Case**: Complex classification with many features
- **Advantages**: Handles non-linear relationships, feature importance
- **Limitations**: Less interpretable than linear models

#### 3. Support Vector Machines
- **Use Case**: High-dimensional data with clear separation
- **Advantages**: Effective in high dimensions, flexible kernels
- **Limitations**: Sensitive to parameter tuning

#### 4. Neural Networks
- **Use Case**: Complex patterns and large datasets
- **Advantages**: Can learn very complex relationships
- **Limitations**: Requires more data, harder to interpret

### Implementing Material Classification

```python
def create_classification_dataset(n_samples=300):
    """
    Create a materials classification dataset
    
    Parameters:
    n_samples: Number of samples to generate
    
    Returns:
    DataFrame with features and target classes
    """
    
    np.random.seed(42)
    
    # Generate features for different material classes
    data = []
    
    for i in range(n_samples):
        # Randomly assign material class
        material_class = np.random.choice(['Aluminum', 'Steel', 'Titanium', 'Copper'])
        
        if material_class == 'Aluminum':
            # Aluminum properties
            density = np.random.normal(2.7, 0.1)
            conductivity = np.random.normal(237, 20)
            hardness = np.random.normal(95, 15)
            strength = np.random.normal(310, 50)
            color_r = np.random.normal(0.8, 0.1)
            color_g = np.random.normal(0.8, 0.1)
            color_b = np.random.normal(0.8, 0.1)
            
        elif material_class == 'Steel':
            # Steel properties
            density = np.random.normal(7.85, 0.2)
            conductivity = np.random.normal(50, 10)
            hardness = np.random.normal(200, 30)
            strength = np.random.normal(500, 100)
            color_r = np.random.normal(0.7, 0.1)
            color_g = np.random.normal(0.7, 0.1)
            color_b = np.random.normal(0.7, 0.1)
            
        elif material_class == 'Titanium':
            # Titanium properties
            density = np.random.normal(4.5, 0.1)
            conductivity = np.random.normal(22, 5)
            hardness = np.random.normal(349, 20)
            strength = np.random.normal(950, 100)
            color_r = np.random.normal(0.8, 0.1)
            color_g = np.random.normal(0.8, 0.1)
            color_b = np.random.normal(0.8, 0.1)
            
        else:  # Copper
            # Copper properties
            density = np.random.normal(8.96, 0.1)
            conductivity = np.random.normal(401, 20)
            hardness = np.random.normal(87, 10)
            strength = np.random.normal(210, 30)
            color_r = np.random.normal(0.8, 0.1)
            color_g = np.random.normal(0.5, 0.1)
            color_b = np.random.normal(0.2, 0.1)
        
        # Add some noise and overlap for realistic classification challenge
        data.append({
            'Density_g_cm3': density + np.random.normal(0, 0.05),
            'Thermal_Conductivity_W_mK': conductivity + np.random.normal(0, 2),
            'Hardness_HV': hardness + np.random.normal(0, 3),
            'Tensile_Strength_MPa': strength + np.random.normal(0, 10),
            'Color_R': np.clip(color_r + np.random.normal(0, 0.02), 0, 1),
            'Color_G': np.clip(color_g + np.random.normal(0, 0.02), 0, 1),
            'Color_B': np.clip(color_b + np.random.normal(0, 0.02), 0, 1),
            'Material_Class': material_class
        })
    
    df = pd.DataFrame(data)
    
    print(f"Classification dataset created with {n_samples} samples")
    print(f"Features: {len(df.columns) - 1}")
    print(f"Classes: {df['Material_Class'].unique()}")
    print(f"Class distribution:")
    print(df['Material_Class'].value_counts())
    
    return df

def prepare_classification_data(df, target_col='Material_Class'):
    """
    Prepare data for classification
    
    Parameters:
    df: DataFrame with features and target
    target_col: Name of target variable
    
    Returns:
    X_train, X_test, y_train, y_test, feature_names
    """
    
    # Select numerical features
    feature_cols = [col for col in df.columns if col != target_col]
    
    X = df[feature_cols]
    y = df[target_col]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    print(f"Features: {feature_cols}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, feature_cols

def train_classification_models(X_train, X_test, y_train, y_test, feature_names):
    """
    Train multiple classification models and compare performance
    
    Parameters:
    X_train, X_test: Scaled feature matrices
    y_train, y_test: Target variables
    feature_names: List of feature names
    
    Returns:
    Dictionary with model results
    """
    
    print("=== TRAINING CLASSIFICATION MODELS ===")
    
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.svm import SVC
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    from sklearn.metrics import confusion_matrix, classification_report
    
    # Define models to test
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'Support Vector Machine': SVC(kernel='rbf', random_state=42),
        'Neural Network': MLPClassifier(hidden_layer_sizes=(100, 50), random_state=42, max_iter=1000)
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        # Train model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        # Calculate metrics
        train_accuracy = accuracy_score(y_train, y_pred_train)
        test_accuracy = accuracy_score(y_test, y_pred_test)
        test_precision = precision_score(y_test, y_pred_test, average='weighted')
        test_recall = recall_score(y_test, y_pred_test, average='weighted')
        test_f1 = f1_score(y_test, y_pred_test, average='weighted')
        
        # Cross-validation score
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        cv_mean = cv_scores.mean()
        cv_std = cv_scores.std()
        
        # Store results
        results[name] = {
            'model': model,
            'train_accuracy': train_accuracy,
            'test_accuracy': test_accuracy,
            'test_precision': test_precision,
            'test_recall': test_recall,
            'test_f1': test_f1,
            'cv_mean': cv_mean,
            'cv_std': cv_std,
            'y_pred_test': y_pred_test,
            'confusion_matrix': confusion_matrix(y_test, y_pred_test)
        }
        
        print(f"  Train Accuracy: {train_accuracy:.3f}")
        print(f"  Test Accuracy: {test_accuracy:.3f}")
        print(f"  Test F1-Score: {test_f1:.3f}")
        print(f"  CV Accuracy: {cv_mean:.3f} ± {cv_std:.3f}")
    
    return results

def evaluate_classification_performance(results, y_test):
    """Evaluate and visualize classification performance"""
    
    print("\n=== CLASSIFICATION PERFORMANCE EVALUATION ===")
    
    # Create performance comparison
    performance_data = []
    for name, result in results.items():
        performance_data.append({
            'Model': name,
            'Test Accuracy': result['test_accuracy'],
            'Test Precision': result['test_precision'],
            'Test Recall': result['test_recall'],
            'Test F1-Score': result['test_f1'],
            'CV Accuracy': result['cv_mean'],
            'CV Std': result['cv_std']
        })
    
    performance_df = pd.DataFrame(performance_data)
    performance_df = performance_df.sort_values('Test Accuracy', ascending=False)
    
    print("\nPerformance Comparison:")
    print(performance_df.round(3))
    
    # Create visualizations
    create_classification_performance_plots(results, y_test)
    
    return performance_df

def create_classification_performance_plots(results, y_test):
    """Create visualizations for classification performance"""
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Accuracy comparison
    models = list(results.keys())
    test_accuracies = [results[model]['test_accuracy'] for model in models]
    
    bars = axes[0,0].bar(models, test_accuracies, color='lightblue', edgecolor='navy')
    axes[0,0].set_title('Test Accuracy Comparison')
    axes[0,0].set_ylabel('Accuracy')
    axes[0,0].tick_params(axis='x', rotation=45)
    axes[0,0].set_ylim(0, 1)
    
    # Add value labels on bars
    for bar, accuracy in zip(bars, test_accuracies):
        height = bar.get_height()
        axes[0,0].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{accuracy:.3f}', ha='center', va='bottom')
    
    # F1-Score comparison
    test_f1_scores = [results[model]['test_f1'] for model in models]
    
    bars = axes[0,1].bar(models, test_f1_scores, color='lightgreen', edgecolor='darkgreen')
    axes[0,1].set_title('Test F1-Score Comparison')
    axes[0,1].set_ylabel('F1-Score')
    axes[0,1].tick_params(axis='x', rotation=45)
    axes[0,1].set_ylim(0, 1)
    
    # Add value labels on bars
    for bar, f1_score in zip(bars, test_f1_scores):
        height = bar.get_height()
        axes[0,1].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{f1_score:.3f}', ha='center', va='bottom')
    
    # Cross-validation comparison
    cv_means = [results[model]['cv_mean'] for model in models]
    cv_stds = [results[model]['cv_std'] for model in models]
    
    bars = axes[1,0].bar(models, cv_means, yerr=cv_stds, capsize=5, 
                         color='lightcoral', edgecolor='darkred')
    axes[1,0].set_title('Cross-Validation Accuracy')
    axes[1,0].set_ylabel('Accuracy')
    axes[1,0].tick_params(axis='x', rotation=45)
    axes[1,0].set_ylim(0, 1)
    
    # Add value labels on bars
    for bar, mean, std in zip(bars, cv_means, cv_stds):
        height = bar.get_height()
        axes[1,0].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{mean:.3f}±{std:.3f}', ha='center', va='bottom')
    
    # Confusion matrix for best model
    best_model = max(results.keys(), key=lambda x: results[x]['test_accuracy'])
    cm = results[best_model]['confusion_matrix']
    
    # Get unique classes for labels
    unique_classes = sorted(y_test.unique())
    
    im = axes[1,1].imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    axes[1,1].set_title(f'Confusion Matrix: {best_model}')
    axes[1,1].set_xlabel('Predicted Label')
    axes[1,1].set_ylabel('True Label')
    
    # Add text annotations
    thresh = cm.max() / 2
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            axes[1,1].text(j, i, format(cm[i, j], 'd'),
                          ha="center", va="center",
                          color="white" if cm[i, j] > thresh else "black")
    
    # Set tick labels
    axes[1,1].set_xticks(range(len(unique_classes)))
    axes[1,1].set_yticks(range(len(unique_classes)))
    axes[1,1].set_xticklabels(unique_classes)
    axes[1,1].set_yticklabels(unique_classes)
    
    plt.tight_layout()
    plt.show()

# Run the classification example
def run_classification_example():
    """Run complete classification example"""
    
    print("=== MATERIAL CLASSIFICATION EXAMPLE ===")
    
    # Create dataset
    df = create_classification_dataset(300)
    
    # Prepare data for ML
    X_train, X_test, y_train, y_test, feature_names = prepare_classification_data(df)
    
    # Train models
    results = train_classification_models(X_train, X_test, y_train, y_test, feature_names)
    
    # Evaluate performance
    performance_df = evaluate_classification_performance(results, y_test)
    
    return df, results, performance_df

# Run the example
if __name__ == "__main__":
    df, results, performance_df = run_classification_example()
```

### Week 12 Assignment: Complete Classification System

**Due**: End of Week 12  
**Points**: 15 points  
**Deliverables**:
1. **Complete classification system** with multiple algorithms
2. **Performance evaluation** using multiple metrics
3. **Confusion matrix visualization** and interpretation
4. **AI integration** for model selection and tuning
5. **Comprehensive documentation** of the classification workflow

**Code Requirements**:
- Clean classification model implementation
- Comprehensive performance evaluation
- Professional visualizations
- Error handling and validation
- Clear documentation

**Analysis Requirements**:
- Implement 5+ classification algorithms
- Evaluate using accuracy, precision, recall, F1-score
- Include cross-validation analysis
- Generate confusion matrices
- Provide model selection guidance

---

## Key Concepts Summary

### Machine Learning Fundamentals
- **Supervised Learning**: Learn from labeled data (regression, classification)
- **Model Selection**: Choose appropriate algorithms for your problem
- **Performance Evaluation**: Use appropriate metrics for your task
- **Cross-Validation**: Ensure robust model evaluation

### Regression Applications
- **Property Prediction**: Predict mechanical, thermal, electrical properties
- **Algorithm Comparison**: Linear models, tree-based models, neural networks
- **Performance Metrics**: R², RMSE, MAE for regression evaluation
- **Feature Importance**: Understand which factors matter most

### Classification Applications
- **Material Classification**: Identify phases, defects, material types
- **Quality Assessment**: Pass/fail classification for quality control
- **Performance Metrics**: Accuracy, precision, recall, F1-score
- **Confusion Matrix**: Visualize classification performance

### AI-Assisted ML
- **Model Selection**: Use AI to choose appropriate algorithms
- **Hyperparameter Tuning**: AI helps optimize model parameters
- **Feature Engineering**: AI suggests relevant features
- **Interpretation**: AI helps understand model results

### Best Practices
- **Start Simple**: Begin with basic models before complex ones
- **Validate Properly**: Use cross-validation for robust evaluation
- **Interpret Results**: Understand what your models are learning
- **Document Everything**: Record your ML workflow and decisions
- **Use AI Wisely**: AI is a tool to enhance, not replace, your expertise

---

## Next Steps

In the next lesson, we'll work on the **2-week capstone project** that integrates all the concepts learned throughout the course.

**Remember**: Machine learning is a powerful tool for materials science, but it's most effective when combined with domain knowledge and proper experimental design.

---

## Resources and References

### Machine Learning
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Machine Learning Mastery](https://machinelearningmastery.com/)
- [Introduction to Statistical Learning](https://www.statlearning.com/)

### Materials Science ML
- [Machine Learning in Materials Science](https://www.nature.com/articles/s41524-020-00387-3)
- [AI for Materials Discovery](https://www.science.org/doi/10.1126/science.aan8287)
- [ML Applications in Materials](https://www.sciencedirect.com/science/article/pii/S0927025618303127)

### AI Integration
- [AI for Model Selection](https://www.kaggle.com/code/andresionek/automl-tutorial)
- [Hyperparameter Optimization](https://optuna.org/)
- [Feature Engineering with AI](https://www.featuretools.com/)

---

**Happy machine learning!** 🚀


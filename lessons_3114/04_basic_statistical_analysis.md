# Lesson 4: Basic Statistical Analysis with AI Assistance
## Making Sense of Materials Science Data

**Duration**: 2 weeks (Weeks 7-8)  
**Weekly Workload**: 3-4 hours  
**Learning Focus**: Statistical analysis fundamentals and AI-assisted interpretation

---

## Learning Objectives

By the end of this lesson, you will be able to:
- **Select appropriate statistical tests** for materials science data
- **Perform basic hypothesis testing** with proper validation
- **Use AI assistance** for statistical interpretation
- **Generate automated reports** for analysis results
- **Validate statistical assumptions** and handle violations

---

## Week 7: Statistical Analysis Fundamentals

### Introduction to Statistical Analysis in Materials Science

Statistical analysis is essential for making sense of experimental data and drawing reliable conclusions. In materials science, we often need to:
- Compare properties between different materials
- Analyze the effect of processing parameters
- Validate experimental results
- Make predictions about material behavior

### Key Statistical Concepts

#### 1. Descriptive Statistics
- **Central Tendency**: Mean, median, mode
- **Variability**: Standard deviation, variance, range
- **Distribution Shape**: Skewness, kurtosis

#### 2. Inferential Statistics
- **Hypothesis Testing**: Comparing groups or conditions
- **Confidence Intervals**: Estimating population parameters
- **Effect Size**: Practical significance of differences

#### 3. Assumptions and Violations
- **Normality**: Data follows normal distribution
- **Independence**: Observations are independent
- **Homogeneity**: Groups have similar variances

### Statistical Test Selection Framework

Let's create a decision tree for choosing the right statistical test:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu
from scipy.stats import f_oneway, kruskal, pearsonr, spearmanr
import warnings
warnings.filterwarnings('ignore')

def statistical_test_selector(data, group_col=None, value_col=None, test_type='comparison'):
    """
    AI-assisted statistical test selection for materials science data
    
    Parameters:
    data: DataFrame with your data
    group_col: Column name for grouping (if applicable)
    value_col: Column name for values to analyze
    test_type: 'comparison', 'correlation', or 'distribution'
    """
    
    print("=== STATISTICAL TEST SELECTION ===")
    print(f"Data shape: {data.shape}")
    print(f"Test type: {test_type}")
    
    if test_type == 'comparison':
        return select_comparison_test(data, group_col, value_col)
    elif test_type == 'correlation':
        return select_correlation_test(data, value_col)
    elif test_type == 'distribution':
        return select_distribution_test(data, value_col)
    else:
        print("Invalid test type. Choose 'comparison', 'correlation', or 'distribution'")

def select_comparison_test(data, group_col, value_col):
    """Select appropriate test for comparing groups"""
    
    if group_col is None or value_col is None:
        print("Error: Need both group_col and value_col for comparison tests")
        return None
    
    # Get unique groups
    groups = data[group_col].unique()
    n_groups = len(groups)
    
    print(f"\nComparing {n_groups} groups for {value_col}")
    print(f"Groups: {groups}")
    
    # Check data for each group
    group_data = []
    for group in groups:
        group_values = data[data[group_col] == group][value_col].dropna()
        group_data.append(group_values)
        print(f"Group {group}: n={len(group_values)}, mean={group_values.mean():.2f}, std={group_values.std():.2f}")
    
    # Test assumptions
    normality_results = []
    for i, group in enumerate(groups):
        stat, p_value = shapiro(group_data[i])
        normality_results.append(p_value > 0.05)
        print(f"Group {group} normality (Shapiro-Wilk): p={p_value:.4f} {'✓' if p_value > 0.05 else '✗'}")
    
    # Test homogeneity of variance
    if n_groups == 2:
        stat, p_value = levene(group_data[0], group_data[1])
        homogeneity = p_value > 0.05
        print(f"Homogeneity of variance (Levene): p={p_value:.4f} {'✓' if homogeneity else '✗'}")
    else:
        # For more than 2 groups, use Bartlett's test
        stat, p_value = stats.bartlett(*group_data)
        homogeneity = p_value > 0.05
        print(f"Homogeneity of variance (Bartlett): p={p_value:.4f} {'✓' if homogeneity else '✗'}")
    
    # Recommend appropriate test
    print("\n=== TEST RECOMMENDATION ===")
    
    if n_groups == 2:
        if all(normality_results) and homogeneity:
            print("✓ RECOMMENDED: Independent t-test (parametric)")
            print("  - Both groups are normally distributed")
            print("  - Homogeneity of variance assumption met")
            return 'ttest_ind'
        else:
            print("✓ RECOMMENDED: Mann-Whitney U test (non-parametric)")
            print("  - Use when normality or homogeneity assumptions violated")
            return 'mannwhitneyu'
    
    elif n_groups > 2:
        if all(normality_results) and homogeneity:
            print("✓ RECOMMENDED: One-way ANOVA (parametric)")
            print("  - All groups are normally distributed")
            print("  - Homogeneity of variance assumption met")
            return 'anova'
        else:
            print("✓ RECOMMENDED: Kruskal-Wallis H test (non-parametric)")
            print("  - Use when normality or homogeneity assumptions violated")
            return 'kruskal'
    
    else:
        print("Error: Need at least 2 groups for comparison")
        return None

def select_correlation_test(data, value_cols):
    """Select appropriate test for correlation analysis"""
    
    if isinstance(value_cols, str):
        value_cols = [value_cols]
    
    print(f"\nAnalyzing correlations between: {value_cols}")
    
    # Check data types and distributions
    numeric_cols = data[value_cols].select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) < 2:
        print("Error: Need at least 2 numeric columns for correlation")
        return None
    
    # Test normality for each column
    normality_results = {}
    for col in numeric_cols:
        stat, p_value = shapiro(data[col].dropna())
        normality_results[col] = p_value > 0.05
        print(f"{col} normality: p={p_value:.4f} {'✓' if p_value > 0.05 else '✗'}")
    
    # Recommend test
    print("\n=== CORRELATION TEST RECOMMENDATION ===")
    
    if all(normality_results.values()):
        print("✓ RECOMMENDED: Pearson correlation (parametric)")
        print("  - All variables are normally distributed")
        print("  - Linear relationship assumed")
        return 'pearson'
    else:
        print("✓ RECOMMENDED: Spearman correlation (non-parametric)")
        print("  - Use when normality assumption violated")
        print("  - Monotonic relationship (not necessarily linear)")
        return 'spearman'

def select_distribution_test(data, value_col):
    """Select appropriate test for distribution analysis"""
    
    print(f"\nAnalyzing distribution of: {value_col}")
    
    # Check for normality
    stat, p_value = shapiro(data[value_col].dropna())
    normality = p_value > 0.05
    
    print(f"Normality test (Shapiro-Wilk): p={p_value:.4f} {'✓' if normality else '✗'}")
    
    # Recommend test
    print("\n=== DISTRIBUTION TEST RECOMMENDATION ===")
    
    if normality:
        print("✓ RECOMMENDED: Parametric tests (t-test, ANOVA)")
        print("  - Data follows normal distribution")
        print("  - Can use mean-based statistics")
    else:
        print("✓ RECOMMENDED: Non-parametric tests (Mann-Whitney, Kruskal-Wallis)")
        print("  - Data does not follow normal distribution")
        print("  - Use median-based statistics")
        print("  - Consider data transformation or larger sample size")
    
    return 'normality_check'
```

### AI-Assisted Statistical Analysis

Now let's use AI to help with statistical interpretation:

#### AI Prompt Template for Statistical Analysis
```
**Context**: I'm analyzing materials science data and need help with statistical interpretation
**Data**: [Describe your dataset and variables]
**Analysis**: [What statistical test you performed]
**Results**: [Report the test statistics and p-values]
**Questions**:
1. How should I interpret these results?
2. Are the assumptions met for this test?
3. What conclusions can I draw?
4. What additional analyses would be helpful?
5. How should I report these findings?

**Output**: Clear interpretation with practical recommendations
```

### Week 7 Assignment: Statistical Test Selection

**Due**: End of Week 7  
**Points**: 10 points  
**Deliverables**:
1. **Complete test selection framework** with decision tree logic
2. **AI interaction log** showing statistical analysis assistance
3. **Test recommendation system** for different data types
4. **Assumption checking functions** for normality and homogeneity
5. **Documentation** explaining the selection process

**Code Requirements**:
- Clean, modular functions for test selection
- Comprehensive assumption checking
- Clear recommendations with explanations
- Error handling and validation
- Professional documentation

**Analysis Requirements**:
- Implement test selection for 2+ groups
- Handle both parametric and non-parametric cases
- Check normality and homogeneity assumptions
- Provide clear recommendations with justification
- Include AI assistance integration

---

## Week 8: Hypothesis Testing and Automated Reporting

### Implementing Statistical Tests

Let's implement the recommended tests and create automated reporting:

```python
def perform_statistical_analysis(data, group_col, value_col, test_type='auto'):
    """
    Perform complete statistical analysis with automated reporting
    
    Parameters:
    data: DataFrame with your data
    group_col: Column name for grouping
    value_col: Column name for values to analyze
    test_type: 'auto' for automatic selection, or specific test name
    """
    
    print("=== COMPLETE STATISTICAL ANALYSIS ===")
    
    # Step 1: Data exploration
    print("\n1. DATA EXPLORATION")
    explore_data(data, group_col, value_col)
    
    # Step 2: Assumption checking
    print("\n2. ASSUMPTION CHECKING")
    assumptions = check_assumptions(data, group_col, value_col)
    
    # Step 3: Test selection (if auto)
    if test_type == 'auto':
        print("\n3. TEST SELECTION")
        test_type = select_comparison_test(data, group_col, value_col)
    
    # Step 4: Perform test
    print(f"\n4. PERFORMING {test_type.upper()} TEST")
    test_results = execute_test(data, group_col, value_col, test_type)
    
    # Step 5: Generate report
    print("\n5. GENERATING REPORT")
    report = generate_statistical_report(data, group_col, value_col, test_type, test_results, assumptions)
    
    return test_results, report

def explore_data(data, group_col, value_col):
    """Explore the data structure and basic statistics"""
    
    print(f"Dataset shape: {data.shape}")
    print(f"Missing values in {value_col}: {data[value_col].isnull().sum()}")
    
    # Group statistics
    groups = data[group_col].unique()
    print(f"\nGroups: {groups}")
    
    for group in groups:
        group_data = data[data[group_col] == group][value_col].dropna()
        print(f"\n{group}:")
        print(f"  Count: {len(group_data)}")
        print(f"  Mean: {group_data.mean():.3f}")
        print(f"  Median: {group_data.median():.3f}")
        print(f"  Std: {group_data.std():.3f}")
        print(f"  Min: {group_data.min():.3f}")
        print(f"  Max: {group_data.max():.3f}")
    
    # Visual exploration
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Box plot
    data.boxplot(column=value_col, by=group_col, ax=axes[0])
    axes[0].set_title(f'{value_col} by {group_col}')
    axes[0].set_xlabel(group_col)
    axes[0].set_ylabel(value_col)
    
    # Histogram
    for group in groups:
        group_data = data[data[group_col == group][value_col].dropna()
        axes[1].hist(group_data, alpha=0.7, label=group, bins=20)
    axes[1].set_title(f'{value_col} Distribution')
    axes[1].set_xlabel(value_col)
    axes[1].set_ylabel('Frequency')
    axes[1].legend()
    
    # Q-Q plot for normality
    for group in groups:
        group_data = data[data[group_col == group][value_col].dropna()
        stats.probplot(group_data, dist="norm", plot=axes[2])
        axes[2].set_title(f'Q-Q Plot for {group}')
    
    plt.tight_layout()
    plt.show()

def check_assumptions(data, group_col, value_col):
    """Check statistical assumptions"""
    
    assumptions = {}
    groups = data[group_col].unique()
    
    # Normality check
    normality_results = {}
    for group in groups:
        group_data = data[data[group_col == group][value_col].dropna()
        stat, p_value = shapiro(group_data)
        normality_results[group] = {
            'statistic': stat,
            'p_value': p_value,
            'is_normal': p_value > 0.05
        }
    
    assumptions['normality'] = normality_results
    
    # Homogeneity of variance check
    if len(groups) == 2:
        group_data_1 = data[data[group_col == groups[0]][value_col].dropna()
        group_data_2 = data[data[group_col == groups[1]][value_col].dropna()
        stat, p_value = levene(group_data_1, group_data_2)
        assumptions['homogeneity'] = {
            'statistic': stat,
            'p_value': p_value,
            'is_homogeneous': p_value > 0.05
        }
    else:
        # For more than 2 groups
        group_data_list = [data[data[group_col == group][value_col].dropna() for group in groups]
        stat, p_value = stats.bartlett(*group_data_list)
        assumptions['homogeneity'] = {
            'statistic': stat,
            'p_value': p_value,
            'is_homogeneous': p_value > 0.05
        }
    
    # Independence check (basic)
    assumptions['independence'] = {
        'note': 'Assuming experimental design ensures independence',
        'assumption_met': True
    }
    
    return assumptions

def execute_test(data, group_col, value_col, test_type):
    """Execute the selected statistical test"""
    
    groups = data[group_col].unique()
    
    if test_type == 'ttest_ind':
        # Independent t-test
        group_data_1 = data[data[group_col == groups[0]][value_col].dropna()
        group_data_2 = data[data[group_col == groups[1]][value_col].dropna()
        
        stat, p_value = ttest_ind(group_data_1, group_data_2)
        
        # Calculate effect size (Cohen's d)
        pooled_std = np.sqrt(((len(group_data_1) - 1) * group_data_1.var() + 
                             (len(group_data_2) - 1) * group_data_2.var()) / 
                            (len(group_data_1) + len(group_data_2) - 2))
        cohens_d = (group_data_1.mean() - group_data_2.mean()) / pooled_std
        
        return {
            'test_name': 'Independent t-test',
            'statistic': stat,
            'p_value': p_value,
            'effect_size': cohens_d,
            'groups': groups
        }
    
    elif test_type == 'mannwhitneyu':
        # Mann-Whitney U test
        group_data_1 = data[data[group_col == groups[0]][value_col].dropna()
        group_data_2 = data[data[group_col == groups[1]][value_col].dropna()
        
        stat, p_value = mannwhitneyu(group_data_1, group_data_2, alternative='two-sided')
        
        return {
            'test_name': 'Mann-Whitney U test',
            'statistic': stat,
            'p_value': p_value,
            'effect_size': 'Effect size not directly available for Mann-Whitney U',
            'groups': groups
        }
    
    elif test_type == 'anova':
        # One-way ANOVA
        group_data_list = [data[data[group_col == group][value_col].dropna() for group in groups]
        stat, p_value = f_oneway(*group_data_list)
        
        # Calculate effect size (eta-squared)
        # This is a simplified calculation
        total_ss = sum([(x - np.concatenate(group_data_list).mean())**2 for x in np.concatenate(group_data_list)])
        between_ss = sum([len(group_data) * (group_data.mean() - np.concatenate(group_data_list).mean())**2 
                         for group_data in group_data_list])
        eta_squared = between_ss / total_ss
        
        return {
            'test_name': 'One-way ANOVA',
            'statistic': stat,
            'p_value': p_value,
            'effect_size': eta_squared,
            'groups': groups
        }
    
    elif test_type == 'kruskal':
        # Kruskal-Wallis H test
        group_data_list = [data[data[group_col == group][value_col].dropna() for group in groups]
        stat, p_value = kruskal(*group_data_list)
        
        return {
            'test_name': 'Kruskal-Wallis H test',
            'statistic': stat,
            'p_value': p_value,
            'effect_size': 'Effect size not directly available for Kruskal-Wallis',
            'groups': groups
        }
    
    else:
        print(f"Test type {test_type} not implemented")
        return None

def generate_statistical_report(data, group_col, value_col, test_type, test_results, assumptions):
    """Generate comprehensive statistical report"""
    
    if test_results is None:
        return "Error: No test results available"
    
    report = f"""
# Statistical Analysis Report

## Analysis Summary
- **Variable Analyzed**: {value_col}
- **Grouping Variable**: {group_col}
- **Statistical Test**: {test_results['test_name']}
- **Number of Groups**: {len(test_results['groups'])}

## Data Description
"""
    
    # Add group statistics
    for group in test_results['groups']:
        group_data = data[data[group_col == group][value_col].dropna()
        report += f"""
### Group: {group}
- Sample Size: {len(group_data)}
- Mean: {group_data.mean():.3f}
- Standard Deviation: {group_data.std():.3f}
- Median: {group_data.median():.3f}
"""
    
    # Add test results
    report += f"""
## Test Results
- **Test Statistic**: {test_results['statistic']:.4f}
- **P-value**: {test_results['p_value']:.4f}
- **Significance Level**: α = 0.05
- **Statistical Decision**: {'Reject H₀' if test_results['p_value'] < 0.05 else 'Fail to reject H₀'}

## Effect Size
- **Effect Size**: {test_results['effect_size']}
"""
    
    # Add assumption check results
    report += """
## Assumption Check Results
"""
    
    for group in test_results['groups']:
        normality_result = assumptions['normality'][group]
        report += f"""
### {group} - Normality Check
- Shapiro-Wilk Statistic: {normality_result['statistic']:.4f}
- P-value: {normality_result['p_value']:.4f}
- Assumption Met: {'Yes' if normality_result['is_normal'] else 'No'}
"""
    
    homogeneity_result = assumptions['homogeneity']
    report += f"""
### Homogeneity of Variance
- Test Statistic: {homogeneity_result['statistic']:.4f}
- P-value: {homogeneity_result['p_value']:.4f}
- Assumption Met: {'Yes' if homogeneity_result['is_homogeneous'] else 'No'}
"""
    
    # Add interpretation
    report += f"""
## Interpretation
"""
    
    if test_results['p_value'] < 0.05:
        report += f"""
The {test_results['test_name']} shows a statistically significant difference 
between the groups (p = {test_results['p_value']:.4f} < 0.05).

**Practical Significance**: 
"""
        
        if 'effect_size' in test_results and isinstance(test_results['effect_size'], (int, float)):
            if test_results['test_name'] == 'Independent t-test':
                if abs(test_results['effect_size']) < 0.2:
                    report += "Effect size is small (|d| < 0.2)"
                elif abs(test_results['effect_size']) < 0.5:
                    report += "Effect size is medium (0.2 ≤ |d| < 0.5)"
                else:
                    report += "Effect size is large (|d| ≥ 0.5)"
            elif test_results['test_name'] == 'One-way ANOVA':
                if test_results['effect_size'] < 0.06:
                    report += "Effect size is small (η² < 0.06)"
                elif test_results['effect_size'] < 0.14:
                    report += "Effect size is medium (0.06 ≤ η² < 0.14)"
                else:
                    report += "Effect size is large (η² ≥ 0.14)"
        else:
            report += "Effect size interpretation not available for this test type."
    else:
        report += f"""
The {test_results['test_name']} does not show a statistically significant difference 
between the groups (p = {test_results['p_value']:.4f} ≥ 0.05).

**Note**: This does not necessarily mean there is no difference. Consider:
- Sample size adequacy
- Effect size magnitude
- Practical significance
"""
    
    # Add recommendations
    report += """
## Recommendations

### For Reporting
1. Always report the test statistic, degrees of freedom, and p-value
2. Include effect size measures when available
3. State the significance level used (α = 0.05)
4. Report whether assumptions were met

### For Further Analysis
1. Consider post-hoc tests if ANOVA shows significant differences
2. Examine effect sizes for practical significance
3. Consider data transformation if assumptions are severely violated
4. Increase sample size if power analysis suggests insufficient power

### Limitations
1. Statistical significance does not guarantee practical significance
2. Small sample sizes may lead to Type II errors
3. Violation of assumptions may affect test validity
4. Correlation does not imply causation
"""
    
    return report

# Example usage
def run_complete_analysis_example():
    """Run a complete statistical analysis example"""
    
    # Generate sample materials science data
    np.random.seed(42)
    n_samples = 50
    
    # Create two groups with different properties
    group_a = np.random.normal(450, 30, n_samples)  # High-strength alloy
    group_b = np.random.normal(380, 25, n_samples)  # Standard alloy
    
    # Create DataFrame
    data = pd.DataFrame({
        'Alloy_Type': ['High_Strength'] * n_samples + ['Standard'] * n_samples,
        'Tensile_Strength_MPa': np.concatenate([group_a, group_b])
    })
    
    print("Sample Materials Science Data:")
    print(data.head())
    print(f"\nDataset shape: {data.shape}")
    
    # Run complete analysis
    test_results, report = perform_statistical_analysis(
        data, 'Alloy_Type', 'Tensile_Strength_MPa'
    )
    
    # Display results
    print("\n" + "="*50)
    print("FINAL REPORT")
    print("="*50)
    print(report)
    
    return test_results, report

# Run the example
if __name__ == "__main__":
    results, report = run_complete_analysis_example()
```

### Week 8 Assignment: Complete Statistical Analysis

**Due**: End of Week 8  
**Points**: 15 points  
**Deliverables**:
1. **Complete statistical analysis system** with all functions
2. **Automated report generation** with professional formatting
3. **Assumption checking** for normality and homogeneity
4. **Effect size calculations** for different test types
5. **AI integration** for statistical interpretation assistance

**Code Requirements**:
- Complete implementation of all statistical tests
- Professional report generation
- Comprehensive assumption checking
- Effect size calculations
- Error handling and validation

**Analysis Requirements**:
- Handle 2+ group comparisons
- Implement both parametric and non-parametric tests
- Generate publication-ready reports
- Include practical significance interpretation
- Provide clear recommendations

---

## Key Concepts Summary

### Statistical Test Selection
- **Parametric Tests**: Use when assumptions are met (t-test, ANOVA)
- **Non-parametric Tests**: Use when assumptions are violated (Mann-Whitney, Kruskal-Wallis)
- **Assumption Checking**: Always verify normality and homogeneity
- **Effect Size**: Consider practical significance, not just statistical significance

### AI-Assisted Analysis
- **Test Selection**: Use AI to help choose appropriate tests
- **Interpretation**: Get AI help with result interpretation
- **Reporting**: Use AI to generate clear, professional reports
- **Validation**: Always verify AI suggestions with domain knowledge

### Best Practices
- **Always check assumptions** before performing tests
- **Report effect sizes** along with p-values
- **Consider practical significance** beyond statistical significance
- **Document your analysis process** for reproducibility
- **Use AI as a tool** to enhance, not replace, your expertise

---

## Next Steps

In the next lesson, we'll learn about **basic experimental design principles** with AI assistance, including DOE (Design of Experiments) and simple parameter optimization.

**Remember**: Good statistical analysis is about more than just running tests - it's about understanding your data, choosing appropriate methods, and interpreting results in the context of your materials science problem.

---

## Resources and References

### Statistical Analysis
- [SciPy Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Statistical Tests in Python](https://python.land/python-data-science/statistical-tests)
- [Effect Size Guidelines](https://www.psychometrica.de/effect_size.html)

### Materials Science Statistics
- "Statistics for Materials Scientists" by Leonid V. Azaroff
- ASTM Standards for Statistical Analysis
- Journal of Materials Science: Statistical methods in materials research

### AI Integration
- [OpenAI Statistical Analysis Prompts](https://platform.openai.com/docs/guides/prompt-engineering)
- [Statistical Interpretation with AI](https://www.statology.org/)

---

**Happy statistical analysis!** 🚀


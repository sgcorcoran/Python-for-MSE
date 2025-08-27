# MSE 3114: AI-Enhanced Statistical Analysis

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

* **Use AI to select and interpret appropriate statistical tests** for materials science data
* **Generate automated statistical reports** with AI assistance while maintaining human oversight
* **Apply AI-enhanced hypothesis testing** to mechanical testing data with multiple variables
* **Create AI-augmented statistical analysis workflows** that are reproducible and professional
* **Critically evaluate AI-generated statistical insights** and identify potential biases or errors
* **Integrate AI tools with traditional statistical software** for comprehensive analysis

---

## 🚀 The AI-Statistical Analysis Revolution

### Beyond Traditional Statistical Software

Traditional statistical analysis in materials science often follows a rigid, step-by-step approach. AI tools can revolutionize this by:

**Traditional Approach:**
- Manual test selection based on textbook rules
- Fixed analysis workflows
- Static reporting templates
- Limited interpretation assistance

**AI-Enhanced Approach:**
- Dynamic test selection based on data characteristics
- Adaptive analysis workflows
- Intelligent interpretation suggestions
- Continuous learning and improvement

> **🤔 Think About This**
> 
> **Consider your current statistical analysis workflow:**
> - How do you decide which statistical tests to use?
> - What happens when your data doesn't meet test assumptions?
> - How do you interpret complex statistical results?
> - Where could AI assistance be most valuable?

### The AI-Statistics Partnership

**AI Strengths in Statistics:**
- **Pattern Recognition**: Identifying data distributions and relationships
- **Test Selection**: Recommending appropriate statistical methods
- **Assumption Checking**: Automatically verifying test requirements
- **Interpretation**: Explaining results in plain language
- **Visualization**: Suggesting appropriate plots and charts

**Human Strengths in Statistics:**
- **Domain Knowledge**: Understanding materials science context
- **Critical Thinking**: Evaluating AI suggestions and results
- **Experimental Design**: Planning studies and sample sizes
- **Ethical Considerations**: Ensuring appropriate use of statistical methods

---

## 🧪 AI-Assisted Statistical Test Selection

### The Test Selection Framework

Effective statistical analysis requires choosing the right test for your data and research question. AI can help by:

1. **Data Characterization**: Understanding your data structure and properties
2. **Assumption Checking**: Verifying test requirements
3. **Test Recommendation**: Suggesting appropriate statistical methods
4. **Alternative Suggestions**: Providing backup options when assumptions fail

### Case Study: Mechanical Testing Data Analysis

Let's work through a real example. You're analyzing the effect of heat treatment temperature on the mechanical properties of aluminum 7075-T6.

**Step 1: Data Collection and Initial Exploration**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Generate realistic mechanical testing data
np.random.seed(42)
n_samples_per_temp = 20
temperatures = [200, 250, 300, 350, 400, 450, 500]

data = []
for temp in temperatures:
    # Base properties with temperature effects
    base_yield = 400 - 0.5 * temp + 0.001 * temp**2  # Quadratic relationship
    base_tensile = base_yield + 50 + np.random.normal(0, 10)
    base_elongation = 15 - 0.02 * temp + np.random.normal(0, 2)
    
    for _ in range(n_samples_per_temp):
        data.append({
            'temperature': temp,
            'yield_strength': base_yield + np.random.normal(0, 15),
            'tensile_strength': base_tensile + np.random.normal(0, 12),
            'elongation': max(0, base_elongation + np.random.normal(0, 1.5)),
            'hardness': 120 - 0.1 * temp + np.random.normal(0, 8)
        })

df = pd.DataFrame(data)

print("Dataset Overview:")
print(f"Shape: {df.shape}")
print(f"Temperature range: {df['temperature'].min()}°C - {df['temperature'].max()}°C")
print(f"Samples per temperature: {n_samples_per_temp}")

print("\nFirst few rows:")
print(df.head())

print("\nBasic statistics by temperature:")
print(df.groupby('temperature').agg({
    'yield_strength': ['mean', 'std', 'count'],
    'tensile_strength': ['mean', 'std', 'count'],
    'elongation': ['mean', 'std', 'count']
}).round(2))
```

**Step 2: AI-Assisted Data Characterization**

Now use AI to help understand your data and select appropriate statistical tests:

**IMPORTANT**: Upload your data file to your AI tool so it can analyze the actual data structure.

```
I'm analyzing the effect of heat treatment temperature on aluminum 7075-T6 mechanical properties. 
I've uploaded my data file so you can see the actual data.

**Research Question**: Does heat treatment temperature significantly affect yield strength, tensile strength, and elongation?

**Data Structure**:
- Independent variable: Temperature (7 levels: 200, 250, 300, 350, 400, 450, 500°C)
- Dependent variables: Yield strength, tensile strength, elongation, hardness
- Sample size: 20 samples per temperature level
- Total samples: 140

**Questions for AI**:
1. What type of statistical analysis is most appropriate for this data?
2. How should I check if the data meets test assumptions?
3. What if the assumptions are violated?
4. How should I handle multiple dependent variables?
5. What post-hoc tests would be appropriate?

Please examine the uploaded data and provide specific recommendations with reasoning.
```

**Step 3: Implementing AI-Recommended Analysis**

Based on AI suggestions, let's implement a comprehensive statistical analysis:

```python
# Data visualization for assumption checking
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Plot 1: Yield strength by temperature
axes[0,0].boxplot([df[df['temperature'] == temp]['yield_strength'] for temp in temperatures], 
                   labels=temperatures)
axes[0,0].set_xlabel('Temperature (°C)')
axes[0,0].set_ylabel('Yield Strength (MPa)')
axes[0,0].set_title('Yield Strength Distribution by Temperature')

# Plot 2: Tensile strength by temperature
axes[0,1].boxplot([df[df['temperature'] == temp]['tensile_strength'] for temp in temperatures], 
                   labels=temperatures)
axes[0,1].set_xlabel('Temperature (°C)')
axes[0,1].set_ylabel('Tensile Strength (MPa)')
axes[0,1].set_title('Tensile Strength Distribution by Temperature')

# Plot 3: Elongation by temperature
axes[0,2].boxplot([df[df['temperature'] == temp]['elongation'] for temp in temperatures], 
                   labels=temperatures)
axes[0,2].set_xlabel('Temperature (°C)')
axes[0,2].set_ylabel('Elongation (%)')
axes[0,2].set_title('Elongation Distribution by Temperature')

# Plot 4: Normality check for yield strength
from scipy.stats import probplot
probplot(df['yield_strength'], dist="norm", plot=axes[1,0])
axes[1,0].set_title('Q-Q Plot: Yield Strength')

# Plot 5: Normality check for tensile strength
probplot(df['tensile_strength'], dist="norm", plot=axes[1,1])
axes[1,1].set_title('Q-Q Plot: Tensile Strength')

# Plot 6: Normality check for elongation
probplot(df['elongation'], dist="norm", plot=axes[1,2])
axes[1,2].set_title('Q-Q Plot: Elongation')

plt.tight_layout()
plt.show()

# Statistical assumption checking
print("=== Statistical Assumption Checking ===")

# Normality tests
print("\nNormality Tests (Shapiro-Wilk):")
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    stat, p_value = stats.shapiro(df[prop])
    print(f"{prop}: W={stat:.3f}, p={p_value:.4f}")

# Homogeneity of variance (Levene's test)
print("\nHomogeneity of Variance (Levene's test):")
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    groups = [df[df['temperature'] == temp][prop].values for temp in temperatures]
    stat, p_value = stats.levene(*groups)
    print(f"{prop}: F={stat:.3f}, p={p_value:.4f}")

# Correlation analysis
print("\nCorrelation Analysis:")
correlation_matrix = df[['temperature', 'yield_strength', 'tensile_strength', 'elongation', 'hardness']].corr()
print(correlation_matrix.round(3))
```

**Self-Check**: What do these plots and tests tell you about your data? Do they support the use of parametric tests?

---

## 📊 AI-Enhanced Hypothesis Testing

### One-Way ANOVA with AI Assistance

Based on AI recommendations, let's perform comprehensive hypothesis testing:

```python
# One-way ANOVA for each mechanical property
print("=== One-Way ANOVA Results ===")

anova_results = {}
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    print(f"\n--- {prop.replace('_', ' ').title()} ---")
    
    # Prepare data for ANOVA
    groups = [df[df['temperature'] == temp][prop].values for temp in temperatures]
    
    # Perform ANOVA
    f_stat, p_value = stats.f_oneway(*groups)
    
    # Calculate effect size (eta-squared)
    ss_between = sum(len(group) * ((group.mean() - df[prop].mean())**2) for group in groups)
    ss_total = sum((val - df[prop].mean())**2 for val in df[prop])
    eta_squared = ss_between / ss_total
    
    print(f"F-statistic: {f_stat:.3f}")
    print(f"p-value: {p_value:.6f}")
    print(f"Effect size (η²): {eta_squared:.3f}")
    
    # Interpret results
    if p_value < 0.001:
        significance = "***"
    elif p_value < 0.01:
        significance = "**"
    elif p_value < 0.05:
        significance = "*"
    else:
        significance = "ns"
    
    print(f"Significance: {significance}")
    
    # Store results
    anova_results[prop] = {
        'f_stat': f_stat,
        'p_value': p_value,
        'eta_squared': eta_squared,
        'significant': p_value < 0.05
    }
    
    # Post-hoc analysis if significant
    if p_value < 0.05:
        print("Post-hoc analysis (Tukey's HSD):")
        from statsmodels.stats.multicomp import pairwise_tukeyhsd
        
        # Perform Tukey's test
        tukey = pairwise_tukeyhsd(df[prop], df['temperature'])
        print(tukey)
        
        # Store significant differences
        significant_pairs = []
        for i, row in enumerate(tukey.pvalues):
            if row < 0.05:
                group1 = tukey.groupsunique[tukey.pvalues < 0.05][i]
                group2 = tukey.groupsunique[tukey.pvalues < 0.05][i]
                significant_pairs.append((group1, group2))
        
        print(f"Significant temperature differences: {significant_pairs}")
```

### AI-Assisted Result Interpretation

Now use AI to help interpret these complex statistical results:

```
I've performed one-way ANOVA on my mechanical testing data. Here are the results:

**Yield Strength**:
- F-statistic: [X]
- p-value: [X]
- Effect size (η²): [X]
- Significant: [Yes/No]

**Tensile Strength**:
- F-statistic: [X]
- p-value: [X]
- Effect size (η²): [X]
- Significant: [Yes/No]

**Elongation**:
- F-statistic: [X]
- p-value: [X]
- Effect size (η²): [X]
- Significant: [Yes/No]

**Post-hoc Results**: [Summarize significant temperature differences]

**Questions for AI**:
1. How should I interpret these F-statistics and p-values?
2. What does the effect size tell me about practical significance?
3. How do I explain these results to non-statisticians?
4. What are the materials science implications?
5. What additional analyses would be helpful?

Please provide clear, practical interpretation of these results.
```

---

## 📈 AI-Generated Statistical Reports

### Automated Report Generation

AI can help create comprehensive statistical reports. Here's how to structure the process:

**Step 1: AI Report Generation Prompt**

```
I need to write a professional statistical analysis report for my materials science research. 
Please help me create a comprehensive report based on my analysis results.

**Research Context**: Effect of heat treatment temperature on Al 7075-T6 mechanical properties

**Statistical Results**: [Paste your ANOVA results here]

**Data Summary**: [Include sample sizes, temperature ranges, etc.]

**Requirements**:
1. Executive summary suitable for engineering management
2. Technical statistical analysis section
3. Materials science interpretation
4. Practical implications and recommendations
5. Professional formatting with clear sections

**Target Audience**: Materials engineers, researchers, and management

Please generate a complete report that I can review and refine.
```

**Step 2: Human Review and Refinement**

```python
# Create a comprehensive results summary
print("=== Comprehensive Statistical Analysis Summary ===")

# Overall significance assessment
significant_properties = [prop for prop, results in anova_results.items() if results['significant']]
print(f"Properties significantly affected by temperature: {len(significant_properties)} out of 3")

# Effect size interpretation
print("\nEffect Size Interpretation:")
for prop, results in anova_results.items():
    eta_sq = results['eta_squared']
    if eta_sq < 0.01:
        effect_size = "negligible"
    elif eta_sq < 0.06:
        effect_size = "small"
    elif eta_sq < 0.14:
        effect_size = "medium"
    else:
        effect_size = "large"
    
    print(f"{prop}: η² = {eta_sq:.3f} ({effect_size} effect)")

# Practical significance assessment
print("\nPractical Significance Assessment:")
for prop in significant_properties:
    # Calculate practical difference (max - min)
    max_val = df.groupby('temperature')[prop].mean().max()
    min_val = df.groupby('temperature')[prop].mean().min()
    practical_diff = max_val - min_val
    
    print(f"{prop}: Maximum difference = {practical_diff:.1f} units")
    
    # Assess if difference is practically meaningful
    if prop == 'yield_strength':
        threshold = 50  # MPa
    elif prop == 'tensile_strength':
        threshold = 60  # MPa
    else:  # elongation
        threshold = 5   # %
    
    if practical_diff > threshold:
        print(f"  → Practically significant (> {threshold} units)")
    else:
        print(f"  → May not be practically significant")

# Temperature optimization recommendations
print("\nTemperature Optimization Recommendations:")
for prop in significant_properties:
    # Find optimal temperature
    temp_means = df.groupby('temperature')[prop].mean()
    if prop in ['yield_strength', 'tensile_strength']:
        optimal_temp = temp_means.idxmax()
        direction = "maximize"
    else:  # elongation
        optimal_temp = temp_means.idxmin()
        direction = "minimize"
    
    print(f"{prop}: Optimal temperature = {optimal_temp}°C to {direction}")
```

**Step 3: AI-Enhanced Visualization**

```python
# Create publication-ready visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Main effects plot
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    temp_means = df.groupby('temperature')[prop].mean()
    temp_stds = df.groupby('temperature')[prop].std()
    
    if prop == 'elongation':
        axes[0,0].errorbar(temperatures, temp_means, yerr=temp_stds, 
                           marker='o', label=prop.replace('_', ' ').title(), capsize=5)
    else:
        axes[0,0].errorbar(temperatures, temp_means, yerr=temp_stds, 
                           marker='s', label=prop.replace('_', ' ').title(), capsize=5)

axes[0,0].set_xlabel('Temperature (°C)')
axes[0,0].set_ylabel('Property Value')
axes[0,0].set_title('Effect of Temperature on Mechanical Properties')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# Plot 2: Statistical significance visualization
significant_matrix = np.zeros((len(temperatures), len(temperatures)))
for i, temp1 in enumerate(temperatures):
    for j, temp2 in enumerate(temperatures):
        if i != j:
            # Check if difference is significant (simplified)
            prop = 'yield_strength'  # Use one property for visualization
            group1 = df[df['temperature'] == temp1][prop]
            group2 = df[df['temperature'] == temp2][prop]
            _, p_val = stats.ttest_ind(group1, group2)
            significant_matrix[i, j] = 1 if p_val < 0.05 else 0

im = axes[0,1].imshow(significant_matrix, cmap='RdYlBu_r', aspect='auto')
axes[0,1].set_xticks(range(len(temperatures)))
axes[0,1].set_yticks(range(len(temperatures)))
axes[0,1].set_xticklabels(temperatures)
axes[0,1].set_yticklabels(temperatures)
axes[0,1].set_xlabel('Temperature (°C)')
axes[0,1].set_ylabel('Temperature (°C)')
axes[0,1].set_title('Statistical Significance Matrix\n(Red = Significant Difference)')
plt.colorbar(im, ax=axes[0,1], label='Significant Difference')

# Plot 3: Effect size comparison
effect_sizes = [anova_results[prop]['eta_squared'] for prop in ['yield_strength', 'tensile_strength', 'elongation']]
properties = ['Yield Strength', 'Tensile Strength', 'Elongation']
colors = ['red' if results['significant'] else 'gray' for results in anova_results.values()]

bars = axes[1,0].bar(properties, effect_sizes, color=colors, alpha=0.7)
axes[1,0].set_ylabel('Effect Size (η²)')
axes[1,0].set_title('Effect Size Comparison')
axes[1,0].set_ylim(0, max(effect_sizes) * 1.2)

# Add significance indicators
for i, (bar, results) in enumerate(zip(bars, anova_results.values())):
    if results['significant']:
        axes[1,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                       '*', ha='center', va='bottom', fontsize=16)

# Plot 4: Residual analysis
from scipy.stats import shapiro
residuals = []
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    for temp in temperatures:
        group_data = df[df['temperature'] == temp][prop]
        group_mean = group_data.mean()
        group_residuals = group_data - group_mean
        residuals.extend(group_residuals)

axes[1,1].hist(residuals, bins=30, alpha=0.7, edgecolor='black')
axes[1,1].set_xlabel('Residuals')
axes[1,1].set_ylabel('Frequency')
axes[1,1].set_title('Residual Distribution')

# Add normality test result
_, p_val = shapiro(residuals)
axes[1,1].text(0.05, 0.95, f'Shapiro-Wilk p = {p_val:.4f}', 
                transform=axes[1,1].transAxes, bbox=dict(boxstyle="round", facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()
```

---

## 🔍 AI-Assisted Assumption Checking

### Advanced Diagnostic Techniques

AI can help identify when traditional parametric tests are inappropriate:

```python
# Comprehensive assumption checking
print("=== Advanced Assumption Checking ===")

# 1. Normality by group
print("\n1. Normality by Temperature Group:")
for temp in temperatures:
    print(f"\nTemperature {temp}°C:")
    for prop in ['yield_strength', 'tensile_strength', 'elongation']:
        group_data = df[df['temperature'] == temp][prop]
        stat, p_val = shapiro(group_data)
        print(f"  {prop}: W={stat:.3f}, p={p_val:.4f}")

# 2. Homogeneity of variance (multiple tests)
print("\n2. Homogeneity of Variance Tests:")
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    groups = [df[df['temperature'] == temp][prop].values for temp in temperatures]
    
    # Levene's test
    levene_stat, levene_p = stats.levene(*groups)
    
    # Bartlett's test
    bartlett_stat, bartlett_p = stats.bartlett(*groups)
    
    # Fligner-Killeen test (more robust)
    fligner_stat, fligner_p = stats.fligner(*groups)
    
    print(f"\n{prop}:")
    print(f"  Levene: F={levene_stat:.3f}, p={levene_p:.4f}")
    print(f"  Bartlett: χ²={bartlett_stat:.3f}, p={bartlett_p:.4f}")
    print(f"  Fligner-Killeen: χ²={fligner_stat:.3f}, p={fligner_p:.4f}")

# 3. Outlier detection
print("\n3. Outlier Detection:")
from scipy.stats import zscore

for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    z_scores = np.abs(zscore(df[prop]))
    outliers = df[z_scores > 3]
    
    if len(outliers) > 0:
        print(f"\n{prop}: {len(outliers)} outliers detected")
        print("Outlier details:")
        for _, row in outliers.iterrows():
            print(f"  Temp: {row['temperature']}°C, {prop}: {row[prop]:.2f}")
    else:
        print(f"\n{prop}: No outliers detected")

# 4. Non-parametric alternatives
print("\n4. Non-parametric Alternative Analysis:")
for prop in ['yield_strength', 'tensile_strength', 'elongation']:
    groups = [df[df['temperature'] == temp][prop].values for temp in temperatures]
    
    # Kruskal-Wallis test
    h_stat, kw_p = stats.kruskal(*groups)
    
    print(f"\n{prop} - Kruskal-Wallis test:")
    print(f"  H-statistic: {h_stat:.3f}")
    print(f"  p-value: {kw_p:.6f}")
    
    # Compare with parametric results
    anova_p = anova_results[prop]['p_value']
    print(f"  ANOVA p-value: {anova_p:.6f}")
    print(f"  Agreement: {'Yes' if (kw_p < 0.05) == (anova_p < 0.05) else 'No'}")
```

### AI-Assisted Assumption Violation Handling

When assumptions are violated, AI can suggest appropriate alternatives:

```
My statistical analysis revealed several assumption violations:

**Normality Issues**: [Describe specific problems]
**Variance Issues**: [Describe specific problems]
**Outlier Issues**: [Describe specific problems]

**Questions for AI**:
1. What non-parametric alternatives should I use?
2. How should I handle the outliers?
3. Can I transform the data to meet assumptions?
4. What are the trade-offs between different approaches?
5. How do I report these violations in my paper?

Please provide specific recommendations for handling these assumption violations.
```

---

## 🎯 Interactive Self-Check

### Concept Check 1: Statistical Test Selection

**Question**: Your AI tool recommends a t-test for comparing 5 temperature groups. What should you do?

A) Use the t-test as recommended - AI is always right
B) Use ANOVA since you have more than 2 groups
C) Ask AI to explain why it chose a t-test
D) Use non-parametric tests to be safe

**Answer**: C - Always understand AI recommendations before implementing

**Why**: AI can make errors in statistical reasoning. Understanding the logic ensures appropriate analysis.

### Concept Check 2: Assumption Violations

**Question**: Your data fails normality tests but ANOVA is robust to violations. What should you do?

A) Proceed with ANOVA anyway
B) Use non-parametric alternatives
C) Transform the data to meet assumptions
D) Report both approaches and compare results

**Answer**: D - Comprehensive analysis provides the most robust conclusions

**Why**: Multiple approaches give you confidence in your results and satisfy different reviewers' preferences.

### Concept Check 3: AI Report Generation

**Question**: AI generates a perfect statistical report. How should you use it?

A) Submit it directly as your work
B) Use it as a template and add your own insights
C) Cite the AI tool as a co-author
D) Rewrite it completely in your own words

**Answer**: B - Use AI as a starting point, not a replacement

**Why**: You must demonstrate understanding and add domain-specific insights that AI cannot provide.

---

## 🏁 Lesson Summary

### What You've Accomplished

✅ **Used AI to select and interpret statistical tests** for materials science data  
✅ **Generated comprehensive statistical reports** with AI assistance  
✅ **Applied AI-enhanced hypothesis testing** to mechanical testing data  
✅ **Created AI-augmented statistical workflows** that are reproducible  
✅ **Critically evaluated AI-generated insights** and identified potential issues  
✅ **Integrated AI tools with traditional statistical software**  

### Key Takeaways

1. **AI excels at test selection and assumption checking** - But understanding remains essential
2. **Multiple statistical approaches provide robustness** - Compare parametric and non-parametric results
3. **AI-generated reports need human refinement** - Add domain expertise and critical thinking
4. **Assumption violations require careful handling** - AI can suggest alternatives
5. **Reproducible workflows combine AI efficiency with human judgment**

### Next Steps

**Before the next lesson:**
- Apply AI-enhanced statistical analysis to your own research data
- Create a comprehensive statistical report using AI assistance
- Practice identifying and handling assumption violations
- Prepare questions about advanced statistical techniques

---

## 🔗 Additional Resources

### Statistical Analysis
- [SciPy Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Statsmodels Documentation](https://www.statsmodels.org/)
- [Materials Science Statistics](https://example.com) *(placeholder)*

### AI-Enhanced Statistics
- [ChatGPT for Statistical Analysis](https://example.com) *(placeholder)*
- [AI-Assisted Research Methods](https://example.com) *(placeholder)*
- [Statistical Assumption Checking](https://example.com) *(placeholder)*

### Advanced Topics
- [Mixed-Effects Models](https://www.statsmodels.org/stable/mixed_linear.html)
- [Non-parametric Methods](https://docs.scipy.org/doc/scipy/reference/stats.html#non-parametric-tests)
- [Effect Size Calculations](https://www.statsmodels.org/stable/stats.html#effect-size)

---

## 📝 Assignment: AI-Enhanced Statistical Analysis

**Due**: End of Week 4  
**Format**: Jupyter notebook with comprehensive analysis and report  
**Length**: 7-9 pages equivalent  

**Requirements**:
1. **Collect and analyze real materials science data** with AI assistance
2. **Perform comprehensive statistical testing** using AI-recommended methods
3. **Generate AI-assisted statistical report** with human refinement
4. **Handle assumption violations** appropriately with AI guidance
5. **Create publication-ready visualizations** and interpretations

**Grading Criteria**:
- Statistical analysis accuracy (25%)
- AI tool integration effectiveness (20%)
- Assumption handling and alternatives (20%)
- Report quality and interpretation (20%)
- Visualization and presentation (15%)

**Submission**: Upload your notebook to Canvas with working code, statistical analysis, and professional report.

---

*Remember: AI enhances your statistical capabilities, but your materials science expertise and critical thinking remain essential for meaningful analysis and interpretation.*

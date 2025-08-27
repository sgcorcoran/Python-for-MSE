# MSE 3114: AI as Your Research Assistant

---

## 🎯 Learning Objectives

After completing this lesson, you will be able to:

* **Master advanced prompt engineering** techniques specifically for materials science problems
* **Use AI to generate and test hypotheses** from materials characterization data
* **Create a comprehensive prompt library** for common materials analysis tasks
* **Integrate AI tools with GitHub Copilot** for enhanced coding workflows
* **Develop AI-augmented experimental design** strategies for materials research

---

## 🚀 The AI Research Assistant Paradigm

### Beyond Simple Q&A

AI tools are evolving from simple question-answer systems to **intelligent research collaborators**. The key is learning to communicate with AI in ways that leverage its strengths while maintaining your scientific judgment.

> **🤔 Think About This**
> 
> **Reflect on your research workflow:**
> - What tasks do you spend the most time on?
> - Which of these could benefit from AI assistance?
> - How do you currently validate your research findings?

### The AI-Human Research Partnership

**AI Strengths:**
- Rapid pattern recognition in large datasets
- Hypothesis generation from complex relationships
- Code generation and optimization
- Literature synthesis and summarization

**Human Strengths:**
- Domain expertise and intuition
- Critical evaluation of results
- Experimental design and validation
- Ethical and safety considerations

**The Sweet Spot**: AI generates possibilities, humans evaluate and refine

---

## 🎨 Advanced Prompt Engineering for Materials Science

### The Prompt Engineering Framework

Effective prompts follow a structured approach:

1. **Context Setting** - Establish the research domain and constraints
2. **Task Definition** - Clearly specify what you want AI to do
3. **Output Format** - Define the structure and style of responses
4. **Quality Criteria** - Specify accuracy and validation requirements
5. **Iteration Plan** - Plan for refining and improving results

### Prompt Template for Materials Analysis

```
**Context**: I'm a materials scientist analyzing [material type] data for [specific application].

**Data Description**: 
- Dataset: [brief description]
- Variables: [list key variables]
- Sample size: [number of samples]
- Measurement method: [how data was collected]

**Task**: Please help me [specific analysis goal]

**Requirements**:
- Explain your reasoning step-by-step
- Suggest validation approaches
- Identify potential limitations
- Recommend next steps

**Output Format**: [structured response format]
```

### Example: Microstructural Analysis Prompt

```
**Context**: I'm analyzing grain size distribution in aluminum 7075-T6 using optical microscopy.

**Data Description**: 
- Dataset: 50 grain size measurements from 3 different regions
- Variables: grain diameter (μm), region identifier, measurement method
- Sample size: 150 total measurements
- Measurement method: linear intercept method

**Task**: Help me determine if there are statistically significant differences in grain size between regions and suggest the best statistical approach.

**Requirements**:
- Explain why you chose specific statistical tests
- Suggest visualization methods
- Identify potential sources of error
- Recommend sample size for future studies

**Output Format**: 
1. Statistical approach with rationale
2. Step-by-step analysis plan
3. Expected outcomes and interpretation
4. Limitations and considerations
```

**Exercise**: Create a similar prompt for your current research area. Share with classmates and refine based on feedback.

---

## 🧪 AI-Assisted Hypothesis Generation

### The Hypothesis Generation Workflow

Traditional hypothesis generation relies heavily on literature review and intuition. AI can accelerate this process by:

1. **Pattern Recognition** - Identifying relationships in complex datasets
2. **Literature Synthesis** - Connecting findings across multiple studies
3. **Parameter Optimization** - Suggesting experimental conditions
4. **Risk Assessment** - Identifying potential failure modes

### Case Study: Alloy Composition Optimization

Let's work through a real example. You're developing a new high-strength aluminum alloy for aerospace applications.

**Step 1: Data Collection and AI Analysis**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import seaborn as sns

# Load alloy composition and properties data
# This would be your actual dataset
np.random.seed(42)
n_samples = 100

# Simulate alloy composition data (Al-Cu-Mg-Zn system)
data = {
    'Al_content': np.random.uniform(85, 95, n_samples),
    'Cu_content': np.random.uniform(1, 5, n_samples),
    'Mg_content': np.random.uniform(0.5, 3, n_samples),
    'Zn_content': np.random.uniform(0.1, 2, n_samples),
    'Heat_treatment_temp': np.random.uniform(400, 550, n_samples),
    'Aging_time': np.random.uniform(1, 24, n_samples)
}

# Simulate mechanical properties (simplified relationships)
data['Yield_Strength'] = (
    200 + 15 * data['Cu_content'] + 
    20 * data['Mg_content'] + 
    10 * data['Zn_content'] +
    0.1 * data['Heat_treatment_temp'] +
    2 * np.log(data['Aging_time']) +
    np.random.normal(0, 15, n_samples)
)

data['Tensile_Strength'] = data['Yield_Strength'] + 50 + np.random.normal(0, 10, n_samples)
data['Elongation'] = 15 - 0.5 * data['Cu_content'] - 0.3 * data['Mg_content'] + np.random.normal(0, 2, n_samples)

df = pd.DataFrame(data)

print("Dataset Overview:")
print(f"Shape: {df.shape}")
print("\nFirst few rows:")
print(df.head())

print("\nCorrelation with Yield Strength:")
correlations = df.corr()['Yield_Strength'].sort_values(ascending=False)
print(correlations)
```

**Step 2: AI-Assisted Pattern Recognition**

Now use AI to analyze this data and generate hypotheses:

```
I'm analyzing aluminum alloy composition data to optimize mechanical properties. Here's what I found:

**Data Summary:**
- 100 alloy samples with varying Al, Cu, Mg, Zn contents
- Heat treatment temperatures: 400-550°C
- Aging times: 1-24 hours
- Measured: Yield Strength, Tensile Strength, Elongation

**Key Correlations:**
- Cu content: strongest positive correlation with yield strength
- Mg content: second strongest positive correlation
- Heat treatment temperature: moderate positive effect
- Aging time: logarithmic relationship with yield strength

**Current Hypothesis**: Cu and Mg are the primary strengthening elements, with heat treatment temperature and aging time providing secondary strengthening through precipitation hardening.

**Questions for AI:**
1. What additional hypotheses should I test?
2. Are there any non-linear interactions I'm missing?
3. What experimental conditions would maximize strength while maintaining ductility?
4. How can I validate these relationships experimentally?

Please suggest specific experiments and statistical approaches to test these hypotheses.
```

**Step 3: Hypothesis Validation Planning**

Based on AI suggestions, create a validation plan:

```python
# Create visualization to test AI-generated hypotheses
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Cu vs Yield Strength
axes[0,0].scatter(df['Cu_content'], df['Yield_Strength'], alpha=0.7)
axes[0,0].set_xlabel('Cu Content (%)')
axes[0,0].set_ylabel('Yield Strength (MPa)')
axes[0,0].set_title('Cu Content vs Yield Strength')
axes[0,0].grid(True, alpha=0.3)

# Plot 2: Mg vs Yield Strength
axes[0,1].scatter(df['Mg_content'], df['Yield_Strength'], alpha=0.7)
axes[0,1].set_xlabel('Mg Content (%)')
axes[0,1].set_ylabel('Yield Strength (MPa)')
axes[0,1].set_title('Mg Content vs Yield Strength')
axes[0,1].grid(True, alpha=0.3)

# Plot 3: Heat Treatment Temperature vs Yield Strength
axes[1,0].scatter(df['Heat_treatment_temp'], df['Yield_Strength'], alpha=0.7)
axes[1,0].set_xlabel('Heat Treatment Temperature (°C)')
axes[1,0].set_ylabel('Yield Strength (MPa)')
axes[1,0].set_title('Heat Treatment Temperature vs Yield Strength')
axes[1,0].grid(True, alpha=0.3)

# Plot 4: Aging Time vs Yield Strength
axes[1,1].scatter(df['Aging_time'], df['Yield_Strength'], alpha=0.7)
axes[1,1].set_xlabel('Aging Time (hours)')
axes[1,1].set_ylabel('Yield Strength (MPa)')
axes[1,1].set_title('Aging Time vs Yield Strength')
axes[1,1].set_xscale('log')
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Test for interaction effects
print("\nTesting for interaction effects...")
df['Cu_Mg_interaction'] = df['Cu_content'] * df['Mg_content']
interaction_corr = df.corr()['Yield_Strength']['Cu_Mg_interaction']
print(f"Cu-Mg interaction correlation with Yield Strength: {interaction_corr:.3f}")
```

**Self-Check**: What patterns do you see in these plots? How do they support or contradict your initial hypotheses?

---

## 🔧 GitHub Copilot Integration

### Setting Up Copilot for Materials Science

GitHub Copilot can significantly accelerate your coding workflow when properly configured:

**Installation and Setup:**
1. Install GitHub Copilot extension in VS Code
2. Authenticate with your GitHub account
3. Configure language-specific settings for Python
4. Set up materials science context

**Materials Science Context Setup:**

```python
# Create a .copilot file in your project root
# This helps Copilot understand your domain

"""
Materials Science Research Project
Domain: Aluminum Alloy Development
Focus: Mechanical Properties Optimization
Key Libraries: pandas, numpy, matplotlib, scipy, scikit-learn
Data Types: Composition data, mechanical properties, microstructural parameters
Common Tasks: Statistical analysis, visualization, curve fitting, optimization
"""
```

### Copilot for Common Materials Science Tasks

**Task 1: Data Loading and Preprocessing**

```python
# Start typing and let Copilot complete:
def load_alloy_data(file_path):
    """
    Load and preprocess alloy composition and properties data
    
    Parameters:
    file_path (str): Path to the data file
    
    Returns:
    pd.DataFrame: Cleaned and preprocessed data
    """
    # Let Copilot suggest the implementation
    pass
```

**Task 2: Statistical Analysis**

```python
# Copilot can help with complex statistical operations:
def analyze_composition_effects(data, target_variable):
    """
    Analyze the effects of alloy composition on target mechanical property
    
    Parameters:
    data (pd.DataFrame): Alloy composition and properties data
    target_variable (str): Name of the target mechanical property
    
    Returns:
    dict: Statistical analysis results including correlations, p-values, etc.
    """
    # Let Copilot implement the analysis
    pass
```

**Task 3: Visualization Generation**

```python
# Copilot excels at creating publication-ready plots:
def create_composition_property_plots(data, property_name):
    """
    Create comprehensive plots showing composition-property relationships
    
    Parameters:
    data (pd.DataFrame): Alloy data
    property_name (str): Name of the mechanical property to plot
    
    Returns:
    matplotlib.figure.Figure: Multi-panel figure with all plots
    """
    # Let Copilot generate the visualization code
    pass
```

**Exercise**: Try using Copilot to complete one of these functions. How does it compare to writing code from scratch?

---

## 📚 Building Your Prompt Library

### The Prompt Library Structure

Your prompt library should be organized by research task type:

```
📁 Materials Science AI Prompt Library/
├── 📁 Data Analysis/
│   ├── 📄 statistical_analysis.md
│   ├── 📄 outlier_detection.md
│   └── 📄 correlation_analysis.md
├── 📁 Experimental Design/
│   ├── 📄 doe_planning.md
│   ├── 📄 sample_size_calculation.md
│   └── 📄 parameter_optimization.md
├── 📁 Literature Review/
│   ├── 📄 paper_synthesis.md
│   ├── 📄 gap_analysis.md
│   └── 📄 methodology_comparison.md
└── 📁 Report Writing/
    ├── 📄 executive_summary.md
    ├── 📄 technical_analysis.md
    └── 📄 conclusions_recommendations.md
```

### Example Prompt Library Entry

**File: `statistical_analysis.md`**

```markdown
# Statistical Analysis Prompts

## Basic Descriptive Statistics
**Use Case**: Initial data exploration and summary
**Prompt Template**:
```
I have [data_type] data with [n_samples] samples measuring [variables]. 
Please help me:
1. Calculate appropriate descriptive statistics
2. Identify any obvious outliers or data quality issues
3. Suggest visualization approaches
4. Recommend next steps for analysis

Data summary: [paste basic info here]
```

## Correlation Analysis
**Use Case**: Understanding relationships between variables
**Prompt Template**:
```
I'm analyzing correlations between [variable_list] in my [material_type] data.
Please help me:
1. Choose appropriate correlation methods (Pearson, Spearman, etc.)
2. Interpret correlation coefficients and significance
3. Identify potential confounding variables
4. Suggest visualization approaches

Data details: [paste relevant info here]
```

## Hypothesis Testing
**Use Case**: Testing specific research hypotheses
**Prompt Template**:
```
I want to test the hypothesis: [specific hypothesis]
My data includes: [data description]
Control group: [control description]
Treatment group: [treatment description]

Please help me:
1. Choose appropriate statistical tests
2. Set up null and alternative hypotheses
3. Interpret p-values and effect sizes
4. Address potential statistical issues
```
```

### Building Your Library

**Step 1: Identify Common Tasks**
- List the 10 most common analysis tasks in your research
- Group them by category (data analysis, experimental design, etc.)
- Prioritize by frequency and time investment

**Step 2: Create Prompt Templates**
- Start with the most common tasks
- Use the framework from earlier in this lesson
- Test and refine prompts with real data

**Step 3: Organize and Document**
- Use consistent formatting and structure
- Include examples of successful prompts
- Add notes on when and how to use each prompt

**Exercise**: Create your first prompt library entry for a common analysis task in your research area.

---

## 🎯 Interactive Self-Check

### Concept Check 1: Prompt Engineering

**Question**: You want AI to help analyze grain size data. Which prompt approach is most effective?

A) "Help me with grain size data"
B) "I have 50 grain size measurements from 3 regions of an aluminum sample. The data shows some variation. Can you help me understand if the differences are significant?"
C) "Analyze this grain size data and tell me everything about it"
D) "What's wrong with my grain size analysis?"

**Answer**: B - Specific, contextual, and actionable

**Why**: Vague prompts lead to generic responses. Specific prompts with context yield targeted, useful analysis.

### Concept Check 2: Hypothesis Generation

**Question**: AI suggests that increasing temperature will always increase material strength. What should you do?

A) Accept it immediately - AI is always right
B) Reject it completely - AI doesn't understand materials science
C) Evaluate it critically against known material behavior
D) Test it experimentally without further consideration

**Answer**: C - Critical evaluation is essential

**Why**: AI can suggest plausible but incorrect hypotheses. Your domain expertise is crucial for validation.

### Concept Check 3: Copilot Usage

**Question**: Copilot generates code that works but you don't understand. What should you do?

A) Use it as-is since it works
B) Ask Copilot to explain the code
C) Study the code until you understand it
D) Rewrite it from scratch

**Answer**: C - Understanding is essential for research integrity

**Why**: You must be able to explain and defend your analysis methods. Blind use of AI-generated code is not acceptable in research.

---

## 🏁 Lesson Summary

### What You've Accomplished

✅ **Mastered advanced prompt engineering** for materials science applications  
✅ **Used AI to generate and test research hypotheses** with real data  
✅ **Created a structured prompt library** for common research tasks  
✅ **Integrated GitHub Copilot** into your coding workflow  
✅ **Developed AI-augmented experimental design** strategies  

### Key Takeaways

1. **Effective prompting requires structure** - Context, task, format, quality, iteration
2. **AI excels at pattern recognition** - Use it to generate hypotheses, not replace judgment
3. **Prompt libraries save time** - Build reusable templates for common tasks
4. **Copilot accelerates coding** - But understanding remains essential
5. **Validation is critical** - Always verify AI suggestions against domain knowledge

### Next Steps

**Before the next lesson:**
- Complete your prompt library with at least 5 entries
- Practice using Copilot on a real analysis task
- Test AI hypothesis generation on your own data
- Prepare questions about advanced AI integration

---

## 🔗 Additional Resources

### Prompt Engineering
- [OpenAI Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Claude System Prompt Guide](https://docs.anthropic.com/claude/docs)
- [Prompt Engineering for Materials Science](https://example.com) *(placeholder)*

### GitHub Copilot
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Setup](https://code.visualstudio.com/docs/editor/github)
- [Copilot Best Practices](https://github.com/github/copilot-docs)

### Statistical Analysis
- [SciPy Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Pandas Statistical Methods](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [Materials Science Statistics](https://example.com) *(placeholder)*

---

## 📝 Assignment: Prompt Library and Hypothesis Testing

**Due**: End of Week 2  
**Format**: Jupyter notebook with embedded documentation  
**Length**: 5-7 pages equivalent  

**Requirements**:
1. Create a comprehensive prompt library (minimum 10 entries)
2. Use AI to generate and test hypotheses on real materials data
3. Document the AI-human collaboration process
4. Reflect on effectiveness and limitations
5. Include code examples and visualizations

**Grading Criteria**:
- Prompt library quality and organization (30%)
- Hypothesis generation and testing (25%)
- AI tool integration effectiveness (20%)
- Critical thinking and validation (15%)
- Professional presentation (10%)

**Submission**: Upload your notebook to Canvas with clear sections, working code, and professional formatting.

---

*Remember: AI is your research assistant, not your research director. You remain the expert who guides the research direction and validates the results.*

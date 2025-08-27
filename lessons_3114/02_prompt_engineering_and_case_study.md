# Lesson 2: Prompt Engineering and Alloy Optimization Case Study
## Mastering AI Communication for Materials Science

**Duration**: 2 weeks (Weeks 3-4)  
**Weekly Workload**: 3-4 hours  
**Learning Focus**: Effective AI communication and basic alloy optimization

---

## Learning Objectives

By the end of this lesson, you will be able to:
- **Design effective prompts** for AI materials science assistance
- **Apply prompt engineering** techniques to research problems
- **Use AI for hypothesis generation** in alloy optimization
- **Build a prompt library** for common materials science tasks
- **Evaluate AI responses** critically and iteratively

---

## Week 3: Prompt Engineering Fundamentals

### Introduction to Prompt Engineering

Prompt engineering is the art and science of communicating effectively with AI tools to get the best possible results. In materials science, this means learning how to ask AI tools the right questions to help with research planning, data analysis, and problem-solving.

### Why Prompt Engineering Matters

**Poor Prompt Example**:
```
"Help me with alloy analysis"
```

**Better Prompt Example**:
```
I'm analyzing aluminum-copper-magnesium alloys for aerospace applications. 
I have composition data and mechanical property measurements for 15 different alloys.
I need to identify which composition factors most strongly influence tensile strength.
Can you suggest a statistical approach and help me interpret the results?
```

The second prompt provides:
- **Context**: Specific application and material system
- **Data**: What you're working with
- **Goal**: Clear objective
- **Request**: Specific type of help needed

### Core Prompt Engineering Principles

#### 1. Context Setting
Always provide relevant background information:

```
**Context**: I'm a materials science student working on [specific problem]
**Application**: [Where/how this will be used]
**Constraints**: [Limitations or requirements]
**Current Knowledge**: [What you already understand]
```

#### 2. Task Definition
Be specific about what you want:

```
**Goal**: [What you want to achieve]
**Deliverable**: [What format/type of response you need]
**Scope**: [How detailed/comprehensive the response should be]
**Timeline**: [When you need this by]
```

#### 3. Output Format
Specify how you want the response structured:

```
**Please provide**:
1. Step-by-step methodology
2. Code examples in Python
3. Expected outcomes and limitations
4. References for further reading
```

#### 4. Quality Criteria
Define what makes a good response:

```
**Quality Requirements**:
- Use materials science terminology correctly
- Provide practical, implementable solutions
- Include error handling and validation steps
- Consider safety and practical constraints
```

### Building Your Prompt Library

Let's create a structured prompt library for common materials science tasks:

#### Template 1: Data Analysis Planning
```
**Context**: I'm analyzing [material type] [data type] for [application]
**Data**: [Describe your dataset structure and size]
**Goal**: [What analysis you want to perform]
**Constraints**: [Time, computational, or practical limitations]
**Output**: [Step-by-step analysis plan with code examples]
```

#### Template 2: Literature Review Assistance
```
**Context**: I'm researching [specific topic] in materials science
**Focus**: [Specific aspect or question you're investigating]
**Current Knowledge**: [What you already know]
**Gaps**: [What you need to understand better]
**Output**: [Key papers, concepts, and research directions]
```

#### Template 3: Experimental Design
```
**Context**: I'm designing experiments to optimize [material property]
**Parameters**: [Variables I can control]
**Objectives**: [What I want to achieve]
**Constraints**: [Budget, time, equipment limitations]
**Output**: [Experimental design matrix and methodology]
```

#### Template 4: Code Debugging
```
**Context**: I'm working on [specific materials science analysis]
**Problem**: [Describe the error or issue]
**Code**: [Relevant code snippet]
**Expected**: [What should happen]
**Actual**: [What's happening instead]
**Output**: [Solution with explanation]
```

### Week 3 Assignment: Prompt Library Development

**Due**: End of Week 3  
**Points**: 10 points  
**Deliverables**:
1. **Personal prompt library** with 5-7 templates for materials science tasks
2. **Test prompts** for 3 different AI tools (ChatGPT, Claude, local LLM)
3. **Response comparison** showing how different AI tools handle the same prompt
4. **Prompt refinement** showing iterative improvement of one prompt

**Submission Format**: Jupyter notebook with markdown documentation

---

## Week 4: Alloy Optimization Case Study

### Case Study: Aluminum Alloy Composition Optimization

We'll apply our prompt engineering skills to a real materials science problem: optimizing aluminum alloy composition for improved strength-to-weight ratio.

#### Problem Statement
```
**Research Question**: How can we optimize the composition of Al-Cu-Mg alloys 
to maximize strength-to-weight ratio while maintaining acceptable ductility?

**Current Alloy**: Al-2024 (Al-4.4Cu-1.5Mg-0.6Mn)
**Target Properties**: 
- Tensile strength > 400 MPa
- Elongation > 8%
- Density < 2.8 g/cm³
**Constraints**: 
- Cu content: 2.0-6.0 wt%
- Mg content: 0.5-2.5 wt%
- Mn content: 0.3-1.0 wt%
```

### AI-Assisted Hypothesis Generation

#### Step 1: Literature Review Prompt
Use this prompt to get AI assistance with literature review:

```
**Context**: I'm researching Al-Cu-Mg alloy composition optimization for aerospace applications
**Focus**: How Cu and Mg content affect strength, ductility, and density
**Current Knowledge**: Basic understanding of precipitation hardening in Al-Cu-Mg systems
**Specific Questions**:
1. What are the key strengthening mechanisms in Al-Cu-Mg alloys?
2. How does Cu:Mg ratio affect precipitate formation?
3. What composition ranges give optimal strength-ductility balance?
4. Are there any recent advances in composition optimization?

**Output**: 
- Key papers and findings
- Composition-property relationships
- Recommended composition ranges
- Research gaps and opportunities
```

#### Step 2: Experimental Design Prompt
Use AI to help design experiments:

```
**Context**: I need to design experiments to optimize Al-Cu-Mg alloy composition
**Parameters**: Cu (2.0-6.0%), Mg (0.5-2.5%), Mn (0.3-1.0%)
**Objectives**: Maximize strength-to-weight ratio, maintain ductility >8%
**Constraints**: 20 experimental runs maximum, standard heat treatment
**Data Available**: Historical data for 15 existing alloys

**Output**:
- Experimental design matrix (DOE approach)
- Sample preparation protocol
- Testing methodology
- Data analysis plan
- Success criteria
```

### Implementing the Case Study

#### 1. Data Generation and Analysis
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Generate sample alloy data based on literature
np.random.seed(42)
n_alloys = 20

# Define composition ranges
cu_range = np.linspace(2.0, 6.0, n_alloys)
mg_range = np.linspace(0.5, 2.5, n_alloys)
mn_range = np.linspace(0.3, 1.0, n_alloys)

# Add some randomness for realistic data
cu_content = cu_range + np.random.normal(0, 0.2, n_alloys)
mg_content = mg_range + np.random.normal(0, 0.1, n_alloys)
mn_content = mn_range + np.random.normal(0, 0.05, n_alloys)

# Calculate properties based on composition (simplified model)
def calculate_properties(cu, mg, mn):
    """Calculate alloy properties based on composition"""
    # Base properties for pure Al
    base_strength = 100  # MPa
    base_ductility = 40  # %
    base_density = 2.70  # g/cm³
    
    # Cu strengthening effect
    cu_strength = 25 * cu
    cu_ductility = -2 * cu
    
    # Mg strengthening effect
    mg_strength = 15 * mg
    mg_ductility = -1.5 * mg
    
    # Mn effect (smaller)
    mn_strength = 5 * mn
    mn_density = 0.1 * mn
    
    # Calculate final properties
    strength = base_strength + cu_strength + mg_strength + mn_strength
    ductility = base_ductility + cu_ductility + mg_ductility
    density = base_density + 0.1 * cu + 0.05 * mg + mn_density
    
    # Add realistic noise
    strength += np.random.normal(0, 10)
    ductility += np.random.normal(0, 2)
    density += np.random.normal(0, 0.02)
    
    # Ensure physical constraints
    strength = np.maximum(strength, 50)
    ductility = np.maximum(ductility, 2)
    density = np.maximum(density, 2.6)
    
    return strength, ductility, density

# Generate properties for all alloys
strengths, ductilities, densities = [], [], []
for i in range(n_alloys):
    s, d, den = calculate_properties(cu_content[i], mg_content[i], mn_content[i])
    strengths.append(s)
    ductilities.append(d)
    densities.append(den)

# Create DataFrame
alloy_data = pd.DataFrame({
    'Cu_wt_pct': cu_content,
    'Mg_wt_pct': mg_content,
    'Mn_wt_pct': mn_content,
    'Tensile_Strength_MPa': strengths,
    'Elongation_Percent': ductilities,
    'Density_g_cm3': densities
})

# Calculate strength-to-weight ratio
alloy_data['Strength_Weight_Ratio'] = alloy_data['Tensile_Strength_MPa'] / alloy_data['Density_g_cm3']

print("Alloy Dataset:")
print(alloy_data.head())
print(f"\nDataset shape: {alloy_data.shape}")
```

#### 2. Data Visualization and Analysis
```python
def analyze_alloy_data(data):
    """Analyze alloy composition-property relationships"""
    
    # Create correlation matrix
    numeric_cols = ['Cu_wt_pct', 'Mg_wt_pct', 'Mn_wt_pct', 
                   'Tensile_Strength_MPa', 'Elongation_Percent', 
                   'Density_g_cm3', 'Strength_Weight_Ratio']
    
    corr_matrix = data[numeric_cols].corr()
    
    # Plot correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.2f')
    plt.title('Alloy Property Correlations')
    plt.tight_layout()
    plt.show()
    
    # Composition-property relationships
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Cu effects
    axes[0,0].scatter(data['Cu_wt_pct'], data['Tensile_Strength_MPa'])
    axes[0,0].set_xlabel('Cu Content (wt%)')
    axes[0,0].set_ylabel('Tensile Strength (MPa)')
    axes[0,0].set_title('Cu vs. Strength')
    axes[0,0].grid(True, alpha=0.3)
    
    axes[0,1].scatter(data['Cu_wt_pct'], data['Elongation_Percent'])
    axes[0,1].set_xlabel('Cu Content (wt%)')
    axes[0,1].set_ylabel('Elongation (%)')
    axes[0,1].set_title('Cu vs. Ductility')
    axes[0,1].grid(True, alpha=0.3)
    
    axes[0,2].scatter(data['Cu_wt_pct'], data['Strength_Weight_Ratio'])
    axes[0,2].set_xlabel('Cu Content (wt%)')
    axes[0,2].set_ylabel('Strength/Weight Ratio')
    axes[0,2].set_title('Cu vs. Strength/Weight')
    axes[0,2].grid(True, alpha=0.3)
    
    # Mg effects
    axes[1,0].scatter(data['Mg_wt_pct'], data['Tensile_Strength_MPa'])
    axes[1,0].set_xlabel('Mg Content (wt%)')
    axes[1,0].set_ylabel('Tensile Strength (MPa)')
    axes[1,0].set_title('Mg vs. Strength')
    axes[1,0].grid(True, alpha=0.3)
    
    axes[1,1].scatter(data['Mg_wt_pct'], data['Elongation_Percent'])
    axes[1,1].set_xlabel('Mg Content (wt%)')
    axes[1,1].set_ylabel('Elongation (%)')
    axes[1,1].set_title('Mg vs. Ductility')
    axes[1,1].grid(True, alpha=0.3)
    
    axes[1,2].scatter(data['Mg_wt_pct'], data['Strength_Weight_Ratio'])
    axes[1,2].set_xlabel('Mg Content (wt%)')
    axes[1,2].set_ylabel('Strength/Weight Ratio')
    axes[1,2].set_title('Mg vs. Strength/Weight')
    axes[1,2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return corr_matrix

# Analyze the data
correlation_matrix = analyze_alloy_data(alloy_data)
print("\nKey Correlations:")
print(f"Cu vs. Strength: {correlation_matrix.loc['Cu_wt_pct', 'Tensile_Strength_MPa']:.3f}")
print(f"Mg vs. Strength: {correlation_matrix.loc['Mg_wt_pct', 'Tensile_Strength_MPa']:.3f}")
print(f"Cu vs. Strength/Weight: {correlation_matrix.loc['Cu_wt_pct', 'Strength_Weight_Ratio']:.3f}")
```

#### 3. AI-Assisted Optimization
Now use AI to help optimize the composition:

**Prompt for AI**:
```
**Context**: I'm optimizing Al-Cu-Mg alloy composition for maximum strength-to-weight ratio
**Data**: I have experimental data for 20 alloys with varying Cu (2-6%), Mg (0.5-2.5%), Mn (0.3-1.0%)
**Findings**: 
- Cu content strongly correlates with strength (r=0.85)
- Mg content moderately correlates with strength (r=0.72)
- Both Cu and Mg reduce ductility
- Strength/weight ratio peaks around Cu=4.5%, Mg=1.8%

**Questions**:
1. What composition would you recommend for maximum strength/weight ratio?
2. How can I balance strength and ductility requirements?
3. What additional experiments would validate this optimization?
4. Are there any practical considerations I'm missing?

**Output**: Specific composition recommendations with justification
```

### Week 4 Assignment: Complete Alloy Optimization Case Study

**Due**: End of Week 4  
**Points**: 15 points  
**Deliverables**:
1. **Complete analysis code** with data generation, visualization, and analysis
2. **AI interaction log** showing your prompt engineering process
3. **Optimization recommendations** based on AI assistance and data analysis
4. **Prompt library entry** for alloy optimization problems
5. **Case study report** summarizing findings and methodology

**Code Requirements**:
- Clean data generation and analysis functions
- Professional visualizations with proper labels
- Error handling and data validation
- Clear documentation and comments

**Analysis Requirements**:
- Generate realistic alloy composition-property data
- Analyze composition-property correlations
- Use AI to assist with optimization
- Provide specific composition recommendations
- Document limitations and assumptions

---

## Key Concepts Summary

### Prompt Engineering Principles
- **Context Setting**: Provide relevant background and constraints
- **Task Definition**: Be specific about goals and deliverables
- **Output Format**: Specify desired response structure
- **Quality Criteria**: Define what makes a good response

### AI-Assisted Research Workflow
1. **Problem Definition**: Clearly state research question and constraints
2. **Literature Review**: Use AI to identify key papers and concepts
3. **Experimental Design**: Get AI help with methodology and planning
4. **Data Analysis**: Use AI for interpretation and optimization
5. **Validation**: Critically evaluate AI suggestions

### Best Practices
- **Always validate AI responses** with domain knowledge
- **Build a personal prompt library** for common tasks
- **Iterate and refine prompts** based on response quality
- **Consider multiple AI tools** for different types of assistance
- **Document your AI interactions** for reproducibility

---

## Next Steps

In the next lesson, we'll learn about **modern data science tools** that go beyond pandas, including Polars for fast data processing and Streamlit for interactive dashboards.

**Remember**: Good prompt engineering is like good experimental design - it requires planning, iteration, and validation to get the best results.

---

## Resources and References

### Prompt Engineering
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Claude Prompting](https://docs.anthropic.com/claude/docs)
- [Prompt Engineering Best Practices](https://www.promptingguide.ai/)

### Alloy Design References
- ASM Handbook Volume 2: Properties and Selection of Aluminum Alloys
- "Aluminum Alloys: Structure and Properties" by L.F. Mondolfo
- Journal of Materials Science: Al-Cu-Mg alloy optimization studies

### Python Resources
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)

---

**Happy prompt engineering!** 🚀


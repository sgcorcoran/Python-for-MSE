"""
Script to create Lesson 05: AI Validation & Critical Evaluation notebook
This creates a comprehensive Jupyter notebook matching the format of lessons 01-04
"""

import json
import os

def create_lesson_05_notebook():
    """Create Lesson 05 notebook with all cells"""
    
    cells = []
    
    # Cell 0: Header and Learning Objectives
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Lesson 5: AI Validation & Critical Evaluation\n",
            "## Detecting Errors and Validating AI Outputs in Materials Science\n",
            "\n",
            "**Duration**: 1 week (Week 9)  \n",
            "**Weekly Workload**: 3 hours  \n",
            "**Learning Focus**: Critical evaluation of AI-generated code, statistical recommendations, and interpretations\n",
            "\n",
            "---\n",
            "\n",
            "## Learning Objectives\n",
            "\n",
            "By the end of this lesson, you will be able to:\n",
            "- **Identify common types of AI errors** in materials science contexts\n",
            "- **Validate AI-generated code** before using it in analysis\n",
            "- **Critically evaluate AI statistical recommendations** for appropriateness\n",
            "- **Verify AI interpretations** against domain knowledge\n",
            "- **Use AI as a tool, not a replacement** for scientific reasoning\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 1: Documentation Requirements
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 📸 **DOCUMENTATION REQUIREMENTS**\n",
            "\n",
            "**Throughout this lesson, you'll document your validation process:**\n",
            "\n",
            "1. **Screenshot 1**: AI-generated code before validation (Task 1)\n",
            "2. **Screenshot 2**: Errors you identified (Task 1)\n",
            "3. **Screenshot 3**: Corrected code with annotations (Task 1)\n",
            "4. **Screenshot 4**: AI statistical recommendation (Task 2)\n",
            "5. **Screenshot 5**: Your validation checklist (Task 2)\n",
            "6. **Screenshot 6**: Final validated analysis output\n",
            "\n",
            "**Save all screenshots in a PDF file with clear captions.**\n",
            "\n",
            "**Also export your AI chat logs** (ChatGPT/Claude conversations) and include in submission.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 2: Time Allocation
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Week 9: AI Validation & Critical Evaluation\n",
            "\n",
            "**Time Allocation**: 3 hours\n",
            "- Mini-Lecture: 25-30 minutes\n",
            "- Guided Activity 1 (Code Validation): 60 minutes\n",
            "- Guided Activity 2 (Statistical Validation): 60 minutes\n",
            "- Reflection & Synthesis: 30 minutes\n",
            "\n",
            "**Prerequisites**: \n",
            "- Completed Lessons 01-04\n",
            "- Access to ChatGPT, Claude, or Cursor AI\n",
            "- Basic Python understanding (from MSE 2114)\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 3: Mini-Lecture Header
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Mini-Lecture: Why AI Validation Matters (25-30 min)\n",
            "\n",
            "### The Critical Problem: AI Makes Mistakes\n",
            "\n",
            "Throughout Lessons 01-04, you've learned to use AI tools for:\n",
            "- Code generation\n",
            "- Statistical test recommendations\n",
            "- Data analysis\n",
            "- Report writing\n",
            "\n",
            "**But here's the critical question**: How do you know if the AI is right?\n",
            "\n",
            "AI tools like ChatGPT, Claude, and GitHub Copilot are **powerful assistants**, but they are **not infallible**. They can:\n",
            "- Generate incorrect code\n",
            "- Recommend inappropriate statistical tests\n",
            "- Misinterpret results\n",
            "- Make up facts (\"hallucinate\")\n",
            "\n",
            "**Your responsibility as a scientist**: **Validate everything** the AI produces.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 4: Types of AI Errors
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Common Types of AI Errors in Materials Science\n",
            "\n",
            "#### 1. **Code Errors**\n",
            "- **Syntax errors**: Invalid Python syntax\n",
            "- **Logic errors**: Code runs but does the wrong thing\n",
            "- **Import errors**: Missing or incorrect library imports\n",
            "- **Data type errors**: Wrong data types (e.g., strings instead of numbers)\n",
            "- **Function misuse**: Using functions incorrectly (wrong parameters, wrong order)\n",
            "\n",
            "**Example**: AI generates `np.mean(data)` when `data` is a DataFrame (should be `data.mean()` or `np.mean(data[column])`)\n",
            "\n",
            "#### 2. **Statistical Errors**\n",
            "- **Wrong test selection**: Recommending t-test when data violates assumptions\n",
            "- **Missing assumptions**: Not checking for normality, equal variances\n",
            "- **Incorrect interpretation**: Misunderstanding what the test actually tests\n",
            "- **P-value misuse**: Treating p < 0.05 as \"proven\" (it's not!)\n",
            "\n",
            "**Example**: AI recommends t-test for non-normal data without mentioning transformations\n",
            "\n",
            "#### 3. **Factual Errors (Hallucinations)**\n",
            "- **Made-up data**: Inventing values or properties that don't exist\n",
            "- **Incorrect formulas**: Wrong equations for materials properties\n",
            "- **Fictional references**: Citing papers that don't exist\n",
            "- **Wrong units**: Mixing up MPa and GPa, or temperature units\n",
            "\n",
            "**Example**: AI states that aluminum has yield strength of 500 MPa (typical is 275-310 MPa)\n",
            "\n",
            "#### 4. **Interpretation Errors**\n",
            "- **Misunderstanding results**: Drawing wrong conclusions from analysis\n",
            "- **Overstating significance**: Claiming effects are larger than they are\n",
            "- **Ignoring context**: Missing important materials science context\n",
            "- **Correlation vs causation**: Confusing correlation with causation\n",
            "\n",
            "**Example**: AI concludes \"heat treatment causes higher strength\" when both are correlated with composition\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 5: Validation Strategy
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Validation Strategy: The \"Trust but Verify\" Approach\n",
            "\n",
            "**Principle**: AI is a starting point, not a final answer.\n",
            "\n",
            "#### Step 1: Initial Check\n",
            "- **Does it look reasonable?** Common sense check\n",
            "- **Are there obvious errors?** Syntax, imports, function names\n",
            "- **Does it match what you requested?** Compare to your prompt\n",
            "\n",
            "#### Step 2: Code Validation (for code)\n",
            "- **Run the code**: Does it execute without errors?\n",
            "- **Test with simple data**: Use known values\n",
            "- **Compare to examples**: Check against documentation\n",
            "- **Use AI to check AI**: Ask another AI tool to review\n",
            "\n",
            "#### Step 3: Logic Validation\n",
            "- **Does the approach make sense?** For your specific problem\n",
            "- **Are the assumptions met?** Check data against test assumptions\n",
            "- **Is the interpretation correct?** Verify understanding\n",
            "\n",
            "#### Step 4: Domain Knowledge Check\n",
            "- **Are the numbers reasonable?** (e.g., yield strength of Al alloys)\n",
            "- **Do the conclusions match MSE principles?** Material behavior\n",
            "- **Would a materials scientist agree?** Peer review mindset\n",
            "\n",
            "**Remember**: Validation takes time, but **saves time** by catching errors early!\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 6: Guided Activity 1 Header
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Guided Activity 1: Code Validation (60 min)\n",
            "\n",
            "**Learning Goal**: Learn to identify and correct errors in AI-generated code.\n",
            "\n",
            "**Scenario**: You've asked AI to generate code for analyzing heat treatment data, but the AI made several mistakes. Your job is to find and fix them.\n",
            "\n",
            "**What you'll do:**\n",
            "1. Examine AI-generated code for errors\n",
            "2. Identify specific problems (syntax, logic, data types)\n",
            "3. Correct the errors\n",
            "4. Validate your corrections work\n",
            "\n",
            "**Why this matters**: In real research, AI-generated code often has errors. Learning to catch them early prevents hours of debugging later.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 7: Task 1: AI-Generated Code (with errors)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Task 1: Examine AI-Generated Code (15 min)\n",
            "\n",
            "**Your Task**: Below is AI-generated code for analyzing heat treatment data. **Your job is to find the errors BEFORE running it.**\n",
            "\n",
            "**Instructions:**\n",
            "1. Read through the code carefully\n",
            "2. Identify potential errors (don't fix them yet!)\n",
            "3. Make a list of what you think is wrong\n",
            "4. Write down why each error is a problem\n",
            "\n",
            "**💡 Python Help**: If you're not comfortable with Python yet:\n",
            "- Look for misspelled function names (e.g., `mean` vs `meen`)\n",
            "- Check for missing parentheses `()` or brackets `[]`\n",
            "- Verify that variable names match (e.g., `data` vs `Data`)\n",
            "- Look for imports that might be missing\n",
            "- Check if function calls match the library documentation\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 8: AI-Generated Code (with intentional errors)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### AI-Generated Code (Contains Errors - DO NOT RUN YET!)\n",
            "\n",
            "**📸 Screenshot Opportunity**: Take a screenshot of this code before you start finding errors.\n",
            "\n",
            "```python\n",
            "# TODO: This code was generated by AI and contains errors\n",
            "# Your task: Find all the errors before running it\n",
            "\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Load data\n",
            "data = pd.read_csv('heat_treatment_data.csv')  # Error 1: File might not exist\n",
            "\n",
            "# Calculate mean hardness for each treatment\n",
            "mean_hardness = np.mean(data['Hardness_HV'])  # Error 2: Should group by treatment\n",
            "\n",
            "# Create visualization\n",
            "plt.plot(data['Treatment'], data['Hardness_HV'])  # Error 3: Wrong plot type for groups\n",
            "plt.title('Hardness by Treatment')\n",
            "plt.show()\n",
            "```\n",
            "\n",
            "**Now make a list of errors you found:**\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 9: Error Identification Worksheet
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📝 Error Identification Worksheet\n",
            "\n",
            "**Your Task**: List all errors you identified:\n",
            "\n",
            "1. **Error 1**: \n",
            "   - What's wrong: \n",
            "   - Why it's a problem: \n",
            "   - How to fix: \n",
            "\n",
            "2. **Error 2**: \n",
            "   - What's wrong: \n",
            "   - Why it's a problem: \n",
            "   - How to fix: \n",
            "\n",
            "3. **Error 3**: \n",
            "   - What's wrong: \n",
            "   - Why it's a problem: \n",
            "   - How to fix: \n",
            "\n",
            "4. **Error 4** (if you found more): \n",
            "\n",
            "**💡 Hint**: There are at least 3 errors in the code above. Can you find them all?\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 10: Dataset Creation for Testing
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "source": [
            "# === Create Sample Dataset for Testing ===\n",
            "# This creates realistic heat treatment data for you to work with\n",
            "\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
            "\n",
            "# Set random seed for reproducibility\n",
            "np.random.seed(42)\n",
            "\n",
            "# Generate heat treatment data\n",
            "n_samples_per_group = 20\n",
            "\n",
            "# Treatment A: Standard T6 (150 HV average)\n",
            "treatment_a = np.random.normal(150, 10, n_samples_per_group)\n",
            "\n",
            "# Treatment B: Modified T6 (165 HV average)\n",
            "treatment_b = np.random.normal(165, 12, n_samples_per_group)\n",
            "\n",
            "# Create DataFrame\n",
            "heat_treatment_data = pd.DataFrame({\n",
            "    'Sample_ID': range(1, 2*n_samples_per_group + 1),\n",
            "    'Treatment': ['Standard_T6']*n_samples_per_group + ['Modified_T6']*n_samples_per_group,\n",
            "    'Hardness_HV': np.concatenate([treatment_a, treatment_b]),\n",
            "    'Temperature_C': [160]*n_samples_per_group + [180]*n_samples_per_group,\n",
            "    'Time_hours': [18]*n_samples_per_group + [12]*n_samples_per_group\n",
            "})\n",
            "\n",
            "# Save to CSV for testing\n",
            "heat_treatment_data.to_csv('heat_treatment_data.csv', index=False)\n",
            "\n",
            "print(\"Dataset created successfully!\")\n",
            "print(f\"Shape: {heat_treatment_data.shape}\")\n",
            "print(f\"\\nFirst 5 rows:\")\n",
            "print(heat_treatment_data.head())\n"
        ]
    })
    
    # Continue with more cells... Let me create a more complete version
    
    print(f"Created {len(cells)} cells so far...")
    return cells

# Create the notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Generate all cells
notebook["cells"] = create_lesson_05_notebook()

# Save notebook
with open('05_ai_validation_critical_evaluation.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Notebook created with {len(notebook['cells'])} cells")


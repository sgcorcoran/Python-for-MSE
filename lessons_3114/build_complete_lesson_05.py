"""
Complete Lesson 05 Notebook Builder
Creates comprehensive AI Validation & Critical Evaluation notebook
Matching format and quality of lessons 01-04
"""

import json

def create_complete_lesson_05():
    """Create complete Lesson 05 notebook with all cells"""
    
    cells = []
    
    # === HEADER SECTION ===
    
    # Cell 0: Title and Learning Objectives
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
            "## 📋 **SUBMISSION REQUIREMENTS**\n",
            "\n",
            "**Turn in this notebook with all cells run showing output.**\n",
            "\n",
            "**Your notebook should contain:**\n",
            "- All error identification work (Task 1)\n",
            "- All corrected code with output visible (Task 2)\n",
            "- All validation checklists completed (Task 2)\n",
            "- All AI recommendations and your validation notes (Task 2)\n",
            "- All reflection questions answered\n",
            "\n",
            "**Required**: Export your AI chat logs (ChatGPT/Claude conversations) and include in submission. This demonstrates your AI interaction process for validation tasks.\n",
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
            "**💡 For Python Beginners**: This lesson includes extra hints and step-by-step guidance. Don't worry if Python feels challenging - you'll learn by finding and fixing errors!\n",
            "\n",
            "---\n"
        ]
    })
    
    # === MINI-LECTURE SECTION ===
    
    # Cell 3: Mini-Lecture Introduction
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
    
    # Cell 4: Types of AI Errors - Part 1
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Common Types of AI Errors in Materials Science\n",
            "\n",
            "#### 1. **Code Errors**\n",
            "\n",
            "**Syntax Errors**: Invalid Python syntax that prevents code from running\n",
            "- Missing colons `:` after if/for statements\n",
            "- Missing parentheses `()` or brackets `[]`\n",
            "- Incorrect indentation (Python is very sensitive to this!)\n",
            "- Missing quotes around strings\n",
            "\n",
            "**Logic Errors**: Code runs but does the wrong thing\n",
            "- Wrong function for the task (e.g., using `mean()` when you need `median()`)\n",
            "- Incorrect calculations (e.g., dividing instead of multiplying)\n",
            "- Missing steps in the analysis workflow\n",
            "\n",
            "**Import/Function Errors**: Missing or incorrect library usage\n",
            "- Using functions that don't exist\n",
            "- Wrong parameters to functions\n",
            "- Missing import statements\n",
            "- Using deprecated functions\n",
            "\n",
            "**Example**: AI generates `np.mean(data)` when `data` is a DataFrame column. Should be `data['column'].mean()` or `np.mean(data['column'])`\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 5: Types of AI Errors - Part 2
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 2. **Statistical Errors**\n",
            "\n",
            "**Wrong Test Selection**: AI recommends tests that don't match your data\n",
            "- Recommending t-test when data violates normality assumptions\n",
            "- Using parametric tests for clearly non-normal data\n",
            "- Wrong test for your research question\n",
            "\n",
            "**Missing Assumption Checks**: AI forgets to check test requirements\n",
            "- Not checking for normality before t-tests\n",
            "- Not checking for equal variances\n",
            "- Not verifying sample sizes are adequate\n",
            "\n",
            "**Incorrect Interpretation**: AI misunderstands what the test means\n",
            "- Confusing correlation with causation\n",
            "- Overstating significance of small effects\n",
            "- Ignoring practical vs. statistical significance\n",
            "\n",
            "**Example**: AI recommends t-test for two groups without checking if data is normal or if variances are equal\n",
            "\n",
            "#### 3. **Factual Errors (Hallucinations)**\n",
            "\n",
            "AI can make up information that sounds plausible:\n",
            "- Inventing property values (e.g., \"aluminum yield strength is 500 MPa\" when typical is 275-310 MPa)\n",
            "- Citing papers that don't exist\n",
            "- Using incorrect formulas\n",
            "- Mixing up units (MPa vs GPa, Celsius vs Fahrenheit)\n",
            "\n",
            "**Example**: AI states that 7075 aluminum has yield strength of 150 MPa (actually ~470 MPa)\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 6: Validation Strategy
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Validation Strategy: The \"Trust but Verify\" Approach\n",
            "\n",
            "**Principle**: AI is a starting point, not a final answer.\n",
            "\n",
            "#### Step 1: Initial Check (5 minutes)\n",
            "- **Does it look reasonable?** Common sense check\n",
            "- **Are there obvious errors?** Syntax, imports, function names\n",
            "- **Does it match what you requested?** Compare to your prompt\n",
            "\n",
            "#### Step 2: Code Validation (for code) - 15-20 minutes\n",
            "- **Run the code**: Does it execute without errors?\n",
            "- **Test with simple data**: Use known values you can verify manually\n",
            "- **Compare to examples**: Check against documentation or lesson examples\n",
            "- **Use AI to check AI**: Ask another AI tool to review (cross-validation)\n",
            "\n",
            "**💡 Python Beginner Tip**: Start with very simple test cases. If AI generates complex code, test each part separately.\n",
            "\n",
            "#### Step 3: Logic Validation (15-20 minutes)\n",
            "- **Does the approach make sense?** For your specific problem\n",
            "- **Are the assumptions met?** Check data against test assumptions\n",
            "- **Is the interpretation correct?** Verify your understanding matches AI's\n",
            "\n",
            "#### Step 4: Domain Knowledge Check (10 minutes)\n",
            "- **Are the numbers reasonable?** (e.g., yield strength of Al alloys is typically 250-500 MPa)\n",
            "- **Do the conclusions match MSE principles?** Material behavior, processing effects\n",
            "- **Would a materials scientist agree?** Peer review mindset\n",
            "\n",
            "**Remember**: Validation takes time, but **saves time** by catching errors early and preventing incorrect results!\n",
            "\n",
            "---\n"
        ]
    })
    
    # === GUIDED ACTIVITY 1: CODE VALIDATION ===
    
    # Cell 7: Guided Activity 1 Header
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
            "1. Examine AI-generated code for errors (15 min)\n",
            "2. Identify specific problems (syntax, logic, data types) (15 min)\n",
            "3. Correct the errors (20 min)\n",
            "4. Validate your corrections work (10 min)\n",
            "\n",
            "**Why this matters**: In real research, AI-generated code often has errors. Learning to catch them early prevents hours of debugging later.\n",
            "\n",
            "**💡 Why This Matters**: Debugging incorrect code later takes 10x longer than catching errors early. Plus, incorrect code can lead to wrong scientific conclusions - a serious problem in research!\n",
            "\n",
            "**💡 For Python Beginners**: Don't worry if you don't catch every error! The goal is to practice looking critically. We'll work through examples together.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 8: Worked Example - Error Detection (NEW)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📚 Worked Example: Finding Your First Error (Practice)\n",
            "\n",
            "**Before you start finding errors on your own, let's walk through one example together!**\n",
            "\n",
            "**Example Code (with one error):**\n",
            "\n",
            "```python\n",
            "# Calculate mean hardness\n",
            "data = pd.read_csv('heat_treatment_data.csv')\n",
            "mean_hardness = data.mean('Hardness_HV')  # ERROR: Wrong function call!\n",
            "```\n",
            "\n",
            "**Step-by-Step Error Finding Process:**\n",
            "\n",
            "1. **Read the code carefully**: What is this code trying to do?\n",
            "   - Goal: Calculate mean hardness\n",
            "\n",
            "2. **Check the function call**: Is `data.mean('Hardness_HV')` correct?\n",
            "   - Let's check the pandas documentation (or remember from previous lessons)\n",
            "   - For a DataFrame column, we use: `data['Hardness_HV'].mean()`\n",
            "   - OR: `data[['Hardness_HV']].mean()` (if using DataFrame method)\n",
            "\n",
            "3. **Identify the error**:\n",
            "   - **What's wrong**: `data.mean('Hardness_HV')` is not the correct syntax\n",
            "   - **Why it's a problem**: `mean()` on a DataFrame doesn't take a column name as a parameter this way\n",
            "   - **How to fix**: Use `data['Hardness_HV'].mean()` instead\n",
            "\n",
            "4. **Verify your understanding**:\n",
            "   - In pandas, to calculate the mean of a specific column:\n",
            "     - Step 1: Select the column: `data['Hardness_HV']`\n",
            "     - Step 2: Calculate mean: `.mean()`\n",
            "     - Combined: `data['Hardness_HV'].mean()`\n",
            "\n",
            "**💡 Why This Matters**: This error is subtle - the code might not run, or might give unexpected results. Learning to spot these errors helps you validate AI-generated code!\n",
            "\n",
            "**Now you're ready to find errors on your own!**\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 8b: Task 1 Header - Code Examination
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Task 1: Examine AI-Generated Code (15 min)\n",
            "\n",
            "**Your Task**: Below is AI-generated code for analyzing heat treatment data. **Your job is to find the errors BEFORE running it.**\n",
            "\n",
            "**💡 Why This Matters**: In real research, AI-generated code often has errors. Learning to catch them early prevents hours of debugging and incorrect results!\n",
            "\n",
            "**Instructions:**\n",
            "1. Read through the code carefully line by line\n",
            "2. Identify potential errors (don't fix them yet!)\n",
            "3. Make a list of what you think is wrong\n",
            "4. Write down why each error is a problem\n",
            "\n",
            "**💡 Python Help for Beginners**:\n",
            "- Look for misspelled function names (e.g., `mean` vs `meen`)\n",
            "- Check for missing parentheses `()` or brackets `[]`\n",
            "- Verify that variable names match (e.g., `data` vs `Data` - Python is case-sensitive!)\n",
            "- Look for imports that might be missing (e.g., code uses `pd` but doesn't import pandas)\n",
            "- Check if function calls match how they're used in lessons 01-04\n",
            "- Look for `=` (assignment) vs `==` (comparison) confusion\n",
            "\n",
            "**💡 Validation Strategy**: Think about what each line is trying to do, then check if it's the right approach for your problem.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 9: Create Sample Dataset First
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
            "print(\"=\"*70)\n",
            "print(\"DATASET CREATED SUCCESSFULLY\")\n",
            "print(\"=\"*70)\n",
            "print(f\"\\nShape: {heat_treatment_data.shape}\")\n",
            "print(f\"\\nFirst 5 rows:\")\n",
            "print(heat_treatment_data.head())\n",
            "print(f\"\\nLast 5 rows:\")\n",
            "print(heat_treatment_data.tail())\n"
        ]
    })
    
    # Cell 10: AI-Generated Code with Errors
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### AI-Generated Code (Contains Errors - DO NOT RUN YET!)\n",
            "\n",
            "\n",
            "Below is code that an AI generated when asked to \"analyze heat treatment data and compare hardness between two treatments\":\n",
            "\n",
            "```python\n",
            "# AI-Generated Code (Contains Errors!)\n",
            "# Task: Analyze heat treatment data\n",
            "\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Load the data\n",
            "data = pd.read_csv('heat_treatment_data.csv')\n",
            "\n",
            "# Calculate mean hardness for each treatment\n",
            "mean_hardness = np.mean(data['Hardness_HV'])\n",
            "print(f\"Mean hardness: {mean_hardness}\")\n",
            "\n",
            "# Create boxplot\n",
            "plt.boxplot([data['Hardness_HV']], labels=['All Data'])\n",
            "plt.xlabel('Treatment')\n",
            "plt.ylabel('Hardness (HV)')\n",
            "plt.title('Hardness by Treatment')\n",
            "plt.show()\n",
            "\n",
            "# Statistical test\n",
            "from scipy import stats\n",
            "result = stats.ttest_1samp(data['Hardness_HV'], 160)\n",
            "print(f\"T-test result: p = {result.pvalue}\")\n",
            "```\n",
            "\n",
            "**Your Task**: Read the code above and identify at least 3 errors.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 11: Error Identification Worksheet
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📝 Error Identification Worksheet\n",
            "\n",
            "**Your Task**: Fill out this worksheet identifying errors in the AI-generated code:\n",
            "\n",
            "**Error 1**: \n",
            "- **What's wrong**: \n",
            "- **Why it's a problem**: \n",
            "- **How to fix**: \n",
            "\n",
            "**Error 2**: \n",
            "- **What's wrong**: \n",
            "- **Why it's a problem**: \n",
            "- **How to fix**: \n",
            "\n",
            "**Error 3**: \n",
            "- **What's wrong**: \n",
            "- **Why it's a problem**: \n",
            "- **How to fix**: \n",
            "\n",
            "**Error 4** (if you found more): \n",
            "- **What's wrong**: \n",
            "- **Why it's a problem**: \n",
            "- **How to fix**: \n",
            "\n",
            "**💡 Hint**: There are at least 3 major errors in the code:\n",
            "1. One related to calculating means (what does the code calculate vs. what should it calculate?)\n",
            "2. One related to visualization (what groups should be shown?)\n",
            "3. One related to statistical testing (is this the right test for comparing two groups?)\n",
            "\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 12: Task 2 - Correct the Code
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Task 2: Correct the Errors (20 min)\n",
            "\n",
            "**Your Task**: Now write corrected code below. Use TODO comments where you're not sure - that's okay!\n",
            "\n",
            "**Instructions:**\n",
            "1. Write code to correctly calculate mean hardness FOR EACH TREATMENT (not overall)\n",
            "2. Create a proper boxplot comparing the two treatments\n",
            "3. Use the correct statistical test to compare two groups\n",
            "4. Add comments explaining what each section does\n",
            "\n",
            "**💡 Python Help for Beginners**:\n",
            "- To group by treatment: `data.groupby('Treatment')['Hardness_HV'].mean()`\n",
            "- For boxplot with groups: Use seaborn `sns.boxplot(data=data, x='Treatment', y='Hardness_HV')` OR create lists for each group\n",
            "- For comparing two groups: Use `stats.ttest_ind()` or `stats.mannwhitneyu()` depending on normality\n",
            "- Look back at Lesson 04 for examples of statistical tests!\n",
            "\n",
            "**Remember**: You're learning! It's okay to use lesson examples as references.\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell 13: Corrected Code (TODO Scaffolding)
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "source": [
            "# === Task 2: Corrected Code (WRITE YOUR CODE BELOW) ===\n",
            "\n",
            "# Step 1: Import libraries\n",
            "# TODO: Import pandas, numpy, matplotlib, seaborn, and scipy.stats\n",
            "# HINT: You've done this in previous lessons - refer back if needed!\n",
            "\n",
            "\n",
            "\n",
            "# Step 2: Load and validate data\n",
            "# TODO: Load the CSV file 'heat_treatment_data.csv'\n",
            "# TODO: Add a validation step to check data loaded (print shape or head)\n",
            "\n",
            "\n",
            "\n",
            "# Step 3: Calculate mean hardness FOR EACH TREATMENT\n",
            "# TODO: Calculate mean hardness separately for each treatment group\n",
            "# HINT: Use .groupby('Treatment')['Hardness_HV'].mean()\n",
            "# WHY: The AI error was calculating overall mean - you need group-specific means\n",
            "print(\"=\"*70)\n",
            "print(\"MEAN HARDNESS BY TREATMENT\")\n",
            "print(\"=\"*70)\n",
            "# TODO: Print the mean by treatment\n",
            "\n",
            "\n",
            "\n",
            "# Step 4: Create boxplot comparing treatments\n",
            "# TODO: Create a boxplot that shows the two treatments separately\n",
            "# HINT: Option 1 - Use seaborn: sns.boxplot(data=data, x='Treatment', y='Hardness_HV')\n",
            "# HINT: Option 2 - Use matplotlib: Separate data first, then plt.boxplot([group1, group2], labels=[...])\n",
            "# WHY: The AI error showed all data together - you need groups separated!\n",
            "plt.figure(figsize=(8, 6))\n",
            "# TODO: Write your boxplot code here\n",
            "\n",
            "plt.xlabel('Treatment')\n",
            "plt.ylabel('Hardness (HV)')\n",
            "plt.title('Hardness by Treatment')\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
            "\n",
            "\n",
            "\n",
            "# Step 5: Statistical test to compare TWO GROUPS\n",
            "# TODO: Separate data into two groups (Standard_T6 and Modified_T6)\n",
            "# TODO: Use appropriate statistical test to compare two groups\n",
            "# HINT: For two independent groups, use stats.ttest_ind() or stats.mannwhitneyu()\n",
            "# WHY: The AI error used ttest_1samp (for one group) - you need a test for two groups!\n",
            "print(\"\\n\" + \"=\"*70)\n",
            "print(\"STATISTICAL TEST: COMPARING TWO GROUPS\")\n",
            "print(\"=\"*70)\n",
            "# TODO: Write your statistical test code here\n",
            "# TODO: Print the p-value and interpret the results\n",
            "\n"
        ]
    })
    
    # Continue with more cells... Due to length, I'll add the remaining critical cells
    
    return cells

# Continue building - let me add reflection, activity 2, and rubrics
def add_remaining_cells():
    """Add remaining cells for complete lesson"""
    additional_cells = []
    
    # Task 3: Validation
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Task 3: Validate Your Corrections (10 min)\n",
            "\n",
            "**Your Task**: Run your corrected code and verify it works correctly.\n",
            "\n",
            "**💡 Why This Matters**: Validation catches errors before they lead to wrong conclusions. Always validate!\n",
            "\n",
            "**Validation Checklist:**\n",
            "- [ ] Code runs without errors\n",
            "- [ ] Mean hardness is calculated separately for each treatment (not overall)\n",
            "- [ ] Boxplot shows two groups clearly separated\n",
            "- [ ] Statistical test is appropriate for comparing two groups\n",
            "- [ ] Results make sense (check if means are reasonable for aluminum T6 treatments: ~150-170 HV)\n",
            "- [ ] Units are included in labels (HV = Vickers Hardness)\n",
            "\n",
            "**💡 Important**: Make sure your corrected code runs successfully and produces output visible in the notebook!\n",
            "\n",
            "**If you got errors**: That's okay! Debugging is part of learning. Try:\n",
            "1. Read the error message carefully\n",
            "2. Check if variable names match\n",
            "3. Verify function calls match documentation\n",
            "4. Ask AI for help understanding the error (but verify its solution!)\n",
            "\n",
            "---\n"
        ]
    })
    
    # Guided Activity 2 Header
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Guided Activity 2: Statistical Validation (60 min)\n",
            "\n",
            "**Learning Goal**: Learn to critically evaluate AI statistical recommendations.\n",
            "\n",
            "**Scenario**: You've consulted AI about which statistical test to use for your data. The AI made recommendations, but are they correct?\n",
            "\n",
            "**💡 Why This Matters**: Using the wrong statistical test gives you wrong conclusions. In materials science, this can lead to incorrect recommendations about materials, processes, or properties. Always validate AI statistical recommendations!\n",
            "\n",
            "**What you'll do:**\n",
            "1. Get AI recommendation for statistical test (10 min)\n",
            "2. Validate the recommendation (20 min)\n",
            "3. Check assumptions (20 min)\n",
            "4. Verify the recommendation is appropriate (10 min)\n",
            "\n",
            "---\n"
        ]
    })
    
    # Task 1 of Activity 2: Get AI Recommendation
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Task 1: Get AI Recommendation (10 min)\n",
            "\n",
            "**Your Task**: Ask AI (ChatGPT or Claude) to recommend a statistical test for your heat treatment data.\n",
            "\n",
            "**Prompt to use**: Copy and paste this prompt into your AI tool:\n",
            "\n",
            "```\n",
            "I have heat treatment data with two groups:\n",
            "- Treatment A: Standard T6 (n=20 samples, hardness measured)\n",
            "- Treatment B: Modified T6 (n=20 samples, hardness measured)\n",
            "\n",
            "I want to know if the two treatments produce different hardness values.\n",
            "\n",
            "Which statistical test should I use? Please:\n",
            "1. Recommend a specific test\n",
            "2. Explain why it's appropriate\n",
            "3. List the assumptions for that test\n",
            "4. Explain how to check those assumptions\n",
            "\n",
            "Provide the recommendation in a clear, step-by-step format.\n",
            "```\n",
            "\n",
            "**Instructions:**\n",
            "1. Paste the prompt above into ChatGPT or Claude\n",
            "2. Copy the AI's response\n",
            "3. Paste it in the cell below (between triple quotes)\n",
            "\n",
            "\n",
            "---\n"
        ]
    })
    
    # Cell for AI Response
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### AI Statistical Recommendation\n",
            "\n",
            "**Paste the AI's response here:**\n",
            "\n",
            "```\n",
            "\n",
            "\n",
            "\n",
            "```\n",
            "\n",
            "---\n"
        ]
    })
    
    # Task 2: Validate Recommendation
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Task 2: Validate the Recommendation (20 min)\n",
            "\n",
            "**Your Task**: Critically evaluate the AI's recommendation using the checklist below.\n",
            "\n",
            "**Validation Checklist:**\n",
            "\n",
            "#### 1. Does the test match the research question?\n",
            "- [ ] Is the AI testing what you actually want to know?\n",
            "- [ ] Are we comparing two groups? (If yes, need a two-group test, not one-sample test)\n",
            "- [ ] Do we need to check for differences? (That's what we want!)\n",
            "\n",
            "#### 2. Are the assumptions reasonable?\n",
            "- [ ] Does the AI list assumptions clearly?\n",
            "- [ ] Are those assumptions realistic for your data?\n",
            "- [ ] Does the AI explain how to check assumptions?\n",
            "\n",
            "#### 3. Is the test appropriate for your data type?\n",
            "- [ ] Continuous data? (Hardness is continuous - ✓)\n",
            "- [ ] Two independent groups? (Yes - ✓)\n",
            "- [ ] Appropriate sample sizes? (n=20 each is usually okay)\n",
            "\n",
            "#### 4. Are there alternatives mentioned?\n",
            "- [ ] Does AI mention what to do if assumptions aren't met?\n",
            "- [ ] Are non-parametric alternatives discussed?\n",
            "\n",
            "**Write your validation notes here:**\n",
            "\n",
            "---\n"
        ]
    })
    
    # Task 3: Check Assumptions
    additional_cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "source": [
            "# === Task 3: Check Statistical Test Assumptions (20 min) ===\n",
            "\n",
            "# Step 1: Import libraries (if not already imported)\n",
            "# TODO: Import necessary libraries (pandas, scipy.stats, matplotlib, etc.)\n",
            "# HINT: You may have already imported these earlier - check your previous cells!\n",
            "\n",
            "\n",
            "\n",
            "# Step 2: Load and prepare data (if not already done)\n",
            "# TODO: Load the data file\n",
            "# TODO: Separate data into two groups (Standard_T6 and Modified_T6)\n",
            "# HINT: Use the same approach you used in Task 2 of Activity 1\n",
            "\n",
            "\n",
            "\n",
            "# Step 3: Check normality assumptions\n",
            "print(\"=\"*70)\n",
            "print(\"ASSUMPTION CHECKING FOR STATISTICAL TEST\")\n",
            "print(\"=\"*70)\n",
            "# TODO: Check normality for each group\n",
            "# HINT: Use stats.shapiro() or stats.normaltest()\n",
            "# WHY: Parametric tests (like t-test) assume data is normally distributed\n",
            "# TODO: Print the results for each group\n",
            "# TODO: Interpret the results (normal if p-value > 0.05)\n",
            "\n",
            "\n",
            "\n",
            "# Step 4: Check equal variances (if using t-test)\n",
            "# TODO: Check if variances are equal between groups\n",
            "# HINT: Use stats.levene() or stats.bartlett()\n",
            "# WHY: Standard t-test assumes equal variances; if not equal, use Welch's t-test\n",
            "# TODO: Print and interpret the results (equal variances if p-value > 0.05)\n",
            "\n",
            "\n",
            "\n",
            "# Step 5: Visual checks (optional but recommended)\n",
            "# TODO: Create visual checks for normality\n",
            "# HINT: Create histograms, Q-Q plots, or both\n",
            "# WHY: Visual checks help confirm statistical test results\n",
            "# HINT: Use plt.subplots() to create multiple plots\n",
            "\n",
            "\n",
            "\n",
            "# Step 6: Recommend appropriate test based on assumptions\n",
            "print(\"\\n\" + \"=\"*70)\n",
            "print(\"RECOMMENDATION BASED ON ASSUMPTIONS\")\n",
            "print(\"=\"*70)\n",
            "# TODO: Based on your assumption checks, recommend the appropriate test\n",
            "# Decision logic:\n",
            "# - If normal AND equal variances: use t-test (stats.ttest_ind)\n",
            "# - If normal BUT unequal variances: use Welch's t-test (stats.ttest_ind with equal_var=False)\n",
            "# - If NOT normal: use Mann-Whitney U test (stats.mannwhitneyu)\n",
            "# TODO: Print your recommendation and explain why\n"
        ]
    })
    
    # Reflection Questions
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Reflection & Synthesis (30 min)\n",
            "\n",
            "**Answer the following questions in your own words.** Word limits help you be concise!\n",
            "\n",
            "---\n"
        ]
    })
    
    # Reflection Question 1
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Reflection Question 1: Code Validation Experience (≤150 words)\n",
            "\n",
            "**Question**: What types of errors did you find in the AI-generated code? Which were easiest to spot, and which were harder? What strategies helped you find errors?\n",
            "\n",
            "**Your Answer**:\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "---\n"
        ]
    })
    
    # Reflection Question 2
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Reflection Question 2: Statistical Validation (≤150 words)\n",
            "\n",
            "**Question**: How did you validate the AI's statistical recommendation? What questions did you ask yourself? What would you do differently next time?\n",
            "\n",
            "**Your Answer**:\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "---\n"
        ]
    })
    
    # Reflection Question 3
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Reflection Question 3: Trust vs. Verify (≤150 words)\n",
            "\n",
            "**Question**: Based on this lesson, how do you balance trusting AI tools with verifying their outputs? When is it okay to trust AI, and when must you verify?\n",
            "\n",
            "**Your Answer**:\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "---\n"
        ]
    })
    
    # Reflection Question 4
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Reflection Question 4: Application (≤150 words)\n",
            "\n",
            "**Question**: How will you apply validation strategies from this lesson to your future research? What will you always check when using AI for materials science analysis?\n",
            "\n",
            "**Your Answer**:\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "---\n"
        ]
    })
    
    # Assignment Deliverables
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Assignment Deliverables\n",
            "\n",
            "**Due**: End of Week 9  \n",
            "**Points**: 50 points\n",
            "\n",
            "### Required Submissions:\n",
            "\n",
            "1. **Completed Notebook** (45 points)\n",
            "   - All code cells completed and run\n",
            "   - All reflection questions answered\n",
            "   - Errors identified and corrected\n",
            "   - Validation checklists completed\n",
            "   - All output visible in notebook\n",
            "\n",
            "2. **AI Chat Logs** (5 points)\n",
            "   - Exported conversations with ChatGPT/Claude\n",
            "   - Include prompts and responses used in this lesson\n",
            "   - Demonstrates your AI interaction process for validation tasks\n",
            "\n",
            "**Submission Format**:\n",
            "- Notebook: `.ipynb` file (all cells run with output visible)\n",
            "- AI logs: PDF or text file\n",
            "\n",
            "---\n"
        ]
    })
    
    # Grading Rubric
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Grading Rubric (50 points)\n",
            "\n",
            "### Guided Activity 1: Code Validation (20 points)\n",
            "\n",
            "| Criterion | Excellent (full points) | Good (80%) | Satisfactory (60%) | Needs Improvement (<60%) | Points |\n",
            "|-----------|------------------------|-----------|-------------------|--------------------------|--------|\n",
            "| **Error Identification** | Identifies 3+ errors with clear explanations | Identifies 2-3 errors with some explanation | Identifies 1-2 errors, explanations unclear | Misses most errors or explanations vague | 8 |\n",
            "| **Code Corrections** | All errors corrected, code runs successfully | Most errors corrected, minor issues remain | Some corrections made but errors remain | Corrections incomplete or incorrect | 7 |\n",
            "| **Validation** | Validates corrections thoroughly, tests work | Basic validation completed | Minimal validation | No validation | 5 |\n",
            "\n",
            "### Guided Activity 2: Statistical Validation (20 points)\n",
            "\n",
            "| Criterion | Excellent (full points) | Good (80%) | Satisfactory (60%) | Needs Improvement (<60%) | Points |\n",
            "|-----------|------------------------|-----------|-------------------|--------------------------|--------|\n",
            "| **AI Recommendation** | AI prompt used, recommendation obtained | AI prompt used, response incomplete | Partial AI interaction | No AI interaction documented | 5 |\n",
            "| **Recommendation Validation** | Thoroughly evaluates recommendation using checklist | Evaluates most checklist items | Basic evaluation | Minimal or no evaluation | 8 |\n",
            "| **Assumption Checking** | Completes assumption checks correctly | Most assumption checks completed | Some checks attempted | Missing or incorrect checks | 7 |\n",
            "\n",
            "### Reflection & Documentation (10 points)\n",
            "\n",
            "| Criterion | Excellent (full points) | Good (80%) | Satisfactory (60%) | Needs Improvement (<60%) | Points |\n",
            "|-----------|------------------------|-----------|-------------------|--------------------------|--------|\n",
            "| **Reflection Questions** | All 4 questions answered thoughtfully, within word limits | 3-4 questions answered, mostly within limits | 2-3 questions answered | Incomplete answers | 5 |\n",
            "| **AI Chat Logs** | Complete logs with prompts and responses for all AI interactions | Most interactions documented | Some documentation missing | Minimal or no documentation | 5 |\n",
            "\n",
            "---\n"
        ]
    })
    
    # Conclusion
    additional_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Congratulations! 🎉\n",
            "\n",
            "You've completed Lesson 5: AI Validation & Critical Evaluation!\n",
            "\n",
            "### Key Skills You've Learned:\n",
            "\n",
            "✅ **Error Detection**: How to identify errors in AI-generated code\n",
            "✅ **Code Validation**: How to test and verify code works correctly\n",
            "✅ **Statistical Validation**: How to critically evaluate AI recommendations\n",
            "✅ **Assumption Checking**: How to verify test assumptions are met\n",
            "✅ **Trust but Verify**: Balancing AI assistance with scientific skepticism\n",
            "\n",
            "### What's Next?\n",
            "\n",
            "In **Lesson 6**, you'll learn to integrate all the tools you've learned (AI, data processing, statistics) into efficient research workflows. You'll discover how to use AI for literature analysis and create reproducible workflows that document all your AI usage.\n",
            "\n",
            "**Remember**: AI is a powerful assistant, but validation is your responsibility. Always verify before trusting!\n",
            "\n",
            "---\n"
        ]
    })
    
    return additional_cells

# Create complete notebook
all_cells = create_complete_lesson_05()
all_cells.extend(add_remaining_cells())

notebook = {
    "cells": all_cells,
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

# Save notebook
with open('05_ai_validation_critical_evaluation.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Lesson 05 notebook created with {len(all_cells)} cells")
print("Notebook saved as: 05_ai_validation_critical_evaluation.ipynb")


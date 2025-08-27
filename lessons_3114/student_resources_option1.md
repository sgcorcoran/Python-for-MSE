# MSE 3114: AI-Augmented Materials Science - Student Resources

**Course:** MSE 3114 - AI-Augmented Materials Science  
**Credits:** 1 credit  
**Prerequisites:** MSE 2114 (Introduction to Python for Materials Science)  

---

## Welcome to MSE 3114!

This resource guide is your comprehensive companion for the AI-Augmented Materials Science course. Here you'll find study guides, troubleshooting tips, AI tool strategies, and additional resources to help you succeed in this innovative course.

## Quick Start Guide

### Before Your First Class
1. **Set up your Python environment** (see Environment Setup section)
2. **Get access to AI tools** (see AI Tools Access section)
3. **Review Python fundamentals** from MSE 2114
4. **Download course materials** and sample datasets

### First Week Checklist
- [ ] Python environment working
- [ ] AI tools accessible
- [ ] Course materials downloaded
- [ ] Lab 1 started
- [ ] Questions prepared for office hours

---

## AI Tools Access and Setup

### Required AI Tools

#### 1. ChatGPT (OpenAI)
- **Access**: [chat.openai.com](https://chat.openai.com)
- **Cost**: Free tier available, Plus ($20/month) recommended
- **Best For**: General analysis planning, code explanation, troubleshooting
- **Setup**: Create account, verify email, start with free tier

#### 2. Claude (Anthropic)
- **Access**: [claude.ai](https://claude.ai)
- [**Cost**: Free tier available, Pro ($20/month) recommended
- **Best For**: Detailed explanations, technical writing, complex analysis
- **Setup**: Create account, verify email, start with free tier

#### 3. GitHub Copilot
- **Access**: [github.com/features/copilot](https://github.com/features/copilot)
- **Cost**: Free for students (GitHub Student Developer Pack)
- **Best For**: Code generation, debugging, best practices
- **Setup**: Apply for GitHub Student Developer Pack, install VS Code extension

#### 4. Local LLMs (Optional but Recommended)
- **Ollama**: [ollama.ai](https://ollama.ai) - Easy local setup
- **LM Studio**: [lmstudio.ai](https://lmstudio.ai) - Advanced local options
- **Best For**: Offline work, data privacy, custom models
- **Setup**: Download and install, download model files

### AI Tool Access Strategies

#### If You Don't Have Premium Access
1. **Use free tiers** strategically (limited but functional)
2. **Form study groups** to share premium features
3. **Use local LLMs** for offline work
4. **Attend AI tool office hours** for group access
5. **Contact instructor** for alternative approaches

#### Maximizing Free Tier Usage
- **Plan your prompts** carefully to minimize iterations
- **Use local LLMs** for initial drafts and testing
- **Combine tools** strategically (e.g., ChatGPT for planning, local LLM for execution)
- **Document everything** to avoid repeating work

---

## Environment Setup

### Python Environment

#### Option 1: Anaconda (Recommended)
```bash
# Download and install Anaconda from anaconda.com
# Then create course environment:

# Create new environment
conda create -n mse3114 python=3.9

# Activate environment
conda activate mse3114

# Install required packages
conda install pandas numpy matplotlib seaborn scipy scikit-learn
pip install polars streamlit plotly psutil

# Verify installation
python -c "import pandas, numpy, matplotlib, seaborn, scipy, sklearn, polars, streamlit, plotly; print('Success!')"
```

#### Option 2: Miniconda (Lightweight)
```bash
# Download and install Miniconda from docs.conda.io
# Then follow same steps as Anaconda above
```

#### Option 3: Virtual Environment
```bash
# If you prefer venv
python -m venv mse3114
source mse3114/bin/activate  # On Windows: mse3114\Scripts\activate
pip install -r requirements.txt
```

### Development Environment

#### VS Code (Recommended)
- **Download**: [code.visualstudio.com](https://code.visualstudio.com)
- **Extensions**: Python, Jupyter, GitHub Copilot
- **Setup**: Install Python extension, select mse3114 environment

#### Jupyter Notebooks
- **Install**: `pip install jupyter notebook`
- **Launch**: `jupyter notebook` in your course directory
- **Kernels**: Ensure mse3114 environment is available

### Troubleshooting Common Setup Issues

#### "Package not found" Errors
```bash
# Solution 1: Update conda
conda update conda

# Solution 2: Use pip for problematic packages
pip install package_name

# Solution 3: Check environment activation
conda activate mse3114
conda list
```

#### "Python not recognized" (Windows)
- Add Python to PATH during installation
- Use Anaconda Prompt instead of Command Prompt
- Check environment variables in System Properties

#### "Permission denied" (Mac/Linux)
```bash
# Use conda instead of pip
conda install package_name

# Or use --user flag
pip install --user package_name
```

---

## Study Strategies

### Weekly Study Plan

#### Before Each Lab
1. **Review previous week's concepts** (30 minutes)
2. **Read new lesson materials** (45 minutes)
3. **Set up any new tools** (15 minutes)
4. **Prepare questions** for lab session

#### During Lab Sessions
1. **Active participation** in guided practice
2. **Take notes** on AI tool usage
3. **Experiment** with different approaches
4. **Ask questions** when stuck

#### After Each Lab
1. **Complete assignment** within 24 hours
2. **Document AI interactions** for submission
3. **Review concepts** that were challenging
4. **Plan next week's preparation**

### AI Tool Learning Strategies

#### Building Prompt Libraries
1. **Start with templates** from course materials
2. **Customize for your needs** and data types
3. **Test and iterate** to improve effectiveness
4. **Organize by task type** (analysis, coding, writing)
5. **Share with classmates** for mutual improvement

#### Effective AI Tool Usage
1. **Plan before prompting** - know what you want
2. **Provide context** - include relevant details
3. **Specify format** - how you want results presented
4. **Validate results** - always check AI-generated output
5. **Iterate and improve** - refine prompts based on results

#### Common Prompt Patterns

**For Data Analysis Planning:**
```
I'm analyzing [data type] with [number] samples and [features]. 
My goal is to [objective]. 
Please help me:
1. Plan my analysis approach
2. Identify appropriate statistical tests
3. Suggest visualization strategies
4. Highlight potential challenges
```

**For Code Generation:**
```
I need to [task description] using [libraries]. 
My data has [structure]. 
Please provide:
1. Complete, working code
2. Comments explaining each step
3. Alternative approaches if applicable
4. Common pitfalls to avoid
```

**For Result Interpretation:**
```
I performed [analysis] and got these results: [results]. 
My data represents [context]. 
Please help me:
1. Interpret these results
2. Identify key insights
3. Suggest next steps
4. Highlight limitations
```

### Time Management

#### Weekly Time Allocation
- **Lecture**: 1 hour
- **Lab**: 2 hours
- **Assignment work**: 3-4 hours
- **Study and review**: 2-3 hours
- **Total**: 8-10 hours per week

#### Project Time Management
- **Week 13**: 8-10 hours (planning and initial work)
- **Week 14**: 12-15 hours (completion and presentation prep)
- **Total**: 20-25 hours for capstone project

---

## Assignment Guidelines

### Lab Assignment Structure

#### Required Components
1. **Working code** that executes without errors
2. **AI interaction logs** documenting all AI tool usage
3. **Results and analysis** with appropriate interpretation
4. **Documentation** including comments and explanations

#### AI Interaction Documentation
For each AI tool interaction, document:
- **Tool used**: ChatGPT, Claude, GitHub Copilot, etc.
- **Prompt/question**: What you asked
- **Response received**: What the AI provided
- **How you used it**: How you applied the AI's response
- **Validation**: How you verified the AI's suggestions

#### Example AI Interaction Log
```python
# AI Interaction Log - Lab 1
# Date: [Date]
# Tool: ChatGPT
# Prompt: "I need help calculating the yield strength from stress-strain data. 
#         My data has columns for stress (MPa) and strain (mm/mm). 
#         What's the best method to identify the yield point?"
# Response: [AI's response]
# Usage: Used AI's suggestion to implement 0.2% offset method
# Validation: Compared results with manual calculation - matched within 2%
```

### Submission Checklist

#### Before Submitting
- [ ] Code runs without errors
- [ ] All AI interactions documented
- [ ] Results clearly presented
- [ ] Code well-commented
- [ ] Assignment requirements met
- [ ] File format correct
- [ ] Submitted on time

#### Common Submission Mistakes
1. **Missing AI interaction logs** - required for full credit
2. **Uncommented code** - makes grading difficult
3. **Missing results** - incomplete analysis
4. **Late submission** - automatic grade deduction
5. **Wrong file format** - check submission requirements

---

## Troubleshooting Guide

### Common Python Errors

#### Import Errors
```python
# Error: ModuleNotFoundError: No module named 'pandas'
# Solution: Activate correct environment
conda activate mse3114

# Error: ImportError: DLL load failed
# Solution: Reinstall package or use conda instead of pip
conda install package_name
```

#### Data Processing Errors
```python
# Error: KeyError: 'column_name'
# Solution: Check column names in your data
print(df.columns.tolist())

# Error: ValueError: Length mismatch
# Solution: Check data shapes before operations
print(f"Data shape: {df.shape}")
```

#### AI Tool Errors

**ChatGPT/Claude Not Responding:**
- Check internet connection
- Try refreshing the page
- Use different browser
- Check if service is down

**GitHub Copilot Not Working:**
- Verify GitHub Student Developer Pack access
- Check VS Code extension installation
- Restart VS Code
- Check authentication status

**Local LLM Issues:**
- Check model file downloads
- Verify system requirements
- Check available memory
- Restart application

### Performance Issues

#### Slow Data Processing
```python
# Use Polars instead of pandas for large datasets
import polars as pl
df = pl.read_csv("large_file.csv")

# Process data in chunks
chunk_size = 10000
for chunk in pd.read_csv("large_file.csv", chunksize=chunk_size):
    # Process chunk
    pass
```

#### Memory Issues
```python
# Use lazy evaluation with Polars
df = pl.scan_csv("large_file.csv")
result = df.filter(pl.col("value") > 0).collect()

# Clear variables when done
del large_dataframe
import gc
gc.collect()
```

#### Streamlit Performance
```python
# Use caching for expensive operations
@st.cache_data
def expensive_calculation(data):
    # Your calculation here
    return result

# Load data efficiently
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

---

## Additional Learning Resources

### Python and Data Science

#### Online Courses
- **DataCamp**: Python for Data Science
- **Coursera**: Applied Data Science with Python
- **edX**: Introduction to Python Programming
- **YouTube**: FreeCodeCamp Python Tutorials

#### Books
- **"Python for Data Analysis"** by Wes McKinney
- **"Python Data Science Handbook"** by Jake VanderPlas
- **"Effective Python"** by Brett Slatkin
- **"Fluent Python"** by Luciano Ramalho

#### Documentation
- **Python**: [docs.python.org](https://docs.python.org)
- **Pandas**: [pandas.pydata.org](https://pandas.pydata.org)
- **NumPy**: [numpy.org](https://numpy.org)
- **Matplotlib**: [matplotlib.org](https://matplotlib.org)

### Materials Science

#### Online Resources
- **Materials Project**: [materialsproject.org](https://materialsproject.org)
- **NIST Materials Database**: [materialsdata.nist.gov](https://materialsdata.nist.gov)
- **ASM Materials Database**: [asminternational.org](https://asminternational.org)
- **Springer Materials**: [materials.springer.com](https://materials.springer.com)

#### Journals and Publications
- **Materials Science and Engineering A**
- **Acta Materialia**
- **Journal of Materials Research**
- **Materials & Design**

### AI and Machine Learning

#### AI Tool Tutorials
- **OpenAI**: [platform.openai.com/docs](https://platform.openai.com/docs)
- **Anthropic**: [docs.anthropic.com](https://docs.anthropic.com)
- **GitHub Copilot**: [github.com/features/copilot](https://github.com/features/copilot)
- **Prompt Engineering**: [promptingguide.ai](https://promptingguide.ai)

#### ML Resources
- **Scikit-learn**: [scikit-learn.org](https://scikit-learn.org)
- **Kaggle**: [kaggle.com](https://kaggle.com) - datasets and competitions
- **Google Colab**: [colab.research.google.com](https://colab.research.google.com)
- **Fast.ai**: [fast.ai](https://fast.ai) - practical ML courses

---

## Study Groups and Collaboration

### Forming Study Groups
1. **Find classmates** with similar schedules
2. **Set regular meeting times** (weekly or bi-weekly)
3. **Share resources** and AI tool strategies
4. **Practice together** on assignments
5. **Review each other's work** for learning

### Collaboration Guidelines
- **Share knowledge** but don't copy code
- **Discuss approaches** and strategies
- **Help troubleshoot** technical issues
- **Review AI prompts** and responses
- **Practice presentations** together

### Office Hours Strategy
1. **Prepare specific questions** before attending
2. **Bring your code** and error messages
3. **Document solutions** for future reference
4. **Ask about AI tool strategies** and best practices
5. **Get feedback** on your approach

---

## Success Tips

### General Strategies
1. **Start early** - don't wait until the last minute
2. **Practice regularly** - use AI tools daily
3. **Document everything** - keep detailed logs
4. **Ask questions** - don't struggle in silence
5. **Form study groups** - learn from peers

### AI Tool Mastery
1. **Experiment freely** - try different approaches
2. **Build your library** - collect effective prompts
3. **Validate everything** - don't trust AI blindly
4. **Learn from failures** - improve your prompts
5. **Share successes** - help classmates improve

### Technical Skills
1. **Understand the basics** - don't just copy code
2. **Practice debugging** - learn to fix errors
3. **Optimize performance** - use appropriate tools
4. **Document your code** - future you will thank you
5. **Stay current** - follow tool updates and improvements

---

## Getting Help

### When to Ask for Help
- **After trying** for 15-20 minutes
- **When you're completely stuck** on a concept
- **If you get the same error** multiple times
- **When AI tools aren't helping** solve the problem
- **Before falling behind** on assignments

### How to Ask for Help
1. **Be specific** about your problem
2. **Include error messages** and code snippets
3. **Show what you've tried** already
4. **Explain your goal** clearly
5. **Be patient** with response times

### Where to Get Help
1. **Office hours** - instructor and TA support
2. **Discussion board** - peer help and collaboration
3. **Study groups** - collaborative problem-solving
4. **Online resources** - documentation and tutorials
5. **AI tools** - for initial troubleshooting

---

## Course Calendar and Deadlines

### Important Dates
- **Lab 1 Due**: End of Week 2
- **Lab 2 Due**: End of Week 4
- **Lab 3 Due**: End of Week 6
- **Lab 4 Due**: End of Week 8
- **Lab 5 Due**: End of Week 10
- **Lab 6 Due**: End of Week 12
- **Capstone Project Due**: End of Week 14
- **Final Presentations**: Week 15

### Weekly Schedule
- **Monday**: Review previous week, prepare for new content
- **Tuesday**: Lecture and lab introduction
- **Wednesday-Friday**: Lab work and assignment completion
- **Weekend**: Review, study, and prepare for next week

---

## Conclusion

MSE 3114 is designed to be both challenging and rewarding. By strategically integrating AI tools with traditional materials science analysis, you'll develop skills that are increasingly valuable in modern research and industry.

Remember:
- **AI tools are assistants**, not replacements for your thinking
- **Practice makes perfect** - use these tools regularly
- **Document everything** - it helps with learning and grading
- **Ask for help** when you need it
- **Collaborate with classmates** - you can learn from each other

Good luck with your studies! The skills you develop in this course will serve you well in your future materials science career.

---

## Quick Reference

### Essential Commands
```bash
# Environment management
conda activate mse3114
conda list
conda install package_name

# Package installation
pip install package_name
pip list

# Python execution
python script.py
jupyter notebook
```

### Common Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import polars as pl
import streamlit as st
import plotly.express as px
from scipy import stats
from sklearn import metrics
```

### AI Tool URLs
- **ChatGPT**: [chat.openai.com](https://chat.openai.com)
- **Claude**: [claude.ai](https://claude.ai)
- **GitHub Copilot**: [github.com/features/copilot](https://github.com/features/copilot)
- **Ollama**: [ollama.ai](https://ollama.ai)

### Course Resources
- **Lesson Materials**: Check course management system
- **Sample Datasets**: Download from course resources
- **Office Hours**: Check instructor schedule
- **Discussion Board**: Post questions and share insights


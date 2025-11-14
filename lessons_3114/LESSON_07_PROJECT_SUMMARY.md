# Lesson 07: Practical Research Project - Summary
## Choices, Content, and Approach

---

## Project Overview

**Duration**: 2 weeks (Weeks 11-12)  
**Total Time**: 6 hours (3 hours per week)  
**Approach**: Structured, scaffolded project with milestones and validation checkpoints

**Purpose**: Apply all learned skills (Lessons 01-06) to a real materials science research question, with emphasis on:
- Systematic validation of AI outputs (from Lesson 05)
- Integrated workflows (from Lesson 06)
- Documentation for reproducibility
- Critical evaluation of results

---

## Project Choices

Students select **ONE** of three project options:

### **Option A: Composition-Property Relationships**

**Research Question**: How do alloy composition variables (e.g., Cu, Mg, Si content) relate to mechanical properties (e.g., yield strength, hardness)?

**What Students Do**:
- Analyze composition data and mechanical properties
- Identify correlations between composition and properties
- Use statistical analysis to quantify relationships
- Create visualizations showing relationships

**Skills Used**: Data loading, statistical analysis, correlation analysis, visualization

**Key Analyses**:
- Correlation analysis (Pearson/Spearman correlation)
- Scatter plots to visualize relationships
- Linear regression (if appropriate)

---

### **Option B: Processing Optimization**

**Research Question**: What are the optimal heat treatment conditions (temperature, time) for achieving target mechanical properties?

**What Students Do**:
- Analyze experimental data with different processing conditions
- Compare treatment groups statistically
- Identify optimal conditions based on analysis
- Create visualizations comparing treatments

**Skills Used**: Statistical comparison, group analysis, visualization, optimization

**Key Analyses**:
- Group comparison tests (t-test, Mann-Whitney U)
- Boxplots comparing treatments
- Assumption checking (normality, equal variances)

---

### **Option C: Material Classification**

**Research Question**: Can materials be classified based on their properties? What properties best distinguish material types?

**What Students Do**:
- Analyze property data for different material types
- Use statistical tests to compare property distributions
- Identify which properties best distinguish materials
- Create visualizations showing classification

**Skills Used**: Statistical comparison, property analysis, visualization, classification

**Key Analyses**:
- Comparison of property distributions across material types
- Multiple group comparison tests
- Visualization of property differences

---

## Project Structure & Approach

### **Week 11: Planning & Analysis (3 hours)**

#### **Phase 1: Project Selection (30 min)**
- Review all three project options
- Choose based on interest and available data
- Document selection and rationale

#### **Phase 2: AI-Assisted Planning (60 min)**
- **Step 1**: Create planning prompt (15 min)
  - Use AI to help plan project systematically
  - Prompt template provided with customization guidance
  - Request: data needs, analyses, visualizations, workflow, time estimates

- **Step 2**: Validate and refine plan (15 min)
  - **Critical validation** (from Lesson 05): Evaluate AI's plan
  - Validation checklist:
    - Does plan address research question?
    - Are analyses appropriate for data type?
    - Is workflow logical and achievable?
    - Are time estimates realistic?
    - Does plan include validation steps?
    - Does plan include documentation?
  - Create validated, refined project plan (4-6 steps)

#### **Phase 3: Data Collection & Initial Analysis (90 min)**
- **Step 1**: Data collection (15 min)
  - **Three data options**:
    1. Use data from previous lessons (heat treatment, alloy data)
    2. Use provided project datasets (if available on Canvas)
    3. Use publicly available materials science datasets (Matbench, NIST)
  - Document data source and description

- **Step 2**: Load and validate data (15 min)
  - Load data using skills from Lesson 01
  - **Validation Checkpoint 1**: Data loading
    - Check data shape, columns, missing values, data types
    - Validation checklist provided
    - Document validation summary

- **Step 3**: Exploratory data analysis (20 min)
  - Calculate descriptive statistics
  - Create initial visualizations based on project type:
    - **Option A**: Scatter plots (composition vs properties)
    - **Option B**: Boxplots (treatments comparison)
    - **Option C**: Boxplots/histograms (material types comparison)
  - Use skills from Lesson 04

- **Step 4**: Statistical analysis (25 min)
  - Choose appropriate statistical test based on project type:
    - **Option A**: Correlation analysis (Pearson/Spearman)
    - **Option B**: Group comparison (t-test, Mann-Whitney U)
    - **Option C**: Multiple group comparison
  - Check assumptions (normality, equal variances)
  - Run statistical test
  - **Validation Checkpoint 2**: Statistical analysis
    - Validate test appropriateness
    - Check assumptions
    - Verify interpretation
    - Validation checklist provided

- **Step 5**: Initial results summary (15 min)
  - Summarize findings from Week 11
  - Document any issues or questions
  - Prepare for Week 12 completion

---

### **Week 12: Completion & Documentation (3 hours)**

#### **Phase 4: Complete Analysis & Validation (90 min)**

- **Step 1**: Finalize statistical analysis (30 min)
  - Complete any remaining analysis
  - Verify all results are correct
  - Create final visualizations
  - **Validation Checkpoint 3**: Final results
    - Validate all analyses completed
    - Verify results make sense
    - Check domain knowledge (are results reasonable?)

- **Step 2**: Validate all AI outputs (30 min)
  - **Critical from Lesson 05**: Validate all AI-generated code and recommendations
  - Use validation checklist from Lesson 05
  - Verify all statistical tests are appropriate
  - Check all visualizations are correct
  - Document validation process

- **Step 3**: Prepare final results (30 min)
  - Organize all results clearly
  - Create summary tables/figures
  - Ensure all output visible in notebook
  - Document any limitations or issues

#### **Phase 5: Documentation & Report Writing (90 min)**

- **Step 1**: Workflow documentation (30 min)
  - Document all AI tool usage:
    - Which tool used (ChatGPT, Claude, Cursor)
    - When used (which step)
    - Why used (what task)
    - What was validated
  - Document workflow steps
  - Note any challenges or solutions

- **Step 2**: Technical report writing (60 min)
  - Write 3-4 page technical report
  - **Report sections**:
    1. Introduction (research question, project choice)
    2. Methods (data source, analysis approach)
    3. Results (statistical findings, visualizations)
    4. Discussion (interpretation, limitations)
    5. Conclusion (key findings, implications)
  - Use AI assistance for writing (but validate!)
  - Include all figures and tables
  - Cite sources appropriately

---

## Key Features & Approach

### **Structured Scaffolding**
- **Clear milestones** at each phase
- **Time estimates** for each step
- **Validation checkpoints** at critical points
- **Step-by-step guidance** throughout

### **Validation Integration**
- **Three validation checkpoints**:
  1. Data loading validation
  2. Statistical analysis validation
  3. Final results validation
- Uses validation strategies from Lesson 05
- Emphasizes "trust but verify" approach

### **AI Integration**
- AI-assisted project planning (with validation)
- AI assistance throughout (with validation)
- Documentation of all AI usage
- Emphasis on validating all AI outputs

### **Workflow Integration**
- Uses integrated workflows from Lesson 06
- Combines all tools learned (AI, data processing, statistics, visualization)
- Documents complete workflow for reproducibility

### **Flexible Data Options**
- Students can use data from previous lessons
- Can use provided datasets
- Can use publicly available materials science datasets
- Accommodates different comfort levels

### **Realistic Scope**
- 6 hours total (3 hours per week)
- Focus on quality over quantity
- Achievable for students with different skill levels
- Multiple project options to match interests

---

## Deliverables (100 points total)

1. **Project Notebook** (40 points)
   - Well-organized Jupyter notebook
   - All analysis with output visible
   - All validation checkpoints completed
   - Workflow documentation included

2. **Technical Report** (40 points)
   - 3-4 page professional report
   - Clear sections: Introduction, Methods, Results, Discussion, Conclusion
   - All figures and tables included
   - Proper citations

3. **Workflow Documentation** (20 points)
   - Complete AI usage log
   - Workflow steps documented
   - Validation process documented
   - Reflection on challenges and solutions

**Optional but Recommended**: AI chat logs (ChatGPT/Claude conversations) demonstrating AI interaction process

---

## Support for Student Concerns (from Survey)

### **Addresses 54% concern about "capstone project - independent work"**:
- ✅ **Structured milestones** instead of open-ended project
- ✅ **Clear checkpoints** at each phase
- ✅ **Step-by-step guidance** throughout
- ✅ **Multiple project options** (not one-size-fits-all)
- ✅ **Realistic scope** (6 hours, not unlimited)

### **Addresses 50% concern about "time constraints"**:
- ✅ **Clear time estimates** for each step
- ✅ **Realistic 3-hour/week** commitment
- ✅ **Flexible data options** (can use previous lesson data)
- ✅ **Focus on quality** over quantity

### **Addresses concerns about complexity**:
- ✅ **Validation checkpoints** prevent errors early
- ✅ **Scaffolded structure** builds confidence
- ✅ **Uses familiar skills** from previous lessons
- ✅ **Clear guidance** at each step

---

## Learning Progression

**Builds on previous lessons**:
- **Lesson 01**: Data loading and validation
- **Lesson 02**: Prompt engineering for planning
- **Lesson 03**: Data processing and visualization
- **Lesson 04**: Statistical analysis
- **Lesson 05**: Validation of AI outputs (critical!)
- **Lesson 06**: Integrated workflows

**Integration emphasis**:
- Students must use skills from all previous lessons
- Must validate all AI outputs (Lesson 05)
- Must use integrated workflows (Lesson 06)
- Must document everything for reproducibility

---

## Summary

**Approach**: Structured, scaffolded project with clear milestones and validation checkpoints

**Choices**: Three project options (Composition-Property, Processing Optimization, Material Classification)

**Content**: Complete research workflow from planning → data → analysis → validation → documentation → reporting

**Time**: 6 hours over 2 weeks (3 hours per week)

**Support**: Step-by-step guidance, validation checkpoints, flexible data options, multiple project choices

**Focus**: Quality over quantity, validation of AI outputs, documentation for reproducibility, realistic scope


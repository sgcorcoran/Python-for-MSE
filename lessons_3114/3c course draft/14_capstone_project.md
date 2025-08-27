# MSE 3114 Capstone Project: AI-Augmented Materials Science Research

## Project Overview
**Duration**: 2 weeks  
**Team Size**: 2-3 students  
**Deliverables**: Research report, interactive dashboard, presentation, code repository

This capstone project challenges you to apply all the AI-augmented materials science techniques learned throughout the course to solve a real-world materials problem. You'll work as a research team to design experiments, collect/analyze data, and present findings using modern AI tools and data science techniques.

## Project Phases

### Week 1: Research Design and Data Collection

#### Phase 1.1: Problem Definition and Literature Review (Days 1-2)
**Objective**: Define a materials science research question and conduct AI-assisted literature review

**Tasks**:
1. **Choose one of these research areas**:
   - **Alloy Optimization**: Design a new aluminum alloy composition for improved strength-to-weight ratio
   - **Heat Treatment Process**: Optimize heat treatment parameters for steel microstructural control
   - **Composite Materials**: Develop a polymer-ceramic composite with enhanced mechanical properties
   - **Surface Engineering**: Optimize coating parameters for corrosion resistance
   - **Additive Manufacturing**: Optimize 3D printing parameters for metal parts

2. **AI-Assisted Literature Review**:
   ```python
   # Use the research workflow techniques from Lesson 13
   # Create a literature database and identify research gaps
   # Generate a synthesis of current state-of-the-art
   ```

3. **Research Question Formulation**:
   - Define specific, measurable objectives
   - Identify key variables and constraints
   - Establish success criteria

**Deliverable**: 2-page research proposal with literature synthesis

#### Phase 1.2: Experimental Design (Days 3-4)
**Objective**: Design experiments using AI-enhanced DOE principles

**Tasks**:
1. **Parameter Space Definition**:
   - Identify 4-6 key process/material parameters
   - Define realistic ranges for each parameter
   - Establish measurement methods for responses

2. **AI-Enhanced Experimental Design**:
   ```python
   # Use techniques from Lesson 5
   # Implement Latin Hypercube Sampling
   # Optimize sample size for statistical power
   # Consider constraints and practical limitations
   ```

3. **Data Collection Plan**:
   - Create standardized data collection protocols
   - Design data validation checks
   - Plan for data storage and version control

**Deliverable**: Experimental design matrix and data collection protocols

#### Phase 1.3: Data Collection and Initial Processing (Days 5-7)
**Objective**: Execute experiments and establish data pipeline

**Tasks**:
1. **Execute Experiments**:
   - Follow designed protocols
   - Document all experimental conditions
   - Collect raw data in multiple formats

2. **Data Pipeline Setup**:
   ```python
   # Use modern data stack from Lesson 3
   # Implement automated data import and cleaning
   # Create data validation checks
   # Set up version control for datasets
   ```

3. **Initial Data Exploration**:
   - Generate basic statistics and visualizations
   - Identify data quality issues
   - Plan data preprocessing steps

**Deliverable**: Raw dataset with metadata and initial exploration report

### Week 2: Analysis, Modeling, and Presentation

#### Phase 2.1: Advanced Data Analysis (Days 8-9)
**Objective**: Apply comprehensive statistical and ML analysis

**Tasks**:
1. **Statistical Analysis**:
   ```python
   # Use techniques from Lesson 4
   # Perform normality tests, correlation analysis
   # Conduct hypothesis testing
   # Generate automated statistical reports
   ```

2. **Machine Learning Modeling**:
   ```python
   # Apply techniques from Lesson 9
   # Train multiple ML models
   # Perform feature importance analysis
   # Optimize hyperparameters
   ```

3. **Model Validation**:
   - Implement cross-validation strategies
   - Generate comprehensive performance metrics
   - Analyze prediction accuracy and reliability

**Deliverable**: Statistical analysis report and ML model performance analysis

#### Phase 2.2: Optimization and Advanced Modeling (Days 10-11)
**Objective**: Optimize process parameters and validate models

**Tasks**:
1. **Parameter Optimization**:
   ```python
   # Use optimization techniques from Lesson 11
   # Implement multi-objective optimization
   # Generate Pareto frontiers
   # Validate optimal solutions
   ```

2. **Advanced Modeling**:
   ```python
   # Apply curve fitting from Lesson 7
   # Implement physics-based models
   # Generate confidence and prediction bands
   # Perform sensitivity analysis
   ```

3. **Validation and Verification**:
   - Test models on new data
   - Perform uncertainty analysis
   - Validate against physical principles

**Deliverable**: Optimization results and advanced model validation

#### Phase 2.3: Dashboard Development and Final Report (Days 12-13)
**Objective**: Create interactive visualizations and comprehensive documentation

**Tasks**:
1. **Interactive Dashboard**:
   ```python
   # Use Streamlit and Plotly from Lessons 3 and 8
   # Create interactive parameter exploration tools
   # Implement real-time model predictions
   # Include data visualization and analysis tools
   ```

2. **Final Report Generation**:
   - Executive summary and key findings
   - Methodology and experimental design
   - Results and statistical analysis
   - Model performance and optimization results
   - Conclusions and recommendations
   - Future work and limitations

3. **Presentation Preparation**:
   - 15-minute technical presentation
   - Live demonstration of dashboard
   - Q&A session

**Deliverable**: Interactive dashboard, comprehensive report, and presentation

## Technical Requirements

### AI Tools Integration
- **ChatGPT/Claude**: Use for literature review, hypothesis generation, and report writing assistance
- **GitHub Copilot**: Implement for code development and optimization
- **Local LLMs**: Use for data analysis planning and interpretation

### Data Science Stack
- **Data Processing**: Polars for large datasets, DuckDB for complex queries
- **Visualization**: Plotly for interactive plots, Matplotlib/Seaborn for publication figures
- **Machine Learning**: Scikit-learn for modeling, Scipy for optimization
- **Image Analysis**: OpenCV for materials characterization (if applicable)

### Code Quality Standards
- **Version Control**: Git repository with clear commit history
- **Documentation**: Comprehensive docstrings and README files
- **Testing**: Unit tests for critical functions
- **Reproducibility**: Requirements.txt and environment setup

## Assessment Criteria

### Technical Implementation (40%)
- **Code Quality**: Clean, efficient, well-documented code
- **AI Integration**: Effective use of AI tools throughout the process
- **Data Pipeline**: Robust data collection, processing, and validation
- **Model Performance**: Accurate and validated models

### Analysis and Results (30%)
- **Statistical Rigor**: Appropriate statistical tests and validation
- **Model Selection**: Justified choice of models and parameters
- **Optimization**: Effective parameter optimization and validation
- **Interpretation**: Clear understanding of results and limitations

### Presentation and Communication (20%)
- **Report Quality**: Clear, professional, comprehensive documentation
- **Dashboard Functionality**: Interactive, user-friendly interface
- **Presentation**: Clear, engaging, technically accurate delivery
- **Q&A Performance**: Ability to defend methods and results

### Innovation and Creativity (10%)
- **Novel Approaches**: Creative use of AI tools and techniques
- **Problem Solving**: Innovative solutions to technical challenges
- **Integration**: Effective combination of multiple course concepts

## Submission Requirements

### 1. Code Repository
- **GitHub/GitLab repository** with complete project code
- **README.md** with setup instructions and project overview
- **requirements.txt** with all dependencies
- **Jupyter notebooks** or Python scripts for each phase

### 2. Interactive Dashboard
- **Streamlit application** with all major functionality
- **Deployed URL** or local setup instructions
- **User manual** for dashboard operation

### 3. Final Report
- **PDF format** (15-20 pages)
- **Executive summary** (1 page)
- **Technical details** with code snippets
- **Results and analysis** with figures and tables
- **Conclusions and recommendations**

### 4. Presentation
- **15-minute technical presentation**
- **Live demonstration** of key features
- **Slides** in PDF or PowerPoint format

## Timeline and Milestones

### Week 1 Milestones
- **Day 2**: Research proposal submitted
- **Day 4**: Experimental design approved
- **Day 7**: Initial data collection complete

### Week 2 Milestones
- **Day 9**: Statistical analysis complete
- **Day 11**: Optimization and modeling complete
- **Day 13**: Final deliverables submitted

## Resources and Support

### Course Materials
- All 13 weekly lessons provide relevant techniques
- Course support files contain sample datasets
- Instructor office hours for technical questions

### AI Tools Access
- ChatGPT Plus or Claude Pro recommended
- GitHub Copilot for code development
- Local LLM setup instructions provided

### Technical Support
- **Instructor Office Hours**: Available daily during project period
- **Peer Collaboration**: Encouraged within teams
- **Online Resources**: Documentation and tutorials linked

## Example Project: AI-Optimized Heat Treatment Process

### Research Question
"How can we optimize the heat treatment parameters (temperature, time, cooling rate) for AISI 4140 steel to achieve maximum hardness while maintaining acceptable toughness?"

### Key Parameters
- **Temperature**: 800-950°C
- **Hold Time**: 30-120 minutes
- **Cooling Rate**: 0.5-5°C/min
- **Quenching Medium**: Oil vs. Air

### Expected Outcomes
- **Statistical Models**: Parameter-response relationships
- **Optimization Results**: Pareto-optimal solutions
- **Validation**: Experimental confirmation of predictions
- **Dashboard**: Interactive parameter exploration tool

## Success Tips

1. **Start Early**: Begin literature review immediately
2. **Plan Thoroughly**: Detailed experimental design saves time later
3. **Document Everything**: Version control and metadata are crucial
4. **Test Incrementally**: Validate each component before moving forward
5. **Use AI Effectively**: Leverage AI tools for planning and analysis
6. **Collaborate**: Team members should complement each other's skills
7. **Focus on Quality**: Better to do fewer things well than many things poorly

## Final Notes

This capstone project represents the culmination of your learning in MSE 3114. It's designed to be challenging but achievable, requiring you to integrate concepts from across the course while applying them to a real materials science problem. The AI tools you've learned will be invaluable throughout the process, helping you work more efficiently and creatively than traditional approaches would allow.

Remember: The goal is not just to complete the project, but to demonstrate mastery of AI-augmented materials science techniques and to produce work that could contribute to real research or industrial applications.

**Good luck with your research!** 🚀

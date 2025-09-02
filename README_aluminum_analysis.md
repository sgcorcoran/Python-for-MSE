# Aluminum 7075-T6 Tensile Test Analysis

This repository contains comprehensive tools for analyzing aluminum 7075-T6 tensile test data to extract mechanical properties and validate results.

## 📁 Files Included

- **`aluminum_7075_tensile_analysis.py`** - Main analysis script with the `TensileTestAnalyzer` class
- **`aluminum_7075_analysis_guide.md`** - Comprehensive analysis guide and methodology
- **`example_usage.py`** - Example script showing how to use the analyzer
- **`requirements.txt`** - Required Python packages
- **`README_aluminum_analysis.md`** - This file

## 🚀 Quick Start

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

### 2. Run the Example
```bash
python example_usage.py
```

### 3. Or Run the Full Analysis Directly
```bash
python aluminum_7075_tensile_analysis.py
```

## 🔧 How to Use

### Basic Usage
```python
from aluminum_7075_tensile_analysis import TensileTestAnalyzer

# Initialize analyzer
analyzer = TensileTestAnalyzer(
    data_file='data_files/Al7075_out.xlsx',
    cross_sectional_area_mm2=25.0
)

# Run complete analysis
analyzer.run_complete_analysis()
```

### Step-by-Step Analysis
```python
# Load data
analyzer.load_data()

# Determine mechanical properties
analyzer.determine_elastic_modulus()
analyzer.determine_yield_strength()
analyzer.determine_tensile_strength()
analyzer.determine_elongation()
analyzer.calculate_toughness()

# Generate plots
analyzer.plot_stress_strain()

# Validate results
analyzer.validate_results()

# Export results
analyzer.export_results()
```

## 📊 What You'll Get

### Mechanical Properties
- **Elastic Modulus** (GPa)
- **Yield Strength** (MPa) - using 0.2% offset method
- **Ultimate Tensile Strength** (MPa)
- **Elongation at Fracture** (%)
- **Toughness** (MJ/m³)

### Visualizations
- Full stress-strain curve
- Initial region plots for detailed analysis
- Elastic modulus fitting plots
- Yield strength determination plots

### Output Files
- **Excel file** with multiple sheets containing results, data, and parameters
- **High-resolution PNG plots** for reports and presentations
- **Console output** with detailed analysis results

## 📋 Analysis Steps

1. **Data Loading** - Import Excel file with tensile test data
2. **Stress-Strain Calculation** - Convert load/displacement to stress/strain
3. **Property Extraction** - Determine mechanical properties using standard methods
4. **Validation** - Compare results with expected ranges for Al 7075-T6
5. **Export** - Save results and plots for reporting

## ⚠️ Important Notes

- **Cross-sectional area**: You may need to adjust the `cross_sectional_area_mm2` parameter based on your specimen geometry
- **Data format**: The script expects columns for load, displacement, time, and optionally stress/strain
- **Units**: Ensure your data uses consistent units (N for load, mm for displacement, mm² for area)

## 🎯 Expected Results for Al 7075-T6

| Property | Expected Range |
|----------|----------------|
| Elastic Modulus | 70-75 GPa |
| Yield Strength | 450-550 MPa |
| Tensile Strength | 520-600 MPa |
| Elongation | 8-15% |

## 🔍 Troubleshooting

### Common Issues
- **Import errors**: Make sure all required packages are installed
- **File not found**: Check that your data files are in the correct location
- **Poor curve fits**: Adjust the strain range for elastic modulus calculation
- **Anomalous values**: Verify your cross-sectional area and data quality

### Getting Help
1. Check the console output for error messages
2. Verify your data file format and units
3. Review the analysis guide for methodology details
4. Ensure all required packages are installed

## 📚 Additional Resources

- **Analysis Guide**: See `aluminum_7075_analysis_guide.md` for detailed methodology
- **ASTM Standards**: E8 (tensile testing), E111 (elastic modulus)
- **Materials Literature**: Callister's Materials Science textbook
- **Course Materials**: Check your MSE course resources for specific requirements

## 🎓 For Students

This analysis follows standard materials science practices and ASTM testing standards. The results can be used for:

- Course assignments and reports
- Laboratory write-ups
- Research projects
- Material property databases

## 📝 Customization

You can modify the analysis by:

- Adjusting strain ranges for property determination
- Changing the offset strain for yield strength (default: 0.002)
- Adding custom validation criteria
- Modifying plot styles and formats
- Extending to other materials or test types

---

**Happy Analyzing!** 🧪📊

If you have questions or need help, refer to the analysis guide or check your course materials.







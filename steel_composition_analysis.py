import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import re

def parse_composition(comp_string):
    """Parse composition string to extract elemental concentrations"""
    # Extract all element concentrations using regex
    pattern = r'([A-Z][a-z]?)(\d+\.?\d*)'
    matches = re.findall(pattern, comp_string)
    
    composition = {}
    for element, concentration in matches:
        composition[element] = float(concentration)
    
    return composition

# Read the JSON data
with open('C:/Users/sgc/OneDrive - Virginia Tech/Dev/GitHub/Python-for-MSE/data_files/database/steels_yield.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['data'], columns=data['columns'])

# Filter for the two ranges
range1 = df[(df['yield strength'] >= 1230) & (df['yield strength'] <= 1330)].copy()
range2 = df[(df['yield strength'] >= 1480) & (df['yield strength'] <= 1830)].copy()

print(f"Range 1 (1230-1330 MPa): {len(range1)} samples")
print(f"Range 2 (1480-1830 MPa): {len(range2)} samples")

# Parse compositions for both ranges
print("\nParsing compositions...")
range1_compositions = []
for idx, row in range1.iterrows():
    comp = parse_composition(row['composition'])
    comp['yield_strength'] = row['yield strength']
    range1_compositions.append(comp)

range2_compositions = []
for idx, row in range2.iterrows():
    comp = parse_composition(row['composition'])
    comp['yield_strength'] = row['yield strength']
    range2_compositions.append(comp)

# Convert to DataFrames
df1 = pd.DataFrame(range1_compositions)
df2 = pd.DataFrame(range2_compositions)

# Get all unique elements
all_elements = set(df1.columns) | set(df2.columns)
all_elements.discard('yield_strength')  # Remove yield strength column
all_elements = sorted(list(all_elements))

print(f"\nFound {len(all_elements)} unique elements: {all_elements}")

# Fill NaN values with 0 (elements not present)
for element in all_elements:
    if element not in df1.columns:
        df1[element] = 0
    if element not in df2.columns:
        df2[element] = 0

# Calculate statistics for each element
print("\n=== COMPOSITIONAL ANALYSIS ===")
results = []

for element in all_elements:
    values1 = df1[element].values
    values2 = df2[element].values
    
    # Calculate means
    mean1 = np.mean(values1)
    mean2 = np.mean(values2)
    
    # Calculate standard deviations
    std1 = np.std(values1)
    std2 = np.std(values2)
    
    # Perform t-test
    if len(values1) > 1 and len(values2) > 1 and (std1 > 0 or std2 > 0):
        t_stat, p_value = stats.ttest_ind(values1, values2)
    else:
        t_stat, p_value = np.nan, np.nan
    
    # Calculate effect size (Cohen's d)
    if std1 > 0 or std2 > 0:
        pooled_std = np.sqrt(((len(values1)-1)*std1**2 + (len(values2)-1)*std2**2) / 
                            (len(values1) + len(values2) - 2))
        if pooled_std > 0:
            cohens_d = (mean2 - mean1) / pooled_std
        else:
            cohens_d = 0
    else:
        cohens_d = 0
    
    results.append({
        'Element': element,
        'Range1_Mean': mean1,
        'Range1_Std': std1,
        'Range2_Mean': mean2,
        'Range2_Std': std2,
        'Difference': mean2 - mean1,
        'P_Value': p_value,
        'Cohens_D': cohens_d,
        'Significant': p_value < 0.05 if not np.isnan(p_value) else False
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('P_Value')

# Display significant differences
significant_results = results_df[results_df['Significant'] == True]
print(f"\n=== SIGNIFICANT DIFFERENCES (p < 0.05) ===")
print(f"Found {len(significant_results)} elements with significant differences:")

for _, row in significant_results.iterrows():
    print(f"\n{row['Element']}:")
    print(f"  Range 1 (1230-1330): {row['Range1_Mean']:.4f} ± {row['Range1_Std']:.4f}")
    print(f"  Range 2 (1480-1830): {row['Range2_Mean']:.4f} ± {row['Range2_Std']:.4f}")
    print(f"  Difference: {row['Difference']:.4f}")
    print(f"  P-value: {row['P_Value']:.6f}")
    print(f"  Effect size (Cohen's d): {row['Cohens_D']:.3f}")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(20, 16))

# 1. Box plots for significant elements
if len(significant_results) > 0:
    n_sig = min(8, len(significant_results))  # Show top 8 significant elements
    sig_elements = significant_results.head(n_sig)['Element'].tolist()
    
    for i, element in enumerate(sig_elements):
        row = i // 4
        col = i % 4
        
        if row < 2 and col < 2:
            data_to_plot = [df1[element].values, df2[element].values]
            axes[row, col].boxplot(data_to_plot, labels=['1230-1330 MPa', '1480-1830 MPa'])
            axes[row, col].set_title(f'{element} (p={significant_results[significant_results["Element"]==element]["P_Value"].iloc[0]:.4f})')
            axes[row, col].set_ylabel('Concentration')
            axes[row, col].grid(True, alpha=0.3)

# 2. P-value plot
axes[1, 1].scatter(range(len(results_df)), -np.log10(results_df['P_Value']), alpha=0.7)
axes[1, 1].axhline(y=-np.log10(0.05), color='red', linestyle='--', label='p=0.05')
axes[1, 1].set_xlabel('Element Rank (by p-value)')
axes[1, 1].set_ylabel('-log10(p-value)')
axes[1, 1].set_title('Statistical Significance of Compositional Differences')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Summary statistics
print(f"\n=== SUMMARY ===")
print(f"Total elements analyzed: {len(all_elements)}")
print(f"Elements with significant differences (p<0.05): {len(significant_results)}")
print(f"Percentage of elements with significant differences: {len(significant_results)/len(all_elements)*100:.1f}%")

# Save detailed results
results_df.to_csv('steel_composition_analysis_results.csv', index=False)
print(f"\nDetailed results saved to: steel_composition_analysis_results.csv")

# Effect size interpretation
print(f"\n=== EFFECT SIZE INTERPRETATION ===")
for _, row in significant_results.iterrows():
    d = abs(row['Cohens_D'])
    if d < 0.2:
        effect = "negligible"
    elif d < 0.5:
        effect = "small"
    elif d < 0.8:
        effect = "medium"
    else:
        effect = "large"
    print(f"{row['Element']}: {effect} effect (d={row['Cohens_D']:.3f})")

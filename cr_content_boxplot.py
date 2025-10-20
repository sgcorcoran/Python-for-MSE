import pandas as pd
import matplotlib.pyplot as plt
import json
import re
import numpy as np
from scipy import stats

def parse_composition(composition_str):
    """Parse composition string to extract elemental concentrations"""
    elements = re.findall(r'([A-Z][a-z]*)(\d*\.?\d*)', composition_str)
    composition = {}
    for element, concentration in elements:
        if concentration:
            composition[element] = float(concentration)
        else:
            composition[element] = 0.0
    return composition

# Read the JSON data
with open('C:/Users/sgc/OneDrive - Virginia Tech/Dev/GitHub/Python-for-MSE/data_files/database/steels_yield.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['data'], columns=data['columns'])
df.rename(columns={'yield strength': 'yield_strength'}, inplace=True)

# Parse compositions and add Cr content to DataFrame
compositions = df['composition'].apply(parse_composition)
df_compositions = pd.DataFrame(list(compositions))
df_with_cr = pd.concat([df, df_compositions], axis=1)

# Create strength groups
high_strength = df_with_cr[df_with_cr['yield_strength'] > 1400].copy()
low_medium_strength = df_with_cr[df_with_cr['yield_strength'] <= 1400].copy()

print(f"=== STRENGTH GROUPS ANALYSIS ===")
print(f"High strength group (>1400 MPa): {len(high_strength)} samples")
print(f"Low-medium strength group (<=1400 MPa): {len(low_medium_strength)} samples")

# Create box plot
plt.figure(figsize=(10, 6))

# Prepare data for box plot
data_to_plot = [high_strength['Cr'], low_medium_strength['Cr']]
labels = [f'High Strength\n(>1400 MPa)\nn={len(high_strength)}', 
          f'Low-Medium Strength\n(<=1400 MPa)\nn={len(low_medium_strength)}']

# Create box plot
box_plot = plt.boxplot(data_to_plot, labels=labels, patch_artist=True, 
                       boxprops=dict(alpha=0.7), medianprops=dict(color='black', linewidth=2))

# Color the boxes
colors = ['lightcoral', 'lightblue']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

plt.xlabel('Strength Group')
plt.ylabel('Cr Content')
plt.title('Cr Content Distribution by Strength Group')
plt.grid(True, alpha=0.3, axis='y')

# Add statistics text
plt.text(0.02, 0.98, f'High Strength:\nMean: {high_strength["Cr"].mean():.4f}\nMedian: {high_strength["Cr"].median():.4f}', 
         transform=plt.gca().transAxes, verticalalignment='top', 
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

plt.text(0.98, 0.98, f'Low-Medium Strength:\nMean: {low_medium_strength["Cr"].mean():.4f}\nMedian: {low_medium_strength["Cr"].median():.4f}', 
         transform=plt.gca().transAxes, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

plt.tight_layout()
plt.savefig('cr_content_boxplot_by_strength.png', dpi=300, bbox_inches='tight')
plt.show()

# Statistical comparison
if len(high_strength) > 1 and len(low_medium_strength) > 1:
    # Levene's test for equal variances
    stat_levene, p_levene = stats.levene(high_strength['Cr'], low_medium_strength['Cr'])
    equal_var = p_levene > 0.05
    
    # T-test
    t_stat, p_value = stats.ttest_ind(high_strength['Cr'], low_medium_strength['Cr'], equal_var=equal_var)
    
    # Calculate Cohen's d for effect size
    diff = high_strength['Cr'].mean() - low_medium_strength['Cr'].mean()
    std_pooled = np.sqrt(((len(high_strength) - 1) * high_strength['Cr'].std()**2 + 
                         (len(low_medium_strength) - 1) * low_medium_strength['Cr'].std()**2) / 
                        (len(high_strength) + len(low_medium_strength) - 2))
    cohens_d = diff / std_pooled if std_pooled != 0 else np.nan
    
    print(f"\n=== STATISTICAL COMPARISON OF Cr CONTENT ===")
    print(f"Levene's test p-value: {p_levene:.4f} (Equal variances: {equal_var})")
    print(f"T-test statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    print(f"Effect size (Cohen's d): {cohens_d:.3f}")
    
    if p_value < 0.05:
        print("Conclusion: There is a significant difference in Cr content between strength groups.")
    else:
        print("Conclusion: There is no significant difference in Cr content between strength groups.")

print(f"\nBox plot saved as 'cr_content_boxplot_by_strength.png'")



import pandas as pd
import matplotlib.pyplot as plt
import json
import re
import numpy as np

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
print(f"Total samples: {len(df_with_cr)}")

# Cr content statistics
print(f"\n=== Cr CONTENT STATISTICS ===")
print(f"High strength group:")
print(f"  Mean Cr: {high_strength['Cr'].mean():.4f}")
print(f"  Median Cr: {high_strength['Cr'].median():.4f}")
print(f"  Std Cr: {high_strength['Cr'].std():.4f}")
print(f"  Min Cr: {high_strength['Cr'].min():.4f}")
print(f"  Max Cr: {high_strength['Cr'].max():.4f}")

print(f"\nLow-medium strength group:")
print(f"  Mean Cr: {low_medium_strength['Cr'].mean():.4f}")
print(f"  Median Cr: {low_medium_strength['Cr'].median():.4f}")
print(f"  Std Cr: {low_medium_strength['Cr'].std():.4f}")
print(f"  Min Cr: {low_medium_strength['Cr'].min():.4f}")
print(f"  Max Cr: {low_medium_strength['Cr'].max():.4f}")

# Create histograms
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# High strength group histogram
axes[0].hist(high_strength['Cr'], bins=20, alpha=0.7, color='red', edgecolor='black')
axes[0].set_xlabel('Cr Content')
axes[0].set_ylabel('Frequency')
axes[0].set_title(f'Cr Content Distribution\nHigh Strength Group (>1400 MPa)\nn={len(high_strength)}')
axes[0].grid(True, alpha=0.3)

# Low-medium strength group histogram
axes[1].hist(low_medium_strength['Cr'], bins=20, alpha=0.7, color='blue', edgecolor='black')
axes[1].set_xlabel('Cr Content')
axes[1].set_ylabel('Frequency')
axes[1].set_title(f'Cr Content Distribution\nLow-Medium Strength Group (<=1400 MPa)\nn={len(low_medium_strength)}')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('cr_content_histograms_by_strength.png', dpi=300, bbox_inches='tight')
plt.show()

# Create a combined histogram for comparison
plt.figure(figsize=(10, 6))
plt.hist(high_strength['Cr'], bins=20, alpha=0.6, color='red', label=f'High Strength (>1400 MPa, n={len(high_strength)})', edgecolor='black')
plt.hist(low_medium_strength['Cr'], bins=20, alpha=0.6, color='blue', label=f'Low-Medium Strength (<=1400 MPa, n={len(low_medium_strength)})', edgecolor='black')
plt.xlabel('Cr Content')
plt.ylabel('Frequency')
plt.title('Cr Content Distribution by Strength Group')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('cr_content_combined_histogram.png', dpi=300, bbox_inches='tight')
plt.show()

# Statistical comparison
from scipy import stats
if len(high_strength) > 1 and len(low_medium_strength) > 1:
    # Levene's test for equal variances
    stat_levene, p_levene = stats.levene(high_strength['Cr'], low_medium_strength['Cr'])
    equal_var = p_levene > 0.05
    
    # T-test
    t_stat, p_value = stats.ttest_ind(high_strength['Cr'], low_medium_strength['Cr'], equal_var=equal_var)
    
    print(f"\n=== STATISTICAL COMPARISON OF Cr CONTENT ===")
    print(f"Levene's test p-value: {p_levene:.4f} (Equal variances: {equal_var})")
    print(f"T-test statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Conclusion: There is a significant difference in Cr content between strength groups.")
    else:
        print("Conclusion: There is no significant difference in Cr content between strength groups.")

print(f"\nPlots saved as 'cr_content_histograms_by_strength.png' and 'cr_content_combined_histogram.png'")

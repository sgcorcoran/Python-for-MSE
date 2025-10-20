import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import re

def parse_composition(comp_string):
    """Parse composition string to extract elemental concentrations"""
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

# Parse all compositions
print("Parsing compositions...")
all_data = []
for idx, row in df.iterrows():
    comp = parse_composition(row['composition'])
    all_data.append({
        'yield_strength': row['yield strength'],
        'Cr': comp.get('Cr', 0),
        'Al': comp.get('Al', 0),
        'Si': comp.get('Si', 0),
        'Mn': comp.get('Mn', 0),
        'Ni': comp.get('Ni', 0),
        'composition_string': row['composition']
    })

# Convert to DataFrame
df_parsed = pd.DataFrame(all_data)

# Create groups based on Cr content (excluding low Cr < 0.01)
# First, filter out samples with Cr < 0.01
df_filtered = df_parsed[df_parsed['Cr'] >= 0.01].copy()

high_cr_group = df_filtered[df_filtered['Cr'] > 0.1].copy()
low_cr_group = df_filtered[df_filtered['Cr'] <= 0.1].copy()

print(f"Total samples after removing Cr < 0.01: {len(df_filtered)}")
print(f"Samples with Cr < 0.01 removed: {len(df_parsed) - len(df_filtered)}")

print(f"\n=== CHROMIUM GROUPS ANALYSIS ===")
print(f"High Cr group (Cr > 0.1): {len(high_cr_group)} samples")
print(f"Low Cr group (Cr <= 0.1): {len(low_cr_group)} samples")

# Calculate statistics for each group
print(f"\n=== YIELD STRENGTH STATISTICS ===")
print(f"High Cr group (Cr > 0.1):")
print(f"  Mean yield strength: {high_cr_group['yield_strength'].mean():.2f} MPa")
print(f"  Std yield strength: {high_cr_group['yield_strength'].std():.2f} MPa")
print(f"  Min yield strength: {high_cr_group['yield_strength'].min():.2f} MPa")
print(f"  Max yield strength: {high_cr_group['yield_strength'].max():.2f} MPa")
print(f"  Median yield strength: {high_cr_group['yield_strength'].median():.2f} MPa")

print(f"\nLow Cr group (Cr <= 0.1):")
print(f"  Mean yield strength: {low_cr_group['yield_strength'].mean():.2f} MPa")
print(f"  Std yield strength: {low_cr_group['yield_strength'].std():.2f} MPa")
print(f"  Min yield strength: {low_cr_group['yield_strength'].min():.2f} MPa")
print(f"  Max yield strength: {low_cr_group['yield_strength'].max():.2f} MPa")
print(f"  Median yield strength: {low_cr_group['yield_strength'].median():.2f} MPa")

# Statistical test
t_stat, p_value = stats.ttest_ind(high_cr_group['yield_strength'], low_cr_group['yield_strength'])
print(f"\n=== STATISTICAL TEST ===")
print(f"t-test results:")
print(f"  t-statistic: {t_stat:.4f}")
print(f"  p-value: {p_value:.6f}")
print(f"  Significant difference: {'Yes' if p_value < 0.05 else 'No'}")

# Effect size (Cohen's d)
n1, n2 = len(high_cr_group), len(low_cr_group)
s1, s2 = high_cr_group['yield_strength'].std(), low_cr_group['yield_strength'].std()
pooled_std = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1 + n2 - 2))
cohens_d = (high_cr_group['yield_strength'].mean() - low_cr_group['yield_strength'].mean()) / pooled_std
print(f"  Effect size (Cohen's d): {cohens_d:.4f}")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Box plot: Yield strength by Cr groups
data_to_plot = [low_cr_group['yield_strength'], high_cr_group['yield_strength']]
box_plot = axes[0, 0].boxplot(data_to_plot, tick_labels=['Cr <= 0.1', 'Cr > 0.1'], patch_artist=True)
axes[0, 0].set_ylabel('Yield Strength (MPa)')
axes[0, 0].set_title('Yield Strength Distribution by Chromium Content')
axes[0, 0].grid(True, alpha=0.3)

# Color the boxes
colors = ['lightblue', 'lightcoral']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

# Add sample sizes to the plot
axes[0, 0].text(1, low_cr_group['yield_strength'].max() + 50, f'n={len(low_cr_group)}', 
                ha='center', va='bottom', fontweight='bold')
axes[0, 0].text(2, high_cr_group['yield_strength'].max() + 50, f'n={len(high_cr_group)}', 
                ha='center', va='bottom', fontweight='bold')

# 2. Histogram: Yield strength distributions
axes[0, 1].hist(low_cr_group['yield_strength'], bins=30, alpha=0.7, color='lightblue', 
                label=f'Cr <= 0.1 (n={len(low_cr_group)})', density=True)
axes[0, 1].hist(high_cr_group['yield_strength'], bins=30, alpha=0.7, color='lightcoral', 
                label=f'Cr > 0.1 (n={len(high_cr_group)})', density=True)
axes[0, 1].set_xlabel('Yield Strength (MPa)')
axes[0, 1].set_ylabel('Density')
axes[0, 1].set_title('Yield Strength Distribution by Chromium Content')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# 3. Scatter plot: Cr vs Yield strength
axes[1, 0].scatter(low_cr_group['Cr'], low_cr_group['yield_strength'], alpha=0.6, 
                   color='blue', label='Cr <= 0.1', s=30)
axes[1, 0].scatter(high_cr_group['Cr'], high_cr_group['yield_strength'], alpha=0.6, 
                   color='red', label='Cr > 0.1', s=30)
axes[1, 0].axvline(x=0.1, color='black', linestyle='--', alpha=0.7, label='Cr = 0.1 threshold')
axes[1, 0].set_xlabel('Chromium Content')
axes[1, 0].set_ylabel('Yield Strength (MPa)')
axes[1, 0].set_title('Yield Strength vs Chromium Content')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. Violin plot: Yield strength distributions
data_for_violin = [low_cr_group['yield_strength'], high_cr_group['yield_strength']]
violin_parts = axes[1, 1].violinplot(data_for_violin, positions=[1, 2], showmeans=True, showmedians=True)
axes[1, 1].set_xticks([1, 2])
axes[1, 1].set_xticklabels(['Cr <= 0.1', 'Cr > 0.1'])
axes[1, 1].set_ylabel('Yield Strength (MPa)')
axes[1, 1].set_title('Yield Strength Distribution (Violin Plot)')
axes[1, 1].grid(True, alpha=0.3)

# Color the violins
colors = ['lightblue', 'lightcoral']
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_alpha(0.7)

plt.tight_layout()
plt.show()

# Additional analysis: Cr content statistics
print(f"\n=== CHROMIUM CONTENT STATISTICS ===")
print(f"High Cr group (Cr > 0.1):")
print(f"  Mean Cr: {high_cr_group['Cr'].mean():.4f}")
print(f"  Std Cr: {high_cr_group['Cr'].std():.4f}")
print(f"  Min Cr: {high_cr_group['Cr'].min():.4f}")
print(f"  Max Cr: {high_cr_group['Cr'].max():.4f}")

print(f"\nLow Cr group (Cr <= 0.1):")
print(f"  Mean Cr: {low_cr_group['Cr'].mean():.4f}")
print(f"  Std Cr: {low_cr_group['Cr'].std():.4f}")
print(f"  Min Cr: {low_cr_group['Cr'].min():.4f}")
print(f"  Max Cr: {low_cr_group['Cr'].max():.4f}")

# Correlation analysis (using filtered data)
correlation = np.corrcoef(df_filtered['Cr'], df_filtered['yield_strength'])[0, 1]
print(f"\n=== CORRELATION ANALYSIS ===")
print(f"Correlation between Cr and yield strength: {correlation:.4f}")

# Save data
high_cr_group.to_csv('high_cr_group.csv', index=False)
low_cr_group.to_csv('low_cr_group.csv', index=False)

print(f"\nData saved to:")
print("- high_cr_group.csv")
print("- low_cr_group.csv")

# Summary
print(f"\n=== SUMMARY ===")
if p_value < 0.05:
    if high_cr_group['yield_strength'].mean() > low_cr_group['yield_strength'].mean():
        print("✅ SIGNIFICANT: High Cr steels have HIGHER yield strength than low Cr steels")
    else:
        print("✅ SIGNIFICANT: High Cr steels have LOWER yield strength than low Cr steels")
else:
    print("❌ NO SIGNIFICANT DIFFERENCE in yield strength between high and low Cr steels")

print(f"Effect size: {cohens_d:.3f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small'})")
print(f"Correlation: {correlation:.3f} ({'strong' if abs(correlation) > 0.7 else 'moderate' if abs(correlation) > 0.3 else 'weak'})")

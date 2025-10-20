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

# Filter for the two ranges
range1 = df[(df['yield strength'] >= 1230) & (df['yield strength'] <= 1330)].copy()
range2 = df[(df['yield strength'] >= 1480) & (df['yield strength'] <= 1830)].copy()

print(f"Range 1 (1230-1330 MPa): {len(range1)} samples")
print(f"Range 2 (1480-1830 MPa): {len(range2)} samples")

# Parse compositions for both ranges
print("\nParsing compositions...")
range1_data = []
for idx, row in range1.iterrows():
    comp = parse_composition(row['composition'])
    # Sum Cr, Al, Si, and Mn
    combined_sum = comp.get('Cr', 0) + comp.get('Al', 0) + comp.get('Si', 0) + comp.get('Mn', 0)
    range1_data.append({
        'yield_strength': row['yield strength'],
        'combined_sum': combined_sum,
        'Cr': comp.get('Cr', 0),
        'Al': comp.get('Al', 0),
        'Si': comp.get('Si', 0),
        'Mn': comp.get('Mn', 0)
    })

range2_data = []
for idx, row in range2.iterrows():
    comp = parse_composition(row['composition'])
    # Sum Cr, Al, Si, and Mn
    combined_sum = comp.get('Cr', 0) + comp.get('Al', 0) + comp.get('Si', 0) + comp.get('Mn', 0)
    range2_data.append({
        'yield_strength': row['yield strength'],
        'combined_sum': combined_sum,
        'Cr': comp.get('Cr', 0),
        'Al': comp.get('Al', 0),
        'Si': comp.get('Si', 0),
        'Mn': comp.get('Mn', 0)
    })

# Convert to DataFrames
df1 = pd.DataFrame(range1_data)
df2 = pd.DataFrame(range2_data)

# Calculate statistics
print(f"\n=== COMBINED ELEMENTS (Cr + Al + Si + Mn) ANALYSIS ===")
print(f"Range 1 (1230-1330 MPa):")
print(f"  Mean combined sum: {df1['combined_sum'].mean():.4f}")
print(f"  Std combined sum: {df1['combined_sum'].std():.4f}")
print(f"  Min combined sum: {df1['combined_sum'].min():.4f}")
print(f"  Max combined sum: {df1['combined_sum'].max():.4f}")

print(f"\nRange 2 (1480-1830 MPa):")
print(f"  Mean combined sum: {df2['combined_sum'].mean():.4f}")
print(f"  Std combined sum: {df2['combined_sum'].std():.4f}")
print(f"  Min combined sum: {df2['combined_sum'].min():.4f}")
print(f"  Max combined sum: {df2['combined_sum'].max():.4f}")

# Statistical test
t_stat, p_value = stats.ttest_ind(df1['combined_sum'], df2['combined_sum'])
print(f"\nStatistical Test:")
print(f"  t-statistic: {t_stat:.4f}")
print(f"  p-value: {p_value:.6f}")
print(f"  Significant difference: {'Yes' if p_value < 0.05 else 'No'}")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Scatter plot: Combined sum vs Yield strength
axes[0, 0].scatter(df1['combined_sum'], df1['yield_strength'], alpha=0.6, 
                   color='blue', label='1230-1330 MPa', s=50)
axes[0, 0].scatter(df2['combined_sum'], df2['yield_strength'], alpha=0.6, 
                   color='red', label='1480-1830 MPa', s=50)
axes[0, 0].set_xlabel('Combined Sum (Cr + Al + Si + Mn)')
axes[0, 0].set_ylabel('Yield Strength (MPa)')
axes[0, 0].set_title('Yield Strength vs Combined Element Sum')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Add trend lines
z1 = np.polyfit(df1['combined_sum'], df1['yield_strength'], 1)
p1 = np.poly1d(z1)
axes[0, 0].plot(df1['combined_sum'], p1(df1['combined_sum']), "b--", alpha=0.8)

z2 = np.polyfit(df2['combined_sum'], df2['yield_strength'], 1)
p2 = np.poly1d(z2)
axes[0, 0].plot(df2['combined_sum'], p2(df2['combined_sum']), "r--", alpha=0.8)

# 2. Box plot: Combined sum distribution
data_to_plot = [df1['combined_sum'], df2['combined_sum']]
axes[0, 1].boxplot(data_to_plot, tick_labels=['1230-1330 MPa', '1480-1830 MPa'])
axes[0, 1].set_ylabel('Combined Sum (Cr + Al + Si + Mn)')
axes[0, 1].set_title('Distribution of Combined Element Sum')
axes[0, 1].grid(True, alpha=0.3)

# 3. Histogram: Combined sum distributions
axes[1, 0].hist(df1['combined_sum'], bins=20, alpha=0.7, color='blue', 
                label='1230-1330 MPa', density=True)
axes[1, 0].hist(df2['combined_sum'], bins=20, alpha=0.7, color='red', 
                label='1480-1830 MPa', density=True)
axes[1, 0].set_xlabel('Combined Sum (Cr + Al + Si + Mn)')
axes[1, 0].set_ylabel('Density')
axes[1, 0].set_title('Distribution of Combined Element Sum')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. Correlation analysis
all_data = pd.concat([df1, df2])
correlation = np.corrcoef(all_data['combined_sum'], all_data['yield_strength'])[0, 1]
print(f"\nOverall correlation between combined sum and yield strength: {correlation:.4f}")

# Scatter plot with correlation
axes[1, 1].scatter(all_data['combined_sum'], all_data['yield_strength'], alpha=0.6, s=30)
axes[1, 1].set_xlabel('Combined Sum (Cr + Al + Si + Mn)')
axes[1, 1].set_ylabel('Yield Strength (MPa)')
axes[1, 1].set_title(f'Overall Correlation: r = {correlation:.3f}')

# Add trend line for all data
z_all = np.polyfit(all_data['combined_sum'], all_data['yield_strength'], 1)
p_all = np.poly1d(z_all)
axes[1, 1].plot(all_data['combined_sum'], p_all(all_data['combined_sum']), 
                "g-", linewidth=2, alpha=0.8)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Individual element correlations
print(f"\n=== INDIVIDUAL ELEMENT CORRELATIONS WITH YIELD STRENGTH ===")
elements = ['Cr', 'Al', 'Si', 'Mn']
for element in elements:
    corr = np.corrcoef(all_data[element], all_data['yield_strength'])[0, 1]
    print(f"{element}: r = {corr:.4f}")

# Save data
df1.to_csv('range1_combined_data.csv', index=False)
df2.to_csv('range2_combined_data.csv', index=False)
all_data.to_csv('all_combined_data.csv', index=False)

print(f"\nData saved to:")
print("- range1_combined_data.csv")
print("- range2_combined_data.csv") 
print("- all_combined_data.csv")



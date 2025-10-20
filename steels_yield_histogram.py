import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the steel yield data
with open('data_files/database/steels_yield.json', 'r') as f:
    steel_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(steel_data['data'], columns=steel_data['columns'])

# Extract yield strength values
yield_strength = df['yield strength'].values

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(yield_strength, bins=30, alpha=0.7, color='steelblue', edgecolor='black')

# Add labels and title
plt.xlabel('Yield Strength (MPa)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Steel Yield Strength', fontsize=14, fontweight='bold')

# Add statistics
mean_strength = np.mean(yield_strength)
std_strength = np.std(yield_strength)
median_strength = np.median(yield_strength)

plt.axvline(mean_strength, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_strength:.1f} MPa')
plt.axvline(median_strength, color='green', linestyle='--', linewidth=2, label=f'Median: {median_strength:.1f} MPa')

# Add text box with statistics
stats_text = f'Statistics:\nCount: {len(yield_strength)}\nMean: {mean_strength:.1f} MPa\nStd Dev: {std_strength:.1f} MPa\nMin: {np.min(yield_strength):.1f} MPa\nMax: {np.max(yield_strength):.1f} MPa'
plt.text(0.75, 0.75, stats_text, transform=plt.gca().transAxes, 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
         verticalalignment='top', fontsize=10)

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Print summary statistics
print("🔬 Steel Yield Strength Analysis")
print("=" * 40)
print(f"Dataset size: {len(yield_strength)} samples")
print(f"Mean yield strength: {mean_strength:.1f} MPa")
print(f"Standard deviation: {std_strength:.1f} MPa")
print(f"Median yield strength: {median_strength:.1f} MPa")
print(f"Range: {np.min(yield_strength):.1f} - {np.max(yield_strength):.1f} MPa")
print(f"Coefficient of variation: {(std_strength/mean_strength)*100:.1f}%")

# Check for normality
from scipy import stats
statistic, p_value = stats.shapiro(yield_strength)
print(f"\nNormality test (Shapiro-Wilk):")
print(f"Statistic: {statistic:.4f}")
print(f"P-value: {p_value:.6f}")
if p_value > 0.05:
    print("✓ Data appears approximately normal (p > 0.05)")
else:
    print("✗ Data does not appear normal (p ≤ 0.05)")


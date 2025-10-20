import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the JSON data
with open('C:/Users/sgc/OneDrive - Virginia Tech/Dev/GitHub/Python-for-MSE/data_files/database/steels_yield.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['data'], columns=data['columns'])

# Filter for the two ranges
range1 = df[(df['yield strength'] >= 1230) & (df['yield strength'] <= 1330)]
range2 = df[(df['yield strength'] >= 1480) & (df['yield strength'] <= 1830)]

print(f"Range 1 (1230-1330 MPa): {len(range1)} samples")
print(f"Range 2 (1480-1830 MPa): {len(range2)} samples")

# Create histograms
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Histogram for range 1 (1230-1330)
ax1.hist(range1['yield strength'], bins=20, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title(f'Yield Strength: 1230-1330 MPa\n(n={len(range1)} samples)')
ax1.set_xlabel('Yield Strength (MPa)')
ax1.set_ylabel('Frequency')
ax1.grid(True, alpha=0.3)

# Add statistics
mean1 = range1['yield strength'].mean()
std1 = range1['yield strength'].std()
ax1.axvline(mean1, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean1:.1f} MPa')
ax1.legend()

# Histogram for range 2 (1480-1830)
ax2.hist(range2['yield strength'], bins=20, alpha=0.7, color='green', edgecolor='black')
ax2.set_title(f'Yield Strength: 1480-1830 MPa\n(n={len(range2)} samples)')
ax2.set_xlabel('Yield Strength (MPa)')
ax2.set_ylabel('Frequency')
ax2.grid(True, alpha=0.3)

# Add statistics
mean2 = range2['yield strength'].mean()
std2 = range2['yield strength'].std()
ax2.axvline(mean2, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean2:.1f} MPa')
ax2.legend()

plt.tight_layout()
plt.show()

# Print summary statistics
print("\n=== SUMMARY STATISTICS ===")
print(f"\nRange 1 (1230-1330 MPa):")
print(f"  Count: {len(range1)}")
print(f"  Mean: {mean1:.2f} MPa")
print(f"  Std Dev: {std1:.2f} MPa")
print(f"  Min: {range1['yield strength'].min():.2f} MPa")
print(f"  Max: {range1['yield strength'].max():.2f} MPa")

print(f"\nRange 2 (1480-1830 MPa):")
print(f"  Count: {len(range2)}")
print(f"  Mean: {mean2:.2f} MPa")
print(f"  Std Dev: {std2:.2f} MPa")
print(f"  Min: {range2['yield strength'].min():.2f} MPa")
print(f"  Max: {range2['yield strength'].max():.2f} MPa")

# Save the filtered data to CSV files
range1.to_csv('steels_yield_range1_1230_1330.csv', index=False)
range2.to_csv('steels_yield_range2_1480_1830.csv', index=False)

print(f"\nFiltered data saved to:")
print("- steels_yield_range1_1230_1330.csv")
print("- steels_yield_range2_1480_1830.csv")

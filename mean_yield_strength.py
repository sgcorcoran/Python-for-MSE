import json
import pandas as pd
import numpy as np

# Read the JSON data
with open('C:/Users/sgc/OneDrive - Virginia Tech/Dev/GitHub/Python-for-MSE/data_files/database/steels_yield.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['data'], columns=data['columns'])

# Calculate mean yield strength
mean_yield = df['yield strength'].mean()
median_yield = df['yield strength'].median()
std_yield = df['yield strength'].std()
min_yield = df['yield strength'].min()
max_yield = df['yield strength'].max()

print(f"=== YIELD STRENGTH STATISTICS FOR ALL STEELS ===")
print(f"Total number of steels: {len(df)}")
print(f"Mean yield strength: {mean_yield:.2f} MPa")
print(f"Median yield strength: {median_yield:.2f} MPa")
print(f"Standard deviation: {std_yield:.2f} MPa")
print(f"Minimum yield strength: {min_yield:.2f} MPa")
print(f"Maximum yield strength: {max_yield:.2f} MPa")
print(f"Range: {max_yield - min_yield:.2f} MPa")

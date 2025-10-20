import pandas as pd
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

# Parse compositions and add elemental content to DataFrame
compositions = df['composition'].apply(parse_composition)
df_compositions = pd.DataFrame(list(compositions))
df_with_elements = pd.concat([df, df_compositions], axis=1)

# Create strength categories
df_with_elements['category'] = df_with_elements['yield_strength'].apply(
    lambda x: 'high_strength' if x > 1400 else 'medium_strength'
)

# Get all elemental columns (exclude the original columns)
element_columns = [col for col in df_with_elements.columns if col not in ['yield_strength', 'composition', 'category']]

# Create the output DataFrame with all compositions
output_columns = ['category', 'yield_strength'] + element_columns
output_df = df_with_elements[output_columns].copy()

# Rename yield_strength column for clarity
output_df = output_df.rename(columns={'yield_strength': 'yield_strength'})

# Sort by category and then by yield strength
output_df = output_df.sort_values(['category', 'yield_strength'])

# Save to CSV
output_df.to_csv('steel_strength_categories.csv', index=False)

print(f"=== CSV FILE CREATED ===")
print(f"File saved as: steel_strength_categories.csv")
print(f"Total records: {len(output_df)}")
print(f"High strength records (>1400 MPa): {len(output_df[output_df['category'] == 'high_strength'])}")
print(f"Medium strength records (<=1400 MPa): {len(output_df[output_df['category'] == 'medium_strength'])}")

# Display first few rows
print(f"\n=== FIRST 10 ROWS ===")
print(output_df.head(10).to_string(index=False))

print(f"\n=== COLUMN NAMES ===")
print(f"Total columns: {len(output_df.columns)}")
print(f"Columns: {list(output_df.columns)}")

print(f"\n=== SUMMARY STATISTICS FOR KEY ELEMENTS ===")
# Focus on key elements for summary
key_elements = ['yield_strength', 'Cr', 'Ni', 'Al', 'Si', 'Mn', 'Mo', 'Co', 'Fe']
available_elements = [col for col in key_elements if col in output_df.columns]

summary_stats = output_df.groupby('category')[available_elements].agg(['count', 'mean', 'std', 'min', 'max']).round(4)
print(summary_stats)

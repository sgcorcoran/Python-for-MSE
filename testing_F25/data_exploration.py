import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def explore_csv_structure(file_path):
    """Comprehensive exploration of CSV file structure and content"""
    print("=== CSV FILE STRUCTURE EXPLORATION ===")
    print(f"File path: {file_path}")
    
    # First, let's look at the raw file content
    print("\n=== RAW FILE CONTENT (First 10 lines) ===")
    try:
        with open(file_path, 'r') as f:
            for i, line in enumerate(f):
                if i < 10:
                    print(f"Line {i+1}: {line.strip()}")
                else:
                    break
    except FileNotFoundError:
        print(f"ERROR: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return None
    
    # Try different header scenarios
    print("\n=== HEADER DETECTION ===")
    
    # Scenario 1: No header (first row is data)
    try:
        data_no_header = pd.read_csv(file_path, header=None)
        print("Scenario 1 - No header:")
        print(f"  Shape: {data_no_header.shape}")
        print(f"  First row: {data_no_header.iloc[0].tolist()}")
        print(f"  Data types: {data_no_header.dtypes.tolist()}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Scenario 2: First row is header
    try:
        data_with_header = pd.read_csv(file_path, header=0)
        print("\nScenario 2 - First row is header:")
        print(f"  Shape: {data_with_header.shape}")
        print(f"  Column names: {data_with_header.columns.tolist()}")
        print(f"  Data types: {data_with_header.dtypes.tolist()}")
        print(f"  First data row: {data_with_header.iloc[0].tolist()}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Scenario 3: Check if there are multiple header rows
    try:
        # Try reading with different header positions
        for header_row in range(5):  # Check first 5 rows as potential headers
            try:
                data_test = pd.read_csv(file_path, header=header_row)
                print(f"\nScenario 3.{header_row+1} - Row {header_row} as header:")
                print(f"  Shape: {data_test.shape}")
                print(f"  Column names: {data_test.columns.tolist()}")
                print(f"  First data row: {data_test.iloc[0].tolist()}")
            except:
                continue
    except Exception as e:
        print(f"  Error: {e}")
    
    # Analyze column names for unit clues
    print("\n=== COLUMN NAME ANALYSIS FOR UNITS ===")
    
    # Common unit patterns in materials science
    unit_patterns = {
        'load': ['N', 'kN', 'lbf', 'kgf'],
        'force': ['N', 'kN', 'lbf', 'kgf'],
        'stress': ['MPa', 'GPa', 'Pa', 'ksi', 'psi'],
        'pressure': ['MPa', 'GPa', 'Pa', 'bar', 'atm'],
        'strain': ['', 'mm/mm', 'in/in', '%'],
        'displacement': ['mm', 'cm', 'm', 'in', 'ft'],
        'length': ['mm', 'cm', 'm', 'in', 'ft'],
        'area': ['mm²', 'cm²', 'm²', 'in²', 'ft²'],
        'time': ['s', 'ms', 'min', 'hr'],
        'temperature': ['°C', 'K', '°F']
    }
    
    # Try to identify units from column names
    if 'data_with_header' in locals():
        for col in data_with_header.columns:
            col_lower = str(col).lower()
            print(f"\nColumn: '{col}'")
            
            # Check for unit patterns
            units_found = []
            for unit_type, possible_units in unit_patterns.items():
                if unit_type in col_lower:
                    units_found.append(unit_type)
                    # Look for specific units in the column name
                    for unit in possible_units:
                        if unit in str(col):
                            units_found.append(f"({unit})")
            
            if units_found:
                print(f"  Likely represents: {', '.join(units_found)}")
            else:
                print(f"  No clear unit pattern identified")
            
            # Check for common abbreviations
            common_abbrevs = {
                'load': ['load', 'force', 'f', 'p'],
                'displacement': ['disp', 'displacement', 'elongation', 'extension'],
                'strain': ['strain', 'eps', 'ε'],
                'stress': ['stress', 'sigma', 'σ'],
                'time': ['time', 't'],
                'area': ['area', 'a', 'cross_section']
            }
            
            for meaning, abbrevs in common_abbrevs.items():
                if any(abbrev in col_lower for abbrev in abbrevs):
                    print(f"  Likely meaning: {meaning}")
                    break
    
    # Check data content for clues
    print("\n=== DATA CONTENT ANALYSIS ===")
    
    if 'data_with_header' in locals():
        for col in data_with_header.columns:
            print(f"\nColumn '{col}':")
            
            # Check data range and characteristics
            col_data = pd.to_numeric(data_with_header[col], errors='coerce')
            if not col_data.isna().all():
                print(f"  Numeric range: {col_data.min():.6f} to {col_data.max():.6f}")
                print(f"  Mean: {col_data.mean():.6f}")
                print(f"  Non-null values: {col_data.count()}")
                
                # Check for reasonable values based on column name
                col_lower = str(col).lower()
                if 'stress' in col_lower or 'pressure' in col_lower:
                    if col_data.max() > 1000:
                        print(f"  → Likely units: MPa or GPa (high values)")
                    elif col_data.max() > 100:
                        print(f"  → Likely units: MPa (moderate values)")
                    else:
                        print(f"  → Likely units: GPa (low values)")
                
                elif 'strain' in col_lower:
                    if col_data.max() > 1:
                        print(f"  → Likely units: % (values > 1)")
                    else:
                        print(f"  → Likely units: mm/mm or in/in (values < 1)")
                
                elif 'load' in col_lower or 'force' in col_lower:
                    if col_data.max() > 10000:
                        print(f"  → Likely units: N (high values)")
                    elif col_data.max() > 1000:
                        print(f"  → Likely units: N (moderate values)")
                    else:
                        print(f"  → Likely units: kN (low values)")
                
                elif 'displacement' in col_lower or 'length' in col_lower:
                    if col_data.max() > 100:
                        print(f"  → Likely units: mm (high values)")
                    elif col_data.max() > 10:
                        print(f"  → Likely units: mm (moderate values)")
                    else:
                        print(f"  → Likely units: mm (low values)")
            else:
                print(f"  Non-numeric data")
                # Show unique values for non-numeric columns
                unique_vals = data_with_header[col].unique()
                if len(unique_vals) <= 10:
                    print(f"  Unique values: {unique_vals}")
                else:
                    print(f"  Unique values: {len(unique_vals)} (showing first 5: {unique_vals[:5]})")
    
    # Recommendations
    print("\n=== RECOMMENDATIONS ===")
    print("Based on the analysis above, you should:")
    print("1. Identify which header scenario is correct")
    print("2. Determine the appropriate units for each column")
    print("3. Convert units if necessary for analysis")
    print("4. Validate that the data makes physical sense")
    
    return data_with_header if 'data_with_header' in locals() else None

# Run the exploration
if __name__ == "__main__":
    # Try different possible file paths
    possible_paths = [
        r'../testing_F25/Al7075.csv',
        r'./Al7075.csv',
        r'Al7075.csv',
        r'../Al7075.csv'
    ]
    
    data = None
    for path in possible_paths:
        print(f"\n{'='*60}")
        print(f"Trying path: {path}")
        print(f"{'='*60}")
        
        try:
            data = explore_csv_structure(path)
            if data is not None:
                print(f"\n✅ Successfully loaded data from: {path}")
                break
        except Exception as e:
            print(f"❌ Failed to load from {path}: {e}")
    
    if data is None:
        print("\n❌ Could not load data from any of the attempted paths")
        print("Please check the file location and try again")
    else:
        print(f"\n🎉 Data loaded successfully!")
        print(f"Final dataset shape: {data.shape}")
        print(f"Columns: {data.columns.tolist()}")


#!/usr/bin/env python3
"""
Standalone script to parse glass composition data and create parallel coordinate plots
for 3-element compositions, colored by glass-forming ability.

Usage:
    python glass_parallel_plot.py [element_or_combination]
    
    If element is provided, only 3-element compositions containing that element will be plotted.
    If combination is provided (e.g., "Al-Fe-Ni"), only compositions containing those elements will be plotted.
    If no argument is provided, all 3-element compositions will be plotted.

Requirements:
    - pandas
    - plotly
    - numpy
    - re (built-in)
"""

import json
import re
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import sys
from pathlib import Path

def parse_composition(comp_string):
    """
    Parse a composition string like "Al(NiB)2" or "Fe79B16Mo5" into element percentages.
    Handles parentheses and subscripts correctly.
    
    Args:
        comp_string (str): Composition string (e.g., "Al(NiB)2", "Fe79B16Mo5")
    
    Returns:
        dict: Dictionary with element symbols as keys and percentages as values
    """
    # First, expand parentheses and subscripts
    expanded = comp_string
    while '(' in expanded:
        # Find parentheses and expand them
        match = re.search(r'\(([^)]+)\)(\d*)', expanded)
        if match:
            content = match.group(1)
            multiplier = int(match.group(2)) if match.group(2) else 1
            
            # Parse the content inside parentheses
            content_elements = re.findall(r'([A-Z][a-z]?)(\d*)', content)
            expanded_content = ''
            for elem, num in content_elements:
                elem_num = int(num) if num else 1
                expanded_content += f'{elem}{elem_num * multiplier}'
            
            expanded = expanded.replace(match.group(0), expanded_content)
    
    # Now parse the expanded string
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, expanded)
    
    elements = {}
    for element, number in matches:
        if number:  # If number is provided
            elements[element] = float(number)
        else:  # If no number, assume 1 (for cases like "FeB" meaning Fe1B1)
            elements[element] = 1.0
    
    # Normalize to percentages if they don't sum to 100
    total = sum(elements.values())
    if total > 0:
        elements = {k: v/total * 100 for k, v in elements.items()}
    
    return elements

def load_glass_data(file_path):
    """
    Load and parse glass data from JSON file.
    
    Args:
        file_path (str): Path to the glass.json file
    
    Returns:
        pd.DataFrame: DataFrame with parsed composition data
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # The data is a pandas-style JSON with columns and data
    if isinstance(data, dict) and "columns" in data and "data" in data:
        # Create DataFrame directly from the pandas JSON format
        df = pd.DataFrame(data["data"], columns=data["columns"])
        # Rename gfa column to forms_glass for consistency
        if "gfa" in df.columns:
            df = df.rename(columns={"gfa": "forms_glass"})
    else:
        # Fallback for other formats
        compositions = []
        glass_forming = []
        
        for item in data:
            if len(item) == 2:
                comp_str, forms_glass = item
                compositions.append(comp_str)
                glass_forming.append(forms_glass)
        
        # Create DataFrame
        df = pd.DataFrame({
            'composition': compositions,
            'forms_glass': glass_forming
        })
    
    # Parse compositions
    parsed_comps = []
    for comp in df['composition']:
        parsed = parse_composition(comp)
        parsed_comps.append(parsed)
    
    # Add parsed compositions as separate columns
    all_elements = set()
    for comp in parsed_comps:
        all_elements.update(comp.keys())
    
    # Create columns for each element
    for element in all_elements:
        df[element] = 0.0
    
    # Fill in the percentages
    for i, comp in enumerate(parsed_comps):
        for element, percentage in comp.items():
            df.loc[i, element] = percentage
    
    return df

def filter_three_element_compositions(df, target_element=None, target_combination=None):
    """
    Filter DataFrame to only include compositions with exactly 3 elements.
    Optionally filter to only compositions containing a specific element or combination.
    
    Args:
        df (pd.DataFrame): DataFrame with element columns
        target_element (str, optional): Element symbol to filter by (e.g., 'Fe', 'Al', 'B')
        target_combination (str, optional): 3-element combination to filter by (e.g., 'Al-Fe-Ni')
    
    Returns:
        pd.DataFrame: Filtered DataFrame with only 3-element compositions
    """
    # Get element columns (exclude 'composition' and 'forms_glass')
    element_cols = [col for col in df.columns if col not in ['composition', 'forms_glass']]
    
    # If target combination is specified, filter to compositions containing those elements
    if target_combination:
        # Parse the combination string (e.g., "Al-Fe-Ni")
        combination_elements = [elem.strip().capitalize() for elem in target_combination.split('-')]
        
        if len(combination_elements) != 3:
            print(f"Error: Combination must have exactly 3 elements. Got: {target_combination}")
            return pd.DataFrame()
        
        # Check if all elements exist in the data
        missing_elements = [elem for elem in combination_elements if elem not in df.columns]
        if missing_elements:
            print(f"Warning: Elements {missing_elements} not found in the data.")
            print(f"Available elements: {sorted([col for col in element_cols if df[col].sum() > 0])}")
            return pd.DataFrame()
        
        # Filter to compositions that contain these 3 elements (but may contain others)
        elem_masks = []
        for elem in combination_elements:
            elem_mask = (df[elem] > 0)
            elem_masks.append(elem_mask)
        
        # Combine masks using logical AND
        combination_mask = elem_masks[0]
        for mask in elem_masks[1:]:
            combination_mask = combination_mask & mask
        filtered_df = df[combination_mask].copy()
        print(f"Filtered to compositions containing combination: {target_combination}")
        
    # If target element is specified (and no combination), filter to only compositions containing that element
    elif target_element:
        # Count non-zero elements for each row
        element_counts = (df[element_cols] > 0).sum(axis=1)
        
        # Filter to exactly 3 elements
        three_element_mask = element_counts == 3
        filtered_df = df[three_element_mask].copy()
        
        target_element = target_element.capitalize()  # Ensure proper capitalization
        if target_element in filtered_df.columns:
            # Filter to compositions where the target element has > 0 concentration
            target_element_mask = filtered_df[target_element] > 0
            filtered_df = filtered_df[target_element_mask].copy()
            print(f"Filtered to compositions containing {target_element}")
        else:
            print(f"Warning: Element '{target_element}' not found in the data.")
            print(f"Available elements: {sorted([col for col in element_cols if filtered_df[col].sum() > 0])}")
            return pd.DataFrame()  # Return empty DataFrame
    
    else:
        # Default: filter to exactly 3 elements
        element_counts = (df[element_cols] > 0).sum(axis=1)
        three_element_mask = element_counts == 3
        filtered_df = df[three_element_mask].copy()
    
    return filtered_df

def analyze_element_combinations(df, target_element):
    """
    Analyze and count all 3-element combinations containing a specific element.
    
    Args:
        df (pd.DataFrame): DataFrame with 3-element compositions
        target_element (str): Element symbol to analyze
    
    Returns:
        pd.DataFrame: DataFrame with combination counts and statistics
    """
    # Filter to compositions containing the target element
    target_element = target_element.capitalize()
    if target_element not in df.columns:
        print(f"Element '{target_element}' not found in data")
        return pd.DataFrame()
    
    # Get compositions containing the target element
    target_compositions = df[df[target_element] > 0].copy()
    
    # Get element columns (exclude 'composition' and 'forms_glass')
    element_cols = [col for col in df.columns if col not in ['composition', 'forms_glass']]
    
    # Create combination strings for each composition
    combinations = []
    for _, row in target_compositions.iterrows():
        # Get the 3 elements present in this composition
        present_elements = [col for col in element_cols if row[col] > 0]
        if len(present_elements) == 3:
            # Sort elements alphabetically for consistent combination naming
            sorted_elements = sorted(present_elements)
            combination = '-'.join(sorted_elements)
            combinations.append({
                'combination': combination,
                'forms_glass': row['forms_glass'],
                'composition': row['composition']
            })
    
    # Create DataFrame and perform value counts
    comb_df = pd.DataFrame(combinations)
    
    if len(comb_df) == 0:
        print(f"No 3-element combinations found containing {target_element}")
        return pd.DataFrame()
    
    # Count total occurrences of each combination
    total_counts = comb_df['combination'].value_counts().reset_index()
    total_counts.columns = ['combination', 'total_count']
    
    # Count glass-forming occurrences
    glass_counts = comb_df[comb_df['forms_glass'] == True]['combination'].value_counts().reset_index()
    glass_counts.columns = ['combination', 'glass_count']
    
    # Count non-glass-forming occurrences
    non_glass_counts = comb_df[comb_df['forms_glass'] == False]['combination'].value_counts().reset_index()
    non_glass_counts.columns = ['combination', 'non_glass_count']
    
    # Merge all counts
    result_df = total_counts.merge(glass_counts, on='combination', how='left')
    result_df = result_df.merge(non_glass_counts, on='combination', how='left')
    
    # Fill NaN values with 0
    result_df['glass_count'] = result_df['glass_count'].fillna(0).astype(int)
    result_df['non_glass_count'] = result_df['non_glass_count'].fillna(0).astype(int)
    
    # Calculate glass-forming percentage
    result_df['glass_percentage'] = (result_df['glass_count'] / result_df['total_count'] * 100).round(1)
    
    # Sort by total count (descending)
    result_df = result_df.sort_values('total_count', ascending=False)
    
    return result_df

def create_parallel_coordinates_plot(df, output_file='glass_parallel_plot.html'):
    """
    Create a parallel coordinates plot for 3-element glass compositions.
    
    Args:
        df (pd.DataFrame): DataFrame with 3-element compositions
        output_file (str): Output HTML file name
    """
    # Get element columns
    element_cols = [col for col in df.columns if col not in ['composition', 'forms_glass']]
    
    # Filter to only elements that appear in the data
    element_cols = [col for col in element_cols if df[col].sum() > 0]
    
    # Round values to 1 decimal place to avoid floating-point precision issues
    df_rounded = df.copy()
    for col in element_cols:
        df_rounded[col] = df_rounded[col].round(1)
    
    # Create the parallel coordinates plot
    fig = go.Figure()
    
    # Separate data by glass-forming ability
    glass_forming = df_rounded[df_rounded['forms_glass'] == True]
    non_glass_forming = df_rounded[df_rounded['forms_glass'] == False]
    
    # Create numeric color column for better Plotly compatibility
    df_rounded['color_numeric'] = df_rounded['forms_glass'].astype(int)  # True=1, False=0
    
    # Create dimensions with consistent 0-100 scale
    dimensions = []
    for col in element_cols:
        dimensions.append(dict(
            label=col,
            values=df_rounded[col],
            range=[0, 100],  # Fixed scale from 0 to 100
            tickvals=list(range(0, 101, 10)),  # Tick marks every 10%
            ticktext=[f"{i}%" for i in range(0, 101, 10)]  # Tick labels with % symbol
        ))
    
    # Add single trace with color-coded lines using custom colorscale
    fig.add_trace(go.Parcoords(
        line=dict(
            color=df_rounded['color_numeric'],
            colorscale=[[0, 'red'], [1, 'blue']],  # 0=red (non-glass), 1=blue (glass)
            cmin=0,
            cmax=1
        ),
        dimensions=dimensions,
        name='Glass Forming Ability'
    ))
    
    # Update layout
    fig.update_layout(
        title='Parallel Coordinates Plot: 3-Element Glass Compositions',
        title_x=0.5,
        font=dict(size=12),
        showlegend=True,
        width=1200,
        height=600,
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    # Save the plot
    fig.write_html(output_file)
    print(f"Parallel coordinates plot saved as: {output_file}")
    
    return fig

def create_ternary_diagram(df, elements=None, a_min=0, b_min=0, c_min=0):
    """
    Create a ternary diagram for 3-element glass compositions.
    
    Args:
        df (pd.DataFrame): DataFrame with 3-element compositions
        elements (list): List of 3 element symbols in order [A, B, C] (e.g., ['Al', 'Fe', 'Ni'])
        a_min (float): Minimum value for A-axis (0-1 range)
        b_min (float): Minimum value for B-axis (0-1 range)
        c_min (float): Minimum value for C-axis (0-1 range)
    
    Returns:
        go.Figure: Plotly figure object for display in notebook
    """
    # Get element columns (should be exactly 3 for ternary plot)
    element_cols = [col for col in df.columns if col not in ['composition', 'forms_glass']]
    element_cols = [col for col in element_cols if df[col].sum() > 0]
    
    if len(element_cols) != 3:
        print(f"Error: Ternary plot requires exactly 3 elements, found {len(element_cols)}")
        return None
    
    # If elements are specified, reorder columns to match the specified order
    if elements:
        if len(elements) != 3:
            print(f"Error: Must specify exactly 3 elements, got {len(elements)}")
            return None
        
        # Check if all specified elements exist in the data
        missing_elements = [elem for elem in elements if elem not in element_cols]
        if missing_elements:
            print(f"Error: Elements {missing_elements} not found in the data")
            print(f"Available elements: {sorted(element_cols)}")
            return None
        
        # Reorder columns to match specified order
        element_cols = elements
    
    # Round values to 1 decimal place
    df_rounded = df.copy()
    for col in element_cols:
        df_rounded[col] = df_rounded[col].round(1)
    
    # Create ternary diagram
    fig = go.Figure()
    
    # Separate data by glass-forming ability
    glass_forming = df_rounded[df_rounded['forms_glass'] == True]
    non_glass_forming = df_rounded[df_rounded['forms_glass'] == False]
    
    # Add trace for glass-forming compositions (blue)
    if not glass_forming.empty:
        fig.add_trace(go.Scatterternary({
            'mode': 'markers',
            'a': glass_forming[element_cols[0]],
            'b': glass_forming[element_cols[1]],
            'c': glass_forming[element_cols[2]],
            'marker': {
                'color': 'blue',
                'size': 8,
                'symbol': 'circle'
            },
            'name': 'Glass Forming',
            'text': glass_forming['composition'],
            'hovertemplate': '<b>%{text}</b><br>' +
                           f'{element_cols[0]}: %{{a}}%<br>' +
                           f'{element_cols[1]}: %{{b}}%<br>' +
                           f'{element_cols[2]}: %{{c}}%<br>' +
                           '<extra></extra>'
        }))
    
    # Add trace for non-glass-forming compositions (red)
    if not non_glass_forming.empty:
        fig.add_trace(go.Scatterternary({
            'mode': 'markers',
            'a': non_glass_forming[element_cols[0]],
            'b': non_glass_forming[element_cols[1]],
            'c': non_glass_forming[element_cols[2]],
            'marker': {
                'color': 'red',
                'size': 8,
                'symbol': 'circle'
            },
            'name': 'Non-Glass Forming',
            'text': non_glass_forming['composition'],
            'hovertemplate': '<b>%{text}</b><br>' +
                           f'{element_cols[0]}: %{{a}}%<br>' +
                           f'{element_cols[1]}: %{{b}}%<br>' +
                           f'{element_cols[2]}: %{{c}}%<br>' +
                           '<extra></extra>'
        }))
    
    # Create title with element information
    title = f"Ternary Plot ({element_cols[0]}-{element_cols[1]}-{element_cols[2]}) with colored glass-forming ability"
    if a_min > 0 or b_min > 0 or c_min > 0:
        title += f" (A≥{a_min:.0%}, B≥{b_min:.0%}, C≥{c_min:.0%})"
    
    # Update layout with the specified ternary configuration
    fig.update_layout(
        title=title,
        title_x=0.5,
        font=dict(size=12),
        showlegend=True,
        width=800,
        height=700,
        margin=dict(l=50, r=50, t=80, b=50),
        ternary=dict(
            sum=1,
            aaxis=dict(
                title=dict(text=f"Component {element_cols[0]}", font=dict(color="red")),
                min=a_min, ticks="outside", tickformat=".0%",
                showline=True, linecolor="red",
                showgrid=True, gridcolor="red",
                tickfont=dict(color="red")
            ),
            baxis=dict(
                title=dict(text=f"Component {element_cols[1]}", font=dict(color="blue")),
                min=b_min, ticks="outside", tickformat=".0%",
                showline=True, linecolor="blue",
                showgrid=True, gridcolor="blue",
                tickfont=dict(color="blue")
            ),
            caxis=dict(
                title=dict(text=f"Component {element_cols[2]}", font=dict(color="green")),
                min=c_min, ticks="outside", tickformat=".0%",
                showline=True, linecolor="green",
                showgrid=True, gridcolor="green",
                tickfont=dict(color="green")
            ),
        )
    )
    
    # Return the figure for notebook display
    return fig

def create_custom_ternary_plot(elements, a_min=0, b_min=0, c_min=0):
    """
    Create a ternary plot with custom element order and axis minimums.
    
    Args:
        elements (list): List of 3 element symbols in order [A, B, C] (e.g., ['Al', 'Fe', 'Ni'])
        a_min (float): Minimum value for A-axis (0-1 range)
        b_min (float): Minimum value for B-axis (0-1 range)
        c_min (float): Minimum value for C-axis (0-1 range)
    
    Returns:
        go.Figure: Plotly figure object for display in notebook
    """
    if len(elements) != 3:
        print(f"Error: Must specify exactly 3 elements, got {len(elements)}")
        return None
    
    # Load data
    data_file = Path("data_files/database/glass.json")
    if not data_file.exists():
        print(f"Error: Data file not found at {data_file}")
        return None
    
    df = load_glass_data(data_file)
    combination_str = '-'.join(elements)
    df_3elem = filter_three_element_compositions(df, target_combination=combination_str)
    
    if len(df_3elem) == 0:
        print(f"No compositions found for combination {combination_str}")
        return None
    
    print(f"Found {len(df_3elem)} compositions for {combination_str}")
    
    # Create ternary diagram with custom parameters
    fig = create_ternary_diagram(
        df_3elem, 
        elements=elements,
        a_min=a_min,
        b_min=b_min,
        c_min=c_min
    )
    
    return fig

def main():
    """Main function to run the analysis."""
    # Parse command line arguments
    target_element = None
    target_combination = None
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # Check if it's a combination (contains hyphens)
        if '-' in arg:
            target_combination = arg
            print(f"Target combination specified: {target_combination}")
        else:
            target_element = arg
            print(f"Target element specified: {target_element}")
    
    # Path to the glass data file
    data_file = Path("data_files/database/glass.json")
    
    if not data_file.exists():
        print(f"Error: Data file not found at {data_file}")
        print("Please ensure the glass.json file exists in the data_files/database/ directory")
        return
    
    print("Loading glass data...")
    df = load_glass_data(data_file)
    print(f"Loaded {len(df)} compositions")
    
    print("Filtering to 3-element compositions...")
    df_3elem = filter_three_element_compositions(df, target_element, target_combination)
    
    if len(df_3elem) == 0:
        if target_combination:
            print(f"No 3-element compositions found with combination {target_combination}!")
        elif target_element:
            print(f"No 3-element compositions found containing {target_element}!")
        else:
            print("No 3-element compositions found!")
        return
    
    if target_combination:
        print(f"Found {len(df_3elem)} compositions containing combination {target_combination}")
    elif target_element:
        print(f"Found {len(df_3elem)} compositions with exactly 3 elements containing {target_element}")
    else:
        print(f"Found {len(df_3elem)} compositions with exactly 3 elements")
    
    # Show summary statistics
    glass_count = df_3elem['forms_glass'].sum()
    non_glass_count = len(df_3elem) - glass_count
    print(f"Glass-forming: {glass_count}")
    print(f"Non-glass-forming: {non_glass_count}")
    
    # Get element columns for summary
    element_cols = [col for col in df_3elem.columns if col not in ['composition', 'forms_glass']]
    element_cols = [col for col in element_cols if df_3elem[col].sum() > 0]
    
    print(f"Elements found in 3-element compositions: {sorted(element_cols)}")
    
    # Perform combination analysis if target element is specified (but not for specific combinations)
    if target_element and not target_combination:
        print(f"\nAnalyzing 3-element combinations containing {target_element}...")
        combination_analysis = analyze_element_combinations(df_3elem, target_element)
        
        if not combination_analysis.empty:
            print(f"\nFound {len(combination_analysis)} unique 3-element combinations containing {target_element}:")
            print("\nTop 20 most common combinations:")
            print("=" * 80)
            print(f"{'Combination':<25} {'Total':<8} {'Glass':<8} {'Non-Glass':<10} {'Glass %':<10}")
            print("=" * 80)
            
            for _, row in combination_analysis.head(20).iterrows():
                print(f"{row['combination']:<25} {row['total_count']:<8} {row['glass_count']:<8} {row['non_glass_count']:<10} {row['glass_percentage']:<10}%")
            
            if len(combination_analysis) > 20:
                print(f"\n... and {len(combination_analysis) - 20} more combinations")
            
            print(f"\nSummary for {target_element}-containing combinations:")
            print(f"  Total unique combinations: {len(combination_analysis)}")
            print(f"  Total compositions: {combination_analysis['total_count'].sum()}")
            print(f"  Glass-forming compositions: {combination_analysis['glass_count'].sum()}")
            print(f"  Non-glass-forming compositions: {combination_analysis['non_glass_count'].sum()}")
            print(f"  Overall glass-forming rate: {(combination_analysis['glass_count'].sum() / combination_analysis['total_count'].sum() * 100):.1f}%")
    
    # Create the parallel coordinates plot
    print("Creating parallel coordinates plot...")
    if target_combination:
        output_filename = f"glass_parallel_plot_{target_combination.replace('-', '_')}.html"
        ternary_filename = f"glass_ternary_plot_{target_combination.replace('-', '_')}.html"
    elif target_element:
        output_filename = f"glass_parallel_plot_{target_element}.html"
        ternary_filename = f"glass_ternary_plot_{target_element}.html"
    else:
        output_filename = "glass_parallel_plot.html"
        ternary_filename = "glass_ternary_plot.html"
    
    fig = create_parallel_coordinates_plot(df_3elem, output_filename)
    
    # Create ternary diagram if we have exactly 3 elements
    element_cols = [col for col in df_3elem.columns if col not in ['composition', 'forms_glass']]
    element_cols = [col for col in element_cols if df_3elem[col].sum() > 0]
    
    if len(element_cols) == 3:
        print("Creating ternary diagram...")
        # Parse elements from target_combination if specified
        elements = None
        if target_combination:
            elements = [elem.strip().capitalize() for elem in target_combination.split('-')]
        
        ternary_fig = create_ternary_diagram(df_3elem, elements=elements)
    else:
        print(f"Skipping ternary diagram: requires exactly 3 elements, found {len(element_cols)}")
    
    # Show some example compositions
    if target_combination:
        print(f"\nExample compositions containing combination {target_combination}:")
    elif target_element:
        print(f"\nExample 3-element compositions containing {target_element}:")
    else:
        print("\nExample 3-element compositions:")
    for i, row in df_3elem.head(10).iterrows():
        glass_status = "Glass" if row['forms_glass'] else "Non-glass"
        elements = [f"{col}{row[col]:.1f}%" for col in element_cols if row[col] > 0]
        print(f"  {row['composition']}: {', '.join(elements)} ({glass_status})")
    
    print(f"\nPlot saved as '{output_filename}'")
    print("Open the HTML file in a web browser to view the interactive plot.")

if __name__ == "__main__":
    main()

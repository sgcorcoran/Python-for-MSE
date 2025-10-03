# Glass Ternary Plot Usage Examples

This document demonstrates how to use the refactored `glass_ternary_plot` functionality to create ternary diagrams with custom element orders and axis minimums.

## Updated Function Signatures

The functions now work as follows:

```python
def create_ternary_diagram(df, elements=None, a_min=0, b_min=0, c_min=0):
def create_custom_ternary_plot(elements=None, a_min=0, b_min=0, c_min=0):
```

### Parameters:
- `df`: DataFrame with 3-element compositions (for `create_ternary_diagram`)
- `elements`: List of 3 element symbols in order [A, B, C] (e.g., ['Al', 'Fe', 'Ni'])
- `a_min`: Minimum value for A-axis (0-1 range, where 0.4 = 40%)
- `b_min`: Minimum value for B-axis (0-1 range)
- `c_min`: Minimum value for C-axis (0-1 range)

## Usage Examples

### Example 1: Basic Usage with Element Order
```python
# Create a ternary plot with Al-Ni-Fe in that specific order
fig = create_custom_ternary_plot(
    elements=['Al', 'Ni', 'Fe']
)

if fig:
    print("✓ Basic Al-Ni-Fe ternary plot created successfully!")
    fig.show()
else:
    print("✗ Failed to create basic ternary plot")
```

### Example 2: Custom Axis Minimums
```python
# Create a ternary plot with Al ≥ 40%, Fe ≥ 0%, Ni ≥ 0%
fig = create_custom_ternary_plot(
    elements=['Al', 'Fe', 'Ni'],
    a_min=0.4,  # Al axis starts at 40%
    b_min=0.0,  # Fe axis starts at 0%
    c_min=0.0   # Ni axis starts at 0%
)

if fig:
    print("✓ Al ≥ 40% ternary plot created successfully!")
    fig.show()
else:
    print("✗ Failed to create Al ≥ 40% ternary plot")
```

### Example 3: Different Element Order
```python
# Create a ternary plot with Ni-Fe-Al order
fig = create_custom_ternary_plot(
    elements=['Ni', 'Fe', 'Al'],
    a_min=0.3,  # Ni axis starts at 30%
    b_min=0.1,  # Fe axis starts at 10%
    c_min=0.0   # Al axis starts at 0%
)

if fig:
    print("✓ Ni-Fe-Al ternary plot created successfully!")
    fig.show()
else:
    print("✗ Failed to create Ni-Fe-Al ternary plot")
```

### Example 4: Direct Function Usage
```python
# Load data and create plot using individual functions
from glass_ternary_diag_functions import load_glass_data, filter_three_element_compositions, create_ternary_diagram

# Load the data
data_file = Path("data_files/database/glass.json")
df = load_glass_data(data_file)

# Filter to Al-Fe-Ni compositions
df_3elem = filter_three_element_compositions(df, target_combination='Al-Fe-Ni')

# Create ternary plot with custom parameters
fig = create_ternary_diagram(
    df_3elem,
    elements=['Al', 'Fe', 'Ni'],
    a_min=0.5,  # Al ≥ 50%
    b_min=0.0,  # Fe ≥ 0%
    c_min=0.0   # Ni ≥ 0%
)

if fig:
    print("✓ Direct usage ternary plot created successfully!")
    fig.show()
else:
    print("✗ Failed to create direct usage ternary plot")
```

## Ternary Plot Layout

The ternary plot uses the exact layout specification with colored axes:

```python
fig.update_layout(
    title="Ternary Diagram: Al-Fe-Ni",
    ternary=dict(
        sum=1,
        aaxis=dict(
            title=dict(text="Al", font=dict(color="red", size=14)),
            min=a_min, ticks="outside", tickformat=".0%",
            showline=True, linecolor="red",
            showgrid=True, gridcolor="red",
            tickfont=dict(color="red", size=10)
        ),
        baxis=dict(
            title=dict(text="Fe", font=dict(color="blue", size=14)),
            min=b_min, ticks="outside", tickformat=".0%",
            showline=True, linecolor="blue",
            showgrid=True, gridcolor="blue",
            tickfont=dict(color="blue", size=10)
        ),
        caxis=dict(
            title=dict(text="Ni", font=dict(color="green", size=14)),
            min=c_min, ticks="outside", tickformat=".0%",
            showline=True, linecolor="green",
            showgrid=True, gridcolor="green",
            tickfont=dict(color="green", size=10)
        ),
    ),
    height=600,
    width=600,
    showlegend=True
)
```

## Key Features

1. **Custom Element Order**: Specify exactly which elements go on which axes
2. **Custom Axis Minimums**: Set minimum values for each axis (0-1 range)
3. **Colored Axes**: Red for A-axis, blue for B-axis, green for C-axis
4. **Glass-Forming Ability**: Blue dots for glass-forming compositions, red dots for non-glass-forming
5. **Interactive Hover**: Hover over points to see composition details
6. **Automatic Title Generation**: Titles include element names and axis minimums
7. **Inline Display**: Plots display directly in Jupyter notebooks (no file saving required)

## Error Handling

The functions include comprehensive error handling:
- Validates that exactly 3 elements are specified
- Checks that all specified elements exist in the data
- Provides helpful error messages with available elements
- Returns None for invalid inputs

## Streamlit Integration

For Streamlit dashboards, use the individual functions:

```python
import streamlit as st
from glass_ternary_diag_functions import load_glass_data, filter_three_element_compositions, create_ternary_diagram

# Load data and create ternary diagram
data_file = Path("data_files/database/glass.json")
df = load_glass_data(data_file)
df_3elem = filter_three_element_compositions(df, target_combination='Al-Ni-Fe')

if len(df_3elem) > 0:
    fig = create_ternary_diagram(df_3elem, elements=['Al', 'Ni', 'Fe'])
    
    if fig:
        st.plotly_chart(fig, use_container_width=True)
        
        # Show stats
        glass_count = len(df_3elem[df_3elem['forms_glass'] == True])
        total_count = len(df_3elem)
        glass_pct = (glass_count / total_count * 100) if total_count > 0 else 0
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Total Points", total_count)
        with col_b:
            st.metric("Glass %", f"{glass_pct:.1f}%")
```

## Interactive Features

All plots are interactive and include:
- **Hover functionality**: Hover over points to see composition details
- **Zoom and pan**: Use mouse wheel to zoom, click and drag to pan
- **Legend**: Toggle visibility of glass-forming vs non-glass-forming points
- **Responsive layout**: Plots adjust to container width
# Greedy Packing Algorithm with Square for Equilateral Triangles

This repository contains a packing algorithm that utilizes a greedy approach to efficiently place components into a given material space. The algorithm has been modified to prioritize the use of squares for packing equilateral triangles, leading to improved space utilization.

## Overview

The algorithm sorts components in descending order based on their dimensions and iteratively attempts to place them in the material space. Specifically, it uses squares to efficiently pack equilateral triangles.

## Components

The `Component` class represents different types of components, including rectangles, circles, and triangles. Notably, for equilateral triangles, the algorithm utilizes squares for packing.

## Greedy Packing

The `pack_components` function has been updated to handle the modified approach. It prioritizes placing larger components first and considers the specific handling of equilateral triangles using squares.

## Visualization

The `plot_packing` function remains responsible for visualizing the packing result using matplotlib. It creates a plot with rectangles, circles, and squares representing the components in their respective positions.

## Usage

To demonstrate the modified algorithm, a set of example components is provided in the `components` list. The algorithm is run multiple times, and the packing result is visualized each time.

```python
# Example Components
components = [
    Component("Rectangle", (width, height), amount),
    Component("Rectangle", (width, height), amount),
    Component("Rectangle", (width, height), amount),
    Component("Triangle", (width, height), amount),
    Component("Triangle", (width, height), amount),
    Component("Circle", (Diameter, Diameter), amount),  # Diameter = radius * 2
    Component("Circle", (Diameter, Diameter), amount),
]

# Initialize counters and arrays
initialize cnt array to zeros of the same length as components
remaining_area_array = []
used = 0

# Continue packing until all components are placed
while sum of remaining quantities in components is not 0:
    initialize cur array to zeros of the same length as components
    record the start time
    
    # Set material dimensions
    material_width = 200
    material_height = 100
    area = material_width * material_height
    
    # Execute packing algorithm
    packed_items, remaining_area = pack_components(material_width, material_height, components)
    
    # Visualize the packing result
    plot_packing(material_width, material_height, packed_items)
    
    # Calculate and append remaining area percentage
    remaining_area_percentage = remaining_area / area
    append remaining_area_percentage to remaining_area_array
    
    # Update counts based on the current and total counts
    for each component in components:
        update cnt array based on current and total counts
    
    # Output information about each iteration

# Output total used time, number of leather pieces used, and remaining area array
print(f' total use time {time.time()-start}')
print(f' use leather {used} pieces')
print(f' remaining_area {remaining_area_array}')


<footer>
    <p>&copy; 2024 ChenYongJin and ChenPinHan. All rights reserved.</p>
</footer>
# Greedy Packing Algorithm with Square for Equilateral Triangles

This repository presents a packing algorithm that employs a greedy approach to place components into a given material space. Notably, the algorithm utilizes squares to pack equilateral triangles efficiently.

## Overview

The modified algorithm prioritizes the use of squares to pack equilateral triangles, aiming for better space utilization. The components are sorted in descending order based on their dimensions, and the algorithm iteratively attempts to place them in the material space.

## Components

The `Component` class still represents different types of components, including rectangles, circles, and triangles. However, for equilateral triangles, the algorithm uses squares for packing.

## Greedy Packing

The `pack_components` function has been updated to handle the modified approach. It now considers the specific handling of equilateral triangles using squares for packing. The algorithm prioritizes placing larger components first.

## Visualization

The `plot_packing` function remains responsible for visualizing the packing result using matplotlib. It creates a plot with rectangles, circles, and squares representing the components in their respective positions.

## Usage

To demonstrate the modified algorithm, a set of example components is provided in the `components` list. The algorithm is run multiple times, and the packing result is visualized each time.

```python
# Example Components
components = [
    Component("Rectangle", (20, 50), 10),
    Component("Rectangle", (20, 15), 20),
    Component("Rectangle", (15, 15), 10),
    Component("Triangle", (10, 10), 20),
    Component("Triangle", (15, 15), 15),
    Component("Circle", (10, 10), 15),
    Component("Circle", (20, 20), 40),
]

# Run the Greedy Packing Algorithm
remaining_area_array = []
used = 0
while sum([i.remaining_quantity for i in components]) != 0:
    # ...

    # Algorithm Execution
    packed_items, remaining_area = pack_components(material_width, material_height, components)
    plot_packing(material_width, material_height, packed_items)

    # ...

    # Update counts
    cnt = [x + y for x, y in zip(cnt, cur)]

    # ...

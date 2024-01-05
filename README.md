# Class to represent different components
class Component:
    function Component(type, dimensions, quantity):
        self.type = type
        self.dimensions = dimensions
        self.quantity = quantity
        self.remaining_quantity = quantity

# Greedy packing algorithm function
function pack_components(material_width, material_height, components, max_iterations=1000):
    packed_items = []
    used_area = 0
    
    # Sort components by area in descending order
    sort components by dimensions[0] * dimensions[1] in descending order
    
    # Create a 2D grid to represent the material space
    material_grid = create 2D array of size material_height x material_width filled with zeros
    
    # Repeat the packing process for a specified number of iterations
    repeat max_iterations times:
        all_placed = true
        
        # Iterate through each component in sorted order
        for each component in components:
            placed_quantity = 0
            
            # Iterate through each position in the material grid
            for i in range(material_height):
                for j in range(material_width):
                    # Try to place the component in the current position
                    if component.remaining_quantity > 0 and try_place_component(material_grid, i, j, component):
                        # Update packed items, remaining quantity, and used area
                        append (i, j, component) to packed_items
                        component.remaining_quantity -= 1
                        placed_quantity += 1
                        
                        # Update used area based on the component type
                        if component.type is "Rectangle":
                            used_area += component.dimensions[0] * component.dimensions[1]
                        elif component.type is "Circle":
                            used_area += component.dimensions[0] * component.dimensions[1] * π / 4
                        elif component.type is "Triangle":
                            used_area += component.dimensions[0] * component.dimensions[1] * √3 / 4
                        
                        all_placed = false
        
        # Calculate remaining area and check termination conditions
        remaining_area = material_width * material_height - used_area
        if remaining_area <= 0 or all_placed:
            exit loop
    
    return packed_items, remaining_area

# Function to attempt placing a component in the material grid
function try_place_component(material_grid, row, col, component):
    height, width = dimensions of material_grid
    
    # Check if the component exceeds the material grid boundaries
    if row + component.dimensions[0] > height or col + component.dimensions[1] > width:
        return false
    
    # Check if the positions in the grid are already occupied
    for i in range(component.dimensions[0]):
        for j in range(component.dimensions[1]):
            if material_grid[row + i][col + j] is not 0:
                return false
    
    # Place the component in the grid
    for i in range(component.dimensions[0]):
        for j in range(component.dimensions[1]):
            material_grid[row + i][col + j] = component.type
    
    return true

# Function to visualize the packing result using matplotlib
function plot_packing(material_width, material_height, packed_items):
    create figure and axes using matplotlib
    set x-axis limit to [0, material_width]
    set y-axis limit to [0, material_height]
    
    # Iterate through each packed item and plot the corresponding patch
    for each item in packed_items:
        component = item[2]
        if component.type is "Rectangle":
            create rectangle patch and add to axes
        elif component.type is "Circle":
            create circle patch and add to axes
        elif component.type is "Triangle":
            create triangle patch and add to axes
    
    # Set aspect ratio of axes to 'equal' and show the plot with a title

# Example components
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

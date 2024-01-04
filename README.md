class Component:
    type
    dimensions
    quantity
    remaining_quantity

function pack_components(material_width, material_height, components, max_iterations=1000):
    packed_items = []
    used_area = 0
    sort components by area in descending order
    initialize material_grid with zeros

    repeat max_iterations times:
        all_placed = true
        for each component in components:
            placed_quantity = 0
            for row in material_height:
                for col in material_width:
                    if try_place_component(material_grid, row, col, component):
                        update packed_items, remaining_quantity, used_area
                        set all_placed to false

        remaining_area = calculate remaining area
        if remaining_area <= 0 or all_placed:
            break

    return packed_items, remaining_area

function try_place_component(material_grid, row, col, component):
    if placement is outside material boundaries:
        return false

    for each cell in component:
        if cell is already occupied:
            return false

    mark cells as occupied
    return true

function plot_packing(material_width, material_height, packed_items):
    create plot
    set plot limits
    for each item in packed_items:
        create shape based on component type and dimensions
        add shape to plot
    display plot

components = [list of Component objects]

remaining_area_arr = empty list
used = 0

while sum of remaining quantities in components is not zero:
    set material_width and material_height
    calculate total area

    perform packing
    plot packing result
    update remaining_area_arr
    print remaining area percentage and time taken for each iteration

    for each component in components:
        print component details

print total time taken and number of leather pieces used
print remaining_area_arr

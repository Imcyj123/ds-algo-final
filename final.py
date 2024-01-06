import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time
import math
start = time.time()

class Component:
    def __init__(self, type, dimensions, quantity):
        self.type = type
        self.dimensions = dimensions
        self.quantity = quantity
        self.remaining_quantity = quantity

def pack_components(material_width, material_height, components, max_iterations=1000):
    packed_items = []
    used_area = 0
    components.sort(key=lambda x: x.dimensions[0] * x.dimensions[1], reverse=True)
    material_grid = [[0 for _ in range(material_width)] for _ in range(material_height)]
    for _ in range(max_iterations):
        all_placed = True
        for idx in range(len(components)):
            placed_quantity = 0
            i = 0
            for i in range(material_height):
                j = 0
                for j in range(material_width):
                    if components[idx].remaining_quantity > 0 and try_place_component(material_grid, i, j, components[idx]):
                        packed_items.append((i, j, components[idx]))
                        components[idx].remaining_quantity -= 1
                        placed_quantity += 1
                        cur[idx]+=1
                        if components[idx].type == "Rectangle":
                            used_area += components[idx].dimensions[0] * components[idx].dimensions[1]
                        elif components[idx].type == "Circle":
                            used_area += components[idx].dimensions[0] * components[idx].dimensions[1] * math.pi / 4
                        elif components[idx].type == "Triangle":
                            used_area += components[idx].dimensions[0] * components[idx].dimensions[1] * math.sqrt(3) / 4
                        all_placed = False
        remaining_area = material_width * material_height - used_area
        if remaining_area <= 0 or all_placed:
            break
    return packed_items, remaining_area


def try_place_component(material_grid, row, col, component):
    height, width = len(material_grid), len(material_grid[0])
    if row + component.dimensions[0] > height or col + component.dimensions[1] > width:
        return False
    for i in range(component.dimensions[0]):
        for j in range(component.dimensions[1]):
            if material_grid[row + i][col + j] != 0:
                return False
    for i in range(component.dimensions[0]):
        for j in range(component.dimensions[1]):
            material_grid[row + i][col + j] = component.type
    return True
def plot_packing(material_width, material_height, packed_items):
    fig, ax = plt.subplots()
    ax.set_xlim([0, material_width])
    ax.set_ylim([0, material_height])
    for item in packed_items:
        component = item[2]
        if component.type == "Rectangle":
            rect = patches.Rectangle((item[1], item[0]), component.dimensions[1], component.dimensions[0], linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(rect)
        elif component.type == "Circle":
            circle = patches.Circle((item[1] + component.dimensions[1] / 2, item[0] + component.dimensions[0] / 2), component.dimensions[1] / 2, linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(circle)
        elif component.type == "Triangle":
            triangle = patches.Polygon([
                (item[1], item[0] + component.dimensions[0]),
                (item[1] + component.dimensions[1] / 2, item[0]),
                (item[1] + component.dimensions[1], item[0] + component.dimensions[0])
            ], linewidth=1, edgecolor='b', facecolor='none')
            ax.add_patch(triangle)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'Packing Result for Components')
    plt.show()
components = [
    Component("Rectangle", (width, height), amount),
    Component("Rectangle", (width, height), amount),
    Component("Rectangle", (width, height), amount),
    Component("Triangle", (width, height), amount),
    Component("Triangle", (width, height), amount),
    Component("Circle", (Diameter, Diameter), amount),  # Diameter = radius * 2
    Component("Circle", (Diameter, Diameter), amount),
]
cnt = [0 for _ in components]
remaining_area_array = []
used = 0
while sum([i.remaining_quantity for i in components]) != 0:
    cur = [0 for _ in components]
    each_time = time.time()
    used += 1
    material_width = width
    material_height = height
    area = material_width * material_height
    packed_items, remaining_area = pack_components(material_width, material_height, components)
    plot_packing(material_width, material_height, packed_items)
    print(f"Remaining Area%: {remaining_area / area}")
    remaining_area_array.append(float(remaining_area / area))
    print(f" each time : {time.time() - each_time}")
    cnt = [x + y for x, y in zip(cnt, cur)]
    for i, component in enumerate(components):
        print(f"{i + 1}. {component.type},{component.dimensions}, {component.quantity}, remaining: {component.remaining_quantity}, total_count: {cnt[i]}, count: {cur[i]}")
print(f' total use time {time.time()-start}')
print(f' use leather {used} pieces')
print(f' remaining_area {remaining_area_array}')

# &copyright © 2024 ChenYongJin and ChenPinHan. All rights reserved. #
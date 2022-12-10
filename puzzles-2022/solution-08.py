"""https://adventofcode.com/2022/day/8

Incomplete and Buggy
"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-08.txt')
    tree_grid = build_two_d_array(lines)
    return find_visible_trees(tree_grid)

def build_two_d_array(lines):
    output = []
    for line in lines:
        digits = [int(x) for x in str(line) if x != '\n']
        output.append(digits)
    return output

def find_visible_trees(tree_grid):
    tree_grid_width = len(tree_grid[0])
    tree_grid_height = len(tree_grid)

    # trees on perimeter
    count = calculate_perimeter(tree_grid_width, tree_grid_height)

    # evalute interior trees
    tree_grid_width_range = range(1, tree_grid_width - 1)
    tree_grid_height_range = range(1, tree_grid_height - 1)
    for row_index in tree_grid_width_range:
        tree_row = tree_grid[row_index]
        for col_index in tree_grid_height_range:
            if is_visible_from_row(col_index, tree_row):
                count += 1
            elif is_visible_from_column(row_index, col_index, tree_grid):
                count += 1
    return count

def calculate_perimeter(width, height):
    width_without_corners = width - 2
    height_without_corners = height - 2
    corners = 4
    return (width_without_corners * 2) + (height_without_corners * 2) + corners

def is_visible_from_row(col_index, tree_row):
    tree = tree_row[col_index]
    left_side = tree_row[0:col_index]
    if is_visible_on_horizontal_side(left_side, tree):
        return True
    right_side = tree_row[col_index+1:]
    if is_visible_on_horizontal_side(right_side, tree):
        return True
    return False

# TODO: double check me
def is_visible_from_column(row_index, col_index, tree_grid):
    tree_grid_side = len(tree_grid)
    tree = tree_grid[row_index][col_index]
    col_top_range = range(0,row_index)
    if is_visible_from_vertical_range(tree_grid, row_index, col_top_range, tree):
        return True
    col_bottom_range = range(row_index, tree_grid_side)
    if is_visible_from_vertical_range(tree_grid, row_index, col_bottom_range, tree):
        return True
    return False

def is_visible_from_vertical_range(tree_grid, row_index, vertical_range, tree):
    for index in vertical_range:
        other_tree = tree_grid[row_index][index]
        if other_tree >= tree:
            return False
    return True

def is_visible_on_horizontal_side(side, tree):
    # initally did with list comp, but this lets me break in middle
    for other_tree in side:
        if other_tree >= tree:
            return False
    return True

print(part_one()) # 2666 is too high ):
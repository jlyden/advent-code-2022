"""https://adventofcode.com/2022/day/8

Part One done
TODO: rework part one for more code reuse (in light of part two)
"""

from helpers import arrays
from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-08.txt')
    tree_grid = arrays.build_two_d_int_array(lines)
    if part == 'one':
        return find_visible_trees(tree_grid)
    scenic_scores = calculate_scenic_scores(tree_grid)
    scenic_scores.sort(reverse=True)
    return scenic_scores[0]

def calculate_scenic_scores(tree_grid):
    scenic_scores = []

    tree_grid_width = len(tree_grid[0])
    tree_grid_height = len(tree_grid)

    # can skip all perimeter trees, b/c 0 vis on one side kills score
    # evalute interior trees
    tree_grid_width_range = range(1, tree_grid_width - 1)
    tree_grid_height_range = range(1, tree_grid_height - 1)
    for tree_row_index in tree_grid_width_range:
        for tree_col_index in tree_grid_height_range:
            tree = tree_grid[tree_row_index][tree_col_index]
            horz_product = get_vis_tree_product_in_horizontal_range(tree, tree_col_index, tree_grid[tree_row_index])
            vertical_product = get_vis_tree_product_in_vertical_range(tree_grid, tree_row_index, tree_col_index)
            scenic_scores.append(horz_product * vertical_product)
    return scenic_scores

def get_vis_tree_product_in_horizontal_range(tree, tree_col_index, tree_row):
    left_vis_tree_count = get_vis_tree_count_in_horizontal_range(tree, tree_row, range(tree_col_index-1, -1, -1))
    right_vis_tree_count = get_vis_tree_count_in_horizontal_range(tree, tree_row, range(tree_col_index+1, len(tree_row)))
    return left_vis_tree_count * right_vis_tree_count

def get_vis_tree_count_in_horizontal_range(tree, tree_row, horz_range):
    vis_tree_count = 0
    for tree_col_index in horz_range:
        other_tree = tree_row[tree_col_index]
        if tree > other_tree:
            vis_tree_count += 1
        elif tree <= other_tree:
            vis_tree_count += 1
            break
    return vis_tree_count

def get_vis_tree_product_in_vertical_range(tree_grid, tree_row_index, tree_col_index):
    tree = tree_grid[tree_row_index][tree_col_index]
    top_vis_tree_count = get_vis_tree_count_in_vertical_range(tree, tree_grid, tree_col_index, range(tree_row_index-1, -1, -1))
    bottom_vis_tree_count = get_vis_tree_count_in_vertical_range(tree, tree_grid, tree_col_index, range(tree_row_index+1, len(tree_grid)))
    return top_vis_tree_count * bottom_vis_tree_count

def get_vis_tree_count_in_vertical_range(tree, tree_grid, tree_col_index, vert_range):
    vis_tree_count = 0
    for tree_row_index in vert_range:
        other_tree = tree_grid[tree_row_index][tree_col_index]
        if tree > other_tree:
            vis_tree_count += 1
        elif tree <= other_tree:
            vis_tree_count += 1
            break
    return vis_tree_count

def find_visible_trees(tree_grid):
    tree_grid_width = len(tree_grid[0])
    tree_grid_height = len(tree_grid)

    # trees on perimeter
    count = calculate_perimeter(tree_grid_width, tree_grid_height)

    # evalute interior trees
    tree_grid_width_range = range(1, tree_grid_width - 1)
    tree_grid_height_range = range(1, tree_grid_height - 1)
    for tree_row_index in tree_grid_width_range:
        tree_row = tree_grid[tree_row_index]
        for tree_col_index in tree_grid_height_range:
            if is_visible_from_row(tree_col_index, tree_row):
                count += 1
            elif is_visible_from_column(tree_row_index, tree_col_index, tree_grid):
                count += 1
    return count

def calculate_perimeter(width, height):
    width_without_corners = width - 2
    height_without_corners = height - 2
    corners = 4
    return (width_without_corners * 2) + (height_without_corners * 2) + corners

def is_visible_from_row(tree_col_index, tree_row):
    tree = tree_row[tree_col_index]
    left_side = tree_row[0:tree_col_index]
    if is_visible_on_horizontal_side(left_side, tree):
        return True
    right_side = tree_row[tree_col_index+1:]
    if is_visible_on_horizontal_side(right_side, tree):
        return True
    return False

def is_visible_from_column(tree_row_index, tree_col_index, tree_grid):
    tree_grid_height = len(tree_grid)
    tree = tree_grid[tree_row_index][tree_col_index]
    col_top_range = range(0,tree_row_index)
    if is_visible_from_vertical_range(tree_grid, tree_col_index, col_top_range, tree):
        return True
    col_bottom_range = range(tree_row_index+1, tree_grid_height)
    if is_visible_from_vertical_range(tree_grid, tree_col_index, col_bottom_range, tree):
        return True
    return False

def is_visible_from_vertical_range(tree_grid, col_index, vertical_range, tree):
    for index in vertical_range:
        other_tree = tree_grid[index][col_index]
        if other_tree >= tree:
            return False
    return True

def is_visible_on_horizontal_side(side, tree):
    # initally did with list comp, but this lets me break in middle
    for other_tree in side:
        if other_tree >= tree:
            return False
    return True

print(runner('one'))
print(runner('two'))
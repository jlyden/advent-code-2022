"""https://adventofcode.com/2022/day/12"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')
    heightmap, S, E = process_lines(lines)

    return


def process_lines(lines):
    coords_S = None
    # I don't think I need this
    coords_E = None
    heightmap = []
    for row_index, line in enumerate(lines):
        line = line.replace('\n', '')
        if coords_S is None:
            coords_S = set_point_coords(row_index, line, 'S')
        if coords_E is None:
            coords_E = set_point_coords(row_index, line, 'E')
        heightmap.append(line)
    return heightmap, coords_S, coords_E

def set_point_coords(row_index, line, target_letter):
    col_index = line.find(target_letter)
    if col_index > -1:
        return row_index, col_index
    return None

def walk_the_map(heightmap, coords_S):
        
    return

def is_accessible_step(current_step, next_step):
    return ord(next_step) <= ord(current_step) + 1

def is_target(current_step_value):
    return current_step_value == 'E'


print(part_one())
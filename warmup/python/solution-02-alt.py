"""https://adventofcode.com/2021/day/2

Alternate solution reducing duplicate code between two problems
"""

import pathlib

def _update_vert_pos_part_one(vert_pos, vert_change, _):
    vert_pos = vert_pos + vert_change
    vert_change = 0
    return vert_pos, vert_change

def _update_vert_pos_part_two(vert_pos, vert_change, value):
    vert_pos = vert_pos + (vert_change * value)
    vert_change = vert_change
    return vert_pos, vert_change

def runner(part):
    match part:
        case 'one':
            update_vert_pos_callback = _update_vert_pos_part_one
        case 'two':
            update_vert_pos_callback = _update_vert_pos_part_two
        case _:
            raise Exception('Invalid part: ' + part)

    input_file = pathlib.Path(__file__).parent.absolute() / 'input-02.txt'
    with open(input_file) as file:
        horz_pos = 0
        vert_pos = 0
        vert_change = 0

        while True:
            line = file.readline()
            if not line:
                break
            
            parts = line.split(' ')
            direction = parts[0]
            value = int(parts[1])

            match direction:
                case 'forward':
                    horz_pos += value
                    vert_pos, vert_change = update_vert_pos_callback(vert_pos, vert_change, value)
                case 'down':
                    vert_change += value
                case 'up':
                    vert_change -= value
                case _:
                    raise Exception('Invalid direction: ' + direction)
    
    return horz_pos * vert_pos

print(runner('one'));
print(runner('two'));
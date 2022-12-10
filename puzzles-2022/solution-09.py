"""https://adventofcode.com/2022/day/9

Incomplete
"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')
    tail_positions = track_movements(lines)
    return len(set(tail_positions))

def track_movements(lines):
    head = [0,0]
    tails = [(0,0)]
    last_direction = None

    for line in lines:
        direction = line[0]
        spaces = int(line[2])
        tail = tails[-1]
        axis = get_axis_of_direction(direction)
        on_same_axis = axis == get_axis_of_direction(last_direction)

        move_func = get_move_func(direction)
        head = move_func(head[0], head[1], spaces)

        if on_same_axis:
            tail_moves = get_tail_moves_same_axis(head, tail, axis, move_func)
        elif spaces == 1:
            # Still touching
            continue
        else:
            print('other axis!')
            # diagonal, then other moves

        tails += tail_moves
        last_direction = direction

        print(spaces)
        print(tails)
    return tails

def get_tail_moves_other_axis(head, current_tail, move_func):

    return

def get_tail_moves_same_axis(head, current_tail, axis, move_func):
    [head_x, head_y] = head
    tail_x, tail_y = current_tail
    tail_moves = []

    match axis:
        case 'y_axis':
            spaces_to_move = head_y - tail_y - 1
        case 'x_axis':
            spaces_to_move = head_x - tail_x - 1
        case _:
            raise Exception('Invalid axis ' + axis)

    for _ in range(spaces_to_move):
        tail_x, tail_y = move_func(tail_x, tail_y, 1)
        tail_moves.append((tail_x, tail_y))

    return tail_moves

def is_same_axis(last_direction, direction):
    return get_axis_of_direction(last_direction) == get_axis_of_direction(direction)

def get_axis_of_direction(direction):
    y_axis = ['U', 'D']
    if direction in y_axis:
        return 'y_axis'
    else:
        return 'x_axis'

def get_move_func(direction):
    match direction:
        case 'R':
            move_func = move_right
        case 'U':
            move_func = move_up
        case 'L':
            move_func = move_left
        case 'D':
            move_func = move_down
        case _:
            raise Exception('Invalid direction')
    return move_func

def move_right(x, y, spaces):
    return x + spaces, y

def move_left(x, y, spaces):
    return x - spaces, y

def move_up(x, y, spaces):
    return x, y + spaces

def move_down(x, y, spaces):
    return x, y - spaces

print(part_one())
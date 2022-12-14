"""https://adventofcode.com/2022/day/13"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')
    valid_packet_indices = get_valid_packet_indices(lines)
    return sum(valid_packet_indices)

def get_valid_packet_indices(lines):
    valid_indices = []
    current_index = 1
    stop = len(lines) - 2

    for lines_index in range(0,stop,3):
        left = lines[lines_index].replace('\n', '')
        right = lines[lines_index + 1].replace('\n', '')

        if are_properly_ordered(left, right):
            valid_indices.append(current_index)
        current_index += 1
    print(valid_indices)
    return valid_indices

# takes two strings that look like lists
def are_properly_ordered(whole_left, whole_right):
    # sanity checks
    if not list_opener(whole_left[0]) or not list_closer(whole_left[-1]):
        raise Exception('Invalid left list? ' + whole_left)
    if not list_opener(whole_right[0]) or not list_closer(whole_right[-1]):
        raise Exception('Invalid right list? ' + whole_right)

    left = whole_left[1:-1]
    right = whole_right[1:-1]

    for index, left_char in enumerate(left):
        right_char = right[index]
        left_num = left_char.isnumeric()
        right_num = right_char.isnumeric()
        if left_num and right_num:
            if int(left_char) > int(right_char):
                return False
        if not left_num and not right_num:
            if left_char == right_char:
                continue
            # either [, ], or ,
        if 

    return True

def list_opener(char):
    return char == '['

def list_closer(char):
    return char == ']'

def is_comma(char):
    return char == ','

print(part_one())


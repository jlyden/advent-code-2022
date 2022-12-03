"""https://adventofcode.com/2022/day/3"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-03.txt')
    shared_items = [find_shared_item_in_split_line(line) for line in lines]
    return sum([calculate_priority(item) for item in shared_items])

def part_two():
    lines = files.get_contents_of_input_file('input-03.txt')
    badges = []

    # process lines in sets of three
    stop = len(lines) - 2
    for i in range(0, stop, 3):
        badges.append(find_common_item_among_three_lines(lines[i], lines[i+1], lines[i+2]))

    return sum([calculate_priority(badge) for badge in badges])

def find_shared_item_in_split_line(line):
    inventory = line.replace('\n','')
    halfway = int(len(inventory)/2)
    first_half = inventory[0:halfway+1]
    second_half = inventory[halfway:]
    for item in first_half:
        if item in second_half:
            # Spec says only one shared item
            return item

def find_common_item_among_three_lines(line_one, line_two, line_three):
    inv_one = line_one.replace('\n','')
    inv_two = line_two.replace('\n','')
    inv_three = line_three.replace('\n','')
    for item in inv_one:
        if item in inv_two:
            if item in inv_three:
                return item

"""Calculates priority per spec, using ascii value as starting point

Used http://sticksandstones.kstrom.com/appen.html for ascii values
"""
def calculate_priority(item):
    ascii_value = ord(item)
    return (ascii_value - 96) if is_lowercase_letter(ascii_value) else (ascii_value - 38)

"""For purposes of this puzzle"""
def is_lowercase_letter(ascii_value):
    return ascii_value > 96

print(part_one())
print(part_two())
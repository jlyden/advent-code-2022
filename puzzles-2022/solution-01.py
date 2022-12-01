"""https://adventofcode.com/2022/day/1"""

import pathlib

def part_one():
    input_file = pathlib.Path(__file__).parent.absolute() / 'input-01.txt'
    with open(input_file) as file:
        lines = file.readlines()
    
    inventories = process_input(lines)
    calories_in_inventories = [sum(inventory) for inventory in inventories]
    return max(calories_in_inventories)

def process_input(lines):
    inventories = []
    inventory = []

    for line in lines:
        if line == '\n':
            # new inventory
            inventories.append(inventory)
            inventory = []
        else:
            inventory.append(int(line))
    
    # last inventory needs to be added
    inventories.append(inventory)
    return inventories


print(part_one())
"""http://adventofcode.com/2022/day/6"""

import pathlib

def part_one():
    input_file = pathlib.Path(__file__).parent / 'input' / 'input-06.txt'

    with open(input_file) as file:
        datastream = file.read()
    
    count = 0
    while True:
        potential_marker = datastream[count:count + 4]
        if is_marker(potential_marker):
            return count + 4
            
        if len(potential_marker) < 4:
            break

        count += 1

    # Broke out of loop, which means value was not found
    raise Exception('Marker not found in this data')    
            
def is_marker(potential_marker):
    # sets values are always unique
    marker_set = set([*potential_marker])
    return len(marker_set) == 4

print(part_one())
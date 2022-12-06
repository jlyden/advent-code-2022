"""http://adventofcode.com/2022/day/6"""

import pathlib

def get_first_marker_for_length(length):
    input_file = pathlib.Path(__file__).parent / 'input' / 'input-06.txt'

    with open(input_file) as file:
        datastream = file.read()
    
    count = 0
    while True:
        potential_marker = datastream[count:count + length]
        if is_marker(potential_marker, length):
            return count + length
            
        if len(potential_marker) < length:
            break

        count += 1

    # Broke out of loop, which means value was not found
    raise Exception('Marker not found in this data')    


def is_marker(potential_marker, length):
    # sets values are always unique
    marker_set = set([*potential_marker])
    return len(marker_set) == length


print(get_first_marker_for_length(4))
print(get_first_marker_for_length(14))
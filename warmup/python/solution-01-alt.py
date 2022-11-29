"""https://adventofcode.com/2021/day/1

Alt approach with more shared code
"""

import pathlib

def runner(part):
    input_file = pathlib.Path(__file__).parent.absolute() / 'input-01.txt'
    with open(input_file) as file:
        increases = 0
        contents = file.readlines()
        measurements = [int(value) for value in contents]
        length = len(measurements)

        match part:
            case 'one':
                previous = measurements[0]
                stop = length
            case 'two':
                previous = sum(measurements[0:3])
                # Stop when not enough measurements for sum of 3
                stop = length-2
            case _:
                raise Exception('Invalid part: ' + part)

        for i in range(1,stop):
            current = measurements[i] if part == 'one' else sum(measurements[i:i+3])
            if (current > previous):
                increases += 1
            previous = current
        
    return increases

print(runner('one'))
print(runner('two'))
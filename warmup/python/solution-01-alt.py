"""https://adventofcode.com/2021/day/1

Alt approach with more shared code
"""

from helpers import files

def runner(part):
    increases = 0
    lines = files.get_contents_of_input_file('input-01.txt')
    measurements = [int(value) for value in lines]
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
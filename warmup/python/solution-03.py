"""https://adventofcode.com/2021/day/3

Could do Part One by building a numpy.array then using numpy.transpose
To avoid extra installs, sticking to loops here
"""

import pathlib

def part_one():
    input_file = pathlib.Path(__file__).parent.absolute() / 'input-03.txt'
    zero_count = []
    line_count = 0
    with open(input_file) as file:
        contents = file.readlines()
        line_count = len(contents)
        first_line = contents.pop(0)
        zero_count = generate_zero_count(first_line)
        for line in contents:
            digits = list(line)
            zero_count = update_zero_count(zero_count, digits)

    gamma_rate, epsilon_rate = _determine_rates(zero_count, line_count)
    return gamma_rate * epsilon_rate

def _determine_rates(zero_count, line_count):
    gamma_rate_string = ''
    epsilon_rate_string = ''
    halfway = int(line_count / 2)
    for value in zero_count:
        if value >= halfway:
            gamma_rate_string += '0'
            epsilon_rate_string += '1'
        else:
            gamma_rate_string += '1'
            epsilon_rate_string += '0'
    gamma_rate = int(gamma_rate_string, 2)
    epsilon_rate = int(epsilon_rate_string, 2)
    return gamma_rate, epsilon_rate

def generate_zero_count(first_line):
    zero_count = []
    digits = list(first_line)
    for digit in digits:
        if (digit != '\n'):
            zero_count.append(1 if digit == '0' else 0)
    return zero_count

def update_zero_count(zero_count, line):
    digits = list(line)
    for count, item in enumerate(digits):
        if (item != '\n'):
            zero_count[count] += (1 if item == '0' else 0)
    return zero_count

print(part_one())
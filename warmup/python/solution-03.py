"""https://adventofcode.com/2021/day/3

Could do Part One by building a numpy.array then using numpy.transpose
To avoid extra installs, sticking to loops here
"""

import pathlib

def runner(part):
    input_file = pathlib.Path(__file__).parent.absolute() / 'input-03.txt'
    with open(input_file) as file:
        contents = file.readlines()
        line_count = len(contents)
        contents_processed = []
        digits = convert_binary_string_to_int_list(contents[0])
        zero_count = initiate_zero_count(digits)
        contents_processed.append(digits)
        for i in range(1, line_count):
            digits = convert_binary_string_to_int_list(contents[i])
            zero_count = update_zero_count(zero_count, digits)
            contents_processed.append(digits)
    gamma_rate_string, epsilon_rate_string = determine_binary_rates(zero_count, line_count)
    
    if part == 'one':
        gamma_rate = int(gamma_rate_string, 2)
        epsilon_rate = int(epsilon_rate_string, 2)
        return gamma_rate * epsilon_rate
    
    # Continue from here for part_two
    for i in range(0,len(gamma_rate)):
        zero_list, one_list = split_list_between_digits_at_position(contents_processed)




    return

def convert_binary_string_to_int_list(line):
    return [int(value) for value in list(line) if value != '\n']

"""Decided two methods was better than a conditional evaluated on every line"""
def initiate_zero_count(digits):
    zero_count = []
    for digit in digits:
        zero_count.append(1 if digit == 0 else 0)
    return zero_count

def update_zero_count(zero_count, digits):
    for count, item in enumerate(digits):
        zero_count[count] += (1 if item == 0 else 0)
    return zero_count

def determine_binary_rates(zero_count, line_count):
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
    return gamma_rate_string, epsilon_rate_string

def split_list_between_digits_at_position(list, position):
    zero_list = []
    one_list = []
    for item in list:
        if item[position] == '0':
            zero_list.append(item)
        else:
            one_list.append(item)
    return zero_list, one_list

def get_most_or_least_list(zero_list, one_list, most):
    zero_len = len(zero_list)
    one_len = len(one_list)

    lists_are_equal = zero_len == one_len
    if lists_are_equal:
        return one_list if most else zero_list

    if most:
        return zero_list if zero_len > one_len else one_list
    else:
        return zero_list if zero_len < one_len else one_list


print(runner('one'))
print(runner('two'))

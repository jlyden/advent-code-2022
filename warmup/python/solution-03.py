"""https://adventofcode.com/2021/day/3

Could do Part One by building a numpy.array then using numpy.transpose
To avoid extra installs, sticking to loops here
"""

from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-03.txt')
    line_count = len(lines)
    contents_processed = []
    digits = convert_binary_string_to_int_list(lines[0])
    zero_count = initiate_zero_count(digits)
    contents_processed.append(digits)
    for i in range(1, line_count):
        digits = convert_binary_string_to_int_list(lines[i])
        zero_count = update_zero_count(zero_count, digits)
        contents_processed.append(digits)
    gamma_rate_string, epsilon_rate_string = determine_binary_rates(zero_count, line_count)
    
    if part == 'one':
        gamma_rate = int(gamma_rate_string, 2)
        epsilon_rate = int(epsilon_rate_string, 2)
        return gamma_rate * epsilon_rate
    
    # Continue from here for part_two
    zero_list, one_list = split_list_between_digits_at_position(contents_processed, 0)
    init_ox_gen_list, init_co_scrub_list = determine_most_least_list(zero_list, one_list)

    ox_gen_rate = calculate_ox_gen_rate(init_ox_gen_list, len(gamma_rate_string))
    co_scrub_rate = calculate_co_scrub_rate(init_co_scrub_list, len(gamma_rate_string))
    return ox_gen_rate * co_scrub_rate

def convert_binary_string_to_int_list(line):
    return [int(value) for value in list(line) if value != '\n']

def convert_int_list_to_binary_string(list):
    return ''.join([str(element) for element in list])

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
        if item[position] == 0:
            zero_list.append(item)
        else:
            one_list.append(item)
    return zero_list, one_list

def determine_most_least_list(zero_list, one_list):
    zero_len = len(zero_list)
    one_len = len(one_list)
    lists_are_equal = zero_len == one_len

    if lists_are_equal or one_len > zero_len:
        return one_list, zero_list
    
    return zero_list, one_list

def calculate_ox_gen_rate(ox_gen_list, digit_range):
    for i in range(1, digit_range):
        zero_list, one_list = split_list_between_digits_at_position(ox_gen_list, i)
        ox_gen_list, drop_co_scrub_list = determine_most_least_list(zero_list, one_list)
        if len(ox_gen_list) == 1:
            break
    ox_gen_string = convert_int_list_to_binary_string(ox_gen_list[0])
    return int(ox_gen_string, 2)


def calculate_co_scrub_rate(co_scrub_list, digit_range):
    for i in range(1, digit_range):
        zero_list, one_list = split_list_between_digits_at_position(co_scrub_list, i)
        drop_ox_gen_list, co_scrub_list = determine_most_least_list(zero_list, one_list)
        if len(co_scrub_list) == 1:
            break
    co_scrub_string = convert_int_list_to_binary_string(co_scrub_list[0])
    return int(co_scrub_string, 2)

print(runner('one'))
print(runner('two'))

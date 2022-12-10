"""https://adventofcode.com/2022/day/10"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-10.txt')
    x_values = calculcate_x_values(lines)
    key_signal_strengths = calculate_key_signal_strengths(x_values)
    print(key_signal_strengths)
    return int(sum(key_signal_strengths))

def calculate_key_signal_strengths(x_values):
    key_signal_strengths = []
    for index in range(20, 221, 40):
        signal_strength = index * x_values[index]
        key_signal_strengths.append(signal_strength)
    return key_signal_strengths

def calculcate_x_values(lines):
    # '0' as placeholder for 0th slot
    # '1' b/c X = 1 in first cycle
    x_values = [0,1]

    for untrimmed_line in lines:
        line = untrimmed_line.replace('\n', '')
        if line == 'noop':
            current_X = x_values[-1]
            x_values.append(current_X)
        else:
            V = float(line.split(' ')[1])
            current_X = x_values[-1]
            x_values.append(current_X)
            x_values.append(current_X + V)
    return x_values

print(part_one())
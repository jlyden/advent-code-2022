"""https://adventofcode.com/2022/day/10"""

from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-10.txt')
    x_values = calculcate_x_values(lines)

    if part == 'one':
        key_signal_strengths = calculate_key_signal_strengths(x_values)
        return sum(key_signal_strengths)

    draw_crt_rows(x_values)
    return

# TODO: start with solution that works, then optimize to avoid double looping
def draw_crt_rows(x_values):
    crt_rows = []
    crt_row = []
    crt_pos = 0
    len_x_vals = len(x_values)

    for index in range(1, len_x_vals):
        X = x_values[index]
        sprite_range = [X-1, X, X+1]
        if crt_pos in sprite_range:
            crt_row.append('#')
        else:
            crt_row.append('.')
        
        crt_pos += 1

        # end of crt row
        if crt_pos == 40:
            crt_line = ''.join(crt_row)
            print(crt_line)
            crt_rows.append(crt_line)
            crt_row = []
            crt_pos = 0

    return crt_rows

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
            x_values.append(int(current_X + V))
    return x_values

print(runner('one'))
print(runner('two'))
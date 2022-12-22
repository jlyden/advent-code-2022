"""https://adventofcode.com/2022/day/21"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-21.txt')
    simple_vars, operations = process_lines(lines)
    operations = substitute_simple_vars(simple_vars, operations)
    return process_operations(operations)

def process_lines(lines):
    simple_vars = {}
    operations = {}

    for untrimmed_line in lines:
        line = untrimmed_line.replace('\n', '')
        line_parts = line.split(' ')
        if len(line_parts) == 2:
            [key, value] = line_parts
            simple_vars[key[0:-1]] = int(value)
        elif len(line_parts) == 4:
            key = line_parts[0][0:-1]
            operations[key] = line_parts[1:]
        else:
            raise Exception('Unexpected line_parts: ' + str(line_parts))
    return simple_vars, operations

# brute forcing it; the loops aren't awesome
# well, even the brute force approach took < 2 secs
def substitute_simple_vars(simple_vars, operations):
    for var_key, var_value in simple_vars.items():
        for op_key, op_value in operations.items():
            if var_key in op_value:
                updated_op_value = [var_value if elem == var_key else elem for elem in op_value]
                operations[op_key] = updated_op_value
    return operations

def process_operations(operations):
    incomplete_ops = {}
    simple_vars = {}
    for op_key, op_value in operations.items():
        [val_one, _, val_two] = op_value
        if isinstance(val_one, int) and isinstance(val_two, int):
            simple_vars[op_key] = run_op(op_value)
        else:
            incomplete_ops[op_key] = op_value

    if len(simple_vars) > 0:
        updated_incomplete_ops = substitute_simple_vars(simple_vars, incomplete_ops)
    if len(incomplete_ops) > 1:
        return process_operations(updated_incomplete_ops)
    if len(incomplete_ops) == 1:
        return run_op(incomplete_ops['root'])

def run_op(operation):
    [val_one, op, val_two] = operation
    match op:
        case '+':
            return val_one + val_two
        case '-':
            return val_one - val_two
        case '*':
            return val_one * val_two
        case '/':
            return int(val_one / val_two)
        case _:
            raise Exception('Invalid operation: ' + str(operation))

print(part_one())
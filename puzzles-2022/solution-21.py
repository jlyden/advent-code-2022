"""https://adventofcode.com/2022/day/21"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')
    simple_vars, operations = process_lines(lines)
    operations = substitute_simple_vars(simple_vars, operations)
    process_result = process_operations(operations)
    if isinstance(process_result, int):
        return process_result
    raise Exception('Expected int resolution of part_one process_operations')

def process_lines(lines):
    simple_vars = {}
    operations = {}

    for untrimmed_line in lines:
        line = untrimmed_line.replace('\n', '')
        line_parts = line.split(' ')
        key = line_parts[0][0:-1]
        if len(line_parts) == 2:
            simple_vars[key] = int(line_parts[1])
        elif len(line_parts) == 4:
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
        if len(updated_incomplete_ops) > 1:
            return process_operations(updated_incomplete_ops)
        if len(updated_incomplete_ops) == 1:
            return run_op(updated_incomplete_ops['root'])
#    elif 'root' in incomplete_ops:
#        [val_one, _, val_two] = incomplete_ops['root']
#        simple_vars[val_one] = val_two
#        updated_incomplete_ops = substitute_simple_vars(simple_vars, incomplete_ops)
#        return process_operations(updated_incomplete_ops)
    else:
        return incomplete_ops

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

def part_two():
    lines = files.get_contents_of_input_file('input-mini.txt')
    simple_vars, operations = process_lines_part_two(lines)
    operations = substitute_simple_vars(simple_vars, operations)
    process_result = process_operations(operations)
    if isinstance(process_result, int):
        raise Exception('Expected non-int resolution of part_two process_operations')
    algebra_result = solve_algebraically(process_result)
    return algebra_result

def process_lines_part_two(lines):
    simple_vars = {}
    operations = {}

    for untrimmed_line in lines:
        line = untrimmed_line.replace('\n', '')
        line_parts = line.split(' ')
        key = line_parts[0][0:-1]
        if key == 'humn': 
            simple_vars[key] = key
        elif key == 'root':
            [val_one, _, val_two] = line_parts[1:]
            operations[key] = [val_one, '=', val_two]
        elif len(line_parts) == 2:
            simple_vars[key] = int(line_parts[1])
        elif len(line_parts) == 4:
            operations[key] = line_parts[1:]
        else:
            raise Exception('Unexpected line_parts: ' + str(line_parts))
    return simple_vars, operations

def solve_algebraically(operations):
    print(operations)
    return

#print(part_one())
print(part_two())

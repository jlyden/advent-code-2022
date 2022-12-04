"""https://adventofcode.com/2022/day/4"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-04.txt')
    return get_count_of_assignment_relationship(lines, 'subset')

def part_two():
    lines = files.get_contents_of_input_file('input-04.txt')
    return get_count_of_assignment_relationship(lines, 'intersection')

def get_count_of_assignment_relationship(lines, relationship):
    match relationship:
        case 'subset':
            has_relationship_callback = _includes_subset
        case 'intersection':
            has_relationship_callback = _has_intersection
        case _:
            raise Exception('Invalid relationship: ' + relationship)

    count = 0
    for line in lines:
        assignments = line.replace('\n','').split(',')
        assignment_sets = [transform_to_set(assignment) for assignment in assignments]
        count = count + 1 if has_relationship_callback(assignment_sets) else count
    return count

def transform_to_set(assignment):
    boundaries = [int(boundary) for boundary in assignment.split('-')]
    # +1 b/c range upper bound is exclusive
    return set(range(boundaries[0], (boundaries[1]+1)))

def _includes_subset(list_of_two_sets):
    set_one, set_two = list_of_two_sets
    if len(set_one) > len(set_two):
        larger_set = set_one
        smaller_set = set_two
    else:
        larger_set = set_two
        smaller_set = set_one
    return smaller_set.issubset(larger_set)

def _has_intersection(list_of_two_sets):
    set_one, set_two = list_of_two_sets
    return len(set_one.intersection(set_two)) > 0

print(part_one())
print(part_two())
"""https://adventofcode.com/2022/day/4

Alternate added after seeing others' approaches
 - Alt preferable - less overhead of data transformation
"""

from helpers import files

def part_one(alternate = False):
    lines = files.get_contents_of_input_file('input-04.txt')
    if alternate:
        return get_count_of_assignment_relationship_alt(lines, 'contains')
    else:
        return get_count_of_assignment_relationship(lines, 'contains')

def part_two():
    lines = files.get_contents_of_input_file('input-04.txt')
    return get_count_of_assignment_relationship(lines, 'overlaps')

def get_count_of_assignment_relationship(lines, relationship):
    match relationship:
        case 'contains':
            has_relationship_callback = _includes_subset
        case 'overlaps':
            has_relationship_callback = _has_intersection
        case _:
            raise Exception('Invalid relationship: ' + relationship)

    count = 0
    for line in lines:
        assignments = line.replace('\n','').split(',')
        assignment_sets = [transform_to_set(assignment) for assignment in assignments]
        count = count + 1 if has_relationship_callback(assignment_sets) else count
    return count

def get_count_of_assignment_relationship_alt(lines, relationship):
    match relationship:
        case 'contains':
            has_relationship_callback = _contains
        case 'overlaps':
            has_relationship_callback = _overlaps
        case _:
            raise Exception('Invalid relationship: ' + relationship)

    count = 0
    for line in lines:
        assignments = line.replace('\n','').split(',')
        count = count + 1 if has_relationship_callback(assignments) else count
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

def _contains(list_of_two_assignments):
    one_bottom, one_top = get_elements(list_of_two_assignments[0])
    two_bottom, two_top = get_elements(list_of_two_assignments[1])
    return _one_inside_two(one_bottom, one_top, two_bottom, two_top) or _two_inside_one(one_bottom, one_top, two_bottom, two_top)

def _overlaps(list_of_two_sets):
    return

def get_elements(assignment):
    return [int(value) for value in assignment.split('-')]

def _one_inside_two(one_bottom, one_top, two_bottom, two_top):
    return (one_bottom >= two_bottom) and (one_top <= two_top)

def _two_inside_one(one_bottom, one_top, two_bottom, two_top):
    return(one_bottom <= two_bottom) and (one_top >= two_top)

print(part_one(False))
print(part_one(True))
#print(part_two())

"""https://adventofcode.com/2022/day/4

Non-set approach added after seeing others' approaches
 - preferable - less overhead of data transformation
"""

from helpers import files

def part_one(sets = True):
    lines = files.get_contents_of_input_file('input-04.txt')
    if sets:
        return get_count_of_assignment_relationship_via_sets(lines, 'contains')
    else:
        return get_count_of_assignment_relationship(lines, _contains)

def part_two(sets = True):
    lines = files.get_contents_of_input_file('input-04.txt')
    if sets:
        return get_count_of_assignment_relationship_via_sets(lines, 'overlaps')
    else:
        return get_count_of_assignment_relationship(lines, _overlaps)

def get_count_of_assignment_relationship_via_sets(lines, relationship):
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

def get_count_of_assignment_relationship(lines, relationship_callback):
    if relationship_callback not in [_contains, _overlaps]:
        raise Exception('Invalid relationship: ' + str(relationship_callback))

    count = 0
    for line in lines:
        assignments = line.replace('\n','').split(',')
        one_bottom, one_top = get_elements(assignments[0])
        two_bottom, two_top = get_elements(assignments[1])
        count = count + 1 if relationship_callback(one_bottom, one_top, two_bottom, two_top) else count
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

def _contains(one_bottom, one_top, two_bottom, two_top):
    return _one_inside_two(one_bottom, one_top, two_bottom, two_top) or _two_inside_one(one_bottom, one_top, two_bottom, two_top)

def _overlaps(one_bottom, one_top, two_bottom, two_top):
    if one_bottom <= two_bottom:
        return two_bottom <= one_top
    else:
        return one_bottom <= two_top

def get_elements(assignment):
    return [int(value) for value in assignment.split('-')]

def _one_inside_two(one_bottom, one_top, two_bottom, two_top):
    return (one_bottom >= two_bottom) and (one_top <= two_top)

def _two_inside_one(one_bottom, one_top, two_bottom, two_top):
    return(one_bottom <= two_bottom) and (one_top >= two_top)
    
print(part_one(True))
print(part_one(False))
print(part_two(True))
print(part_two(False))

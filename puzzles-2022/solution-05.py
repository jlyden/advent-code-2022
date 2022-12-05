"""http://adventofcode.com/2022/day/5

deques are also an option, but for this quantity of data,
I stuck with a list
https://docs.python.org/2/library/collections.html#collections.deque
"""

from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')
    stacks, unprocessed_moves = process_lines(lines)
    stacks_after_moves = move_crates(stacks, unprocessed_moves)
    return get_message(stacks_after_moves)

def process_lines(lines):
    # process crates input
    crate_slices = []
    for line_count, line in enumerate(lines):
        # finished processing crate slices
        if line[1] == '1':
            break
        crate_slice = []
        stop = len(line) - 2
        for i in range(0, stop, 4):
            crate_label = line[i+1] if line[i+1] != ' ' else '*'
            crate_slice.append(crate_label)
        crate_slices.append(crate_slice)

    # flip crate_slices array to create stacks
    print(crate_slices)
    stacks = [ [] for _ in range(len(crate_slices[0])) ]
    for slice in crate_slices:
        for count, crate_label in enumerate(slice):
            if crate_label != '*':
                stacks[count].insert(0, crate_label)

    # slice crate data out of lines to get list of moves
    unprocessed_moves = lines[line_count+2:]

    return stacks, unprocessed_moves

def move_crates(stacks, unprocessed_moves):
    # loop through moves
    for sentence in unprocessed_moves:
        # tried isnumeric(), was not picking up all ints - TODO: circle back
        # parse move
        move = [int(value) for count,value in enumerate(sentence.split(' ')) if count % 2 == 1]
        count, source, target = move

        # in loop:
        for _ in range(count):
            crate = stacks[source-1].pop()
            stacks[target-1].append(crate)
    return stacks

def get_message(stacks):
    # TODO:
    return

print(part_one())
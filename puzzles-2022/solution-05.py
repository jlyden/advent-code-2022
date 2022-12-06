"""http://adventofcode.com/2022/day/5

deques are also an option, but for this quantity of data,
I stuck with a list
https://docs.python.org/2/library/collections.html#collections.deque
"""

from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-05.txt')
    stacks, unprocessed_moves = process_lines(lines)
    if part == 'one':
        stacks_after_moves = move_crates_singly(stacks, unprocessed_moves)
    elif part == 'two':
        stacks_after_moves = move_crates_stacked(stacks, unprocessed_moves)
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
    stacks = [ [] for _ in range(len(crate_slices[0])) ]
    for slice in crate_slices:
        for count, crate_label in enumerate(slice):
            if crate_label != '*':
                stacks[count].insert(0, crate_label)

    # slice crate data out of lines to get list of moves
    unprocessed_moves = lines[line_count+2:]

    return stacks, unprocessed_moves

"""crates move from stack one-at-a-time, so their order is reversed"""
def move_crates_singly(stacks, unprocessed_moves):
    for sentence in unprocessed_moves:
        count, source, target = parse_move_sentence(sentence)
        for _ in range(count):
            crate = stacks[source-1].pop()
            stacks[target-1].append(crate)
    return stacks

"""multiple crates move from stack as a mini-stack, order preserved"""
def move_crates_stacked(stacks, unprocessed_moves):
    for sentence in unprocessed_moves:
        count, source, target = parse_move_sentence(sentence)
        len_source = len(stacks[source-1])
        crates = stacks[source-1][len_source-count:]
        stacks[source-1] = stacks[source-1][0:len_source-count]
        stacks[target-1] = stacks[target-1] + crates
    return stacks

def parse_move_sentence(sentence):
    # tried isnumeric(), was not picking up all ints - TODO: circle back
    move = [int(value) for count,value in enumerate(sentence.split(' ')) if count % 2 == 1]
    count, source, target = move
    return count, source, target

def get_message(stacks):
    return ''.join([stack[-1] for stack in stacks])

print(runner('one'))
print(runner('two'))
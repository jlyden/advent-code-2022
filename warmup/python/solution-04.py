"""https://adventofcode.com/2021/day/4"""

import pathlib
import re

def part_one():
    input_file = pathlib.Path(__file__).parent.absolute() / 'input-mini.txt'
    with open(input_file) as file:
        contents = file.readlines()

    # store numbers to be called
    callables = contents.pop(0).replace('\n','').split(',')
    
    # store boards
    boards = prepare_boards(contents)

    # find first winning board

    # calculcate score
    return

def prepare_boards(raw_contents):
    boards = []
    expected_board_count = int(len(raw_contents)/6)
    for i in range(0,expected_board_count):
        # first row will be blank
        blank_row = raw_contents.pop(0)
        if (blank_row != '\n'):
            raise Exception('Expecting blank row, got ' + blank_row)

        this_board = []
        # next 5 rows will be board
        for i in range(0,5):
            row = re.split('\s+', raw_contents.pop(0).replace('\n',''))
            this_board.append(row)
        
        boards.append(this_board)
    print(boards)
    return

print(part_one())
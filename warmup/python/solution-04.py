"""https://adventofcode.com/2021/day/4"""

import re
from helpers import files

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')

    # store numbers to be called
    callables = lines.pop(0).replace('\n','').split(',')
    print(callables)

    # setup bingo records
    bingo_records = prepare_bingo_records(lines)

    # find first winning board

    # calculcate score
    return

def prepare_bingo_records(lines):
    bingo_records = []
    expected_record_count = int(len(lines)/6)
    for i in range(expected_record_count):
        # first row will be blank
        blank_row = lines.pop(0)
        if (blank_row != '\n'):
            raise Exception('Expecting blank row, got ' + blank_row)

        this_board = []
        # next 5 rows will be board
        for i in range(5):
            row = re.split('\s+', lines.pop(0).replace('\n',''))
            this_board.append(row)
        bingo_records.append(BingoRecord(this_board))

    return bingo_records


"""Class representing a BingoRecord

board: two-dimensional array
board_sorted: sorted flat list of values on board
marks: count of numbers on board that have been marked X

"""
class BingoRecord:
    MARK = 'X'

    def __init__(self, board):
        self.board = board
        self.board_sorted = self.generate_sorted_board()
        self.marks = 0

    def __str__(self):
        return 'BingoRecord: marks: ' + str(self.marks) + ' | board: ' + str(self.board)

    def generate_sorted_board(self):
        return [item for row in self.board for item in row].sort()

    def is_number_on_board(self, number):
        return number in self.board_sorted

    def mark_board(self, number):
        x,y = self.get_index_for_number(self, number)
        self.board[x,y] = self.MARK
        self.marks += 1

    def get_index_for_number(self, number):
        for i, e in enumerate(self.board):
            return i, e.index(number)


print(part_one())
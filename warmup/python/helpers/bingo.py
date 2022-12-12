"""Class representing a BingoRecord

see: https://adventofcode.com/2021/day/4

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
        return sum(self.board, []).sort()

    def is_number_on_board(self, number):
        return number in self.board_sorted

    def mark_board(self, number):
        x,y = self.get_index_for_number(self, number)
        self.board[x][y] = self.MARK
        self.marks += 1

    def get_index_for_number(self, number):
        for i, e in enumerate(self.board):
            return i, e.index(number)

    def get_marks_count(self):
        return self.marks
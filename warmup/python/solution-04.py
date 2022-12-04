"""https://adventofcode.com/2021/day/4"""

from helpers import files
from helpers import bingo

def part_one():
    lines = files.get_contents_of_input_file('input-mini.txt')
    callables = lines.pop(0).replace('\n','').split(',')
    bingo_records = prepare_bingo_records(lines)

    for number_called in callables:
        winning_board = check_boards(bingo_records, number_called)
        if winning_board:
            break
    
    return calculate_score(winning_board, number_called)

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
            row = lines.pop(0).replace('\n', '').split()
            this_board.append(row)
        bingo_records.append(bingo.BingoRecord(this_board))

    return bingo_records

def check_boards(bingo_records, number_called):
    print(number_called)
    for record in bingo_records:
        print(record)
        if record.is_number_on_board(number_called):
            record.mark_board(number_called)
            print(record)
            if record.get_marks_count() > 4:
                #TODO
                return True
    return False


print(part_one())
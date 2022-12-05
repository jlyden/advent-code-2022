import unittest
import bingo

class BingoRecordTest(unittest.TestCase):
    test_board = [['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']]
    bingo_record = bingo.BingoRecord(test_board)

    def test_0_check_initial_board(self):
        self.assertEqual(self.test_board, self.bingo_record.board)

    def test_1_check_sorted_board(self):
        return

    def test_2_check_initial_marks(self):
        self.assertEqual(0, self.bingo_record.marks)

    def test_3_test_generate_sorted_board(self):
        return

if __name__ == '__main__':
    unittest.main()
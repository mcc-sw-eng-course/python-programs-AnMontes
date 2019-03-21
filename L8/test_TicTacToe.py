import unittest
import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_print_board(self):
        obj = TicTacToe.Board()
        obj.print_board()
        self.assertEqual(obj.string_to_print,"")

    def test_mark_set_valid_position(self):
        obj = TicTacToe.Board()
        obj.set_mark(15)
        self.assertEqual(obj.valid_position,1)
        obj.set_mark(5)
        self.assertEqual(obj.valid_position,0)
    def test_mark_set_occupied(self):
        obj = TicTacToe.Board()
        obj.set_mark(5)
        obj.set_mark(5)
        self.assertEqual(obj.unocuppied,1)
        obj.set_mark(4)
        self.assertEqual(obj.unocuppied,0)

    def test_someone_won(self):
        obj = TicTacToe.Board()
        obj.set_mark(1)
        obj.set_mark(2)
        obj.set_mark(3)
        self.assertEqual(obj.o_won or obj.x_won, 1)
        obj.reset_game()
        self.assertEqual(obj.x_won or obj.o_won,0)

if __name__ == '__main__':
    unittest.main()

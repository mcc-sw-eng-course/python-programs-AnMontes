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

    def test_check_solution_reached(self):
        obj = TicTacToe.Board()
        obj.machine_turn_manual(1)
        obj.machine_turn_manual(2)
        obj.machine_turn_manual(3)
        self.assertEqual(obj.x_won,1)
        obj.reset_game()
        obj.machine_turn_manual(1)
        obj.machine_turn_manual(4)
        obj.machine_turn_manual(7)
        self.assertEqual(obj.x_won,1)
        obj.reset_game()
        obj.machine_turn_manual(4)
        obj.machine_turn_manual(5)
        obj.machine_turn_manual(6)
        self.assertEqual(obj.x_won,1)
        obj.reset_game()
        obj.machine_turn_manual(7)
        obj.machine_turn_manual(8)
        obj.machine_turn_manual(9)
        self.assertEqual(obj.x_won,1)
        obj.reset_game()
        obj.machine_turn_manual(2)
        obj.machine_turn_manual(5)
        obj.machine_turn_manual(8)
        self.assertEqual(obj.x_won,1)
        obj.reset_game()
        obj.machine_turn_manual(3)
        obj.machine_turn_manual(6)
        obj.machine_turn_manual(9)
        self.assertEqual(obj.x_won,1)
        obj.reset_game()
        obj.machine_turn_manual(3)
        obj.machine_turn_manual(5)
        obj.machine_turn_manual(7)
        self.assertEqual(obj.x_won,1)
        obj.machine_turn_manual(1)
        obj.machine_turn_manual(5)
        obj.machine_turn_manual(9)
        self.assertEqual(obj.x_won,1)

    def test_o_won(self):
        obj = TicTacToe.Board()
        obj.set_mark(1)
        obj.set_mark(2)
        obj.set_mark(3)
        self.assertEqual(obj.o_won,1)

    def test_tie(self):
        obj = TicTacToe.Board()
        obj.set_mark(1)
        obj.machine_turn_manual(2)
        obj.set_mark(3)
        obj.machine_turn_manual(5)
        obj.set_mark(4)
        obj.machine_turn_manual(7)
        obj.set_mark(6)
        obj.machine_turn_manual(9)
        obj.set_mark(8)
        self.assertEqual(obj.tie,1)

    def test_game(self):
        obj=TicTacToe.Board()
        self.assertEqual(obj.start_game(), None)
if __name__ == '__main__':
    unittest.main()

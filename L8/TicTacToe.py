

class Board:
    def __init__(self):
        self.board = [" ", "|", " ", "|", " ",
                      "-", "-", "-", "-", "-",
                      " ", "|", " ", "|", " ",
                      "-", "-", "-", "-", "-",
                      " ", "|", " ", "|", " "]
        self.available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.string_to_print = ""
        self.writable_slots = {1: 0,
                               2: 2,
                               3: 4,
                               4: 10,
                               5: 12,
                               6: 14,
                               7: 20,
                               8: 22,
                               9: 24
                               }

        # 0 for human turn and 1 for machine.
        # Determines if program should type an X or O
        self.player_mark = 0

    def print_board(self):
        for i in range(len(self.board)):
            if i % 5 == 0:
                self.string_to_print += "\n"
            self.string_to_print += self.board[i]
        print(self.string_to_print)
        self.string_to_print = ""

    def set_mark(self, pos):
        if 1 <= pos <= 9:
            if pos in self.available_spaces:
                for i in range(len(self.available_spaces)):
                    if self.available_spaces[i] == pos:
                        self.available_spaces.pop(i)
                        break
                if self.player_mark == 0:
                    self.board[self.writable_slots[pos]] = "X"
                    self.player_mark = 1
                    self.print_board()
                else:
                    self.board[self.writable_slots[pos]] = "O"
                    self.player_mark = 0
                    self.print_board()
            else:
                print("Please choose an unoccupied slot.")
        else:
            print("Please choose a valid position, i.e. from 1 to 9.")


game1 = Board()
game1.print_board()
game1.set_mark(1)
game1.set_mark(2)
game1.set_mark(8)
game1.set_mark(4)
game1.set_mark(5)
game1.set_mark(6)
game1.set_mark(7)
game1.set_mark(3)
game1.set_mark(9)

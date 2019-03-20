

class Board:
    def __init__(self):
        self.board = [" ", "|", " ", "|", " ",
                      "-", "-", "-", "-", "-",
                      " ", "|", " ", "|", " ",
                      "-", "-", "-", "-", "-",
                      " ", "|", " ", "|", " "]
        self.available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.string_to_print = ""

    def print_board(self):
        for i in range(len(self.board)):
            if i % 5 == 0:
                self.string_to_print += "\n"
            self.string_to_print += self.board[i]
        print(self.string_to_print)
        self.string_to_print = ""


game1 = Board()
game1.print_board()


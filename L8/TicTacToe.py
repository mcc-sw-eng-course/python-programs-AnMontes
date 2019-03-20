import random


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

        self.mark_memory = {1: (0, 0),
                            2: (1, 0),
                            3: (2, 0),
                            4: (0, 1),
                            5: (1, 1),
                            6: (1, 2),
                            7: (2, 0),
                            8: (2, 1),
                            9: (2, 2)
                            }
        self.x_marks = []
        self.o_marks = []

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

                self.board[self.writable_slots[pos]] = "O"
                self.o_marks.append(self.mark_memory[pos])
                print(self.o_marks)
                self.print_board()
                self.machine_turn()
            else:
                print("Please choose an unoccupied slot.")
        else:
            print("Please choose a valid position, i.e. from 1 to 9.")

    # Randomly decide where to place a mark.
    def machine_turn(self):
        pos = random.choice(self.available_spaces)
        for i in range(len(self.available_spaces)):
            if self.available_spaces[i] == pos:
                self.available_spaces.pop(i)
                break
        self.x_marks.append(self.mark_memory[pos])
        print(self.x_marks)
        self.board[self.writable_slots[pos]] = "X"
        self.print_board()

    def check_solution_reached(self):
        pass


game1 = Board()
game1.print_board()
game1.set_mark(1)
game1.set_mark(2)
game1.set_mark(3)

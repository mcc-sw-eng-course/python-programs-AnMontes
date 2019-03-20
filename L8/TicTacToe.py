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
                # print(self.o_marks)
                self.print_board()
                if self.check_solution_reached(self.o_marks):
                    print("O won the game!")
                    self.reset_game()
                else:
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

        self.board[self.writable_slots[pos]] = "X"
        self.x_marks.append(self.mark_memory[pos])
        # print(self.x_marks)
        self.print_board()
        if self.check_solution_reached(self.x_marks):
            print("X won the game!")
            self.reset_game()

    @staticmethod
    def check_solution_reached(mark_memory):
        if len(mark_memory) >= 3:
            if (0, 0) in mark_memory and (1, 1) in mark_memory and (2, 2) in mark_memory:
                return 1
            elif (0, 2) in mark_memory and (1, 1) in mark_memory and (2, 0) in mark_memory:
                return 1
            elif (0, 0) in mark_memory and (1, 0) in mark_memory and (2, 0) in mark_memory:
                return 1
            elif (0, 1) in mark_memory and (1, 1) in mark_memory and (2, 1) in mark_memory:
                return 1
            elif (0, 2) in mark_memory and (1, 2) in mark_memory and (2, 2) in mark_memory:
                return 1
            elif (0, 0) in mark_memory and (0, 1) in mark_memory and (0, 2) in mark_memory:
                return 1
            elif (1, 0) in mark_memory and (1, 1) in mark_memory and (1, 2) in mark_memory:
                return 1
            elif (2, 0) in mark_memory and (2, 1) in mark_memory and (2, 2) in mark_memory:
                return 1
            else:
                return 0
        else:
            return 0

    def reset_game(self):
        print("Resetting game...")
        self.board = [" ", "|", " ", "|", " ",
                      "-", "-", "-", "-", "-",
                      " ", "|", " ", "|", " ",
                      "-", "-", "-", "-", "-",
                      " ", "|", " ", "|", " "]
        self.available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.x_marks = []
        self.o_marks = []
        self.print_board()


game1 = Board()
game1.print_board()
game1.set_mark(1)
game1.set_mark(5)
game1.set_mark(9)

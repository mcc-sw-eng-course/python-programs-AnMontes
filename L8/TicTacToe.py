import random
import socket
import pickle



HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

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
                            3: (0, 2),
                            4: (0, 1),
                            5: (1, 1),
                            6: (1, 2),
                            7: (2, 0),
                            8: (2, 1),
                            9: (2, 2)
                            }
        self.x_marks = []
        self.o_marks = []
        self.unocuppied = 0
        self.valid_position = 0
        self.o_won= 0
        self.x_won = 0
        self.tie = 0
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
                self.unocuppied = 0
                self.valid_position = 0
                self.board[self.writable_slots[pos]] = "O"
                self.o_marks.append(self.mark_memory[pos])
                # print(self.o_marks)
                self.print_board()
                if self.check_solution_reached(self.o_marks):
                    print("O won the game!")
                    self.o_won = 1
                    #self.reset_game()
                elif len(self.available_spaces) == 0:
                    print("Tie!")
                    self.tie= 1
            else:
                self.unocuppied = 1
                print("Please choose an unoccupied slot.")
        else:
            self.valid_position = 1
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
            self.x_won = 1
            # self.reset_game()
        elif len(self.available_spaces) == 0:
            print("Tie!")
            self.tie=1

        self.board[self.writable_slots[pos]] = "X"
        self.x_marks.append(self.mark_memory[pos])
        # print(self.x_marks)
        self.print_board()
        if self.check_solution_reached(self.x_marks):
            print("X won the game!")
            self.x_won = 1
            #self.reset_game()
        elif len(self.available_spaces) == 0:
            print("Tie!")
            self.tie=1

    def machine_turn_manual(self,pos):
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
            self.x_won = 1
            # self.reset_game()
        elif len(self.available_spaces) == 0:
            print("Tie!")
            self.tie=1

        self.board[self.writable_slots[pos]] = "X"
        self.x_marks.append(self.mark_memory[pos])
        # print(self.x_marks)
        self.print_board()
        if self.check_solution_reached(self.x_marks):
            print("X won the game!")
            self.x_won = 1
            #self.reset_game()
        elif len(self.available_spaces) == 0:
            print("Tie!")
            self.tie=1
    @staticmethod
    def check_solution_reached(mark_memory):
        if len(mark_memory) >= 3:
            if (0, 0) in mark_memory and (1, 1) in mark_memory and (2, 2) in mark_memory:
                return 1
            elif (0, 2) in mark_memory and (1, 1) in mark_memory and (2, 0) in mark_memory:
                return 1
            elif (0, 0) in mark_memory and (1, 0) in mark_memory and (0, 2) in mark_memory:
                return 1
            elif (0, 1) in mark_memory and (1, 1) in mark_memory and (1, 2) in mark_memory:
                return 1
            elif (0, 2) in mark_memory and (1, 2) in mark_memory and (2, 2) in mark_memory:
                return 1
            elif (0, 0) in mark_memory and (0, 1) in mark_memory and (2, 0) in mark_memory:
                return 1
            elif (1, 0) in mark_memory and (1, 1) in mark_memory and (2, 1) in mark_memory:
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
        self.o_won = 0
        self.x_won = 0
        self.tie=0

    def start_game(self):
        a = True
        jugador1=1
        jugador2=0
        modo_de_juego = int(input("Choose 1 for PVP or 2 for PVE:"))
        if(modo_de_juego==2):
            self.print_board()
            while self.check_solution_reached(self.o_marks) == 0 and self.check_solution_reached(self.x_marks) ==0 and self.tie==0:
                mark = int(input("Introduzca la posición:"))
                self.set_mark(mark)
                if(self.check_solution_reached(self.o_marks) == 0 and self.check_solution_reached(self.x_marks) ==0):
                    self.machine_turn()
            decision = input("Desea continuar? Y o N")
            if(decision == "N"):
                return None
            else:
                self.reset_game()
                self.start_game()
        if(modo_de_juego==1):
            self.print_board()
            while self.check_solution_reached(self.o_marks) == 0 and self.check_solution_reached(self.x_marks) ==0 and self.tie==0:
                if(jugador1==1):
                    mark = int(input("Introduzca la posición:"))
                    self.set_mark(mark)
                    jugador1=0
                    jugador2=1
                    a = True
                if(jugador2==1):
                    if(self.check_solution_reached(self.o_marks) == 0 and self.check_solution_reached(self.x_marks) ==0):
                        while a == True:
                            full_msg = b""
                            new_msg = True
                            while a == True:
                                msg = s.recv(16)
                                if new_msg:
                                    msglen = int(msg[:HEADERSIZE])
                                    new_msg = False

                                full_msg += msg
                                if len(full_msg) - HEADERSIZE == msglen:
                                    #print(full_msg[HEADERSIZE:])

                                    d = pickle.loads(full_msg[HEADERSIZE:])
                                    print(d)

                                    new_msg = True
                                    full_msg = b''
                                    a = False
                        self.machine_turn_manual(d)
                        jugador1=1
                        jugador2=0
            decision = input("Desea continuar? Y o N")
            if (decision == "N"):
                return None
            else:
                self.reset_game()
                self.start_game()
game1 = Board()
game1.start_game()
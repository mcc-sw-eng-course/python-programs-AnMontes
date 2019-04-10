import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.grep_checker = "|"
        self.line_checker = "-"
        self.empty_btn = " "
        self.curr_selected_btn_coord = [0, 0]
        self.toggle_selection = False
        self.store_checker = ""
        self.line_score = 0
        self.grep_score = 0

        self.init_ui()
    
    def init_ui(self):
        self.l_empty_space = QtWidgets.QLabel("            ")

        self.b1_1 = QtWidgets.QPushButton(self.grep_checker)
        self.b1_2 = QtWidgets.QPushButton(self.grep_checker)
        self.b1_3 = QtWidgets.QPushButton(self.grep_checker)
        self.b1_4 = QtWidgets.QPushButton(self.grep_checker)

        self.b2_1 = QtWidgets.QPushButton(self.grep_checker)
        self.b2_2 = QtWidgets.QPushButton(self.grep_checker)
        self.b2_3 = QtWidgets.QPushButton(self.grep_checker)
        self.b2_4 = QtWidgets.QPushButton(self.grep_checker)

        self.b3_1 = QtWidgets.QPushButton(self.grep_checker)
        self.b3_2 = QtWidgets.QPushButton(self.grep_checker)
        self.b3_3 = QtWidgets.QPushButton(self.grep_checker)
        self.b3_4 = QtWidgets.QPushButton(self.grep_checker)

        self.b4_1 = QtWidgets.QPushButton(self.empty_btn)
        self.b4_2 = QtWidgets.QPushButton(self.empty_btn)
        self.b4_3 = QtWidgets.QPushButton(self.empty_btn)
        self.b4_4 = QtWidgets.QPushButton(self.empty_btn)

        self.b5_1 = QtWidgets.QPushButton(self.empty_btn)
        self.b5_2 = QtWidgets.QPushButton(self.empty_btn)
        self.b5_3 = QtWidgets.QPushButton(self.empty_btn)
        self.b5_4 = QtWidgets.QPushButton(self.empty_btn)

        self.b6_1 = QtWidgets.QPushButton(self.line_checker)
        self.b6_2 = QtWidgets.QPushButton(self.line_checker)
        self.b6_3 = QtWidgets.QPushButton(self.line_checker)
        self.b6_4 = QtWidgets.QPushButton(self.line_checker)

        self.b7_1 = QtWidgets.QPushButton(self.line_checker)
        self.b7_2 = QtWidgets.QPushButton(self.line_checker)
        self.b7_3 = QtWidgets.QPushButton(self.line_checker)
        self.b7_4 = QtWidgets.QPushButton(self.line_checker)

        self.b8_1 = QtWidgets.QPushButton(self.line_checker)
        self.b8_2 = QtWidgets.QPushButton(self.line_checker)
        self.b8_3 = QtWidgets.QPushButton(self.line_checker)
        self.b8_4 = QtWidgets.QPushButton(self.line_checker)

        self.l_prompt_message = QtWidgets.QLabel("Game running normal")

        h_tile8 = QtWidgets.QHBoxLayout()
        h_tile8.addWidget(self.l_empty_space)
        h_tile8.addWidget(self.b8_1)
        h_tile8.addWidget(self.l_empty_space)
        h_tile8.addWidget(self.b8_2)
        h_tile8.addWidget(self.l_empty_space)
        h_tile8.addWidget(self.b8_3)
        h_tile8.addWidget(self.l_empty_space)
        h_tile8.addWidget(self.b8_4)

        h_tile7 = QtWidgets.QHBoxLayout()
        h_tile7.addWidget(self.b7_1)
        h_tile7.addWidget(self.l_empty_space)
        h_tile7.addWidget(self.b7_2)
        h_tile7.addWidget(self.l_empty_space)
        h_tile7.addWidget(self.b7_3)
        h_tile7.addWidget(self.l_empty_space)
        h_tile7.addWidget(self.b7_4)
        h_tile7.addWidget(self.l_empty_space)

        
        h_tile6 = QtWidgets.QHBoxLayout()
        h_tile6.addWidget(self.l_empty_space)
        h_tile6.addWidget(self.b6_1)
        h_tile6.addWidget(self.l_empty_space)
        h_tile6.addWidget(self.b6_2)
        h_tile6.addWidget(self.l_empty_space)
        h_tile6.addWidget(self.b6_3)
        h_tile6.addWidget(self.l_empty_space)
        h_tile6.addWidget(self.b6_4)

        h_tile5 = QtWidgets.QHBoxLayout()
        h_tile5.addWidget(self.b5_1)
        h_tile5.addWidget(self.l_empty_space)
        h_tile5.addWidget(self.b5_2)
        h_tile5.addWidget(self.l_empty_space)
        h_tile5.addWidget(self.b5_3)
        h_tile5.addWidget(self.l_empty_space)
        h_tile5.addWidget(self.b5_4)
        h_tile5.addWidget(self.l_empty_space)

        h_tile4 = QtWidgets.QHBoxLayout()
        h_tile4.addWidget(self.l_empty_space)
        h_tile4.addWidget(self.b4_1)
        h_tile4.addWidget(self.l_empty_space)
        h_tile4.addWidget(self.b4_2)
        h_tile4.addWidget(self.l_empty_space)
        h_tile4.addWidget(self.b4_3)
        h_tile4.addWidget(self.l_empty_space)
        h_tile4.addWidget(self.b4_4)

        h_tile3 = QtWidgets.QHBoxLayout()
        h_tile3.addWidget(self.b3_1)
        h_tile3.addWidget(self.l_empty_space)
        h_tile3.addWidget(self.b3_2)
        h_tile3.addWidget(self.l_empty_space)
        h_tile3.addWidget(self.b3_3)
        h_tile3.addWidget(self.l_empty_space)
        h_tile3.addWidget(self.b3_4)
        h_tile3.addWidget(self.l_empty_space)

        h_tile2 = QtWidgets.QHBoxLayout()
        h_tile2.addWidget(self.l_empty_space)
        h_tile2.addWidget(self.b2_1)
        h_tile2.addWidget(self.l_empty_space)
        h_tile2.addWidget(self.b2_2)
        h_tile2.addWidget(self.l_empty_space)
        h_tile2.addWidget(self.b2_3)
        h_tile2.addWidget(self.l_empty_space)
        h_tile2.addWidget(self.b2_4)

        h_tile1 = QtWidgets.QHBoxLayout()
        h_tile1.addWidget(self.b1_1)
        h_tile1.addWidget(self.l_empty_space)
        h_tile1.addWidget(self.b1_2)
        h_tile1.addWidget(self.l_empty_space)
        h_tile1.addWidget(self.b1_3)
        h_tile1.addWidget(self.l_empty_space)
        h_tile1.addWidget(self.b1_4)
        h_tile1.addWidget(self.l_empty_space)

        h_tile0 = QtWidgets.QHBoxLayout()
        h_tile0.addStretch()
        h_tile0.addWidget(self.l_prompt_message)
        h_tile0.addStretch()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_tile8)
        v_box.addLayout(h_tile7)
        v_box.addLayout(h_tile6)
        v_box.addLayout(h_tile5)
        v_box.addLayout(h_tile4)
        v_box.addLayout(h_tile3)
        v_box.addLayout(h_tile2)
        v_box.addLayout(h_tile1)
        v_box.addLayout(h_tile0)

        self.setLayout(v_box)
        self.setWindowTitle("Checkers")

        # Do whatever is inside the connect.
        self.b1_1.clicked.connect(self.btn_selected1_1)
        self.b3_1.clicked.connect(self.btn_selected3_1)
        self.b3_2.clicked.connect(self.btn_selected3_2)
        self.b4_1.clicked.connect(self.btn_selected4_1)

        self.b5_2.clicked.connect(self.btn_selected5_2)

        self.b6_1.clicked.connect(self.btn_selected6_1)
        self.b6_2.clicked.connect(self.btn_selected6_2)
        self.show()

    def btn_selected1_1(self):
        if self.toggle_selection:
            self.b1_1.setStyleSheet("")
            self.b1_1.setText(self.empty_btn)
            self.curr_selected_btn_coord[0] = 0
            self.curr_selected_btn_coord[1] = 0
        else:
            self.b1_1.setStyleSheet("background-color: rgb(255,0,0)")
            self.curr_selected_btn_coord[0] = 1
            self.curr_selected_btn_coord[1] = 1

        self.toggle_selection = not self.toggle_selection
        # self.b1_1.setStyleSheet("")

    def btn_selected3_1(self):      # Fully implemented.
        if self.toggle_selection:
            # Allow to be move to if this btn is empty.
            if self.b3_1.text() == self.empty_btn:
                if self.store_checker == self.grep_checker:     # If a grep was selected.
                    if self.curr_selected_btn_coord[0] == 2 and self.curr_selected_btn_coord[1] == 1:
                        self.b3_1.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 1 and self.curr_selected_btn_coord[1] == 2 \
                        and self.b2_1.text() == self.line_checker:
                        self.b3_1.setText(self.store_checker)
                        self.b2_1.setText(self.empty_btn)   # Limpiar el checker que se comio.
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    else:
                        self.l_prompt_message.setText("Checker progresssion is incorrect.")
                        self.reset_btns_state()
                elif self.store_checker == self.line_checker:   # If a line was selected.
                    if self.curr_selected_btn_coord[0] == 4 and self.curr_selected_btn_coord[1] == 1:
                        self.b3_1.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    # CHECAR SI VA A COMER.
                    elif self.curr_selected_btn_coord[0] == 5 and self.curr_selected_btn_coord[1] == 2 \
                        and self.b4_1.text() == self.grep_checker:
                        self.b3_1.setText(self.store_checker)
                        self.b4_1.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1
                    else:
                        self.l_prompt_message.setText("Checker progresssion is incorrect.")
                        self.reset_btns_state()
            else:
                self.l_prompt_message.setText("This button isn't empty")
                self.reset_btns_state()
        else:
            if not self.b3_1.text() == self.empty_btn:
                self.l_prompt_message.setText("Game running normal")
                self.b3_1.setStyleSheet("background-color: rgb(255,0,0)")
                self.curr_selected_btn_coord[0] = 3
                self.curr_selected_btn_coord[1] = 1
                self.store_checker = self.b3_1.text()
                self.toggle_selection = not self.toggle_selection
            else:
                self.l_prompt_message.setText("Select a button that has a checker")
                self.reset_btns_state()

    def btn_selected3_2(self):      # Fully implemented.
        if self.toggle_selection:   # If a btn has been previously pressed.
            # Allow to be move to if this btn is empty.
            if self.b3_2.text() == self.empty_btn:
                if self.store_checker == self.grep_checker:     # If a grep was selected.
                    if self.curr_selected_btn_coord[0] == 2 and \
                            (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for forward movement...
                        self.b3_2.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    # CHECAR SI VA A COMER
                    elif self.curr_selected_btn_coord[0] == 1 and self.curr_selected_btn_coord[1] == 1 \
                            and self.b2_1.text() == self.line_checker:
                        self.b3_2.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b2_1.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    elif self.curr_selected_btn_coord[0] == 1 and self.curr_selected_btn_coord[1] == 3 \
                            and self.b2_2.text() == self.line_checker:
                        self.b3_2.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b2_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
                elif self.store_checker == self.line_checker:   # If a line was selected.
                    if self.curr_selected_btn_coord[0] == 4 \
                            and (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for backward movement...
                        self.b3_2.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 4 and self.curr_selected_btn_coord[1] == 1 \
                            and self.b5_1.text() == self.grep_checker:
                        self.b5_2.setText(self.store_checker)
                        self.b4_1.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1

                    elif self.curr_selected_btn_coord[0] == 4 and self.curr_selected_btn_coord[1] == 3 \
                            and self.b5_2.text() == self.grep_checker:
                        self.b5_2.setText(self.store_checker)
                        self.b4_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
            else:
                self.l_prompt_message.setText("This button isn't empty")
                self.reset_btns_state()
        else:
            # If the btn initially selected is empty.
            if not self.b3_2.text() == self.empty_btn:
                self.l_prompt_message.setText("Game running normal")
                self.b3_2.setStyleSheet("background-color: rgb(255,0,0)")
                self.store_checker = self.b3_2.text()
                self.curr_selected_btn_coord[0] = 3
                self.curr_selected_btn_coord[1] = 2
                self.toggle_selection = not self.toggle_selection
            else:
                self.l_prompt_message.setText(
                    "Select a button that has a checker")
                self.reset_btns_state()

    def btn_selected4_1(self):      # Fully implemented.
        if self.toggle_selection:   # If a btn has been previously pressed.
            if self.b4_1.text() == self.empty_btn:  # Allow to be move to if this btn is empty.
                if self.store_checker == self.grep_checker:     # If a grep was selected.
                    if self.curr_selected_btn_coord[0] == 3 and \
                            (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for forward movement...
                        self.b4_1.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 1 and self.curr_selected_btn_coord[1] == 2 \
                            and self.b2_1.text() == self.line_checker:
                        self.b4_1.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b3_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    else:
                        self.l_prompt_message.setText("Checker progresssion is incorrect.")
                        self.reset_btns_state()
                elif self.store_checker == self.line_checker:   # If a line was selected.
                    if self.curr_selected_btn_coord[0] == 5 \
                        and (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for backward movement...
                        self.b4_1.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    # CHECAR SI VA A COMER.
                    elif self.curr_selected_btn_coord[0] == 6 and self.curr_selected_btn_coord[1] == 2 \
                            and self.b5_2.text() == self.grep_checker:
                        self.b4_1.setText(self.store_checker)
                        self.b5_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1
                    else:
                        self.l_prompt_message.setText("Checker progresssion is incorrect.")
                        self.reset_btns_state()
            else:
                self.l_prompt_message.setText("This button isn't empty")
                self.reset_btns_state()
        else:
            if not self.b4_1.text() == self.empty_btn:      # If the btn initially selected is empty.
                self.l_prompt_message.setText("Game running normal")
                self.b4_1.setStyleSheet("background-color: rgb(255,0,0)")
                self.store_checker = self.b4_1.text()
                self.curr_selected_btn_coord[0] = 4
                self.curr_selected_btn_coord[1] = 1
                self.toggle_selection = not self.toggle_selection
            else:
                self.l_prompt_message.setText("Select a button that has a checker")
                self.reset_btns_state()

    def btn_selected5_2(self):      # Fully implemented.
        if self.toggle_selection:   # If a btn has been previously pressed.
            # Allow to be move to if this btn is empty.
            if self.b5_2.text() == self.empty_btn:
                if self.store_checker == self.grep_checker:     # If a grep was selected.
                    if self.curr_selected_btn_coord[0] == 4 and \
                            (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for forward movement...
                        self.b5_2.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 3 and self.curr_selected_btn_coord[1] == 1 \
                            and self.b4_1.text() == self.line_checker:
                        self.b5_2.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b4_1.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    elif self.curr_selected_btn_coord[0] == 3 and self.curr_selected_btn_coord[1] == 3 \
                            and self.b4_2.text() == self.line_checker:
                        self.b5_2.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b4_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
                elif self.store_checker == self.line_checker:   # If a line was selected.
                    if self.curr_selected_btn_coord[0] == 6 \
                            and (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for backward movement...
                        self.b5_2.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 7 and self.curr_selected_btn_coord[1] == 1 \
                            and self.b6_1.text() == self.grep_checker:
                        self.b5_2.setText(self.store_checker)
                        self.b6_1.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1

                    elif self.curr_selected_btn_coord[0] == 7 and self.curr_selected_btn_coord[1] == 3 \
                            and self.b6_2.text() == self.grep_checker:
                        self.b5_2.setText(self.store_checker)
                        self.b6_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
            else:
                self.l_prompt_message.setText("This button isn't empty")
                self.reset_btns_state()
        else:
            # If the btn initially selected is empty.
            if not self.b5_2.text() == self.empty_btn:
                self.l_prompt_message.setText("Game running normal")
                self.b5_2.setStyleSheet("background-color: rgb(255,0,0)")
                self.store_checker = self.b5_2.text()
                self.curr_selected_btn_coord[0] = 5
                self.curr_selected_btn_coord[1] = 2
                self.toggle_selection = not self.toggle_selection
            else:
                self.l_prompt_message.setText(
                    "Select a button that has a checker")
                self.reset_btns_state()

    def btn_selected6_1(self):      # Fully implemented.
        if self.toggle_selection:   # If a btn has been previously pressed.
            # Allow to be move to if this btn is empty.
            if self.b6_1.text() == self.empty_btn:
                if self.store_checker == self.grep_checker:     # If a grep was selected.
                    if self.curr_selected_btn_coord[0] == 5 and \
                            (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for forward movement...
                        self.b6_1.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 4 and self.curr_selected_btn_coord[1] == 2 \
                            and self.b5_2.text() == self.line_checker:
                        self.b6_1.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b5_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
                elif self.store_checker == self.line_checker:   # If a line was selected.
                    if self.curr_selected_btn_coord[0] == 7 \
                            and (self.curr_selected_btn_coord[1] == 1 or self.curr_selected_btn_coord[1] == 2):
                        # Checking for backward movement...
                        self.b6_1.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    # CHECAR SI VA A COMER.
                    elif self.curr_selected_btn_coord[0] == 8 and self.curr_selected_btn_coord[1] == 2 \
                            and self.b7_2.text() == self.grep_checker:
                        self.b6_1.setText(self.store_checker)
                        self.b7_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
            else:
                self.l_prompt_message.setText("This button isn't empty")
                self.reset_btns_state()
        else:
            # If the btn initially selected is empty.
            if not self.b6_1.text() == self.empty_btn:
                self.l_prompt_message.setText("Game running normal")
                self.b6_1.setStyleSheet("background-color: rgb(255,0,0)")
                self.store_checker = self.b6_1.text()
                self.curr_selected_btn_coord[0] = 6
                self.curr_selected_btn_coord[1] = 1
                self.toggle_selection = not self.toggle_selection
            else:
                self.l_prompt_message.setText(
                    "Select a button that has a checker")
                self.reset_btns_state()

    def btn_selected6_2(self):      # Fully implemented.
        if self.toggle_selection:   # If a btn has been previously pressed.
            # Allow to be move to if this btn is empty.
            if self.b6_2.text() == self.empty_btn:
                if self.store_checker == self.grep_checker:     # If a grep was selected.
                    if self.curr_selected_btn_coord[0] == 5 and \
                            (self.curr_selected_btn_coord[1] == 2 or self.curr_selected_btn_coord[1] == 3):
                        # Checking for forward movement...
                        self.b6_2.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    elif self.curr_selected_btn_coord[0] == 4 and self.curr_selected_btn_coord[1] == 1 \
                            and self.b5_2.text() == self.line_checker:
                        self.b6_2.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b5_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    elif self.curr_selected_btn_coord[0] == 4 and self.curr_selected_btn_coord[1] == 3 \
                            and self.b5_2.text() == self.line_checker:
                        self.b6_2.setText(self.store_checker)
                        # Limpiar el checker que se comio.
                        self.b5_3.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.grep_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
                elif self.store_checker == self.line_checker:   # If a line was selected.
                    if self.curr_selected_btn_coord[0] == 7 \
                            and (self.curr_selected_btn_coord[1] == 2 or self.curr_selected_btn_coord[1] == 3):
                        # Checking for backward movement...
                        self.b6_2.setText(self.store_checker)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                    # CHECAR SI VA A COMER.
                    elif self.curr_selected_btn_coord[0] == 8 and self.curr_selected_btn_coord[1] == 1 \
                            and self.b7_2.text() == self.grep_checker:
                        self.b6_2.setText(self.store_checker)
                        self.b7_2.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1

                    elif self.curr_selected_btn_coord[0] == 8 and self.curr_selected_btn_coord[1] == 3 \
                            and self.b7_3.text() == self.grep_checker:
                        self.b6_2.setText(self.store_checker)
                        self.b7_3.setText(self.empty_btn)
                        self.clear_btn_checker()
                        self.reset_btns_state()
                        self.line_score += 1
                    else:
                        self.l_prompt_message.setText(
                            "Checker progresssion is incorrect.")
                        self.reset_btns_state()
            else:
                self.l_prompt_message.setText("This button isn't empty")
                self.reset_btns_state()
        else:
            # If the btn initially selected is empty.
            if not self.b6_2.text() == self.empty_btn:
                self.l_prompt_message.setText("Game running normal")
                self.b6_2.setStyleSheet("background-color: rgb(255,0,0)")
                self.store_checker = self.b6_2.text()
                self.curr_selected_btn_coord[0] = 6
                self.curr_selected_btn_coord[1] = 2
                self.toggle_selection = not self.toggle_selection
            else:
                self.l_prompt_message.setText(
                    "Select a button that has a checker")
                self.reset_btns_state()


    def clear_btn_bkgn(self):
        self.b1_1.setStyleSheet("")
        self.b1_2.setStyleSheet("")
        self.b1_3.setStyleSheet("")
        self.b1_4.setStyleSheet("")
        
        self.b2_1.setStyleSheet("")
        self.b2_2.setStyleSheet("")
        self.b2_3.setStyleSheet("")
        self.b2_4.setStyleSheet("")

        self.b3_1.setStyleSheet("")
        self.b3_2.setStyleSheet("")
        self.b3_3.setStyleSheet("")
        self.b3_4.setStyleSheet("")

        self.b4_1.setStyleSheet("")
        self.b4_2.setStyleSheet("")
        self.b4_3.setStyleSheet("")
        self.b4_4.setStyleSheet("")

        self.b5_1.setStyleSheet("")
        self.b5_2.setStyleSheet("")
        self.b5_3.setStyleSheet("")
        self.b5_4.setStyleSheet("")

        self.b6_1.setStyleSheet("")
        self.b6_2.setStyleSheet("")
        self.b6_3.setStyleSheet("")
        self.b6_4.setStyleSheet("")

        self.b7_1.setStyleSheet("")
        self.b7_2.setStyleSheet("")
        self.b7_3.setStyleSheet("")
        self.b7_4.setStyleSheet("")

        self.b8_1.setStyleSheet("")
        self.b8_2.setStyleSheet("")
        self.b8_3.setStyleSheet("")
        self.b8_4.setStyleSheet("")

    def clear_btn_checker(self):
        if self.curr_selected_btn_coord == [1, 1]:
            self.b1_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [1, 2]:
            self.b1_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [1, 3]:
            self.b1_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [1, 4]:
            self.b1_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [2, 1]:
            self.b2_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [2, 2]:
            self.b2_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [2, 3]:
            self.b2_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [2, 4]:
            self.b2_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [3, 1]:
            self.b3_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [3, 2]:
            self.b3_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [3, 3]:
            self.b3_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [3, 4]:
            self.b3_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [4, 1]:
            self.b4_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [4, 2]:
            self.b4_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [4, 3]:
            self.b4_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [4, 4]:
            self.b4_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [5, 1]:
            self.b5_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [5, 2]:
            self.b5_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [5, 3]:
            self.b5_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [5, 4]:
            self.b5_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [6, 1]:
            self.b6_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [6, 2]:
            self.b6_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [6, 3]:
            self.b6_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [6, 4]:
            self.b6_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [7, 1]:
            self.b7_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [7, 2]:
            self.b7_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [7, 3]:
            self.b7_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [7, 4]:
            self.b7_4.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [8, 1]:
            self.b8_1.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [8, 2]:
            self.b8_2.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [8, 3]:
            self.b8_3.setText(self.empty_btn)
        elif self.curr_selected_btn_coord == [8, 4]:
            self.b8_4.setText(self.empty_btn)
        
    def reset_btns_state(self):
        self.clear_btn_bkgn()
        self.store_checker = ""
        self.curr_selected_btn_coord[0] = 0
        self.curr_selected_btn_coord[1] = 0
        self.toggle_selection = False


# TODO: Check if lines can move as intended. IMPLEMENTED BUT NEEDS TESTING.
# TODO: Check if btn that is going to move to is occupied. IMPLEMENTED BUT NEEDS TESTING.
# TODO: Eat checkers.
# TODO: Method for continously checking score.
# TODO: PLAYER TURNS.
# TODO: Colgar ropa.

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


import sys
from time import sleep
import functools
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, pyqtSignal, pyqtProperty, QPropertyAnimation, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QStyle, QWidget, QGraphicsEffect
from ui.ui_UltimateTicTacToe import Ui_UltimateTicTacToeWindow
from ui.ui_MainMenu import Ui_MainMenuWindow
FIRST_LETTER = "X"
ZERO_LETTER = "0"
BOARD_HEIGHT = 3
BOARD_LENGTH = 3
WIN_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

class UltimateMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 800)
        self.setStyleSheet("QWidget {color: #9A8C98; background-color: #22223B;}")
        self.setWindowTitle("UltimateTicTacToe")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget()
        self.UltimateTicTacToeInterface = UltimateTicTacToeWindow()
        self.MainMenuInterface = MainMenuWindow()
        self.UltimateTicTacToeInterface.button_reset_clicked.connect(self.init_btn_back)
        self.init_btn_back()
        self.MainMenuInterface.btn_start.clicked.connect(self.toggle_interface)
        self.stacked_widget.addWidget(self.MainMenuInterface)
        self.stacked_widget.addWidget(self.UltimateTicTacToeInterface)


        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.setAlignment(Qt.AlignCenter)
        self.central_widget.setLayout(layout)
    def init_btn_back(self):
        self.UltimateTicTacToeInterface.btn_back.clicked.connect(self.toggle_interface)

    def toggle_interface(self):
        current_index = self.stacked_widget.currentIndex()
        next_index = (current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(next_index)

class MainMenuWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class UltimateTicTacToeWindow(QMainWindow, Ui_UltimateTicTacToeWindow):
    button_reset_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.new_game()

    def new_game(self):

        self.game_pos = [
            [-1 for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
            for _ in range(BOARD_HEIGHT * BOARD_LENGTH)
        ]

        self.local_zero_pos = [[] for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]
        self.local_first_pos = [[] for _ in range(BOARD_HEIGHT * BOARD_LENGTH)]

        self.global_first_pos = []
        self.global_zero_pos = []

        self.local_end = False
        self.global_end = False

        self.current_global_field = -1

        self.local_winner = '0'
        self.global_winner = '0'

        self.zero_turn = False
        self.setupUi(self)

        self.label.setText(f"Ход {self.ultimate_tictactoe_swapper(self.zero_turn)}")

        self.setup_click_handler()


    def field_click_handler(self):

        while True:
            self.global_field, self.local_field = int(self.sender().objectName().split('_')[2]), int(self.sender().objectName().split('_')[5]) # global_field_0_local_field_0

            if not self.field_is_free():
                print("Не свободно")
                break

            if self.current_global_field != self.global_field and self.current_global_field != -1:
                print('Не то поле')
                break

            self.insert_move_into_list("game_pos")
            self.insert_move_into_list("local_pos")

            self.zero_turn = not self.zero_turn
            self.current_global_field = self.local_field

            self.sender().setText(f"{self.ultimate_tictactoe_swapper(self.game_pos[self.global_field][self.local_field])}")
            self.label.setText(f"Ход {self.ultimate_tictactoe_swapper(self.zero_turn)}")

            if self.local_win()[0]:
                self.local_winner = self.local_win()[1]
                self.insert_move_into_list("global_pos")
                print(f'выигрыш {self.local_winner} в поле {self.global_field}')

            if self.global_win()[0]:
                self.global_winner = self.global_win()[1]
                print(f'выигрыш {self.global_winner}')
                break
            break

    def btn_reset_handler(self):
        self.new_game()
        self.button_reset_clicked.emit()

    def setup_click_handler(self):
        self.global_field_0_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_0_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_1_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_1_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_2_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_2_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_3_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_3_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_4_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_4_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_5_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_5_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_6_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_6_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_7_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_7_local_field_8.clicked.connect(self.field_click_handler)

        self.global_field_8_local_field_0.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_1.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_2.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_3.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_4.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_5.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_6.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_7.clicked.connect(self.field_click_handler)
        self.global_field_8_local_field_8.clicked.connect(self.field_click_handler)

        self.btn_reset.clicked.connect(self.btn_reset_handler)

    def local_win(self):

        if tuple(self.local_zero_pos[self.global_field]) in WIN_COMBINATIONS:
            return (True, ZERO_LETTER)

        elif tuple(self.local_first_pos[self.global_field]) in WIN_COMBINATIONS:
            return (True, FIRST_LETTER)

        else:
            return (False, None)

    def global_win(self):
        if tuple(self.global_first_pos) in WIN_COMBINATIONS:
            return (True, FIRST_LETTER)

        elif tuple(self.global_zero_pos) in WIN_COMBINATIONS:
            return (True, ZERO_LETTER)

        else:
            return (False, None)

    def field_is_free(self):
        return self.game_pos[self.global_field][self.local_field] == -1

    def insert_move_into_list(self, list_to_insert):
        if list_to_insert == "game_pos":
            self.game_pos[self.global_field][
                self.local_field
            ] = self.ultimate_tictactoe_swapper(
                self.ultimate_tictactoe_swapper(self.zero_turn)
            )

        if list_to_insert == "local_pos":
            if self.zero_turn:
                self.local_zero_pos[self.global_field].append(self.local_field)

            else:
                self.local_first_pos[self.global_field].append(self.local_field)

        if list_to_insert == "global_pos":
            if self.zero_turn:
                self.global_zero_pos.append(self.global_field)

            else:
                self.global_first_pos.append(self.global_field)

    def ultimate_tictactoe_swapper(self, var):  # bool->str->num->str
        if type(var) is int:
            if var == 0:
                return ZERO_LETTER
            if var == 1:
                return FIRST_LETTER
            if var == -1:
                return " "
            else:
                return var

        if type(var) is bool:
            if var:
                return ZERO_LETTER
            else:
                return FIRST_LETTER

        return 0 if var == ZERO_LETTER else 1

if __name__ == '__main__':

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = UltimateMainWindow()
    ex.resize(800, 800)
    ex.show()
    sys.exit(app.exec())


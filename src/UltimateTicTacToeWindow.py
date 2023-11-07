from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from svghelper import set_color
import themes_config
from ui.ui_UltimateTicTacToe import Ui_UltimateTicTacToeWindow

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

class UltimateTicTacToeWindow(QMainWindow, Ui_UltimateTicTacToeWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_click_handler()
        self.new_game()

    def draw_board(self):
        for global_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
            for local_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
                field = self.findChild(QtCore.QObject, f"global_field_{global_field_index}_local_field_{local_field_index}")

                field.setText(self.ultimate_tictactoe_swapper(self.game_pos[global_field_index][local_field_index]))
                field.change_theme(themes_config.current_theme)

    def change_theme(self, theme):

        self.setStyleSheet("QWidget {\n"
                            f"    color: {themes_config.themes[theme]['text_color']};\n"
                            f"    background-color: {themes_config.themes[theme]['background_color']};\n"
                            "    font-family: Rubik;\n"
                            "    font-size: 16pt;\n"
                            "}"
                            "\n"
                            "QFrame[frameShape=\"4\"],\n"
                            "QFrame[frameShape=\"5\"]\n"
                            "{\n"
                            "    border: none;\n"
                            f"   background: {themes_config.themes[theme]['edge_color']};\n"
                            "}"
                            "QPushButton {\n"
                            "    background-color: transparent;\n"
                            "    border: none;\n"
                            "    border-radius: 10px;\n"
                            "}\n"
                            )

        set_color(u"ui/icons/back_icon.svg", u"ui/icons/back_icon.svg", themes_config.themes[theme]['text_color'])
        btn_back_icon = QtGui.QIcon()
        btn_back_icon.addFile(u"ui/icons/back_icon.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(btn_back_icon)

        set_color(u"ui/icons/reset_icon.svg", u"ui/icons/reset_icon.svg", themes_config.themes[theme]['text_color'])
        btn_reset_icon = QtGui.QIcon()
        btn_reset_icon.addFile(u"ui/icons/reset_icon.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset.setIcon(btn_reset_icon)

        self.btn_back.setStyleSheet(f"background-color: {themes_config.themes[theme]['background_color']};")
        self.btn_back.change_theme(theme)

        self.btn_reset.setStyleSheet(f"background-color: {themes_config.themes[theme]['background_color']};")
        self.btn_reset.change_theme(theme)

        self.draw_board()

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

        self.label.setText(f"Ход {self.ultimate_tictactoe_swapper(self.zero_turn)}")

        self.draw_board()

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

    def setup_click_handler(self):

        for global_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
            for local_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
                field = self.findChild(QtCore.QObject, f"global_field_{global_field_index}_local_field_{local_field_index}")
                field.clicked.connect(self.field_click_handler)

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
                return ""
            else:
                return var

        if type(var) is bool:
            if var:
                return ZERO_LETTER
            else:
                return FIRST_LETTER

        return 0 if var == ZERO_LETTER else 1

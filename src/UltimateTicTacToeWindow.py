from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from svghelper import set_color
from db_handler import *
import themes_config
from ui.ui_UltimateTicTacToe import Ui_UltimateTicTacToeWindow
from WinWindow import WinWindow
from UploadGame import UploadGame

FIRST_LETTER = "X"
ZERO_LETTER = "0"
BOARD_HEIGHT = 3
BOARD_LENGTH = 3
WIN_COMBINATIONS = (
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {2, 4, 6}
)

class UltimateTicTacToeWindow(QMainWindow, Ui_UltimateTicTacToeWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_global_field = 0
        self.numpad_control = False
        self.make_widgets()


        self.layout = QtWidgets.QGridLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(QtCore.QMargins(8, 8, 8, 8))
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.new_game()

        self.setup_click_handler()

    def make_widgets(self):
        self.win_window = WinWindow()
        self.upload_game_window = UploadGame()

    def draw_board(self):
        for global_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
            for local_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
                field = self.findChild(QtCore.QObject, f"global_field_{global_field_index}_local_field_{local_field_index}")

                field.setText(self.ultimate_tictactoe_swapper(self.game_pos[global_field_index][local_field_index]))
                field.change_theme(themes_config.current_theme)

    def toggle_numpad_control(self):
        self.numpad_control = not self.numpad_control

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

        set_color(u"ui/icons/upload_icon.svg", u"ui/icons/upload_icon.svg", themes_config.themes[theme]['text_color'])
        btn_upload_icon = QtGui.QIcon()
        btn_upload_icon.addFile(u"ui/icons/upload_icon.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_upload.setIcon(btn_upload_icon)

        set_color(u"ui/icons/save_icon.svg", u"ui/icons/save_icon.svg", themes_config.themes[theme]['text_color'])
        btn_save_icon = QtGui.QIcon()
        btn_save_icon.addFile(u"ui/icons/save_icon.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(btn_save_icon)

        self.btn_back.setStyleSheet(f"background-color: {themes_config.themes[theme]['background_color']};")
        self.btn_back.change_theme(theme)

        self.btn_reset.setStyleSheet(f"background-color: {themes_config.themes[theme]['background_color']};")
        self.btn_reset.change_theme(theme)

        self.btn_save.setStyleSheet(f"background-color: {themes_config.themes[theme]['background_color']};")
        self.btn_save.change_theme(theme)

        self.btn_upload.setStyleSheet(f"background-color: {themes_config.themes[theme]['background_color']};")
        self.btn_upload.change_theme(theme)

        self.build_label(theme)

        self.win_window.change_theme(theme)
        self.upload_game_window.change_theme(theme)

        self.draw_board()

    def build_label(self, theme):
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_LENGTH):
                field_index = int(row * BOARD_LENGTH + col)
                outer_label = QtWidgets.QLabel()
                opacity_effect = QtWidgets.QGraphicsOpacityEffect()
                outer_label.setGraphicsEffect(opacity_effect)
                outer_label.graphicsEffect().setOpacity(0)
                outer_label.setObjectName(f"outer_label_{field_index}")
                outer_label.setStyleSheet(
                    f"background-color: {themes_config.themes[theme]['outer_color']}; border-radius: 25px")
                outer_label.setAttribute(Qt.WA_TransparentForMouseEvents)
                self.layout.addWidget(outer_label, row, col)

        self.current_outer_label = self.layout.itemAt(0).widget()

        self.field_layout.addLayout(self.layout, 0, 0)

        for label_text in (0, 1):
            for row in range(0, BOARD_HEIGHT + 2, 2):
                for col in range(0, BOARD_LENGTH + 2, 2):

                    field_index = int((row / 2) * BOARD_LENGTH + (col / 2))
                    inner_label = QtWidgets.QLabel()
                    opacity_effect = QtWidgets.QGraphicsOpacityEffect()
                    inner_label.setGraphicsEffect(opacity_effect)
                    inner_label.setObjectName(f"inner_label_{label_text}_{field_index}")
                    inner_label.graphicsEffect().setOpacity(0)
                    inner_label.setStyleSheet(
                        f"background-color: {themes_config.themes[theme][f'win_{label_text}_color']}; border-radius: 10px")
                    inner_label.setAttribute(Qt.WA_TransparentForMouseEvents)
                    self.main_layout.addWidget(inner_label, row, col)

    def reset_labels(self):
        for i in range(self.main_layout.count()):
            if self.main_layout.itemAt(i).widget().__class__.__name__ == "QLabel":
                self.main_layout.itemAt(i).widget().graphicsEffect().setOpacity(0)
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().graphicsEffect().setOpacity(0)

    def new_game(self, custom_game=False):

        if not custom_game:
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

            self.zero_turn = False

            self.local_ends = set()

            self.local_field = 0

            self.any_field = False

        self.label.setText(f"Ход {self.ultimate_tictactoe_swapper(self.zero_turn)}")

        self.reset_labels()

        self.draw_board()

    def keyPressEvent(self, event):
        if self.numpad_control:
            press_list = [6, 7, 8, 3, 4, 5, 0, 1, 2]
            if event.key() >= Qt.Key_1 and event.key() <= Qt.Key_9:
                field = self.findChild(QtCore.QObject, f"global_field_{0 if self.current_global_field == -1 else self.current_global_field}_local_field_{press_list[event.key() - 49]}")
                field.click()



    def field_click_handler(self, *args, global_field="default", local_field="default"):

        if local_field == 'default':
            self.global_field, self.local_field = int(self.sender().objectName().split('_')[2]), int(
                self.sender().objectName().split('_')[5])  # global_field_0_local_field_0
        else:
            self.local_field = local_field

        while True:

            if self.current_global_field != self.global_field and self.current_global_field != -1 and not self.any_field:
                print('Не то поле')
                break

            if not self.field_is_free():
                print("Не свободно")
                break

            self.insert_move_into_list("game_pos")
            self.insert_move_into_list("local_pos")

            self.zero_turn = not self.zero_turn

            self.current_global_field = self.local_field

            self.sender().setText(f"{self.ultimate_tictactoe_swapper(self.game_pos[self.global_field][self.local_field])}")
            self.label.setText(f"Ход {self.ultimate_tictactoe_swapper(self.zero_turn)}")

            self.recolor_outer_label()

            if self.field_in_local_ends():
                print('поле уже было завершено, ставьте в любой')
                self.any_field = True
            else:
                self.any_field = False

            local_win_data = self.local_win()

            if local_win_data[0]:
                local_winner = local_win_data[1]
                self.insert_move_into_list("global_pos")
                self.local_ends.add(self.global_field)
                self.recolor_inner_label(self.ultimate_tictactoe_swapper(local_winner))
                print(f'выигрыш {local_winner} в поле {self.global_field}')


            global_win_data = self.global_win()

            if global_win_data[0]:
                self.global_winner = global_win_data[1]
                print(f'выигрыш {self.global_winner}')
                self.win_window.show()
                break
            break

    def recolor_outer_label(self):
        self.current_outer_label.graphicsEffect().setOpacity(0)
        for i in range(self.layout.count()):
            if self.layout.itemAt(i).widget().objectName() == f"outer_label_{self.local_field}":
                self.layout.itemAt(i).widget().graphicsEffect().setOpacity(0.2)
                self.current_outer_label = self.layout.itemAt(i).widget()
                break


    def recolor_inner_label(self, winner_color):
        for i in range(self.main_layout.count()):
            if self.main_layout.itemAt(i).widget().__class__.__name__ == "QLabel":
                if self.main_layout.itemAt(i).widget().objectName() == f"inner_label_{winner_color}_{self.global_field}":
                    self.main_layout.itemAt(i).widget().graphicsEffect().setOpacity(0.2)
                    break

    def btn_reset_handler(self):
        self.recolor_outer_label()
        self.new_game()



    def setup_click_handler(self):

        self.any_field = False
        for global_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
            for local_field_index in range(BOARD_HEIGHT * BOARD_LENGTH):
                field = self.findChild(QtCore.QObject, f"global_field_{global_field_index}_local_field_{local_field_index}")
                field.clicked.connect(self.field_click_handler)
        self.win_window.save_game_btn.clicked.connect(self.save_game)
        self.btn_reset.clicked.connect(self.btn_reset_handler)
        self.btn_upload.clicked.connect(self.show_upload_game)
        self.upload_game_window.upload_btn.clicked.connect(self.upload_game)
        self.btn_save.clicked.connect(self.save_game)

    def show_upload_game(self):
        self.upload_game_window.fill_data()
        self.upload_game_window.show()

    def upload_game(self):

        id = self.upload_game_window.table.currentRow()
        print(id)
        data = get_data(id)[0]

        self.game_pos = data_formatter(data[1], "game_pos")

        self.local_zero_pos = data_formatter(data[2], "local_pos")
        self.local_first_pos = data_formatter(data[3], "local_pos")

        self.global_first_pos = data_formatter(data[4], "global_pos")
        self.global_zero_pos = data_formatter(data[5], "global_pos")

        self.local_end = True if data[6] == "True" else False
        self.global_end = True if data[7] == "True" else False

        self.current_global_field = int(data[8])

        self.zero_turn = True if data[9] == "True" else False

        self.local_ends = data_formatter(data[10], "local_ends")

        self.any_field = True if data[11] == "True" else False

        self.current_outer_label = self.layout.itemAt(0).widget()

        self.local_field = int(data[13])

        self.new_game(custom_game=True)

    def save_game(self):
        info = (str(self.game_pos), str(self.local_zero_pos), str(self.local_first_pos), str(self.global_first_pos), str(self.global_zero_pos),
                str(self.local_end), str(self.global_end), str(self.current_global_field), str(self.zero_turn), str(self.local_ends),
                str(self.any_field), str(self.current_outer_label), str(self.local_field))
        save_game(info)

    def local_win(self):

        if self.global_field not in self.local_ends:
            for combination in WIN_COMBINATIONS:
                if set(self.local_zero_pos[self.global_field]) & combination == combination:
                    return (True, ZERO_LETTER, combination)

                elif set(self.local_first_pos[self.global_field]) & combination == combination:
                    return (True, FIRST_LETTER, combination)

        return (False,)

    def global_win(self):
        for combination in WIN_COMBINATIONS:
            if set(self.global_zero_pos) & combination == combination:
                return (True, ZERO_LETTER, combination)

            elif set(self.global_first_pos) & combination == combination:
                return (True, FIRST_LETTER, combination)

        return (False,)

    def field_in_local_ends(self):
        return self.local_field in self.local_ends

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
                self.global_first_pos.append(self.global_field)
            else:
                self.global_zero_pos.append(self.global_field)


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
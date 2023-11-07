from PyQt5.QtWidgets import QMainWindow
from ui.ui_Settings import Ui_SettingsWindow
import themes_config

class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def change_theme(self, theme):
        self.setStyleSheet(
            "QWidget {" + f'color: {themes_config.themes[theme]["text_color"]}; background-color: {themes_config.themes[theme]["background_color"]};' + "}"
            "QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
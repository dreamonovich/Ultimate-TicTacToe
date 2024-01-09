from ui.ui_WinWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
import config

class WinWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def change_theme(self, theme):
        self.setStyleSheet(
            "QWidget {" + f'color: {config.themes[theme]["text_color"]}; background-color: {config.themes[theme]["background_color"]};' + "}"
            "QPushButton {\n"
                            f"   background-color: {config.themes[theme]['button_color']};\n"
                            "    border: none;\n"
                            "    border-radius: 10px;\n"
                            "}\n")

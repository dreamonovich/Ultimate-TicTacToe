from PyQt5.QtWidgets import QMainWindow
from ui.ui_Settings import Ui_SettingsWindow
from PyQt5 import QtGui, QtCore
from qtwidgets import AnimatedToggle
import config

class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.numpad_toggle = AnimatedToggle(
            checked_color="#4E5754",
            pulse_checked_color="#808080"
        )
        self.numpad_toggle.setFixedSize(70,50)
        self.gridLayout.addWidget(self.numpad_toggle, 1, 1, QtCore.Qt.AlignRight)

        self.setWindowIcon(QtGui.QIcon(u"ui/icons/settings_icon_static.svg"))

    def change_theme(self, theme):

        self.setStyleSheet(
            "QWidget {" + f'color: {config.themes[theme]["text_color"]}; background-color: {config.themes[theme]["background_color"]};' + "}"
            "QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon1 = QtGui.QIcon(QtGui.QPixmap("ui\\icons/theme1_icon.png"))
        self.theme1.setIcon(icon1)

        icon2 = QtGui.QIcon(QtGui.QPixmap("ui\\icons/theme2_icon.png"))
        self.theme2.setIcon(icon2)

        icon3 = QtGui.QIcon(QtGui.QPixmap("ui\\icons/theme3_icon.png"))
        self.theme3.setIcon(icon3)
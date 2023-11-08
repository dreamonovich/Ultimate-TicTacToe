from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from SettingsWindow import *
from ui.ui_MainMenu import Ui_MainMenuWindow

class MainMenuWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings_window = SettingsWindow()

        self.github_button.clicked.connect(lambda: QtGui.QDesktopServices().openUrl(QUrl("https://github.com/dreamonovich/Ultimate-TicTacToe")))

        self.settings_button.clicked.connect(lambda: self.settings_window.show())
    def change_theme(self, theme):
        self.setStyleSheet(
                            "QPushButton {\n"
                            f"   background-color: {themes_config.themes[theme]['button_color']};\n"
                            "    border: none;\n"
                            "    border-radius: 10px;\n"
                            "}\n")

        self.btn_play.change_theme(theme)
        set_color(u"src/ui/icons/github_icon.svg", u"src/ui/icons/github_icon.svg", themes_config.themes[theme]['text_color'])
        github_icon = QtGui.QIcon()
        github_icon.addFile(u"src/ui/icons/github_icon.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.github_button.setIcon(github_icon)

        set_color(u"src/ui/icons/settings_icon.svg", u"src/ui/icons/settings_icon.svg", themes_config.themes[theme]['text_color'])
        settings_icon = QtGui.QIcon()
        settings_icon.addFile(u"src/ui/icons/settings_icon.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(settings_icon)

        self.settings_window.change_theme(theme)

from PyQt5.QtCore import QUrl
from svghelper import set_color
from SettingsWindow import *
from ui.ui_MainMenu import Ui_MainMenuWindow


class MainMenuWindow(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings_window = SettingsWindow()

        # handle button click
        self.github_button.clicked.connect(
            lambda: QtGui.QDesktopServices().openUrl(
                QUrl("https://github.com/dreamonovich/Ultimate-TicTacToe")
            )
        )

        self.settings_button.clicked.connect(lambda: self.settings_window.show())

    def change_theme(self, theme):
        self.setStyleSheet(
            "QPushButton {\n"
            f"   background-color: {config.themes[theme]['button_color']};\n"
            "    border: none;\n"
            "    border-radius: 10px;\n"
            "}\n"
        )

        self.btn_play.change_theme(theme)
        set_color(
            "ui/icons/github_icon.svg",
            "ui/icons/github_icon.svg",
            config.themes[theme]["text_color"],
        )
        github_icon = QtGui.QIcon()
        github_icon.addFile(
            "ui/icons/github_icon.svg",
            QtCore.QSize(),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.github_button.setIcon(github_icon)

        set_color(
            "ui/icons/settings_icon.svg",
            "ui/icons/settings_icon.svg",
            config.themes[theme]["text_color"],
        )
        settings_icon = QtGui.QIcon()
        settings_icon.addFile(
            "ui/icons/settings_icon.svg",
            QtCore.QSize(),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.settings_button.setIcon(settings_icon)

        self.settings_window.change_theme(theme)

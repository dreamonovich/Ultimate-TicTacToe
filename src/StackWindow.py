from MainMenuWindow import *
from PyQt5 import Qt
from UltimateTicTacToeWindow import *
from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

class StackWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.MainMenuInterface.settings_window.theme1.clicked.connect(self.theme_clicked)
        self.MainMenuInterface.settings_window.theme2.clicked.connect(self.theme_clicked)
        self.MainMenuInterface.settings_window.theme3.clicked.connect(self.theme_clicked)
        self.MainMenuInterface.settings_window.numpad_toggle.clicked.connect(self.UltimateTicTacToeInterface.toggle_numpad_control)

    def theme_clicked(self):
        config.current_theme = self.sender().objectName()
        self.change_theme(config.current_theme)

    def initUI(self):
        self.resize(800, 800)
        self.setWindowTitle("UltimateTicTacToe")
        window_icon = QtGui.QIcon('ui/icons/UltimateTicTacToe_icon.svg')
        self.setWindowIcon(window_icon)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget()
        self.UltimateTicTacToeInterface = UltimateTicTacToeWindow()
        self.MainMenuInterface = MainMenuWindow()
        self.init_btn_back()
        self.MainMenuInterface.btn_play.clicked.connect(self.toggle_interface)
        self.stacked_widget.addWidget(self.MainMenuInterface)
        self.stacked_widget.addWidget(self.UltimateTicTacToeInterface)
        self.change_theme(config.current_theme)
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.setAlignment(Qt.AlignCenter)
        self.central_widget.setLayout(layout)

    def change_theme(self, theme):
        self.setStyleSheet("QWidget {"+f'color: {config.themes[theme]["text_color"]}; background-color: {config.themes[theme]["background_color"]};'+"}")
        self.UltimateTicTacToeInterface.change_theme(theme)
        self.MainMenuInterface.change_theme(theme)

    def init_btn_back(self):
        self.UltimateTicTacToeInterface.btn_back.clicked.connect(self.toggle_interface)

    def toggle_interface(self):
        current_index = self.stacked_widget.currentIndex()
        next_index = (current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(next_index)
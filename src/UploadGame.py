from ui.ui_UploadGame import Ui_uploadgame
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3
import themes_config

class UploadGame(QMainWindow, Ui_uploadgame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def change_theme(self, theme):
        self.setStyleSheet(
            "QWidget {" + f'color: {themes_config.themes[theme]["text_color"]}; background-color: {themes_config.themes[theme]["background_color"]};' + "}"
            "QPushButton {\n"
                            f"   background-color: {themes_config.themes[theme]['button_color']};\n"
                            "    border: none;\n"
                            "    border-radius: 10px;\n"
                            "}\n")
    def fill_data(self):
        self.connection = sqlite3.connect("saves.sqlite")
        cursor = self.connection.execute('select * from saves')
        res = self.connection.cursor().execute("SELECT * FROM saves").fetchall()
        # Заполним размеры таблицы
        self.table.setColumnCount(12)
        self.table.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()



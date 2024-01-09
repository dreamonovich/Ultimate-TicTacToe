import sys
from PyQt5.QtWidgets import QApplication
from StackWindow import StackWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StackWindow()
    ex.resize(800, 800)
    ex.show()
    sys.exit(app.exec())
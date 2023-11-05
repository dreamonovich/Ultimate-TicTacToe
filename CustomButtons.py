from PyQt5 import QtCore, QtWidgets, QtGui
from themes import themes
import current_theme
import functools

class Field(QtWidgets.QPushButton):
    button_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Field, self).__init__(parent)
        self.button_signal.connect(self.animate_button)
        self.change_theme(current_theme.current_theme)
        pass

    def enterEvent(self, event):
        self.button_signal.emit("enterEvent")

    def leaveEvent(self, event):
        self.button_signal.emit("leaveEvent")

    def animate_button(self, button_signal):

        self.init_animation()

        if button_signal == "enterEvent":
            self.setStyleSheet("Field {background-color: " + themes[current_theme.current_theme]["hover_color"] + ";}")


        elif button_signal == "leaveEvent":
            self.fade_animation.valueChanged.connect(functools.partial(self.helper_function, self))
            self.wait_animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
            self.wait_animation.finished.connect(lambda: self.fade_animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped))

    def init_animation(self):

        self.fade_animation = QtCore.QVariantAnimation(
            self,
            duration=200,
            startValue=self.hover_color,
            endValue=self.end_color,
        )

        self.wait_animation = QtCore.QVariantAnimation(
            self,
            duration=100,
            startValue=self.hover_color,
            endValue=self.hover_color,
        )

    def change_theme(self, theme):
        self.hover_color = QtGui.QColor(themes[theme]["hover_color"])
        self.end_color = QtGui.QColor(themes[theme]["background_color"])
        self.setStyleSheet(f"background-color: {themes[theme]['background_color']};")


    def helper_function(self, widget, color):
        widget.setStyleSheet("background-color: {}".format(color.name()))

class HoveringButton(Field):

    def __init__(self, parent=None):
        super(HoveringButton, self).__init__(parent)

    def change_theme(self, theme):
        self.hover_color = QtGui.QColor(themes[theme]["hover_color"])
        self.end_color = QtGui.QColor(themes[theme]["button_color"])
        self.setStyleSheet(f"background-color: {themes[theme]['button_color']};")


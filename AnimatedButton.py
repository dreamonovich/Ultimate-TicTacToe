from PyQt5 import QtCore, QtWidgets, QtGui
import functools

class AnimatedButton(QtWidgets.QPushButton):
    button_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(AnimatedButton, self).__init__(parent)
        self.button_signal.connect(self.animate_button)
        self.start_color = QtGui.QColor("#2f2f50")
        self.end_color = QtGui.QColor("#22223B")
        pass

    def enterEvent(self, event):
        self.button_signal.emit("enterEvent")

    def leaveEvent(self, event):
        self.button_signal.emit("leaveEvent")

    def animate_button(self, button_signal):

        self.fade_animation = QtCore.QVariantAnimation(
            self,
            duration=200,
            startValue=self.start_color,
            endValue=self.end_color,
        )

        self.wait_animation = QtCore.QVariantAnimation(
            self,
            duration=100,
            startValue=self.start_color,
            endValue=self.start_color,
        )

        if button_signal == "enterEvent":
            self.setStyleSheet("AnimatedButton {background-color: #2f2f50;}")


        elif button_signal == "leaveEvent":
            self.fade_animation.valueChanged.connect(functools.partial(self.helper_function, self))
            self.wait_animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
            self.wait_animation.finished.connect(lambda: self.fade_animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped))



    def helper_function(self, widget, color):
        widget.setStyleSheet("background-color: {}".format(color.name()))
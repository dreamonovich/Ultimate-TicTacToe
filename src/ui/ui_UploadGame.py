# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\ui_UploadGame.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uploadgame(object):
    def setupUi(self, uploadgame):
        uploadgame.setObjectName("uploadgame")
        uploadgame.resize(700, 500)
        uploadgame.setMinimumSize(QtCore.QSize(700, 500))
        uploadgame.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(uploadgame)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.upload_btn = HoveringButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_btn.sizePolicy().hasHeightForWidth())
        self.upload_btn.setSizePolicy(sizePolicy)
        self.upload_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.upload_btn.setObjectName("upload_btn")
        self.verticalLayout.addWidget(self.upload_btn, 0, QtCore.Qt.AlignHCenter)
        uploadgame.setCentralWidget(self.centralwidget)

        self.retranslateUi(uploadgame)
        QtCore.QMetaObject.connectSlotsByName(uploadgame)

    def retranslateUi(self, uploadgame):
        _translate = QtCore.QCoreApplication.translate
        uploadgame.setWindowTitle(_translate("uploadgame", "Загрузить игру"))
        self.upload_btn.setText(_translate("uploadgame", "Загрузить"))


from CustomButtons import HoveringButton

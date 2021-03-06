# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_eye_timer = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eye_timer.sizePolicy().hasHeightForWidth())
        self.btn_eye_timer.setSizePolicy(sizePolicy)
        self.btn_eye_timer.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_eye_timer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_eye_timer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_eye_timer.setFont(font)
        self.btn_eye_timer.setIconSize(QtCore.QSize(16, 16))
        self.btn_eye_timer.setObjectName("btn_eye_timer")
        self.verticalLayout.addWidget(self.btn_eye_timer)
        self.btn_reminder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reminder.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_reminder.setFont(font)
        self.btn_reminder.setObjectName("btn_reminder")
        self.verticalLayout.addWidget(self.btn_reminder)
        self.btn_note = QtWidgets.QPushButton(self.centralwidget)
        self.btn_note.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_note.setFont(font)
        self.btn_note.setObjectName("btn_note")
        self.verticalLayout.addWidget(self.btn_note)
        self.btn_arithmetic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_arithmetic.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_arithmetic.setFont(font)
        self.btn_arithmetic.setObjectName("btn_arithmetic")
        self.verticalLayout.addWidget(self.btn_arithmetic)
        self.btn_pc_timer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pc_timer.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_pc_timer.setFont(font)
        self.btn_pc_timer.setObjectName("btn_pc_timer")
        self.verticalLayout.addWidget(self.btn_pc_timer)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????!"))
        self.label.setText(_translate("MainWindow", "????????????!"))
        self.btn_eye_timer.setText(_translate("MainWindow", "????????????, ????????????!"))
        self.btn_reminder.setText(_translate("MainWindow", "????????????, ??????????????????????!"))
        self.btn_note.setText(_translate("MainWindow", "????????????, ??????????????!"))
        self.btn_arithmetic.setText(_translate("MainWindow", "????????????, ???????????? ????????!"))
        self.btn_pc_timer.setText(_translate("MainWindow", "????????????, ??????????????????!"))

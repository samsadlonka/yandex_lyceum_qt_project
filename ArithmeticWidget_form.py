# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArithmeticWidget_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ArithmeticWidget(object):
    def setupUi(self, ArithmeticWidget):
        ArithmeticWidget.setObjectName("ArithmeticWidget")
        ArithmeticWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ArithmeticWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ArithmeticWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(ArithmeticWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.main_label = QtWidgets.QLabel(ArithmeticWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet("")
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.verticalLayout.addWidget(self.main_label)
        self.lineEdit = QtWidgets.QLineEdit(ArithmeticWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.progressBar = QtWidgets.QProgressBar(ArithmeticWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label_ans = QtWidgets.QLabel(ArithmeticWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ans.setFont(font)
        self.label_ans.setObjectName("label_ans")
        self.verticalLayout.addWidget(self.label_ans)

        self.retranslateUi(ArithmeticWidget)
        QtCore.QMetaObject.connectSlotsByName(ArithmeticWidget)

    def retranslateUi(self, ArithmeticWidget):
        _translate = QtCore.QCoreApplication.translate
        ArithmeticWidget.setWindowTitle(_translate("ArithmeticWidget", "Устный счет"))
        self.label.setText(_translate("ArithmeticWidget", "Выберете знак"))
        self.comboBox.setItemText(0, _translate("ArithmeticWidget", "+"))
        self.comboBox.setItemText(1, _translate("ArithmeticWidget", "-"))
        self.comboBox.setItemText(2, _translate("ArithmeticWidget", "*"))
        self.main_label.setText(_translate("ArithmeticWidget", "5 + 7"))
        self.label_ans.setText(_translate("ArithmeticWidget", "Нажмиет Enter, чтобы ответить"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NotesWidget_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Note(object):
    def setupUi(self, Note):
        Note.setObjectName("Note")
        Note.resize(400, 300)
        Note.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Note)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(Note)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)

        self.retranslateUi(Note)
        QtCore.QMetaObject.connectSlotsByName(Note)

    def retranslateUi(self, Note):
        _translate = QtCore.QCoreApplication.translate
        Note.setWindowTitle(_translate("Note", "Заметка"))
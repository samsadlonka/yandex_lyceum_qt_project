import sqlite3
import sys
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from NotesWidget_form import Ui_Note

from CONST import NOTES_DB


class NoteWidget(QWidget, Ui_Note):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Pi_.ico'))
        self.date = datetime.today().date()

    def closeEvent(self, a0):
        if self.textEdit.toPlainText():
            text = self.textEdit.toPlainText()
            con = sqlite3.connect(NOTES_DB)
            cur = con.cursor()
            sql = """INSERT INTO Notes(date, text)
            VALUES(?, ?)"""
            cur.execute(sql, (self.date, text))
            con.commit()
            ok = QMessageBox.question(self, 'Заметка', 'Заметка успешно добавлена!', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteWidget()
    ex.show()
    sys.exit(app.exec())

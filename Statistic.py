import csv
import random
import sqlite3
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QScrollArea, QPushButton

from StatistikWidjet_form import Ui_Statistic
import datetime as dt

from CONST import NOTES_DB, STATISTIC_DB, ARITHMETIC_DB, FUNNY_TEXTS


class StatisticWidget(QWidget, Ui_Statistic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Pi_.ico'))
        self.save_btn = None

        self.con = sqlite3.connect(STATISTIC_DB)

        self.calendarWidget.clicked.connect(self.show_info)

        self.sum_time = dt.timedelta()

        self.show_info()

    def show_info(self):
        self.listWidget.clear()
        self.verticalLayout.removeWidget(self.save_btn)
        if self.save_btn is not None:
            self.save_btn.deleteLater()
            self.save_btn = None

        d = self.calendarWidget.selectedDate().getDate()
        self.d = dt.datetime(year=d[0], month=d[1], day=d[2]).date()
        sql = """SELECT time, time_end, date_end FROM Activity
        WHERE date = ?"""
        cur = self.con.cursor()
        items = cur.execute(sql, (self.d,)).fetchall()
        self.sum_time = dt.timedelta()
        for item in items:
            timedelt = self.find_delta(item)
            self.sum_time += timedelt
            if timedelt.days == 0:
                self.listWidget.addItem(' - '.join(item[:2]) + '; Длительность сессии: ' + str(timedelt))
        self.listWidget.addItem('Всего за день: ' + str(self.sum_time))

        math_count = self.arithmetic_count()
        self.listWidget.addItem('Кол-во решенных примеров: ' + str(math_count))

        self.change_label()
        self.show_notes()

    def change_label(self):
        f = open(FUNNY_TEXTS, 'rt', encoding='utf-8')

        data = f.readlines()
        text = random.choice(data)
        text = text.split(' ')
        result = '\n'.join([' '.join(text[i:min(i + 6, len(text))]) for i in range(0, len(text), 6)])
        self.label.setText(result)

    def show_notes(self):
        con = sqlite3.connect(NOTES_DB)
        cur = con.cursor()
        sql = """SELECT text, id FROM Notes
        WHERE date = ?"""
        notes = cur.execute(sql, (self.d,)).fetchall()

        def clearLayout(layout):
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        clearLayout(self.verticalLayout_2)
        self.TextEditGroup = []
        for text, Id in notes:
            lineEdit = QTextEdit(text)
            lineEdit.setStyleSheet("background-color: rgb(255, 255, 127);")

            self.TextEditGroup.append([lineEdit, Id])
            self.verticalLayout_2.addWidget(lineEdit)
        for el in self.TextEditGroup:
            el[0].textChanged.connect(self.add_save_btn)

    def add_save_btn(self):
        if self.save_btn is None:
            self.save_btn = QPushButton('Сохранить изменения')
            self.verticalLayout.addWidget(self.save_btn)
            self.save_btn.clicked.connect(self.save_note_changed)

    def save_note_changed(self):
        cur = self.con.cursor()
        sql_update = """UPDATE Notes SET text = ?
        WHERE id = ?"""
        sql_delete = """DELETE FROM Notes
        WHERE id = ?"""
        for text_edit, Id in self.TextEditGroup:
            if text_edit.toPlainText().strip() == '':
                request = cur.execute(sql_delete, (Id,))
            else:
                request = cur.execute(sql_update, (text_edit.toPlainText(), Id))
        self.con.commit()

    def find_delta(self, item):
        t1 = dt.time.fromisoformat(item[0])
        t2 = dt.time.fromisoformat(item[1])
        dt1 = dt.datetime.combine(self.d, t1)
        d2 = dt.date.fromisoformat(item[2])
        dt2 = dt.datetime.combine(d2, t2)
        return dt2 - dt1

    def arithmetic_count(self):
        con = sqlite3.connect(ARITHMETIC_DB)
        cur = con.cursor()
        sql = """SELECT count FROM Arithmetic
        WHERE date = ?"""
        count = cur.execute(sql, (self.d,)).fetchall()
        count = [elem[0] for elem in count]
        return sum(count)


class Statistic:
    def __init__(self):
        now = dt.datetime.today()
        self.start_dt = dt.datetime(now.year, now.month, now.day, now.hour, now.minute)

    def end(self):
        now = dt.datetime.today()
        self.end_dt = dt.datetime(now.year, now.month, now.day, now.hour, now.minute)

        con = sqlite3.connect(STATISTIC_DB)
        cur = con.cursor()

        if self.start_dt + dt.timedelta(minutes=1) <= self.end_dt:
            sql = """INSERT INTO Activity(date, time, date_end, time_end)
            VALUES (?, ?, ?, ?)"""

            cur.execute(sql, (self.start_dt.date(), self.start_dt.strftime("%H:%M"),
                              self.end_dt.date(), self.end_dt.strftime("%H:%M")))
            con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StatisticWidget()
    ex.show()
    sys.exit(app.exec())

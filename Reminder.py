import sys

from PyQt5 import QtMultimedia, QtCore, QtGui
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QWidget, QApplication

from ReminderWidget_form import Ui_Reminder
import sqlite3
import datetime as dt

from CONST import REMINDER_DB


class Reminders:
    def __init__(self):
        self.remind_list = []
        self.con = sqlite3.connect(REMINDER_DB)
        cur = self.con.cursor()

        sql = """SELECT * FROM Reminders
        WHERE time BETWEEN ? AND ?"""
        self.today = dt.datetime.today().date()
        d2 = self.today + + dt.timedelta(days=1)
        self.data = cur.execute(sql, (self.today, d2)).fetchall()
        self.data = [[dt.datetime.fromisoformat(e[1]), e[2]] for e in self.data]  # [ dt.datetime | text ]

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.tick)
        self.ex = []

    def add_reminder(self, m, text):
        d = dt.datetime.today() + dt.timedelta(minutes=m)
        end_d = dt.datetime(d.year, d.month, d.day, d.hour, d.minute)
        if d.date() == self.today:
            self.data.append([end_d, text])

        sql = """INSERT INTO Reminders(time, text)
        VALUES(?, ?)"""
        cur = self.con.cursor()
        end_d = dt.datetime(d.year, d.month, d.day, d.hour, d.minute)
        cur.execute(sql, (end_d, text))
        self.con.commit()

    def call_reminder(self, text):
        ex = ReminderWidget(text)
        self.ex.append(ex)
        self.ex[-1].show()

    def tick(self):
        d = dt.datetime.today()
        new_data = self.data[:]
        for elem in self.data:
            if d >= elem[0]:
                self.call_reminder(elem[1] + ' - ' + elem[0].strftime("%d-%m-%Y %H:%M"))
                self.del_reminder(elem[0], elem[1])
                new_data.remove(elem)
        self.data = new_data

        self.timer.start(1000 * 60)

    def del_reminder(self, date, text):
        cur = self.con.cursor()
        sql = """DELETE from Reminders
        WHERE time = ? AND text = ?"""
        cur.execute(sql, (date, text))
        self.con.commit()


class ReminderWidget(QWidget, Ui_Reminder):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Pi_.ico'))
        self.setStyleSheet("background-color: #ffc0cb;")
        self.textEdit.setText(args[0])
        self.setWindowState(Qt.WindowActive)
        self.play_sound('Reminder_sound.mp3')

    def play_sound(self, filename):
        player = QtMultimedia.QMediaPlayer()

        def handle_state_changed(state):
            if state == QtMultimedia.QMediaPlayer.StoppedState:
                player.stop()

        player.stateChanged.connect(handle_state_changed)

        url = QtCore.QUrl.fromLocalFile(filename)
        player.setMedia(QtMultimedia.QMediaContent(url))
        player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReminderWidget('blablabla')
    ex.show()
    sys.exit(app.exec())

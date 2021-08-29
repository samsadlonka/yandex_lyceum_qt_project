import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from MathWidget import ArithmeticWidget
from EyetTimerWidget import EyeTimerWidget
from NoteWidget import NoteWidget
from Reminder import ReminderWidget, Reminders
from Statistic import Statistic, StatisticWidget

from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QStyle, QAction, QMenu, qApp, \
    QSystemTrayIcon, QMessageBox

from MainWindow_form import Ui_MainWindow

NOTES_DB = 'MainDB.db'
STATISTIC_DB = "MainDB.db"
REMINDER_DB = 'MainDB.db'
ARITHMETIC_DB = "MainDB.db"

FUNNY_TEXTS = 'motivation.txt'  # Файл текст;кол-во часов, которое необходимо, чтобы показать это сообщение(число)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Pi_.ico'))
        self.tray_work()

        self.remainder = Reminders()
        self.statistic = Statistic()

        self.btn_eye_timer.clicked.connect(self.start_eye_timer)

        self.btn_reminder.clicked.connect(self.btn_reminder_handler)

        self.btn_pc_timer.clicked.connect(self.btn_pc_timer_handler)

        self.btn_note.clicked.connect(self.btn_note_handler)

        self.btn_arithmetic.clicked.connect(self.btn_arithmetic_handler)

    def closeEvent(self, a0):
        self.statistic.end()

    def tray_work(self):
        # Инициализируем QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))

        '''
            Объявим и добавим действия для работы с иконкой системного трея
            show - показать окно
            hide - скрыть окно
            exit - выход из программы
        '''
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def start_eye_timer(self):
        minutes = QInputDialog.getInt(self, 'Время', 'Через сколько минут будет приходить оповещение?',
                                      30, 5, 60, 1)
        if minutes[1]:
            self.eye_timer_widget = EyeTimerWidget(self, minutes[0])
            self.eye_timer_widget.show()

    def btn_reminder_handler(self):
        minutes = QInputDialog.getInt(self, 'Время', 'Через сколько минут нужно напомнить?',
                                      10, 1, 9999999, 1)
        if minutes[1]:
            text = QInputDialog.getText(self, 'Текст', 'Что напомнить?')
            if text[1]:
                self.remainder.add_reminder(minutes[0], text[0])
                ok = QMessageBox.question(self, 'Напоминание', 'Напоминание успешно добавлена!', QMessageBox.Yes)

    def btn_pc_timer_handler(self):
        self.statistic_widget = StatisticWidget()
        self.statistic_widget.show()

    def btn_note_handler(self):
        self.note_widget = NoteWidget()
        self.note_widget.show()

    def btn_arithmetic_handler(self):
        out = QInputDialog.getInt(self, 'Быстрый счет', 'Какое кол-во задач вы хотите решить?',
                                  10, 1, 100, 1)
        if out[1]:
            self.arithmetic_widjet = ArithmeticWidget(out[0])
            self.arithmetic_widjet.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

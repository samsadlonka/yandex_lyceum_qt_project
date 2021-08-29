from PyQt5 import QtMultimedia, QtCore, QtGui
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QWidget, QInputDialog, QMenu, qApp, QAction, QSystemTrayIcon, QStyle

from EyeTimerWidget_form import Ui_EyeTimerForm

import datetime as dt

'''Этот класс очень опасный!
В нём ужасный и непонятный код
Таймеры испоьзуют свои потоки, и всё плохо...
Однозначно стоит переписать!
Но с горем пополам это всё работает...'''


class EyeTimerWidget(QWidget, Ui_EyeTimerForm):
    def __init__(self, *args):
        super().__init__()
        self.main_window = args[0]
        self.minutes = args[1]
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Pi_.ico'))


        self.tray_init()

        self.time = dt.datetime(1, 1, 1, 0, self.minutes, 0)

        self.relax_timer = QTimer()
        self.relax_timer.timeout.connect(self.change_text)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.tick)

        self.pushButton.clicked.connect(self.to_tray)

    def closeEvent(self, a0):  # так работает но, возможно, лучше сделать по-другому
        self.timer.killTimer(self.timer.timerId())
        self.relax_timer.killTimer(self.relax_timer.timerId())
        self.hide()
        self.tray_icon.hide()

    def tick(self):
        self.timer.start(1000)
        # work with time
        self.time -= dt.timedelta(seconds=1)
        # update label time
        self.label.setText(self.time.strftime('%M:%S'))

        if self.time.time() == dt.time(0, 0, 0):
            self.show()
            self.setWindowState(Qt.WindowActive)
            self.reload_timer()

    def reload_timer(self):
        self.timer.stop()
        self.do_relax()

    def do_relax(self):
        self.relax_text = ['1. Быстро-быстро моргайте в течение 30 секунд.',
                           '2. Крепко зажмурьте глаза на 3 секунды,\nзатем откройте на то же время.',
                           '3. Двигайте глазными яблоками в разных направлениях:\nслева-направо, справа-налево,\n'
                           ' по кругу по часовой стрелке и против.',
                           '4. Бережно помассируйте глаза через \nзакрытые веки подушечками пальцев',
                           '5. Посмотрите на ближайший объект, \nзатем на дальний. Чередуйте 10–15 раз.']

        self.label.setText('Пора отдохнуть!\n\n\n')

        self.label.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.setStyleSheet('background-color: #90EE90;')


        self.relax_timer.start(1000 * 1)

        self.i = 0

    def change_text(self):
        if self.i == 5:
            self.label.setText('00:00')
            self.label.setStyleSheet('font: 100pt "Tahoma";')
            self.setStyleSheet('background-color: white;')

            self.relax_timer.stop()
            self.relax_timer.killTimer(self.relax_timer.timerId())
            self.time = dt.datetime(1, 1, 1, 0, self.minutes, 0)

            self.timer.start(1000)
            return

        self.play_sound('Eye_sound.mp3')
        self.label.setText('Пора отдохнуть!\n\n\n' + self.relax_text[self.i])
        self.i += 1
        self.relax_timer.start(1000 * 30)

    def tray_init(self):
        # Инициализируем QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_TrashIcon))

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
        quit_action.triggered.connect(self.close)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def to_tray(self):
        self.hide()

    def play_sound(self, filename):
        player = QtMultimedia.QMediaPlayer()

        def handle_state_changed(state):
            if state == QtMultimedia.QMediaPlayer.StoppedState:
                player.stop()

        player.stateChanged.connect(handle_state_changed)

        url = QtCore.QUrl.fromLocalFile(filename)
        player.setMedia(QtMultimedia.QMediaContent(url))
        player.play()

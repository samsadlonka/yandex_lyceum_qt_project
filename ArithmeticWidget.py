import random
import sqlite3
import sys
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from ArithmeticWidget_form import Ui_ArithmeticWidget

ARITHMETIC_DB = "StatisticDB.db"


class ArithmeticWidget(QWidget, Ui_ArithmeticWidget):
    def __init__(self, n):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.setFocus()
        self.n = n
        self.correct_ans = 0
        self.start = datetime.today()
        self.new_task()

        self.lineEdit.returnPressed.connect(self.check_ans)

    def closeEvent(self, event):
        con = sqlite3.connect(ARITHMETIC_DB)
        cur = con.cursor()
        cur.execute("INSERT INTO Arithmetic(date, count) VALUES(?, ?)", (self.start.date(), self.correct_ans))
        con.commit()

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Enter:
    def check_ans(self):
        try:
            user_ans = int(self.lineEdit.text())
            ans = eval(self.main_label.text())
            if user_ans == ans:
                self.label_ans.setText('Правильно!')
                self.correct_ans += 1
                self.progressBar.setValue(int(self.correct_ans / self.n * 100))
            else:
                self.label_ans.setText('Неправильно\nПравильный ответ: ' + str(ans))

            if self.progressBar.value() != 100:
                self.new_task()
            else:
                ok = QMessageBox.question(self, '', 'Вы молодец!\nВаше время(сек): '
                                          + str((datetime.today() - self.start).total_seconds()), QMessageBox.Yes)
                self.close()

        except ValueError:
            self.label_ans.setText('В ответе должно быть целое число')

    def new_task(self):
        n1 = random.randint(1, 99)
        n2 = random.randint(1, 99)
        if n2 > n1:
            n1, n2 = n2, n1
        if self.comboBox.currentText() == '*':
            if random.random() > 0.5:
                n2 = random.randint(2, 10)
            else:
                n1 = random.randint(2, 10)
        self.main_label.setText(str(n1) + ' ' + self.comboBox.currentText() + ' ' + str(n2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FastArithmeticWidget(3)
    ex.show()
    sys.exit(app.exec())

import sys  # sys нужен для передачи argv в QApplication
import random
import time
from typing import List, Any

from PyQt6 import QtWidgets, QtGui

import design  # Это наш конвертированный файл дизайна

n = 1
list_1 = ["играют в баскетбол", "читают книги", "путешествуют на поезде"]
list_2 = ["готовят завтрак", "сажают картошку на марсе", "смотрят на закат"]
list_3 = ["строят лунопарк на луне", "отдыхают на море", "делают снеговиков"]
curI = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    global curI

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()
        self.setStyleSheet('.QWidget {background-image: url(pic/bg.png);}')
        self.progressBar.setValue(0)

    def initUI(self):

        self.listWidget.itemClicked.connect(self.clicked1)
        self.pushButton.clicked.connect(self.clicked2)

    def clicked1(self):
        current_item_1 = int(self.listWidget.currentRow()) + 1
        self.listWidget_2.clear()
        if current_item_1 == 1:
            for s in list_1:
                self.listWidget_2.addItem(s)
        if current_item_1 == 2:
            for s in list_2:
                self.listWidget_2.addItem(s)
        if current_item_1 == 3:
            for s in list_3:
                self.listWidget_2.addItem(s)

    def clicked2(self):
        current_item_3 = int(self.listWidget_3.currentRow())
        current_item_2 = int(self.listWidget_2.currentRow())
        current_item_1 = int(self.listWidget.currentRow())

        print(current_item_1, current_item_2, current_item_3)
        count = curI[current_item_1][current_item_2][current_item_1]
        print(count)
        s = "pic/" + str(current_item_1) + "/" + str(current_item_2) + "/" + str(current_item_3) + "/" + str(
            count) + ".png"
        pixmap = QtGui.QPixmap(s)
        self.listWidget.setEnabled(False)
        self.listWidget_2.setEnabled(False)
        self.listWidget_3.setEnabled(False)
        self.pushButton.setEnabled(False)
        i = 0
        while i < 100:
            t = random.randint(0, 1)
            i += t
            self.progressBar.setValue(i)
            time.sleep(round(random.uniform(0.01, 0.07), 3))
        self.pic.clear()
        self.pic.setPixmap(pixmap)
        self.progressBar.setValue(100)
        self.listWidget.setEnabled(True)
        self.listWidget_2.setEnabled(True)
        self.listWidget_3.setEnabled(True)
        self.pushButton.setEnabled(True)

        count += 1
        print(curI[current_item_1][current_item_2][current_item_3])
        if count == 6:
            count = 0
        curI[current_item_1][current_item_2][current_item_3] = count


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

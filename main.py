import sys  # sys нужен для передачи argv в QApplication
import random
import time
from typing import List, Any

from PyQt6 import QtWidgets, QtGui, QtCore

import design  # Это наш конвертированный файл дизайна

curI = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
list_0 = ["играют в баскетбол", "читают книги", "путешествуют на поезде"]
list_1 = ["готовят завтрак", "сажают картошку на марсе", "смотрят на закат"]
list_2 = ["строят лунопарк на луне", "отдыхают на море", "делают снеговиков"]
current_item_1 = 0
current_item_2 = 0
current_item_3 = 0
buttonPressedStyle = "background-color: rgb(180, 209, 255);\n border-radius: 20px;"
buttonUnpressedStyle = "background-color: rgb(240, 220, 238);\n border-radius: 20px;"


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    global curI
    global current_item_1
    global current_item_2
    global current_item_3
    global buttonPressedStyle
    global buttonUnpressedStyle

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()
        self.setStyleSheet('.QWidget {background-image: url(pic/bg.png);}')
        self.progressBar.setValue(0)

    def initUI(self):
        self.pushButton.clicked.connect(self.generate)
        self.actionButton_0.clicked.connect(self.actionButtonPressed_0)
        self.actionButton_1.clicked.connect(self.actionButtonPressed_1)
        self.actionButton_2.clicked.connect(self.actionButtonPressed_2)
        self.styleButton_0.clicked.connect(self.styleButtonPressed_0)
        self.styleButton_1.clicked.connect(self.styleButtonPressed_1)
        self.styleButton_2.clicked.connect(self.styleButtonPressed_2)
        self.themeButton_0.clicked.connect(self.themeButtonPressed_0)
        self.themeButton_1.clicked.connect(self.themeButtonPressed_1)
        self.themeButton_2.clicked.connect(self.themeButtonPressed_2)

    def themeButtonPressed_0(self):
        global current_item_1
        current_item_1 = 0
        _translate = QtCore.QCoreApplication.translate
        self.themeButton_0.setStyleSheet(buttonPressedStyle)
        self.themeButton_1.setStyleSheet(buttonUnpressedStyle)
        self.themeButton_2.setStyleSheet(buttonUnpressedStyle)
        self.actionButton_0.setText(_translate("MainWindow", list_0[0]))
        self.actionButton_1.setText(_translate("MainWindow", list_0[1]))
        self.actionButton_2.setText(_translate("MainWindow", list_0[2]))

    def themeButtonPressed_1(self):
        global current_item_1
        current_item_1 = 1
        _translate = QtCore.QCoreApplication.translate
        self.themeButton_1.setStyleSheet(buttonPressedStyle)
        self.themeButton_0.setStyleSheet(buttonUnpressedStyle)
        self.themeButton_2.setStyleSheet(buttonUnpressedStyle)
        self.actionButton_0.setText(_translate("MainWindow", list_1[0]))
        self.actionButton_1.setText(_translate("MainWindow", list_1[1]))
        self.actionButton_2.setText(_translate("MainWindow", list_1[2]))

    def themeButtonPressed_2(self):
        global current_item_1
        current_item_1 = 2
        _translate = QtCore.QCoreApplication.translate
        self.themeButton_2.setStyleSheet(buttonPressedStyle)
        self.themeButton_0.setStyleSheet(buttonUnpressedStyle)
        self.themeButton_1.setStyleSheet(buttonUnpressedStyle)
        self.actionButton_0.setText(_translate("MainWindow", list_2[0]))
        self.actionButton_1.setText(_translate("MainWindow", list_2[1]))
        self.actionButton_2.setText(_translate("MainWindow", list_2[2]))


    def actionButtonPressed_0(self):
        global current_item_2
        current_item_2 = 0
        self.actionButton_0.setStyleSheet(buttonPressedStyle)
        self.actionButton_1.setStyleSheet(buttonUnpressedStyle)
        self.actionButton_2.setStyleSheet(buttonUnpressedStyle)

    def actionButtonPressed_1(self):
        global current_item_2
        current_item_2 = 1
        self.actionButton_1.setStyleSheet(buttonPressedStyle)
        self.actionButton_0.setStyleSheet(buttonUnpressedStyle)
        self.actionButton_2.setStyleSheet(buttonUnpressedStyle)

    def actionButtonPressed_2(self):
        global current_item_2
        current_item_2 = 2
        self.actionButton_2.setStyleSheet(buttonPressedStyle)
        self.actionButton_0.setStyleSheet(buttonUnpressedStyle)
        self.actionButton_1.setStyleSheet(buttonUnpressedStyle)

    def styleButtonPressed_0(self):
        global current_item_3
        current_item_3 = 0
        self.styleButton_0.setStyleSheet(buttonPressedStyle)
        self.styleButton_1.setStyleSheet(buttonUnpressedStyle)
        self.styleButton_2.setStyleSheet(buttonUnpressedStyle)

    def styleButtonPressed_1(self):
        global current_item_3
        current_item_3 = 1
        self.styleButton_1.setStyleSheet(buttonPressedStyle)
        self.styleButton_0.setStyleSheet(buttonUnpressedStyle)
        self.styleButton_2.setStyleSheet(buttonUnpressedStyle)

    def styleButtonPressed_2(self):
        global current_item_3
        current_item_3 = 2
        self.styleButton_2.setStyleSheet(buttonPressedStyle)
        self.styleButton_0.setStyleSheet(buttonUnpressedStyle)
        self.styleButton_1.setStyleSheet(buttonUnpressedStyle)

    def generate(self):
        print(current_item_1, current_item_2, current_item_3)
        print(current_item_1, current_item_2, current_item_3)
        count = curI[current_item_1][current_item_2][current_item_3]
        print(count)
        s = "pic/" + str(current_item_1) + "/" + str(current_item_2) + "/" + str(current_item_3) + "/" + str(
            count) + ".png"
        pixmap = QtGui.QPixmap(s)
        self.actionButton_0.setEnabled(False)
        self.actionButton_1.setEnabled(False)
        self.actionButton_2.setEnabled(False)
        self.themeButton_0.setEnabled(False)
        self.themeButton_1.setEnabled(False)
        self.themeButton_2.setEnabled(False)
        self.styleButton_0.setEnabled(False)
        self.styleButton_1.setEnabled(False)
        self.styleButton_2.setEnabled(False)
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

        self.actionButton_0.setEnabled(True)
        self.actionButton_1.setEnabled(True)
        self.actionButton_2.setEnabled(True)
        self.themeButton_0.setEnabled(True)
        self.themeButton_1.setEnabled(True)
        self.themeButton_2.setEnabled(True)
        self.styleButton_0.setEnabled(True)
        self.styleButton_1.setEnabled(True)
        self.styleButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)

        count += 1
        print(curI[current_item_1][current_item_2][current_item_3])
        if count == 6:
            count = 0
        curI[current_item_1][current_item_2][current_item_3] = count


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.showFullScreen()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

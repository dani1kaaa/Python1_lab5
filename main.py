#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        self.plainTextEdit.clear()
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                   "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.readlines()
            self.plainTextEdit.appendPlainText("Полученные данные: ")
            # выводим считанные данные на экран
            for lines in data:
                self.plainTextEdit.appendPlainText(lines.strip('\n'))

            global list_of_numbers
            list_of_numbers = []

            for lines in data:
                lineSplit = lines.split()
                list_of_numbers.append(lineSplit)

    def process_data(self):
        if validation_of_data():
            proverka = finder()

            # -*- выполнение задания -*-
            if proverka == True:
                doubling()

                self.plainTextEdit.appendPlainText(
                    "Данные обработаны! " + '\n')

                # выводим список на экран
                for lists in list_of_numbers:
                    for i in lists:
                        new_str = "{:6}".format(str(i))
                        self.plainTextEdit.insertPlainText(new_str)
                        # чтобы текст был в виде таблицы, делаем отступ после
                        # 6 элемента

                    self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    "Максимум не в последней строке таблицы! \n")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранным нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:6}".format(str(i))
                    file.write(new_str)
                file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText(
                "Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def finder():
    """
    находим максимум в списке
    :return: итог проверки
    """
    max = 0
    maxi = 0
    proverka = False

    for lists in list_of_numbers:
        for i in lists:
            if int(i) >= max:
                max = int(i)
                maxi = list_of_numbers.index(lists)
    if maxi == 5:
        proverka = True
    return proverka


def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    lenth_list = 0
    for lists in list_of_numbers:
        lenth_list += len(lists)
    if lenth_list == 30:
        for lists in list_of_numbers:
            for i in lists:
                try:
                    int(i)
                except Exception:
                    return False
        return True
    else:
        return False

def doubling():
    """
    удвоение первого столбца
    :return: pass
    """
    for lists in list_of_numbers:
        zn = int(lists[0])
        zn *= 2
        lists[0] = str(zn)
    pass


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

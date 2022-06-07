# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfacemc2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate,QDateTime,QTime
from datetime import date


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 189, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 40, 189, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 10, 189, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 430, 189, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 430, 189, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 10, 200, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 40, 104, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 40, 104, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 420, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(630, 460, 113, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 70, 741, 331))
        self.tableView.setColumnWidth(1, 100)
        self.tableView.setColumnWidth(2, 200)
        self.tableView.setColumnWidth(3, 100)
        self.tableView.setColumnWidth(4, 120)
        self.tableView.setObjectName("tableView")
        # self.tableView.setStyleSheet("border-color: #ffffff;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 400, 401, 21))
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(650, 40, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 10, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(10, 460, 189, 32))
        current_date = date.today()
        self.dateEdit.setDate(current_date)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(200, 0, 20, 71))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(430, 0, 20, 71))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(450, 40, 189, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 460, 171, 32))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MoneyControl"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить покупку"))
        self.pushButton_8.setText(_translate("MainWindow", "Показать все расходы"))
        self.pushButton_4.setText(_translate("MainWindow", "Показать по категории"))
        self.pushButton_5.setText(_translate("MainWindow", "Удалить запись №"))
        self.pushButton_9.setText(_translate("MainWindow", "Показать по дате"))
        self.pushButton_10.setText(_translate("MainWindow", "Сортировать"))
        self.comboBox.setItemText(0, _translate("MainWindow", "По дате"))
        self.comboBox.setItemText(1, _translate("MainWindow", "По стоимости"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Min->Max"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Max->Min"))
        self.pushButton_11.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_7.setText(_translate("MainWindow", "Импорт"))
        self.pushButton_2.setText(_translate("MainWindow", "Экспорт"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-mm-dd"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Еда"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Развлечения"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Дом"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Инвестиции"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Авто"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Работа"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Другое"))

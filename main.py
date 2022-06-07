from PyQt5 import QtWidgets, QtSql, QtCore, QtGui
from designmc2 import Ui_MainWindow
import sys
import sqlite3 as sq
import pandas as pd
import csv


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(QtWidgets.qApp.quit)
        self.ui.pushButton_2.clicked.connect(self.save_file)
        self.ui.pushButton_4.clicked.connect(self.show_by_category)
        self.ui.pushButton_5.clicked.connect(self.delrecord)
        self.ui.pushButton_6.clicked.connect(self.addrecord)
        self.ui.pushButton_7.clicked.connect(self.import_from_csv)
        self.ui.pushButton_8.clicked.connect(self.show_all)
        self.ui.pushButton_9.clicked.connect(self.show_by_date)
        self.ui.pushButton_10.clicked.connect(self.sort_expanses)

    def show_all(self):
        tv = self.ui.tableView
        tv.setModel(stm)
        self.ui.tableView.setModel(stm)
        tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))
        con1.open()
        stm.setTable('expenses')
        stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
        stm.select()
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Категория')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Стоимость')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Дата\n yyyy-mm-dd')
        count = stm.rowCount()
        con1.close()
        self.ui.label.setText('<font color=green>Успешно! Отображено {} записей</font>'.format(count))

    def addrecord(self):
        tv = self.ui.tableView
        tv.setModel(stm)
        tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))
        con1.open()
        stm.setTable('expenses')
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Категория')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Стоимость')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Дата\n yyyy-mm-dd')
        stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
        stm.select()
        stm.insertRow(stm.rowCount())
        self.ui.label.setText('<font color=green>Запись успешно добавлена!</font>')

    def delrecord(self):
        tv = self.ui.tableView
        tv.setModel(stm)
        tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))
        con1.open()
        stm.setTable('expenses')
        stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
        stm.select()
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Категория')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Стоимость')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Дата\n yyyy-mm-dd')
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(0, 10000, parent=window))
        count = str(stm.rowCount())
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-{}]".format(count)), parent=window)
        self.ui.lineEdit.setValidator(validator)
        id = int(self.ui.lineEdit.text())
        stm.removeRow(id - 1)
        self.ui.label.setText('<font color=green>Запись успешно удалена!</font>')

    def sort_expanses(self):
        combobox_1 = self.ui.comboBox.currentText()
        combobox_2 = self.ui.comboBox_2.currentText()
        tv = self.ui.tableView
        tv.setModel(stm)
        tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))
        con1.open()
        stm.setTable('expenses')
        stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Категория')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Стоимость')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Дата\n yyyy-mm-dd')
        if combobox_1 == "По дате" and combobox_2 == "Min->Max":
            stm.setSort(3, QtCore.Qt.AscendingOrder)
            self.ui.label.setText('<font color=green>Успешно!</font>')
        elif combobox_1 == "По дате" and combobox_2 == "Max->Min":
            stm.setSort(3, QtCore.Qt.DescendingOrder)
            self.ui.label.setText('<font color=green>Успешно!</font>')
        elif combobox_1 == "По стоимости" and combobox_2 == "Min->Max":
            stm.setSort(2, QtCore.Qt.AscendingOrder)
            self.ui.label.setText('<font color=green>Успешно!</font>')
        elif combobox_1 == "По стоимости" and combobox_2 == "Max->Min":
            stm.setSort(2, QtCore.Qt.DescendingOrder)
            self.ui.label.setText('<font color=green>Успешно!</font>')
        stm.select()
        con1.close()

    def show_by_date(self):
        dataedit3 = self.ui.dateEdit.date().toString('yyyy-MM-dd')
        tv = self.ui.tableView
        tv.setModel(stm)
        tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))
        con1.open()
        stm.setTable('expenses')
        stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
        datafilter = "data = '{}'".format(dataedit3)
        stm.setFilter(datafilter)
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Категория')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Стоимость')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Дата\n yyyy-mm-dd')
        stm.select()
        count = stm.rowCount()
        con1.close()
        self.ui.label.setText('<font color=green>Успешно! Отображено {} записей</font>'.format(count))

    def show_by_category(self):
        categ = self.ui.comboBox_3.currentIndex()
        tv = self.ui.tableView
        tv.setModel(stm)
        tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))
        con1.open()
        stm.setTable('expenses')
        stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
        categoryfilter = "category = '{}'".format(categ + 1)
        stm.setFilter(categoryfilter)
        stm.setSort(3, QtCore.Qt.AscendingOrder)
        stm.select()
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Категория')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Стоимость')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Дата\n yyyy-mm-dd')
        count = stm.rowCount()
        con1.close()
        self.ui.label.setText('<font color=green>Успешно! Отображено {} записей</font>'.format(count))

    def import_from_csv(self):
        file = QtWidgets.QFileDialog.getOpenFileName(parent=window, caption="Выбор файла", directory="c:\\python36",
                                                     filter="csv format (*.csv)",
                                                     initialFilter="csv format (*.csv)")
        filename = file[0]
        if filename != "":
            with open(filename, 'r') as fin:
                dr = csv.DictReader(fin)
                to_db = [(i['id_exp'], i['category'], i['name'], i['cost'], i['data']) for i in dr]
                cur.executemany(
                    "INSERT OR IGNORE INTO expenses (id_exp,category, name, cost, data) VALUES (?, ?, ?, ?, ?);", to_db)
                con.commit()
                self.ui.label.setText('<font color=green>Файл успешно загружен!</font>')
        else:
            self.ui.label.setText('<font color=red>Вы ничего не выбрали!</font>')

    def save_file(self):

        f = QtWidgets.QFileDialog.getSaveFileName(parent=window, caption="Выбор папки",
                                                  directory=QtCore.QDir.currentPath(),
                                                  filter="CSV Format (*.csv)")
        file = f[0]
        if file != "":
            df = pd.read_sql("SELECT * FROM expenses", con)
            df.to_csv(file)
            self.ui.label.setText('<font color=green>Файл успешно выгружен!</font>')
        else:
            self.ui.label.setText('<font color=red>Вы ничего не выбрали!</font>')


with sq.connect("money.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS categoryname (
                    id_cat INTEGER PRIMARY KEY ,
                    category_name VARCHAR NOT NULL )
                    """)
    records = [(1, "Еда"), (2, "Развлечения"), (3, "Дом"), (4, "Инвестиции"), (5, "Авто"), (6, "Работа"), (7, "Другое")]
    cur.executemany("INSERT OR IGNORE INTO categoryname (id_cat,category_name) VALUES (?,?)", records)

    cur.execute("""CREATE TABLE IF NOT EXISTS expenses (
            category INTEGER NOT NULL,
            name VARCHAR NOT NULL,
            cost INT NOT NULL,
            data DATA NOT NULL,
            FOREIGN KEY (category) REFERENCES categoryname (id))
            """)
    con.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    obj = MainWindow()
    con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    con1.setDatabaseName('money.db')
    con1.open()
    stm = QtSql.QSqlRelationalTableModel(parent=window)
    stm.setRelation(0, QtSql.QSqlRelation('categoryname', 'id_cat', 'category_name'))
    con1.close()
    window.show()
    sys.exit(app.exec_())

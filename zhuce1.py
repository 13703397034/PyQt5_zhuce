# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import zhuce1
from PyQt5.QtWidgets  import QApplication,QMainWindow,QTableView, QHeaderView, QFormLayout,   QVBoxLayout,QWidget,QHBoxLayout, QPushButton,QGridLayout,QLabel
#修复高分辨率导致的显示不一致问题
import caozuo
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(50, 270, 850, 192))
        self.tableView_2.setObjectName("tableView_2")
        self.model = QStandardItemModel(45,6)#设置table_view 的行，列数
        self.tableView_2.setModel(self.model)#初始化表格
        self.tableView_2.setColumnWidth(3, 300)#设置第三列宽度为300
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 140, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 180, 491, 30))
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 90, 341, 40))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(240, 240, 494, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.caozuo = caozuo.ChuLi()
        self.pushButton.clicked.connect(self.get_linetext)
        self.pushButton_2.clicked.connect(self.serch_two)
        self.cmboBox_list()


    def cmboBox_list(self):
        for i in self.caozuo.set_list('xuebu'):
            self.comboBox_4.addItem(i)
        self.comboBox_4.currentIndexChanged.connect(self.selectionchange)
        for j in self.caozuo.set_list('zy'):
            self.comboBox_3.addItem(j)
        self.comboBox_3.currentIndexChanged.connect(self.selectionchange)
        for k in self.caozuo.set_list('bj'):
            self.comboBox_2.addItem(k)
        self.comboBox_2.currentIndexChanged.connect(self.selectionchange)
        for m in self.caozuo.set_list('zt'):
            self.comboBox.addItem(m)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "新生入学注册系统"))
        self.label_2.setText(_translate("MainWindow", " "))
        self.label_8.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "身份证号"))
        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.pushButton_2.setText(_translate("MainWindow", "查询"))
        self.label_7.setText(_translate("MainWindow", "学   部"))
        self.label_3.setText(_translate("MainWindow", "专   业"))
        self.label_4.setText(_translate("MainWindow", "班    级"))
        self.label_5.setText(_translate("MainWindow", "是否注册"))
        self.pushButton_3.setText(_translate("MainWindow", "查询"))
        #设置table_view的列标题
        self.model.setHorizontalHeaderLabels(['学号', '姓名', '学部', '专业','班级','是否注册'])


    def get_linetext(self):
        self.str1 = self.lineEdit.text()
        if  self.caozuo.panduan(self.str1):
            self.caozuo.zhuce(self.str1)
            self.label_2.setText("注册成功")
        else:
            self.label_2.setText("输入错误")

    def serch_two (self):
        self.str1 =self.lineEdit.text()
        if self.caozuo.panduan(self.str1):
            self.result=self.caozuo.serch_table(self.str1)
            #table_view表格中赋值
            for column in range(6):
                self.i=QStandardItem(self.result[column])
                self.model.setItem(0,column,self.i)
        else:
            self.label_8.setText("输入错误,请重新输入")

    def serch_one(self):
        self.str1 = self.lineEdit.text()
        if  self.caozuo.panduan(self.str1):
            self.text = self.caozuo.serch_one(self.str1)
            self.label_8.setText(self.text)
            print(self.text)
        else:
            self.label_8.setText("输入错误,请重新输入")

    def selectionchange(self):
        val4 = self.comboBox_4.currentText()
        val3 = self.comboBox_3.currentText()
        val2 = self.comboBox_2.currentText()
        val = self.comboBox.currentText()
        print(val,val2,val3,val4)








if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = zhuce1.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
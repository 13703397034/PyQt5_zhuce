import sys
import  zhuce1
from PyQt5.QtWidgets  import QApplication,QMainWindow
#修复高分辨率导致的显示不一致问题
from PyQt5 import QtCore
import linkmysql

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = zhuce1.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    #mysql = linkmysql.MysqlHelp()
    #sql = 'select * from new_students'
    #result = mysql.serch(sql)
    #print(result)
    mainWindow.show()
    sys.exit(app.exec_())
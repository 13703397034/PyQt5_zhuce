import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication
from PyQt5.QtGui import  QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        #继承父类FirstMainWin()
        super(FirstMainWin,self).__init__()
        #设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        #设置主窗口的尺寸
        self.resize(1000,800)
        #获得当前下面的状态栏（不是必须的）
        self.status =self.statusBar()
        self.status.showMessage('只存在五秒的时间',5000)

if __name__=='__main__':
    app =QApplication(sys.argv)
    #制作图标（不是必须的）
    app.setWindowIcon(QIcon(r'C:\Users\guanlibu\Desktop\bitbug_favicon.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())

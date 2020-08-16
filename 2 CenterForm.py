#让主窗口居中
# 使用QDesktopWidget类
import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import  QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        #继承父类FirstMainWin()
        super(CenterForm,self).__init__()
        #设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        #设置主窗口的尺寸
        self.resize(1000,800)
        #获得当前下面的状态栏（不是必须的）
        self.status =self.statusBar()
        self.status.showMessage('只存在五秒的时间',5000)

#让窗口居中
    def center(self):
        #获取屏幕坐标系
        screen= QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size =self.geometry()
        #左右坐标取中
        newLeft =(screen.width()-size.width())/2
        #上下坐标取中
        newTop =(screen.height()-size.height())/2
        #移动坐标到新的位置
        self.move(newLeft,newTop)


if __name__=='__main__':
    app =QApplication(sys.argv)
    #制作图标（不是必须的）
    app.setWindowIcon(QIcon(r'C:\Users\guanlibu\Desktop\bitbug_favicon.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())


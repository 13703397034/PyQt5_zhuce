#通过按钮退出主程序
import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication,QDesktopWidget,QHBoxLayout,QPushButton,QWidget
from PyQt5.QtGui import  QIcon
class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(1000,800)
        self.setWindowTitle("通过按钮退出主程序")
        #添加button（按钮）
        self.button1 = QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(lambda :self.onClick_Button())
        #布局按钮
        layout =QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrom =QWidget()
        mainFrom.setLayout(layout)
        self.setCentralWidget(mainFrom)
        #按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        #通过sender获得button1
        sender = self.sender()
        #print(sender.text() +"按钮被按下")
        app = QApplication.instance()
        #退出应用程序
        app.quit()

if __name__=='__main__':
    app =QApplication(sys.argv)
    #制作图标（不是必须的）
    app.setWindowIcon(QIcon(r'C:\Users\guanlibu\Desktop\bitbug_favicon.ico'))
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
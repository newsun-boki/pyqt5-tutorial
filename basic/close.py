'''
Author: your name
Date: 2021-12-03 01:13:27
LastEditTime: 2021-12-03 01:13:53
LastEditors: newsun-HP-Pavilion-Gaming-Laptop-15-dk0xxx
Description: In User Settings Edit
FilePath: /pyqt5/close.py
'''

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication
# ##***关闭窗口***## #
class CloseW(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()

   def initUI(self):
       qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
       # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
       # 父组件是Example组件，它继承了QWiget类。
       qbtn.clicked.connect(QCoreApplication.instance().quit)
       qbtn.resize(qbtn.sizeHint())
       qbtn.move(500, 50)
       self.setGeometry(300, 100, 600, 600)
       self.setWindowTitle('excise')
       self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = CloseW()
   sys.exit(app.exec_())
'''
Author: newsun
Date: 2021-12-04 00:27:48
LastEditTime: 2021-12-04 00:37:13
LastEditors: newsun-HP-Pavilion-Gaming-Laptop-15-dk0xxx
Description: In User Settings Edit
FilePath: /pyqt5/event/signals.py
'''
#! /usr/bin/python3
# -*- coding: utg-8 -*-

"""
本样例中，我们把QSlider的一个信号连接到QLCDNumber的槽里面
"""

import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout,QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Signal & slot')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
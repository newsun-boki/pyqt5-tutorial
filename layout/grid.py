'''
Author: your name
Date: 2021-12-03 02:07:54
LastEditTime: 2021-12-03 02:17:09
LastEditors: newsun-HP-Pavilion-Gaming-Laptop-15-dk0xxx
Description: In User Settings Edit
FilePath: /pyqt5/layout/grid.py
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial 

In this example, we create a skeleton
of a calculator using a QGridLayout.

author: Jan Bodnar
website: py40.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        grid = QGridLayout()
        self.setLayout(grid)
 
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        
        positions = [(i,j) for i in range(5) for j in range(4)]
        
        for position, name in zip(positions, names):
            
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
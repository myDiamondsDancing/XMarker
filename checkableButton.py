import sys

from PyQt5.Qt import *

class CheckableButton(QPushButton):
    def __init__(self, text, parent=None):
        super(CheckableButton, self).__init__(parent)
        self.initUi()
        self.connectUi()
        self.repaint()
        
        self.setText(text)
        
    def initUi(self):
        self.setCheckable(True)

    def connectUi(self):
        self.toggled.connect(self.repaint)
        
    def repaint(self):
        if self.isChecked():
            self.setStyleSheet('background : aqua;')
        else:
            self.setStyleSheet('background : gray;')        
               
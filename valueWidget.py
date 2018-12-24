import sys

from PyQt5.Qt import *
from PyQt5.QtCore import *

class ValueWidget(QWidget):
    def __init__(self, parent=None):
        super(ValueWidget, self).__init__(parent)
        self.initUi()
        self.setTheme(2)
        self.setTooltips(0)
        
    def initUi(self):
        self.mainLayout = QHBoxLayout()
        
        self.legendEdit = QLineEdit()
        self.label = QLabel(':')
        self.valueBox = QDoubleSpinBox()
        
        self.deleteButton = QPushButton('Delete')
        self.deleteButton.setStyleSheet('background : red;')
        
        self.mainLayout.addWidget(self.legendEdit)
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.valueBox)
        self.mainLayout.addWidget(self.deleteButton)
        
        self.setLayout(self.mainLayout)
        
    def setTheme(self, theme):
        if theme == 0:
            self.setLightTheme()
        elif theme == 1:
            self.setGrayTheme()
        else:
            self.setDarkTheme()

    def setLightTheme(self):
        _translate = QCoreApplication.translate
        self.setStyleSheet('background : rgb(238, 238, 238;)')
        self.legendEdit.setStyleSheet('background : rgb(252, 252, 252);')
        self.valueBox.setStyleSheet('background : rgb(252, 252, 252);')

        self.label.setText(_translate("self", '<html></head><body><p align="center"><span style="font-weight:600; color:#000000">:</span></p></body></html>'))    

    def setGrayTheme(self):
        _translate = QCoreApplication.translate
        self.setStyleSheet('background : rgb(176, 176, 176);')
        self.legendEdit.setStyleSheet('background : rgb(232, 232, 232);')
        self.valueBox.setStyleSheet('background : rgb(232, 232, 232);') 

        self.label.setText(_translate("self", '<html></head><body><p align="center"><span style="font-weight:600; color:#000000">:</span></p></body></html>'))  

    def setDarkTheme(self):        
        _translate = QCoreApplication.translate
        self.setStyleSheet('background : rgb(103, 103, 103);')
        self.legendEdit.setStyleSheet('background : rgb(182, 182, 182);')
        self.valueBox.setStyleSheet('background : rgb(182, 182, 182);') 

        self.label.setText(_translate("self", '<html></head><body><p align="center"><span style="font-weight:600; color:#ececec">:</span></p></body></html>'))  

    def setTooltips(self, flag):
        if flag == 1:
            self.onTooltips()
        else:
            self.deleteTooltips()  

    def onTooltips(self):
        _translate = QCoreApplication.translate
        self.legendEdit.setToolTip(_translate("self", '<html></head><body><p align="center">Enter description</p></body></html>'))
        self.valueBox.setToolTip(_translate("self", '<html></head><body><p align="center">Enter value</p></body></html>'))    
        self.deleteButton.setToolTip(_translate("self", '<html></head><body><p align="center">Delete this element</p></body></html>'))

    def deleteTooltips(self):
        self.legendEdit.setToolTip('')
        self.valueBox.setToolTip('')    
        self.deleteButton.setToolTip('')    
        
    def returnResults(self):
        return (self.legendEdit.text(), self.valueBox.value())    

  
        








        
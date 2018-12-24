import sys

from PyQt5 import QtCore as QC
from PyQt5.Qt import *

from clickableLabel import ClickableLabel

class SymbolSettingsWidget(QWidget):
    def __init__(self, parent=None, name='', description='', mainWidget=None):
        super(SymbolSettingsWidget, self).__init__(parent)
        self.loadFields(name, description)
        self.initUi()
        self.connectUi()
        self.onToolTips()
        self.setTheme(self.theme)
        self.mainWidget = mainWidget
        
    def initUi(self):
        '''|private method
        |Inits user interface of widget'''
        self.mainLayout = QVBoxLayout()
        
        _translate = QC.QCoreApplication.translate       
        
        self.nameLabel = QLabel()
        self.helpLabel = QLabel()
        
        self.boldButton = QPushButton('B')
        self.boldButton.setCheckable(True)
        self.italicButton = QPushButton('I')
        self.italicButton.setCheckable(True)
        self.underlineButton = QPushButton('U')
        self.underlineButton.setCheckable(True)
        self.overlineButton = QPushButton('O')
        self.overlineButton.setCheckable(True)
        
        self.underlineColorButton = QPushButton('UC')
        
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(5)
        self.buttonsLayout.addWidget(self.boldButton)
        self.buttonsLayout.addWidget(self.italicButton)
        self.buttonsLayout.addWidget(self.underlineButton)
        self.buttonsLayout.addWidget(self.overlineButton)
        self.buttonsLayout.addWidget(self.underlineColorButton)
        
        self.fontBox = QFontComboBox()
        self.fontPointSizeBox = QSpinBox()
        self.fontPointSizeBox.setValue(12)
        
        self.fontLayout = QHBoxLayout()
        self.fontLayout.setSpacing(5)
        self.fontLayout.addWidget(self.helpLabel)
        self.fontLayout.addWidget(self.fontBox)
        self.fontLayout.addWidget(self.fontPointSizeBox)
        
        self.copyButton = QPushButton('Copy')
        self.insertButton = QPushButton('Insert')
        
        self.trash1 = QLabel()
        self.trash2 = QLabel()
        self.trash3 = QLabel()
        self.trash4 = QLabel()
        
        self.thirdRow = QHBoxLayout()
        self.thirdRow.addWidget(self.trash1)
        self.thirdRow.addWidget(self.trash4)
        self.thirdRow.addWidget(self.copyButton)
        self.thirdRow.addWidget(self.insertButton)
        self.thirdRow.addWidget(self.trash2)
        self.thirdRow.addWidget(self.trash3)
       
          
        self.firstRowLayout = QHBoxLayout()
        self.firstRowLayout.addWidget(self.nameLabel)
        self.firstRowLayout.addLayout(self.buttonsLayout)
        
        self.mainLayout.addLayout(self.firstRowLayout)
        self.mainLayout.addLayout(self.fontLayout)
        self.mainLayout.addLayout(self.thirdRow)
        
        self.setLayout(self.mainLayout)
        
        self.reserveField = QTextEdit(self.name)
        
    def connectUi(self):
        '''|private method
        |Connects all signals with methods'''
        self.underlineColorButton.clicked.connect(self.chooseUnderlineColor)    
        self.copyButton.clicked.connect(self.copy)
        self.insertButton.clicked.connect(self.insert)
        
        
    def loadFields(self, name, description):
        '''|private method
        |Loads local fields for class(theme: (0, 1, 2), name: str, description: str, color: str)'''
        self.theme = 0
        self.name = name 
        self.description = description 
        self.underlineColor = 'white'

    def setToolTip(self, flag):
        '''|public method
        |Turns off tool tips if flag is False, else turns on tool tips'''
        if flag is True:
            self.onToolTips()
        else:
            self.deleteToolTips()
            
    def chooseUnderlineColor(self):
        '''|private method
        |Chooses color for underline'''
        dialog = QColorDialog(self)
        dialog.setCurrentColor(QColor(self.underlineColor))
        if dialog.exec_():
            self.underlineColor = dialog.currentColor().name()
            self.underlineColorButton.setStyleSheet('background : {0}'.format(self.underlineColor))
        
            
    def setTheme(self, theme):
        '''|public method
        |Sets current theme for widget{0: Light, 1: Gray, 2: Dark}'''        
        if theme == 0:     
            self.setLightTheme()
        elif theme == 1:
            self.setGrayTheme()
        else:
            self.setDarkTheme()
        self.theme = theme

    def setLightTheme(self):
        '''|private method
        |Sets light theme for widget'''
        _translate = QC.QCoreApplication.translate
        self.setStyleSheet('background : rgb(238, 238, 238);')
        self.fontBox.setStyleSheet('background: rgb(252, 252, 252)')
        self.fontPointSizeBox.setStyleSheet('background: rgb(252, 252, 252)')
        self.helpLabel.setText(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 600; color:#000000">???</span></p></body></html>'))
        self.nameLabel.setText(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 600; color:#000000">{0}</span></p></body></html>'.format(self.name)))
    
    def setGrayTheme(self):
        '''|private method 
        |Sets gray theme for widget'''
        _translate = QC.QCoreApplication.translate
        self.setStyleSheet('background: rgb(176, 176, 176);')
        self.fontBox.setStyleSheet('background: rgb(232, 232, 232);')
        self.fontPointSizeBox.setStyleSheet('background: rgb(232, 232, 232);')
        self.helpLabel.setText(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 500; color:#000000">???</span></p></body></html>'))
        self.nameLabel.setText(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 600; color:#000000">{0}</span></p></body></html>'.format(self.name)))
        
    def setDarkTheme(self):
        '''|private method
        |Sets dark theme for widget'''
        _translate = QC.QCoreApplication.translate
        self.setStyleSheet('background: rgb(103, 103, 103);')
        self.fontBox.setStyleSheet('background: rgb(182, 182, 182)')        
        self.fontPointSizeBox.setStyleSheet('background: rgb(182, 182, 182)')
        self.helpLabel.setText(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 500; color:#ececec">???<span></p></body></html>'))
        self.nameLabel.setText(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 500; color:#ececec">{0}</span></p></body></html>'.format(self.name)))
     
    def setToolTips(self, flag):
        if flag is True:
            self.onToolTips()
        else:
            self.deleteToolTips()        
     
    def onToolTips(self):
        '''|private method
        |Turns on tool tips for widget'''
        self.boldButton.setToolTip('Check this to choose Bold')
        self.italicButton.setToolTip('Check this to choose Italic')
        self.underlineButton.setToolTip('Check this to choose Underline')
        self.overlineButton.setToolTip('Check this to choose Overline')      
        _translate = QC.QCoreApplication.translate   
        self.helpLabel.setToolTip(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 10pt; font-weight: 500; color:#000000">{0}</span></p></body></html>').format(self.description))        
        self.fontBox.setToolTip(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 9pt; font-style:italic, color:#000000;">Choose font</span></p></body></html>'))
        self.fontPointSizeBox.setToolTip(_translate("MainWindow", '<html><head/><body><p align="center"><span style=" font-size: 9pt; font-style:italic; color:#000000">Choose font size</span></p></body></html>'))
        self.underlineColorButton.setToolTip(_translate("MainWindow", '<html><head/><body><p align="center"><span style="font-size: 9pt; font-style:italic; color:#000000">Click on this to check underline color</span></body></html>'))  

    def deleteToolTips(self):
        '''|private method
        |Deletes tool tips for widget'''        
        self.boldButton.setToolTip('')
        self.italicButton.setToolTip('')
        self.underlineButton.setToolTip('')
        self.overlineButton.setToolTip('')
        self.helpLabel.setToolTip('')
        self.fontBox.setToolTip('')
        self.fontPointSizeBox.setToolTip('')
        self.underlineColorButton.setToolTip('')
        
    def copy(self):
        QApplication.clipboard().setText(self.name)
        
    def insert(self):
        self.mainWidget.currentWidget().insert(self.name) 

    def returnFormat(self):
        format = QTextCharFormat()
        format.setFontWeight(73 if self.boldButton.isChecked() else 50)
        format.setFontItalic(self.italicButton.isChecked())
        format.setFontUnderline(self.underlineButton.isChecked())
        format.setFontOverline(self.overlineButton.isChecked())
        format.setFont(self.fontBox.currentFont())    
        format.setFontPointSize(self.fontPointSizeBox.value())
        format.setUnderlineColor(QColor(self.underlineColor))
        
        if self.name == 'sin(x)':
            print(self.italicButton.isChecked())
            print(self.boldButton.isChecked())
            
            print(format.fontItalic())
            print(format.fontWeight())

        return format

        
               
        
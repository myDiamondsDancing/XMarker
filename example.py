import sys

from PyQt5.Qt import *

from getName import getFileName, getFormat

from checkableButton import CheckableButton


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.initUi()
        self.posCursor = 0
               
    def initUi(self):
        self.mainLayout = QVBoxLayout()
        
        self.edit = QTextEdit()
        self.edit.setFocus()
        self.edit.cursorPositionChanged.connect(self.setCursorPosition)
        self.mainLayout.addWidget(self.edit)
        self.setLayout(self.mainLayout)

    def replaceText(self):
        pass   
        
    def setCursorPosition(self):
        cursor = self.edit.textCursor()
        self.posCursor = cursor.position()

    def cursorPosition(self):
        return self.posCursor    
        
    def saveFile(self, path):
        try:
            if getFormat(path) == '.txt':
                with open(path, 'w') as f:
                    f.write(self.edit.toPlainText())
            elif getFormat(path) == '.html':
                with open(path, 'w') as f:
                    f.write(self.edit.toHtml())        
        except Exception as ex:
            self.showDialog('Error of saving')         
            

    def showDialog(self, text):
        '''|showDialog(self, text)
       |text : String
       |private method : shows error dialog with input text'''         
        dlg = QMessageBox(self)
        dlg.setText(text)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()     

    def insert(self, text):
        cursor = self.edit.textCursor()
        cursor.setPosition(self.posCursor)
        cursor.insertText(text)  
        self.edit.setFocus()        

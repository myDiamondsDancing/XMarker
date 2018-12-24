import sys
import time

from PyQt5 import QtCore as QC
from PyQt5.Qt import *

class ClickableLabel(QLabel):
    def __init__(self, parent=None, text='', tooltipText=''):
        super(ClickableLabel, self).__init__(parent)
        
        self.setMinimumSize(QSize(25, 25))
        
        self.loadFields(text, tooltipText)
        self.repaint()
       
       
    def mouseReleaseEvent(self, e):
        '''|private method
        |Changes state of widget(True, False)'''
        if e.button() == 1:
            self.checked = not self.checked        
            self.repaint()
        else:
            pass
            
            
    def repaint(self):
        '''|private method
        |Sets color for widget depending current state and theme'''
        _translate = QC.QCoreApplication.translate
        if self.theme == 0:
            if self.checked is True:
                self.setStyleSheet('background : rgb(185, 185, 185)')
                self.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">{0}</span></p></body></html>".format(self.text)))
            else:
                self.setStyleSheet('background : rgb(238, 238, 238)')
                self.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">{0}</span></p></body></html>".format(self.text)))              
        elif self.theme == 1:
            if self.checked is True:
                self.setStyleSheet('background : rgb(130, 130, 130)')
                self.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ececec;\">{0}</span></p></body></html>".format(self.text)))                
            else:
                self.setStyleSheet('background : rgb(176, 176, 176);')   
                self.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\"> {0}</span></p></body></html>".format(self.text)))             
        elif self.theme == 2:
            if self.checked is False:
                self.setStyleSheet('background : rgb(103, 103, 103);')   
                self.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ececec;\">{0}</span></p></body></html>".format(self.text)))    
            else:
                self.setStyleSheet('background : rgb(70, 70, 70)')
                self.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ececec;\"> {0}</span></p></body></html>".format(self.text)))
        self.setToolTip(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:500; color:#000000\">{0}</span></p></body></html>".format(self.tooltipText)))                             
                
    def setTheme(self, theme):
        '''|public method
        |Sets current theme for widget{0: Light, 1: Gray, 2: Dark}'''
        if theme == 0:
             self.theme = 0
        elif theme == 1:
             self.theme = 1
        else:
             self.theme = 2    

        self.repaint() 
        self.repaint()         
                
   
    def loadFields(self, text, tooltipText):
        '''|private method
        |Loads local fields for class(checked: bool, theme : (0, 1, 2), text: str)'''
        
        self.checked = False
        self.theme = 0
        self.text = text
        self.tooltipText = tooltipText
        self.toolTips = True
        self.tooltip = tooltipText
        
    def setToolTips(self, flag):
        self.toolTips = flag
        if flag is False:
            self.tooltipText = ''               
        else:
            self.tooltipText = self.tooltip 
        self.repaint()           
        
        
    def isChecked(self):
        '''|public method
        |isChecked >>> flag: bool''' 
        return self.checked      
        
                   
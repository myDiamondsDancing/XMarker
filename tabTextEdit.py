import sys
import pickle

from PyQt5.Qt import *

from example import Example
from dictOfTabs import dictOfTabs
from getName import getFileName 
from highLighter import MyHighlighter

class TabTextEdit(QTabWidget):
    def __init__(self, parent=None):
        super(TabTextEdit, self).__init__(parent)
        self.initUi()
        self.parent = parent
        self.connectUi()
        
        self.listofHighlighters = list()
        
        self.dictOfTabsEdits = dictOfTabs()
     
    def initUi(self):
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setUsesScrollButtons(True)
        
    
    def connectUi(self):
        self.tabCloseRequested.connect(self.tabEditClose)
        self.currentChanged.connect(self.setTitle)
        self.currentChanged.connect(self.parent.setValuesOfFormat)
        
    def addTabEdit(self, path):
        if path is not None:
            e = Example()
            highLighter = MyHighlighter(self.parent.symbolWidget, parent=e.edit.document())
            self.listofHighlighters.append(highLighter)
            try:
                with open(path, 'r') as f:
                    text = f.read() 
                    e.edit.setText(text)                       
            except Exception:
                pass          
            self.dictOfTabsEdits.addPath(path, e)
            self.addTab(e, getFileName(path)) 
            e.edit.cursorPositionChanged.connect(self.parent.setValuesOfFormat)
        else: 
            e = Example()
            highLighter = MyHighlighter(self.parent.symbolWidget, parent=e.edit.document())
            self.listofHighlighters.append(highLighter)          
            self.dictOfTabsEdits.addPath(path, e)
            self.addTab(e, getFileName(path)) 
            e.edit.cursorPositionChanged.connect(self.parent.setValuesOfFormat)        

    def tabEditClose(self, ind):
        w = self.widget(ind)
        w.saveFile(self.dictOfTabsEdits.path(w))
        self.dictOfTabsEdits.removePath(w)
        self.removeTab(ind)
        if self.count() == 0:
            self.addTabEdit(None)
        
    def saveFileAs(self, path):
        w = self.currentWidget()
        w.saveFile(path)   

    def saveFile(self):
        w = self.currentWidget()
        if self.dictOfTabsEdits.path(w) is None:
            path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")   
            if path is None:
                return
            w.saveFile(path)  
            self.dictOfTabsEdits.insertPath(w, path) 
        else:
            w.saveFile(self.dictOfTabsEdits.path(w))  

    def setTitle(self):
    
        print(self.count())
        if self.count() != 0 : 
            if self.dictOfTabsEdits.path(self.currentWidget()) is not None:
                self.parent.setWindowTitle('{}; '.format(self.dictOfTabsEdits.path(self.currentWidget())) + 'Xmark') 
            else: 
                self.parent.setWindowTitle('Empty file, XMarker')
        else: pass;
        
 
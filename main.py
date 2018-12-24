import sys
import os

import numpy as np

from PyQt5.Qt import *

from chartWidget import *
from tabTextEdit import TabTextEdit
from scrollArea import ScrollArea
from histWidget import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUi()
        
    def initUi(self):      
        self.setWindowTitle('XMark')
        
        self.chartLayout = QVBoxLayout()
        
        self.l = QWidget()
    
        self.chartWidget = ChartWidget()
        self.histWidget = HistWidget()
        
        tab = QTabWidget()
        
        tab.addTab(self.chartWidget, 'Chart')
        tab.addTab(self.histWidget, 'Hist')
        
        
        fileToolBar = QToolBar("File")
        fileToolBar.setIconSize(QSize(14, 14))
        self.addToolBar(fileToolBar)
        fileMenu = self.menuBar().addMenu("&File")

        self.openFileAction = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
        self.openFileAction.setStatusTip("Open file")
        self.openFileAction.triggered.connect(self.openFile)
        fileMenu.addAction(self.openFileAction)
        fileToolBar.addAction(self.openFileAction)

        self.saveFileAction = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
        self.saveFileAction.setStatusTip("Save current page")
        self.saveFileAction.triggered.connect(self.saveFile)
        fileMenu.addAction(self.saveFileAction)
        fileToolBar.addAction(self.saveFileAction)

        saveAsFileAction = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
        saveAsFileAction.setStatusTip("Save current page to specified file")
        saveAsFileAction.triggered.connect(self.saveFileAs)
        fileMenu.addAction(saveAsFileAction)
        fileToolBar.addAction(saveAsFileAction)

        self.print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        self.print_action.setStatusTip("Print current page")
        self.print_action.triggered.connect(self.printFile)
        fileMenu.addAction(self.print_action)
        fileToolBar.addAction(self.print_action)

        editToolbar = QToolBar("Edit")
        editToolbar.setIconSize(QSize(16, 16))
        self.addToolBar(editToolbar)
        editMenu = self.menuBar().addMenu("&Edit")

        self.undoAction = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        self.undoAction.setStatusTip("Undo last change")
        editToolbar.addAction(self.undoAction)
        editMenu.addAction(self.undoAction)

        self.redoAction = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        self.redoAction.setStatusTip("Redo last change")
        editToolbar.addAction(self.redoAction)
        editMenu.addAction(self.redoAction)

        editMenu.addSeparator()

        cutAction = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cutAction.setStatusTip("Cut selected text")
        cutAction.setShortcut(QKeySequence.Cut)
        editToolbar.addAction(cutAction)
        editMenu.addAction(cutAction)

        self.copyAction = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        self.copyAction.setStatusTip("Copy selected text")
        self.copyAction.setShortcut(QKeySequence.Copy)
        editToolbar.addAction(self.copyAction)
        editMenu.addAction(self.copyAction)

        self.pasteAction = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        self.pasteAction.setStatusTip("Paste from clipboard")
        self.pasteAction.setShortcut(QKeySequence.Paste)
        editToolbar.addAction(self.pasteAction)
        editMenu.addAction(self.pasteAction)

        self.selectAction = QAction(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
        self.selectAction.setStatusTip("Select all text")
        cutAction.setShortcut(QKeySequence.SelectAll)
        editMenu.addAction(self.selectAction)

        editMenu.addSeparator()

        formatToolbar = QToolBar("Format")
        formatToolbar.setIconSize(QSize(16, 16))
        self.addToolBar(formatToolbar)
        formatMenu = self.menuBar().addMenu("&Format")

        self.fonts = QFontComboBox()
        formatToolbar.addWidget(self.fonts)

        self.fontPointSize = QSpinBox()
        self.fontPointSize.setValue(12)
        self.fontPointSize.setSingleStep(2)
        self.fontPointSize.setRange(1, 72)

        formatToolbar.addWidget(self.fontPointSize)

        self.boldAction = QAction(QIcon(os.path.join('images', 'edit-bold.png')), "Bold", self)
        self.boldAction.setStatusTip("Bold")
        self.boldAction.setShortcut(QKeySequence.Bold)
        self.boldAction.setCheckable(True)
        formatToolbar.addAction(self.boldAction)
        formatMenu.addAction(self.boldAction)

        self.italicAction = QAction(QIcon(os.path.join('images', 'edit-italic.png')), "Italic", self)
        self.italicAction.setStatusTip("Italic")
        self.italicAction.setShortcut(QKeySequence.Italic)
        self.italicAction.setCheckable(True)
        formatToolbar.addAction(self.italicAction)
        formatMenu.addAction(self.italicAction)

        self.underlineAction = QAction(QIcon(os.path.join('images', 'edit-underline.png')), "Underline", self)
        self.underlineAction.setStatusTip("Underline")
        self.underlineAction.setShortcut(QKeySequence.Underline)
        self.underlineAction.setCheckable(True)
        formatToolbar.addAction(self.underlineAction)
        formatMenu.addAction(self.underlineAction)

        formatMenu.addSeparator()

        self.alignLeftAction = QAction(QIcon(os.path.join('images', 'edit-alignment.png')), "Align left", self)
        self.alignLeftAction.setStatusTip("Align text left")
        self.alignLeftAction.setCheckable(True)
        formatToolbar.addAction(self.alignLeftAction)
        formatMenu.addAction(self.alignLeftAction)

        self.alignCenterAction = QAction(QIcon(os.path.join('images', 'edit-alignment-center.png')), "Align center", self)
        self.alignCenterAction.setStatusTip("Align text center")
        self.alignCenterAction.setCheckable(True)
        formatToolbar.addAction(self.alignCenterAction)
        formatMenu.addAction(self.alignCenterAction)

        self.alignRightAction = QAction(QIcon(os.path.join('images', 'edit-alignment-right.png')), "Align right", self)
        self.alignRightAction.setStatusTip("Align text right")
        self.alignRightAction.setCheckable(True)
        formatToolbar.addAction(self.alignRightAction)
        formatMenu.addAction(self.alignRightAction)

        self.alignJustifyAction = QAction(QIcon(os.path.join('images', 'edit-alignment-justify.png')), "Justify", self)
        self.alignJustifyAction.setStatusTip("Justify text")
        self.alignJustifyAction.setCheckable(True)
        formatToolbar.addAction(self.alignJustifyAction)
        formatMenu.addAction(self.alignJustifyAction)

        formatGroup = QActionGroup(self)
        formatGroup.setExclusive(True)
        formatGroup.addAction(self.alignLeftAction)
        formatGroup.addAction(self.alignCenterAction)
        formatGroup.addAction(self.alignRightAction)
        formatGroup.addAction(self.alignJustifyAction)
        
        self.darkThemeAction = QAction(QIcon(os.path.join('images', 'dark-theme.png')), "Dark theme", self)
        self.darkThemeAction.setStatusTip("Set dark theme")
        self.darkThemeAction.triggered.connect(lambda : self.setTheme(2))
        
        self.grayThemeAction = QAction(QIcon(os.path.join('images', 'gray-theme.png')), "Gray theme", self)
        self.grayThemeAction.setStatusTip("Set gray theme")      
        self.grayThemeAction.triggered.connect(lambda : self.setTheme(1))        

        self.lightThemeAction = QAction(QIcon(os.path.join('images', 'light-theme.png')), "Light theme", self)
        self.lightThemeAction.setStatusTip("Set light theme")      
        self.lightThemeAction.triggered.connect(lambda : self.setTheme(0))        
        
        themeMenu = self.menuBar().addMenu("Themes")
        
        themeMenu.addAction(self.darkThemeAction)
        themeMenu.addAction(self.grayThemeAction)
        themeMenu.addAction(self.lightThemeAction)
        
        themesToolbar = QToolBar("Themes")
        themesToolbar.addAction(self.darkThemeAction)
        themesToolbar.addAction(self.grayThemeAction)
        themesToolbar.addAction(self.lightThemeAction)
        self.addToolBar(themesToolbar)
        
        
        themeGroup = QActionGroup(self)
        themeGroup.setExclusive(True)
        themeGroup.addAction(self.darkThemeAction)
        themeGroup.addAction(self.grayThemeAction)
        themeGroup.addAction(self.lightThemeAction)

        formatMenu.addSeparator()  
 
        self.mainWidget = TabTextEdit(parent=self)  
        self.symbolWidget = ScrollArea(mainWidget=self.mainWidget)        
        self.mainWidget.addTabEdit(os.getcwd() + '\\start.txt')  

        self.mainLayout = QHBoxLayout(self.l)
        self.mainLayout.addWidget(self.mainWidget)
        self.chartLayout.addWidget(tab)
        self.chartLayout.addWidget(self.symbolWidget)
        self.mainLayout.addLayout(self.chartLayout)
        
        self.chartWidget.toFieldButton.clicked.connect(self.insertChartPlot)
        self.histWidget.toFieldButton.clicked.connect(self.insertHistPlot)
    
        self.undoAction.triggered.connect(self.mainWidget.currentWidget().edit.undo)    
        self.redoAction.triggered.connect(self.mainWidget.currentWidget().edit.redo)    
        cutAction.triggered.connect(self.mainWidget.currentWidget().edit.cut)    
        self.copyAction.triggered.connect(self.mainWidget.currentWidget().edit.copy)    
        self.pasteAction.triggered.connect(self.mainWidget.currentWidget().edit.paste)        
        self.selectAction.triggered.connect(lambda : self.mainWidget.currentWidget().edit.selectAll) 
        
        self.fontPointSize.valueChanged.connect(lambda s: self.mainWidget.currentWidget().edit.setFontPointSize(s) )
        self.fontPointSize.setValue(12)
        self.fontPointSize.setSingleStep(2)
        self.fonts.currentFontChanged.connect(self.mainWidget.currentWidget().edit.setCurrentFont)        
        
        self.boldAction.triggered.connect(lambda x: self.mainWidget.currentWidget().edit.setFontWeight(QFont.Bold if x else QFont.Normal))
        self.italicAction.triggered.connect(self.mainWidget.currentWidget().edit.setFontItalic)        
        self.underlineAction.triggered.connect(self.mainWidget.currentWidget().edit.setFontUnderline)        

        self.alignLeftAction.triggered.connect(lambda: self.mainWidget.currentWidget().edit.setAlignment(Qt.AlignLeft))        
        self.alignCenterAction.triggered.connect(lambda: self.mainWidget.currentWidget().edit.setAlignment(Qt.AlignCenter))
        self.alignRightAction.triggered.connect(lambda: self.mainWidget.currentWidget().edit.setAlignment(Qt.AlignRight))        
        self.alignJustifyAction.triggered.connect(lambda: self.mainWidget.currentWidget().edit.setAlignment(Qt.AlignJustify))  
        

        self.setCentralWidget(self.l)        

        self.setValuesOfFormat()
        
    def openFile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")
        self.mainWidget.addTabEdit(path)

    def saveFileAs(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")
        self.mainWidget.saveFileAs(path)  

    def saveFile(self):
        self.mainWidget.saveFile() 
        
    def printFile(self):
        dial = QPrintDialog()        
        if dial.exec_():
            self.mainWidget.currentWidget().edit.print_(dial.printer())
            
    def insertChartPlot(self):
        position = self.mainWidget.currentWidget().cursorPosition()
        self.chartWidget.figure.savefig(os.getcwd() + '\\test.png', format='png') 
        self.mainWidget.currentWidget().edit.setFocus()
        cursor = self.mainWidget.currentWidget().edit.textCursor()
        cursor.setPosition(position)
        cursor.insertImage(QImage(os.getcwd() + '\\test.png'))
        
    def insertHistPlot(self):
        position = self.mainWidget.currentWidget().cursorPosition()
        self.histWidget.figure.savefig(os.getcwd() + '\\test.png', format='png') 
        self.mainWidget.currentWidget().edit.setFocus()
        cursor = self.mainWidget.currentWidget().edit.textCursor()
        cursor.setPosition(position)
        cursor.insertImage(QImage(os.getcwd() + '\\test.png')) 
        
    def setTheme(self, theme):
        if theme == 0:
            self.setLightTheme()
        elif theme == 1:
            self.setGrayTheme()
        else:
            self.setDarkTheme()

    def setLightTheme(self):
        self.setStyleSheet('background : rgb(238, 238, 238)')
        self.mainWidget.setStyleSheet('background : rgb(252, 252, 252)')
        self.fontPointSize.setStyleSheet('background : rgb(252, 252, 252)')
        self.fonts.setStyleSheet('background : rgb(252, 252, 252)')        
        self.symbolWidget.setTheme(0)         
        self.chartWidget.setTheme(0)
        
    def setGrayTheme(self):
        self.setStyleSheet('background : rgb(176, 176, 176)')
        self.mainWidget.setStyleSheet('background : rgb(232, 232, 232)')
        self.fontPointSize.setStyleSheet('background : rgb(232, 232, 232)')
        self.fonts.setStyleSheet('background : rgb(232, 232, 232)')        
        self.symbolWidget.setTheme(1)
        self.chartWidget.setTheme(1) 

    def setDarkTheme(self):
        self.setStyleSheet('background : rgb(103, 103, 103)')
        self.mainWidget.setStyleSheet('background : rgb(182, 182, 182)')
        self.fontPointSize.setStyleSheet('background : rgb(182, 182, 182)')
        self.fonts.setStyleSheet('background : rgb(182, 182, 182)')        
        self.symbolWidget.setTheme(2)
        self.chartWidget.setTheme(2) 

    def setValuesOfFormat(self):
    
        try:
            format = self.mainWidget.currentWidget().edit.textCursor().charFormat()

            self.boldAction.setChecked(format.fontWeight() == QFont.Bold)

            self.italicAction.setChecked(format.fontItalic())

            self.underlineAction.setChecked(format.fontUnderline())

            self.fontPointSize.setValue(format.fontPointSize())
        except Exception:
            pass        

                
           
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()        
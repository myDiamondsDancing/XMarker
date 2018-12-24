import sys
import sip

from numpy import *

from PyQt5.Qt import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import *

from histScrollArea import ScrollWidget

class HistWidget(QWidget):
    def __init__(self, parent=None):
        super(HistWidget, self).__init__(parent)
        self.initUi()
        self.connectUi()
        self.loadFields()
        self.setTheme(self.theme)
        
    def initUi(self):
        '''private method : inits user interface'''
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure) 
        self.toolBar = NavigationToolbar(self.canvas, self)
        
        self.drawAreaLayout = QVBoxLayout()
        self.drawAreaLayout.addWidget(self.canvas)
        self.drawAreaLayout.addWidget(self.toolBar)
        
        self.addButton = QPushButton('Add chart')
        self.toFieldButton = QPushButton('To field')
        self.plotButton = QPushButton('Plot')
        
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addWidget(self.addButton)
        self.buttonsLayout.addWidget(self.toFieldButton)
        
        self.area = ScrollWidget()
        
        self.areaLayout = QVBoxLayout()
        self.areaLayout.addLayout(self.buttonsLayout)
        self.areaLayout.addWidget(self.area)
        self.areaLayout.addWidget(self.plotButton)
        
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.areaLayout)
        self.mainLayout.addLayout(self.drawAreaLayout)
        
        self.setLayout(self.mainLayout)
        
    def loadFields(self):
        '''|loadFields(self)
       |private method : loads local field(theme)'''
        self.theme = 0     
        
    def connectUi(self):
        '''private method : connects all needed signals with class methods'''
        self.addButton.clicked.connect(self.area.addWidget)
        self.plotButton.clicked.connect(self.plot)
        
    def plot(self):
        '''|plot(self)
       |public method : plots chart is canvas using chartSettingsWidget.results
       |plot >>> True if plotting is success else False '''
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        values = [ widget.returnResults()[1] for widget in self.area.listOfWidgets]
        legends = [ widget.returnResults()[0] for widget in self.area.listOfWidgets]
        
        x_axis = arange(len(legends))
        
        ax.set_xticks(x_axis)
        ax.set_xticklabels(legends, rotation=30, animated=True)
        ax.bar(x_axis, values, align='center')
        
        self.canvas.draw()
                  
        
    def setTheme(self, flag):
        '''|setTheme(self, flag)
       |flag : (0: Light, 1: Gray, 2: Dark) 
       |public method : sets theme for widgets
       |setTheme >>> None'''
        self.theme = flag
        if flag == 0:
            self.setLigthTheme()
        elif flag == 1:
            self.setGrayTheme()
        else:
            self.setDarkTheme()        

    def setLigthTheme(self):
        '''|setLigthTheme(self)
       |private method : sets light theme for widgets'''
       
        self.setStyleSheet("background : rgb(238, 238, 238);")
        self.area.setTheme(0)    

    def setGrayTheme(self):
        '''|setGrayTheme(self)
       |private method : sets gray theme for widgets''' 
        self.setStyleSheet("background : rgb(176, 176, 176);") 
        self.area.setTheme(1)

    def setDarkTheme(self):
        '''|setGrayTheme(self)
       |private method : sets dark theme for widget''' 
        self.setStyleSheet("background : rgb(103, 103, 103);")
        self.area.setTheme(2)  
        
    def showDialog(self, text):
        '''|showDialog(self, text)
       |text : String
       |private method : shows error dialog with input text'''         
        dlg = QMessageBox(self)
        dlg.setText(text)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show() 
 
  
      
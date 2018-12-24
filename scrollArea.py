# -*- coding: utf-8 -*-

import sys

from symbolSettingsWidget import SymbolSettingsWidget

from PyQt5.Qt import *

class ScrollArea(QWidget):
    def __init__(self, parent=None, mainWidget=None):
        super(ScrollArea, self).__init__(parent)
        self.mainWidget = mainWidget
        self.initUi()
        
    def initUi(self):       
        self.layoutV = QVBoxLayout(self)

        self.area = QScrollArea(self)
        self.area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()

        self.layoutH = QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QVBoxLayout()
        self.layoutH.addLayout(self.gridLayout)

        self.area.setWidget(self.scrollAreaWidgetContents)
        self.layoutV.addWidget(self.area)
        
        self.dictOfWidgets = dict()
        
        ###############################################################################################################################
        
        self.row1 = QHBoxLayout()
        
        self.sinWidget = SymbolSettingsWidget(name='sin(x)', description='Trigonometric function of an angle.', mainWidget=self.mainWidget)
        self.row1.addWidget(self.sinWidget)
        self.dictOfWidgets['sin'] = self.sinWidget

        self.cosWidget = SymbolSettingsWidget(name='cos(x)', description='Trigonometric function of an angle', mainWidget=self.mainWidget)
        self.row1.addWidget(self.cosWidget)
        self.dictOfWidgets['cos'] = self.cosWidget     
        
        self.gridLayout.addLayout(self.row1)
        
        ###############################################################################################################################
        
        self.row2 = QHBoxLayout()
        
        self.tgWidget = SymbolSettingsWidget(name='tg(x)', description='Trigonometric function of an angle', mainWidget=self.mainWidget)
        self.dictOfWidgets['tg'] = self.tgWidget
        self.row2.addWidget(self.tgWidget)
        
        self.ctgWidget = SymbolSettingsWidget(name='ctg(x)', description='Trigonometric function of an angle', mainWidget=self.mainWidget)
        self.dictOfWidgets['ctg'] = self.ctgWidget
        self.row2.addWidget(self.ctgWidget)
        
        self.gridLayout.addLayout(self.row2)
        
        ###############################################################################################################################
        self.row3 = QHBoxLayout()
   
        self.alphaWidget = SymbolSettingsWidget(name='α', description='First letter of the Greek alphabet. Usually denotes the angle', mainWidget=self.mainWidget)
        self.dictOfWidgets['α'] = self.alphaWidget      
        self.row3.addWidget(self.alphaWidget)

        self.betaWidget = SymbolSettingsWidget(name='β', description='Second letter of the Greek alphabet. Usually denotes the angle', mainWidget=self.mainWidget)  
        self.dictOfWidgets['β'] = self.betaWidget
        self.row3.addWidget(self.betaWidget)

        self.gridLayout.addLayout(self.row3)

        ###############################################################################################################################
        
        self.row4 = QHBoxLayout()
         
        self.xWidget = SymbolSettingsWidget(name='x', description='Often denotes the roots in the equation', mainWidget=self.mainWidget)
        self.dictOfWidgets['x'] = self.xWidget
        self.row4.addWidget(self.xWidget)

        self.yWidget = SymbolSettingsWidget(name='Y', description='The letter of the Greek alphabet. Usually denotes a function', mainWidget=self.mainWidget)
        self.dictOfWidgets['y'] = self.yWidget
        self.row4.addWidget(self.yWidget)

        self.gridLayout.addLayout(self.row4)   

        ###############################################################################################################################

        self.row5 = QHBoxLayout()
       
        self.gammaWidget = SymbolSettingsWidget(name='γ', description='The letter of the Greek alphabet. Denotes the Euler gamma function', mainWidget=self.mainWidget)
        self.dictOfWidgets['γ'] = self.gammaWidget        
        self.row5.addWidget(self.gammaWidget)
        
        self.deltaWidget = SymbolSettingsWidget(name='Δ', description='The letter of the Greek alphabet. Usually means the difference, changing.', mainWidget=self.mainWidget)
        self.dictOfWidgets['Δ'] =self.deltaWidget
        self.row5.addWidget(self.deltaWidget)
        
        self.gridLayout.addLayout(self.row5)
        
        ##############################################################################################################################
        
        self.row6 = QHBoxLayout()
        
        self.epsilonWidget = SymbolSettingsWidget(name='ε', description='The letter of the Greek alphabet. In computer science denotes an empty string.', mainWidget=self.mainWidget)
        self.dictOfWidgets['ε'] = self.epsilonWidget
        self.row6.addWidget(self.epsilonWidget)
        
        self.nuWidget = SymbolSettingsWidget(name='μ',description='The letter of the Greek alphabet. In physics, usually denotes the coefficient of friction', mainWidget=self.mainWidget)
        self.dictOfWidgets['μ'] = self.nuWidget
        self.row6.addWidget(self.nuWidget)
        
        self.gridLayout.addLayout(self.row6)
        
        ##############################################################################################################################        
        
        self.row7 = QHBoxLayout()
        
        self.epsilonWidget = SymbolSettingsWidget(name='κ', description='The letter of the Greek alphabet. In physics, usually denotes the coefficients.', mainWidget=self.mainWidget)
        self.dictOfWidgets['κ'] = self.epsilonWidget
        self.row7.addWidget(self.epsilonWidget)
        
        self.nuWidget = SymbolSettingsWidget(name='τ',description='The letter of the Greek alphabet. τ = 2π. Also usually denotes time.', mainWidget=self.mainWidget)
        self.dictOfWidgets['τ'] = self.nuWidget
        self.row7.addWidget(self.nuWidget)
        
        self.gridLayout.addLayout(self.row7)
        
         ##############################################################################################################################
        
        self.row8 = QHBoxLayout()
        
        self.epsilonWidget = SymbolSettingsWidget(name='π', description='The letter of the Greek alphabet. Denotes constant, π = 3, 14...', mainWidget=self.mainWidget)
        self.dictOfWidgets['ε'] = self.epsilonWidget
        self.row8.addWidget(self.epsilonWidget)
        
        self.nuWidget = SymbolSettingsWidget(name='Ω',description='The letter of the Greek alphabet. In physics, usually denotes oscillation frequency.', mainWidget=self.mainWidget)
        self.dictOfWidgets['Ω'] = self.nuWidget
        self.row8.addWidget(self.nuWidget)
        
        self.gridLayout.addLayout(self.row8)       
             
    def setToolTips(self, flag):
        for key in self.dictOfWidgets:
            self.dictOfWidgets[key].setToolTips(flag)            
        
    def setTheme(self, theme):
        if theme == 0:
            self.setLightTheme()
        elif theme == 1:
            self.setGrayTheme()
        else:
            self.setDarkTheme()        

    def setLightTheme(self):
        self.setStyleSheet('background : rgb(238, 238, 238)')
        for key in self.dictOfWidgets:
            self.dictOfWidgets[key].setTheme(0)    

    def setGrayTheme(self):
        self.setStyleSheet('background : rgb(176, 176, 176)')
        for key in self.dictOfWidgets:
            self.dictOfWidgets[key].setTheme(1)    

    def setDarkTheme(self):
        self.setStyleSheet('background : rgb(103, 103, 103)')
        for key in self.dictOfWidgets:
            self.dictOfWidgets[key].setTheme(2)                  
      
      

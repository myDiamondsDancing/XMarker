# -*- coding: utf-8 -*-

import sys

from PyQt5.Qt import *

class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, widget, parent=None):
        super(MyHighlighter, self).__init__(parent)
        
        self.widget = widget
       

    def highlightBlock(self, text):
    
        for regexp, widget in self.widget.dictOfWidgets.items():
            expression = QRegularExpression(regexp)
            it = expression.globalMatch(text)
            charFormat = widget.returnFormat()
                    
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), charFormat)
        
        
        
        
        

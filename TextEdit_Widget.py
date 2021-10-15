from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

class TextEdit_Widget(QWidget):
    def __init__(self):
        super().__init__()

        print("class : TextEdit_Widget")

        # self.widget = QTextEdit()
        self.widget = QTextBrowser()
        # self.widget.setAcceptRichText(True)
        # href="https://www.naver.com"
        # self.label = QLabel()
        # self.label.setText('<a href='+href+' >Naver</a> ')

        # # self.widget = QTextBrowser()
        self.widget.setReadOnly(False)
        # # self.widget.setReadOnly(True)
        # # self.widget.setText('<a href= https://www.naver.com >Naver</a>')
        # self.label.setOpenExternalLinks(True)
        # self.widget.setText(self.label.text())
        # self.widget.setOpenExternalLinks(True)

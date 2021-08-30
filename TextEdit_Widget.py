from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

class TextEdit_Widget(QWidget):
    def __init__(self):
        super().__init__()

        print("class : TextEdit_Widget")

        self.widget = QTextEdit()
        self.widget.setAcceptRichText(False)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

from Folder_Widget import *

class MemoManager(QWidget):
    def __init__(self, parent):
        super(MemoManager, self).__init__(parent)
        self.parent = parent

        print("MemoManger().__init__()")
        
        self.Hboxlayout = QHBoxLayout()
        self.Hboxlayout_Left = QHBoxLayout()
        self.Vboxlayout_Right = QVBoxLayout()

        self.textEdit_stackedwidget = QStackedWidget()
        self.textEdit_stackedwidget.addWidget(QTextEdit())

        # 레이아웃 배치
        # 스텍 위젯 - 여러 위젯을 한 공간에 저장해서 선택할 수 있게 한다.(위젯 배열느낌)
        self.stackedwidget = QStackedWidget()
        self.stackedwidget.addWidget(File_Widgit(self.textEdit_stackedwidget, None, -1).widget)

        self.folder_treewidget = Folder_Widget(self.stackedwidget, self.textEdit_stackedwidget, self.parent)

        self.UI()

        self.show()

    def UI(self):
        self.Hboxlayout.addLayout(self.Hboxlayout_Left)
        self.Hboxlayout.setSpacing(1)

        H_splitter = QSplitter(Qt.Horizontal)
        V_splitter = QSplitter(Qt.Vertical)

        V_splitter.addWidget(self.stackedwidget)
        V_splitter.addWidget(self.textEdit_stackedwidget)

        H_splitter.addWidget(self.folder_treewidget.widget)
        H_splitter.addWidget(V_splitter)

        H_splitter.setStretchFactor(1, 3)
        H_splitter.setStretchFactor(0, 1)
        V_splitter.setStretchFactor(1, 1)
        
        self.Hboxlayout_Left.addWidget(H_splitter)

        self.setLayout(self.Hboxlayout)
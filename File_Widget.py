from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

class File_Widgit(QWidget):
    def __init__(self):
        super().__init__()

        print("class : File_Widgit")

        self.widget = QTreeWidget()
        self.file_root = QTreeWidget.invisibleRootItem(self.widget)

        self.folderText = ""

        self.UI()
        self.contextMenu()

    def __del__(self):
        print("File_Widgit __del__()")

    def UI(self):
        self.widget.setHeaderLabels(["제목", "생성일", "수정일", "그룹"])
        self.widget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.widget.setColumnWidth(0, 160)
        self.widget.setColumnWidth(1, 150)
        self.widget.setColumnWidth(2, 150)

    def get_widget(self):
        return self.widget

    def contextMenu(self):
        self.newfile = QAction("새 파일", self.widget)
        self.widget.addAction(self.newfile)
        self.newfile.setEnabled(False)

        self.newfile.triggered.connect(lambda : self.newfile_contextClick())

    # 파일추가
    def addFile(self, title, date, modify, group):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem()

        item.setText(0, title)
        item.setText(1, date)
        item.setText(2, modify)
        item.setText(3, group)

        return item

    def newfile_contextClick(self):
        print("newfile.triggered.connect()")

        day = QDate.currentDate()
        time = QTime.currentTime()

        self.file_root.addChild(self.addFile("bird 파일", day.toString('yyyy/MM/dd') + " - " + time.toString('hh:mm:ss'), day.toString('yyyy/MM/dd')+ " - " + time.toString('hh:mm:ss'), self.folderText))
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

from TextEdit_Widget import *

# self.file_list에 추가됨
class File_Widgit(QWidget):
    def __init__(self, stackedwidget, folder_list, folderIndex):
        super().__init__()

        print("class : File_Widgit")

        self.stackedwidget = stackedwidget
        self.folderIndex = folderIndex

        self.folder_list = folder_list
        self.textEdit_list = list()

        print("{0}번 폴더에 생성".format(self.folderIndex))

        self.widget = QTreeWidget()
        self.file_root = QTreeWidget.invisibleRootItem(self.widget)

        self.folderText = ""
        self.fileIndex = 0

        self.UI()
        self.contextMenu()

        self.widget.itemPressed.connect(self.file_pressedItem)
        # self.widget.itemChanged.connect(self.file_changedItem)

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

        self.removefile = QAction("파일 삭제", self.widget)
        self.widget.addAction(self.removefile)
        self.removefile.setEnabled(False)

        self.newfile.triggered.connect(lambda : self.newfile_contextClick())
        self.removefile.triggered.connect(lambda : self.removefile_contextClick())
        

    # 파일추가
    def addFile(self, title, date, modify, group):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem()

        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsEditable)

        item.setText(0, title)
        item.setText(1, date)
        item.setText(2, modify)
        item.setText(3, group)

        return item

    def newfile_contextClick(self):
        print("newfile.triggered.connect()")
        print("folderIndex : {0}".format(self.folderIndex))

        self.textEdit_list.append(TextEdit_Widget())
        self.folder_list[self.folderIndex] = self.textEdit_list
        
        list_len = len(self.textEdit_list)
        print("textEdit : {0}".format(list_len))
        # listIndex = self.widget.currentIndex().row()

        self.stackedwidget.addWidget(self.folder_list[self.folderIndex][list_len-1].widget)

        day = QDate.currentDate()
        time = QTime.currentTime()

        self.file_root.addChild(self.addFile("bird 파일", day.toString('yyyy/MM/dd') + " - " + time.toString('hh:mm:ss'), day.toString('yyyy/MM/dd')+ " - " + time.toString('hh:mm:ss'), self.folderText))

    def removefile_contextClick(self):
        print("removefolder.triggered.connect()")

        listIndex = self.widget.currentIndex().row()

        self.file_root.removeChild(self.file_item)

        self.stackedwidget.removeWidget(self.folder_list[self.folderIndex][listIndex].widget)

        del self.folder_list[self.folderIndex][listIndex]

        if(len(self.folder_list[self.folderIndex]) == 0):
            self.folder_list.append(0)
            self.stackedwidget.setCurrentIndex(0)
        elif (listIndex-1) == -1:
            self.stackedwidget.setCurrentWidget(self.folder_list[self.folderIndex][listIndex].widget)
        else:
            self.stackedwidget.setCurrentWidget(self.folder_list[self.folderIndex][listIndex-1].widget)
            print(listIndex-1)

        self.removefile.setEnabled(False)

        print(self.file_root.childCount())

        # self.parent.statusBar().showMessage("삭제됨 : {0}     [선택 행/전체 수]: [{1}/{2}]".format(self.folderText, listIndex+1, self.folder_root.childCount()))

    # def file_changedItem(self, item):
    #     print("file_changedItem")
    #     listIndex = self.widget.currentIndex().row()

    #     self.folder_item = item
    #     self.folderText = item.text(0)
    #     self.file_list[listIndex].folderText = item.text(0)

    #     file_childCount = self.file_list[listIndex].file_root.childCount()

    def file_pressedItem(self, item):
        print("file_pressedItem")
        
        listIndex = self.widget.currentIndex().row()
        self.fileIndex = listIndex

        print(item.text(0), "클릭 {0}번 폴더 {1}번 파일".format(self.folderIndex, self.widget.currentIndex().row()))

        self.file_item = item

        if item.isSelected() == True:
            self.removefile.setEnabled(True)

        self.stackedwidget.setCurrentWidget(self.folder_list[self.folderIndex][listIndex].widget)
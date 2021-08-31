from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

from File_Widget import *

class Folder_Widget(QWidget):
    def __init__(self, stackedwidget, textEdit_stackedwidget, parent):
        super().__init__()

        self.stackedwidget = stackedwidget
        self.textEdit_stackedwidget = textEdit_stackedwidget
        self.parent = parent

        print("class : Folder_Widget")

        self.widget = QTreeWidget()
        self.folder_root = QTreeWidget.invisibleRootItem(self.widget)

        self.file_list = list()
        self.folder_list = list()

        # for i in range(10):
        #     self.folder_list.append(i)
    
        self.widget.setMouseTracking(True)

        self.folderText = ""

        self.UI()
        self.contextMenu()

        self.widget.itemPressed.connect(self.folder_pressedItem)
        self.widget.itemChanged.connect(self.folder_changedItem)

    def __del__(self):
        print("Folder_Widgit __del__()")

    def UI(self):
        self.widget.setHeaderLabel("목록")
        self.widget.setContextMenuPolicy(Qt.ActionsContextMenu)

    def contextMenu(self):
        self.newfolder = QAction("새 폴더", self.widget)
        self.widget.addAction(self.newfolder)

        self.removefolder = QAction("폴더 삭제", self.widget)
        self.widget.addAction(self.removefolder)
        self.removefolder.setEnabled(False)

        self.newfolder.triggered.connect(lambda : self.newfolder_contextClick())
        self.removefolder.triggered.connect(lambda : self.removefolder_contextClick())

    # 폴더추가
    def addFolder(self, title):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem()
        # 항목 속성 지정
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsEditable)
        item.setText(0, title)

        return item

    def newfolder_contextClick(self):
        print("newfolder.triggered.connect()")

        self.folder_list.append(0)

        # 폴더 생성 시 리스트에 파일 위젯 추가
        self.file_list.append(File_Widgit(self.textEdit_stackedwidget, self.folder_list, self.folder_root.childCount()))
        list_len = len(self.file_list)
        print("list : {0}".format(list_len))

        self.stackedwidget.addWidget(self.file_list[list_len-1].widget)

        self.folder_root.addChild(self.addFolder("bird 폴더"))

        listIndex = self.widget.currentIndex().row()
        self.parent.statusBar().showMessage("생성됨 : {0}     [선택 행/전체 수]: [{1}/{2}]".format("bird 폴더", listIndex+1, self.folder_root.childCount()))
        # print(self.folder_root.childCount())

    def removefolder_contextClick(self):
        print("removefolder.triggered.connect()")

        listIndex = self.widget.currentIndex().row()

        self.folder_root.removeChild(self.folder_item)

        self.stackedwidget.setCurrentIndex(listIndex)
        self.stackedwidget.removeWidget(self.file_list[listIndex].widget)

        del self.file_list[listIndex]

        # folerIndex를 한칸씩 밀고 folder_list 삭제
        for index in range(listIndex, len(self.folder_list)-1):
            print(index, len(self.folder_list))
            self.file_list[index].folderIndex = self.file_list[index].folderIndex - 1

        del self.folder_list[listIndex]

        print(self.folder_root.childCount())

        self.parent.statusBar().showMessage("삭제됨 : {0}     [선택 행/전체 수]: [{1}/{2}]".format(self.folderText, listIndex+1, self.folder_root.childCount()))

    def folder_changedItem(self, item):
        print("folder_changedItem")
        listIndex = self.widget.currentIndex().row()

        self.folder_item = item
        self.folderText = item.text(0)
        self.file_list[listIndex].folderText = item.text(0)

        file_childCount = self.file_list[listIndex].file_root.childCount()

        for count in range(file_childCount):
            file_child = self.file_list[listIndex].file_root.child(count)
            file_child.setText(3, self.folderText)


        self.parent.statusBar().showMessage("선택 목록 : " + self.folderText)

    def folder_pressedItem(self, item):
        print("folder_pressedItem")
            
        print(item.text(0), "클릭 {0}번 폴더".format(self.widget.currentIndex().row()))
        print("folder_list : {0}개".format(len(self.folder_list)))

        listIndex = self.widget.currentIndex().row()

        self.folder_item = item
        self.folderText = item.text(0)
        self.file_list[listIndex].folderText = item.text(0)

        if item.isSelected() == True:
            self.removefolder.setEnabled(True)
            self.file_list[listIndex].newfile.setEnabled(True)
        else:
            self.removefolder.setEnabled(False)
            self.file_widget.newfile.setEnabled(False)

        # 스텟에 저장된 위젯을 선택한다(+1 은 임시위젯으로 인해 0번 자리가 채워졌기 때문)
        self.stackedwidget.setCurrentIndex(listIndex+1)

        self.parent.statusBar().showMessage("선택 목록 : {0}     [선택 행/전체 수]: [{1}/{2}]".format(self.folderText, listIndex+1, self.folder_root.childCount()))
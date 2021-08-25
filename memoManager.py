from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys

class MemoManager(QWidget):
    def __init__(self, parent):
        super(MemoManager, self).__init__(parent)
        self.parent = parent
        self.folderText = ""
        self.file_list = list()

        print("MemoManger().__init__()")
        
        # 레이아웃 배치
        # 스텍 위젯 - 여러 위젯을 한 공간에 저장해서 선택할 수 있게 한다.(위젯 배열느낌)
        self.stackedwidget = QStackedWidget()
        self.stackedwidget.addWidget(File_Widgit().widget)

        self.Hboxlayout = QHBoxLayout()
        self.Hboxlayout_Left = QHBoxLayout()
        self.Vboxlayout_Right = QVBoxLayout()

        self.folder_treewidget = QTreeWidget()

        # 마우스 트래킹
        self.folder_treewidget.setMouseTracking(True)
        # text = print('x : {0}, y : {1}'.format(self.folder_treewidget.x, self.folder_treewidget.y))
        # print(text)

        self.textEdit = QTextEdit()
        self.textEdit.setAcceptRichText(False)

        self.folder_root = QTreeWidget.invisibleRootItem(self.folder_treewidget)

        #self.folder_treewidget.itemClicked.connect(self.clickItem)
        self.folder_treewidget.itemPressed.connect(self.folder_pressedItem)
        self.folder_treewidget.itemChanged.connect(self.folder_changedItem)
        # 갔다대기만해도 호출됨 -> 다른 활용방법을 생각해봐야할듯
        #self.folder_treewidget.itemEntered.connect(self.EnteredItem)

        self.UI()
        self.contextMenu()

        self.show()

    def UI(self):
        self.folder_treewidget.setHeaderLabel("목록")
        self.folder_treewidget.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.Hboxlayout.addLayout(self.Hboxlayout_Left)
        self.Hboxlayout.setSpacing(1)

        H_splitter = QSplitter(Qt.Horizontal)
        V_splitter = QSplitter(Qt.Vertical)

        V_splitter.addWidget(self.stackedwidget)
        V_splitter.addWidget(self.textEdit)

        H_splitter.addWidget(self.folder_treewidget)
        H_splitter.addWidget(V_splitter)

        H_splitter.setStretchFactor(1, 3)
        H_splitter.setStretchFactor(0, 1)
        V_splitter.setStretchFactor(1, 1)
        
        self.Hboxlayout_Left.addWidget(H_splitter)

        self.setLayout(self.Hboxlayout)


    def contextMenu(self):
        self.newfolder = QAction("새 폴더", self.folder_treewidget)
        self.folder_treewidget.addAction(self.newfolder)

        self.removefolder = QAction("폴더 삭제", self.folder_treewidget)
        self.folder_treewidget.addAction(self.removefolder)
        self.removefolder.setEnabled(False)

        # self.foldertree_newfile = QAction("새 파일", self.folder_treewidget)
        # self.folder_treewidget.addAction(self.foldertree_newfile)
        # self.foldertree_newfile.setEnabled(False)

        # self는 실제로 bool 변수가 된다 -> 파이썬 규칙
        # 함수를 클래스 외부에 놓거나 인수를 추가할때는 lambda를 사용
        self.newfolder.triggered.connect(lambda : self.folder_contextClick())
        self.removefolder.triggered.connect(lambda : self.removefolder_contextClick())

    # 폴더추가
    def addFolder(self, title):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem()
        # 항목 속성 지정
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsEditable)
        item.setText(0, title)

        return item


    def folder_contextClick(self):
        print("newfolder.triggered.connect()")

        # 폴더 생성 시 리스트에 파일 위젯 추가
        self.file_list.append(File_Widgit())
        self.listIndex = len(self.file_list)
        print("list : {0}".format(self.listIndex))

        self.stackedwidget.addWidget(self.file_list[self.listIndex-1].widget)

        self.folder_root.addChild(self.addFolder("bird 폴더"))
        # print(self.folder_root.childCount())


    def removefolder_contextClick(self):
        print("removefolder.triggered.connect()")

        listIndex = self.folder_treewidget.currentIndex().row()

        self.folder_root.removeChild(self.folder_item)

        self.stackedwidget.setCurrentIndex(listIndex)
        self.stackedwidget.removeWidget(self.file_list[listIndex].widget)

        del self.file_list[listIndex]

        # print(self.folder_root.childCount())

    # def clickItem(self, item):
    #     print("clickItem")

    #     print(item.text(0), "클릭")
    #     print(self.folder_treewidget.currentIndex().row())

    def folder_pressedItem(self, item):
        print("pressedItem")
            
        print(item.text(0), "클릭 {0}번 트리".format(self.folder_treewidget.currentIndex().row()))

        listIndex = self.folder_treewidget.currentIndex().row()

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

    def folder_changedItem(self, item):
        print("changed")
        listIndex = self.folder_treewidget.currentIndex().row()

        self.folder_item = item
        self.folderText = item.text(0)
        self.file_list[listIndex].folderText = item.text(0)

        file_childCount = self.file_list[listIndex].file_root.childCount()

        for count in range(file_childCount):
            file_child = self.file_list[listIndex].file_root.child(count)
            file_child.setText(3, self.folderText)


        self.parent.statusBar().showMessage("선택 목록 : " + self.folderText)
        

        # if(self.newfolder.isEnabled != True):
        #     print("newfolder True")
        #     self.newfolder.setEnabled(False)

    # def EnteredItem(self, item):
    #     print("EnteredItem")
    #     print(item.text(0))
    #     print(self.folder_treewidget.currentIndex().row())


    # def contextMenuEvent(self, event):
    #     contextmenu = QMenu(self)
    #     new = contextmenu.addAction("New")
    #     action = contextmenu.exec_(self.mapToGlobal(event.pos()))


# 파일 위젯
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

    # 파일추가
    def addFile(self, title, date, modify, group):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem()

        item.setText(0, title)
        item.setText(1, date)
        item.setText(2, modify)
        item.setText(3, group)

        return item

    def contextMenu(self):
        self.newfile = QAction("새 파일", self.widget)
        self.widget.addAction(self.newfile)
        self.newfile.setEnabled(False)

        self.newfile.triggered.connect(lambda : self.file_contextClick())

    def file_contextClick(self):
        print("newfile.triggered.connect()")

        day = QDate.currentDate()
        time = QTime.currentTime()

        self.file_root.addChild(self.addFile("bird 파일", day.toString('yyyy/MM/dd') + " - " + time.toString('hh:mm:ss'), day.toString('yyyy/MM/dd')+ " - " + time.toString('hh:mm:ss'), self.folderText))


from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class memoUI:
    def __init__(self, widget):
        print("UI 생성자")
        self.widget = widget
        self.UI()

    def UI(self):
        # Widget
        # widget = QWidget()

        # 레이아웃 배치
        Hboxlayout = QHBoxLayout()
        Hboxlayout_Left = QHBoxLayout()
        Vboxlayout_Right = QVBoxLayout()

        # addWidget, addLayout 의 두번째 매개변수를 사용하여 위젯을 확장할수있다. 25 75
        Hboxlayout.addLayout(Hboxlayout_Left)
        #Hboxlayout.addLayout(Vboxlayout_Right, 75)

        # Hboxlayout 안에 배치된 위젯 또는 레이아웃의 간격이 줄어든다.
        Hboxlayout.setSpacing(1)


        H_splitter = QSplitter(Qt.Horizontal)
        V_splitter = QSplitter(Qt.Vertical)

        # UI
        #------------------------------------------------------------
        folder_treeview = self.Folder_Treeview()
        file_treeview = self.File_Treeview()
        textEdit = self.TextEdit()

        V_splitter.addWidget(file_treeview)
        V_splitter.addWidget(textEdit)

        H_splitter.addWidget(folder_treeview)
        H_splitter.addWidget(V_splitter)

        # 배치된 Widget의 비율설정
        H_splitter.setStretchFactor(1, 3)
        H_splitter.setStretchFactor(0, 1)
        V_splitter.setStretchFactor(1, 1)
        
        #Hboxlayout_Left.addWidget(self.folder_treeview)
        Hboxlayout_Left.addWidget(H_splitter)
        #Vboxlayout_Right.addWidget(self.file_treeview, 30)
        #Vboxlayout_Right.addWidget(self.textEdit, 70)

        self.widget.setLayout(Hboxlayout)


    def Folder_Treeview(self):
        treeview = QTreeWidget()
        treeview.setHeaderLabel("폴더")
        # treeview.setRootIsDecorated(False)

        self.addFolder(treeview, '폴더1')

        return treeview


    def File_Treeview(self):
        treeview = QTreeWidget()
        treeview.setHeaderLabels(["제목", "생성일", "수정일", "그룹"])

        # 최상위 항목 확장 및 축소에 대한 컨트롤 표시 여부
        # treeview.setRootIsDecorated(False)
        # 짝수 항목 배경에 색상 표시 여부
        #treeview.setAlternatingRowColors(True)

        self.addFile(treeview, '제목', '2021-07-31', '2021-07-31', 'ㅁㅁ')

        return treeview


    def TextEdit(self):
        textEdit = QTextEdit()
        textEdit.setAcceptRichText(False)

        return textEdit

    # 폴더추가
    def addFolder(self, treeview, title):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem(treeview)

        item.setText(0, title)


    # 파일추가
    def addFile(self, treeview, title, date, modify, group):
        # 트리위젯에 추가할 아이템 생성
        item = QTreeWidgetItem(treeview)

        item.setText(0, title)
        item.setText(1, date)
        item.setText(2, modify)
        item.setText(3, group)

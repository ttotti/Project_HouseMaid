# QMainWindow는 위젯을 추가할 때 setCentralWidget() 함수를 사용하여 
# 단 하나만 추가 가능하다.  layout이 아니라 위젯을 추가해야한다!!!
# 여러개의 위젯이 포함된 화면을 만들기위해서 별도의 위젯으로 만들어주어야한다.
# QWidget을 상속받은 클래스를 만들어 필요한 레이아웃과 위젯들을 추가해주고
# 이 클래스의 인스턴스를 생성해서 setCentralWidget() 함수로 메인 함수에 추가해주면 된다.
# -> QMainWindow.py 참고
# 출처: https://lifeiseggs.tistory.com/862 [어쩌다 한번 하는 삽질]

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

from MemoManager import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.memoManager = MemoManager()

        self.UI()
        self.showWindow()

        #self.memo = MemoManager()
        #self.widget = QWidget()

    def showWindow(self):
        self.setWindowTitle('House Maid')

        # 모니터의 화면 해상도를 구함
        screen_rect = app.desktop().screenGeometry()
        width = screen_rect.width()
        height = screen_rect.height()

        self.setMouseTracking(True)

        # self.setGeometry(width/2 - 500, height/2 - 400, 800, 600)
        self.setGeometry(3500, 56, 800, 600)

        self.show()

    def UI(self):
        # MemoManager 위젯 출력
        self.setCentralWidget(self.memoManager)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    #ex2 = MemoManager()
    sys.exit(app.exec_())
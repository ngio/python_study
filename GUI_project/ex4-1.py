## Ex 4-1. 절대적 배치.  https://wikidocs.net/21944
## Ex 4-2. 박스 레이아웃.
## Ex 4-3. 그리드 레이아웃.
 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
#QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 정렬하는 레이아웃 클래스 입니다.
#QHBoxLayout, QVBoxLayout 생성자는 수평, 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있습니다.


from PyQt5.QtWidgets import (QGridLayout, QLineEdit, QTextEdit)  ## Ex 4-3. 그리드 레이아웃.


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        #grid = QGridLayout()
        #self.setLayout(grid)
#
        #grid.addWidget(QLabel('Title:'), 0, 0)
        #grid.addWidget(QLabel('Author:'), 1, 0)
        #grid.addWidget(QLabel('Review:'), 2, 0)
#
        #grid.addWidget(QLineEdit(), 0, 1)
        #grid.addWidget(QLineEdit(), 1, 1)
        #grid.addWidget(QTextEdit(), 2, 1)
        
        #두 개의 버튼을 만들었습니다.
        okButton     = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        #필요한 공간을 만들기 위해 addStretch() 메서드를 사용하고, 'stretch factor'를 조절해 보겠습니다.
        hbox = QHBoxLayout() # horizontally 
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1) 
        
        vbox = QVBoxLayout() # vertically 
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        
        #라벨(label1, label2)과 푸시버튼(btn1, btn2)의 x, y 좌표를 설정함으로써 위치를 조절합니다.
        #위젯의 위치를 설정하기 위해 move() 메서드를 사용합니다.
        #라벨을 하나 만들고, x=20, y=20에 위치하도록 옮겨줍니다.
        label1 = QLabel('Label1', self) 
        label1.move(20, 20)   
        label2 = QLabel('Label2', self)
        label2.move(20, 60)
        
        #푸시버튼을 하나 만들고, x=80, y=13에 위치하도록 옮겨줍니다.
        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        ##self.setWindowTitle('QGridLayout')
        ##self.setWindowTitle('Absolute Positioning')
        self.setWindowTitle('Box Layout')
        #self.setGeometry(300, 300, 400, 200)
        self.setGeometry(200, 200, 700, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
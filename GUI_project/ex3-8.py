## Ex 3-8. 창을 화면의 가운데로.
## 창이 화면의 정가운데에 띄워집니다.
## Ex 3-9. 날짜와 시간 표시하기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow 
from PyQt5.QtCore import QDate, Qt 

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.date = QDate.currentDate()  #현재 시간
        self.initUI()

    def initUI(self):        
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        
        self.setWindowTitle('Centering')        
        self.resize(500, 350)
        self.center()                   #center() 메서드를 통해서 창이 화면의 가운데에 위치하게 됩니다.
        self.show()

    def center(self):
        qr = self.frameGeometry()                           #frameGeometry() 메서드를 이용해서 창의 위치와 크기 정보를 가져옵니다.
        cp = QDesktopWidget().availableGeometry().center()  #사용하는 모니터 화면의 가운데 위치를 파악합니다.
        qr.moveCenter(cp)        #창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())  #현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.


if __name__ == '__main__':        # 프로그램의 시작점일 때만 아래 코드 실행
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
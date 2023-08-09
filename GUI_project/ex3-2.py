## Ex 3-2. 어플리케이션 아이콘 넣기. QIcon
## Ex 3-3. 창 닫기.  QPushButton
## Ex 3-4. 툴팁 나타내기.QToolTip

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


# 2023-05-18 ngio add
# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
#현재 폴더 경로; 작업 폴더 기준
print(os.getcwd())
#현재 파일의 폴더 경로; 작업 파일 기준
real_path = os.path.dirname(os.path.realpath(__file__))
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path)



class MyApp(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    
    QToolTip.setFont(QFont('SansSerif', 10))
    self.setToolTip('This is a <b>QWidget</b> widget')
    
    
    btn = QPushButton('Button', self)
    btn.setToolTip('This is a <b>QPushButton</b> widget')
    btn.move(150, 50)
    btn.resize(btn.sizeHint())
            
    btn = QPushButton('Quit', self)
    btn.setToolTip('This is a <b>Quit Button</b> widget')
    btn.move(50, 50)
    btn.resize(btn.sizeHint())
    btn.clicked.connect(QCoreApplication.instance().quit)
    
    #self.setWindowTitle('Icon')
    self.setWindowIcon(QIcon('./img/web.png'))
    self.setWindowTitle('Quit Button')
    self.setGeometry(300, 300, 300, 200)
    self.show()
 
  
        

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())
  
  
  
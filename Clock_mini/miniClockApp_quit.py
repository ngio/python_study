# PyQt5 초미니 시계 & 전체 화면 토글 & 드래그 & 종료 버튼 프로그램


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt, QPoint
from PyQt5.QtGui import QFont

class MiniClockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.is_fullscreen = False # 전체 화면 상태 추적 변수
        self.old_pos = None        # 창 이동을 위한 이전 마우스 위치 저장
        
        self.initUI()
        
        # 창 플래그 설정: 프레임 없이, 항상 위에, 배경 투명 (초미니 시계에 적합)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) 
        self.setAttribute(Qt.WA_TranslucentBackground) 

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('초미니 시계')
        self.setGeometry(100, 100, 300, 100) # x, y, width(300px 고정), height (초기 크기)
        self.setMinimumWidth(300) # 최소 넓이 300px
        self.setMaximumWidth(300) # 최대 넓이 300px (고정)

        # 메인 레이아웃 (세로 방향)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 시간 표시 레이블
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter) # 중앙 정렬
        self.time_label.setFont(QFont('Arial', 40)) # 폰트 및 크기 설정
        self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,150); border-radius: 10px;") # 텍스트 색상, 배경 투명도 있는 검정, 둥근 모서리

        main_layout.addWidget(self.time_label)

        # 버튼들을 위한 수평 레이아웃
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout) # 메인 레이아웃에 버튼 레이아웃 추가

        # 풀스크린 버튼
        self.fullscreen_button = QPushButton('Full Screen', self)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen) # 버튼 클릭 시 함수 연결
        self.fullscreen_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* 초록색 */
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        button_layout.addWidget(self.fullscreen_button)

        # 종료 버튼 추가
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(QApplication.instance().quit) # 앱 종료 연결
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; /* 빨간색 */
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        button_layout.addWidget(self.exit_button)

        # 시간 업데이트 타이머 설정
        timer = QTimer(self)
        timer.timeout.connect(self.update_time) # 1초마다 update_time 함수 호출
        timer.start(1000) # 1000ms = 1초

        # 초기 시간 업데이트
        self.update_time()

    def update_time(self):
        # 현재 시간 가져와서 레이블에 표시
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss') # 시간:분:초 형식
        self.time_label.setText(display_text)

    def toggle_fullscreen(self):
        if not self.is_fullscreen:
            # 전체 화면으로 전환
            self.showFullScreen()
            self.time_label.setFont(QFont('Arial', 150)) # 전체 화면 시 폰트 크기 키우기
            self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,200);") # 배경 불투명도 조절
            self.fullscreen_button.setText('Exit Full Screen')
            self.exit_button.setVisible(False) # 전체 화면 시 종료 버튼 숨김 (선택 사항)
            self.is_fullscreen = True
        else:
            # 원래 크기로 복귀
            self.showNormal()
            self.setGeometry(100, 100, 300, 100) # 원래 위치 및 크기 (넓이 300px 고정)
            self.time_label.setFont(QFont('Arial', 40)) # 폰트 크기 원래대로
            self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,150); border-radius: 10px;")
            self.fullscreen_button.setText('Full Screen')
            self.exit_button.setVisible(True) # 원래 크기 시 종료 버튼 다시 보이기
            self.is_fullscreen = False
            
    # --- 마우스 드래그로 창 이동 기능 추가 ---
    def mousePressEvent(self, event):
        # 전체 화면이 아닐 때만 드래그 가능
        if event.button() == Qt.LeftButton and not self.is_fullscreen:
            self.old_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        # 전체 화면이 아닐 때만 드래그 가능
        if event.buttons() == Qt.LeftButton and not self.is_fullscreen:
            if self.old_pos is not None:
                self.move(event.globalPos() - self.old_pos)
                event.accept()

    def mouseReleaseEvent(self, event):
        # 드래그 끝
        if event.button() == Qt.LeftButton:
            self.old_pos = None
            event.accept()

# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock_app = MiniClockApp()
    clock_app.show()
    sys.exit(app.exec_())



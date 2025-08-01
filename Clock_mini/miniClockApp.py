import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont

class MiniClockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.is_fullscreen = False # 전체 화면 상태 추적 변수
        self.initUI()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # 프레임 없이 항상 위에
        self.setAttribute(Qt.WA_TranslucentBackground) # 배경 투명하게 (선택 사항)

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('초미니 시계')
        self.setGeometry(100, 100, 200, 100) # x, y, width, height (초기 크기)

        # 메인 레이아웃 (세로 방향)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 시간 표시 레이블
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter) # 중앙 정렬
        self.time_label.setFont(QFont('Arial', 40)) # 폰트 및 크기 설정
        self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,150); border-radius: 10px;") # 텍스트 색상, 배경 투명도 있는 검정, 둥근 모서리

        main_layout.addWidget(self.time_label)

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
        main_layout.addWidget(self.fullscreen_button)

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
            self.is_fullscreen = True
        else:
            # 원래 크기로 복귀
            self.showNormal()
            self.setGeometry(100, 100, 200, 100) # 원래 위치 및 크기 (필요시 조절)
            self.time_label.setFont(QFont('Arial', 40)) # 폰트 크기 원래대로
            self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,150); border-radius: 10px;")
            self.fullscreen_button.setText('Full Screen')
            self.is_fullscreen = False

# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock_app = MiniClockApp()
    clock_app.show()
    sys.exit(app.exec_())

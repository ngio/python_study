# pyinstaller --onefile --windowed miniClockApp_finance_003.py
# 시간과 슬라이드 바 사이에 공백이 없이 100% fill 로 처리하는데 시계는 center에 위치하고 아래의 버튼과도 100% fill.
# 공백을 완전히 없애고 100% 채움(fill) 처리하며, 시계는 중앙에 위치하도록 수정
"""
초미니 시계가 나타나고, 상단에는 주식의 이름, 현재가, 목표가, 그리고 차이가 함께 표시되며 주기적으로 순환합니다.
'Full Screen' 버튼을 눌러 전체 화면으로 전환하면 전체 배경이 불투명 검은색으로 변하고, 주식 및 시계 정보가 더 크게 표시됩니다. 
바탕화면을 클릭하면 다시 원래 크기로 돌아옵니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt5.QtCore import QTimer, QTime, Qt, QPoint, QEvent
from PyQt5.QtGui import QFont, QColor
import yfinance as yf # 주식 데이터 가져오기 위한 라이브러리

class MiniClockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.is_fullscreen = False  # 전체 화면 상태 추적 변수
        self.old_pos = None         # 창 이동을 위한 이전 마우스 위치 저장
        
        # 모니터링할 주식 목록과 목표 가격 설정
        self.stocks_to_monitor = {
            '007310.KS': ('오뚜기', 396167),
            '215200.KQ': ('메가스터디교육', 36900),
            '005930.KS': ('삼성전자', 49900),
            '005387.KS': ('현대차2우B', 133300),
            '138910.KS': ('KODEX 구리 선물 ETF', 7190),
            'META': ('메타', 450.80),
            'AMZN': ('아마존', 151.61)
        }
        self.formatted_stock_data = [] # 주식 전체 정보를 저장할 리스트
        self.current_stock_index = 0 # 현재 표시 중인 주식 정보 인덱스

        self.initUI()
        
        # 창 플래그 설정: 프레임 없이, 항상 위에, 배경 투명 (초미니 시계에 적합)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) 
        self.setAttribute(Qt.WA_TranslucentBackground) 

        # 전체화면 시 바탕화면 클릭 감지를 위한 이벤트 필터 설치
        QApplication.instance().installEventFilter(self)

        # 1초마다 시간 업데이트 타이머
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time) 
        self.time_timer.start(1000) 

        # 30초마다 주식 가격 데이터 가져오기 타이머
        self.stock_fetch_timer = QTimer(self)
        self.stock_fetch_timer.timeout.connect(self.fetch_and_process_stock_prices)
        self.stock_fetch_timer.start(30000) # 30초마다 업데이트

        # 3초마다 주식 정보 순환 표시 타이머
        self.stock_display_timer = QTimer(self)
        self.stock_display_timer.timeout.connect(self.display_next_stock_info)
        self.stock_display_timer.start(3000) # 3초마다 순환

        # 초기 업데이트
        self.update_time()
        self.fetch_and_process_stock_prices() # 앱 시작 시 바로 주식 데이터 가져오기

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('초미니 시계 & 주식 모니터')
        self.setGeometry(100, 100, 400, 400) # 초기 위치 및 크기
        self.setMinimumSize(400, 400) # 최소 크기 400x400으로 고정

        # 메인 레이아웃 (세로 방향)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        # 전체 레이아웃의 안쪽 여백과 위젯 간 간격을 모두 0으로 설정하여 꽉 차게 만듦
        main_layout.setContentsMargins(0, 0, 0, 0) 
        main_layout.setSpacing(0) 

        # 주식 정보 표시 레이블
        self.stock_info_label = QLabel(self)
        self.stock_info_label.setAlignment(Qt.AlignCenter) # 중앙 정렬
        self.stock_info_label.setFont(QFont('Arial', 12)) # 폰트 크기 12px
        self.stock_info_label.setStyleSheet("color: #FFFFFF; background-color: rgba(0,0,0,180); padding: 0px;") 
        # 수직 방향으로 확장 가능하도록 설정 (Vertical, Expanding)
        self.stock_info_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        main_layout.addWidget(self.stock_info_label)

        # 시간 표시 레이블
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter) # 중앙 정렬
        self.time_label.setFont(QFont('Arial', 40)) # 폰트 및 크기 설정
        self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,150); padding: 0px;") 
        # 수직 방향으로 확장 가능하도록 설정 (Vertical, Expanding)
        self.time_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        main_layout.addWidget(self.time_label)

        # 버튼들을 위한 수평 레이아웃
        button_layout = QHBoxLayout()
        # 버튼 레이아웃은 수직으로 고정 (Fixed) 또는 선호(Preferred)로 설정하여
        # 남은 공간을 주식 정보와 시계가 나눠 갖도록 함
        button_layout.setSizeConstraint(QHBoxLayout.SetFixedSize) # 버튼 레이아웃이 자체 크기를 유지하도록 설정
        main_layout.addLayout(button_layout) 

        # 풀스크린 버튼
        self.fullscreen_button = QPushButton('Full Screen', self)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen) 
        self.fullscreen_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 0px; 
                padding: 10px; 
                height: 50px; /* 버튼 높이 고정 */
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        button_layout.addWidget(self.fullscreen_button)

        # 종료 버튼 추가
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(QApplication.instance().quit) 
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border-radius: 0px; 
                padding: 10px; 
                height: 50px; /* 버튼 높이 고정 */
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        button_layout.addWidget(self.exit_button)

    def update_time(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss') 
        self.time_label.setText(display_text)

    def fetch_and_process_stock_prices(self):
        temp_stock_data = []
        for ticker, (name, target_price) in self.stocks_to_monitor.items():
            try:
                stock_info = yf.Ticker(ticker).history(period='1d')
                if not stock_info.empty:
                    current_price = stock_info['Close'].iloc[-1]
                    price_diff = current_price - target_price

                    diff_color_code = "#AAAAAA" 
                    if price_diff > 0:
                        diff_text = f'+{price_diff:,.2f}'
                        diff_color_code = "#FF0000" 
                    elif price_diff < 0:
                        diff_text = f'{price_diff:,.2f}' 
                        diff_color_code = "#0000FF" 
                    else:
                        diff_text = f'0.00'
                    
                    formatted_text = (
                        f'<span style="font-size:14px; font-weight:bold;">{name}</span><br>'
                        f'<span style="font-size:12px;">현재가: {current_price:,.2f} | '
                        f'목표가: {target_price:,.2f} | '
                        f'<span style="color:{diff_color_code};">차이: {diff_text}</span></span>'
                    )
                    temp_stock_data.append((formatted_text))

                else:
                    temp_stock_data.append(f'{name}: 데이터 없음')
            except Exception as e:
                temp_stock_data.append(f'{name}: 오류 발생')
                print(f"Error fetching {ticker}: {e}")
        
        self.formatted_stock_data = temp_stock_data
        self.current_stock_index = 0
        self.display_next_stock_info() 

    def display_next_stock_info(self):
        if not self.formatted_stock_data:
            self.stock_info_label.setText("주식 정보 없음")
            self.stock_info_label.setStyleSheet("color: #AAAAAA; background-color: rgba(0,0,0,180); padding: 0px;")
            return

        text = self.formatted_stock_data[self.current_stock_index]
        self.stock_info_label.setText(text)
        
        self.current_stock_index = (self.current_stock_index + 1) % len(self.formatted_stock_data)

    def toggle_fullscreen(self):
        if not self.is_fullscreen:
            self.showFullScreen()
            # 전체 화면 시 폰트 크기 및 배경 불투명도 조절
            self.time_label.setFont(QFont('Arial', 200)) 
            self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,220); padding: 0px;")
            
            # 전체 화면 시 주식 정보 폰트 크기 키우기 및 배경 색상 변경
            self.stock_info_label.setFont(QFont('Arial', 40)) 
            self.stock_info_label.setStyleSheet("color: #FFFFFF; background-color: rgba(0,0,0,220); padding: 0px;")
            
            # 전체 앱의 배경을 불투명 검은색으로 변경
            QApplication.instance().setStyleSheet("QWidget { background-color: rgba(0,0,0,220); }")

            self.fullscreen_button.setText('Exit Full Screen')
            self.exit_button.setVisible(False) 
            self.is_fullscreen = True
        else:
            self.showNormal()
            self.setGeometry(100, 100, 400, 400) 
            
            # 원래 폰트 크기 및 배경 불투명도 복원
            self.time_label.setFont(QFont('Arial', 40))
            self.time_label.setStyleSheet("color: white; background-color: rgba(0,0,0,150); padding: 0px;")
            
            # 주식 정보 폰트 크기 원래대로 및 배경색 복원
            self.stock_info_label.setFont(QFont('Arial', 12)) 
            self.stock_info_label.setStyleSheet("color: #FFFFFF; background-color: rgba(0,0,0,180); padding: 0px;")
            
            # 전체 앱의 배경을 원래대로 복원 (투명)
            QApplication.instance().setStyleSheet("QWidget { background-color: transparent; }")

            self.fullscreen_button.setText('Full Screen')
            self.exit_button.setVisible(True) 
            self.is_fullscreen = False
            
    # --- 마우스 드래그로 창 이동 기능 ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.is_fullscreen:
            self.old_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and not self.is_fullscreen:
            if self.old_pos is not None:
                self.move(event.globalPos() - self.old_pos)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None
            event.accept()

    # --- 이벤트 필터: 전체화면일 때 외부 클릭 감지 ---
    def eventFilter(self, obj, event):
        if self.is_fullscreen and event.type() == QEvent.MouseButtonPress:
            if not self.rect().contains(self.mapFromGlobal(event.globalPos())):
                self.toggle_fullscreen() 
                return True 
        return super().eventFilter(obj, event) 

# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 애플리케이션 전체 기본 스타일 시트 (창 배경은 기본 투명)
    app.setStyleSheet("""
        QWidget {
            background-color: transparent; /* 기본 창 배경 투명 */
            color: #EEEEEE; /* 기본 글자색 밝게 */
            font-family: Arial;
        }
        QPushButton {
            font-size: 14px;
        }
    """)
    
    clock_app = MiniClockApp()
    clock_app.show()
    sys.exit(app.exec_())

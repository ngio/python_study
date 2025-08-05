# 대상 주식5개(오뚜기, 메가스터디교육,삼성전자,현대차2우B,메타)의 의 현재 가격과 목표 가격을 실시간으로 보여주는 qt 프로그램
# pip install PyQt5 yfinance

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QFrame
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QColor
import yfinance as yf

class StockMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.stock_widgets = {} # 주식 정보를 담을 위젯 딕셔너리
        self.load_stocks()
        
        # 5초마다 주식 가격 업데이트 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stock_prices)
        self.timer.start(5000) # 5초 (5000 밀리초)마다 업데이트

        # 초기 가격 업데이트
        self.update_stock_prices()

    def initUI(self):
        self.setWindowTitle('실시간 주식 모니터')
        self.setGeometry(100, 100, 500, 600) # 초기 윈도우 크기

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 타이틀 레이블
        title_label = QLabel('실시간 주식 가격 모니터')
        title_label.setFont(QFont('Arial', 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(10)

        # 스크롤 가능한 영역 설정
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # 스크롤 영역에 들어갈 위젯 (내용물)
        self.content_widget = QWidget()
        scroll_area.setWidget(self.content_widget)

        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignTop) # 위젯들을 상단에 정렬

    def load_stocks(self):
        # 모니터링할 주식 목록과 목표 가격 설정
        # key: 티커, value: (한국어 이름, 목표 가격)
        self.stocks_to_monitor = {
            '007310.KS': ('오뚜기', 375500),
            '072870.KQ': ('메가스터디교육', 36900),
            '005930.KS': ('삼성전자', 49900),
            '005387.KS': ('현대차2우B', 133300),
            'META': ('메타', 450.80)
        }

        # 각 주식에 대한 위젯 생성
        for ticker, (name, target_price) in self.stocks_to_monitor.items():
            stock_frame = QFrame(self.content_widget)
            stock_frame.setFrameShape(QFrame.StyledPanel)
            stock_frame.setFrameShadow(QFrame.Raised)
            stock_frame.setStyleSheet("background-color: #333333; border-radius: 8px; padding: 10px; margin-bottom: 5px;")
            
            stock_layout = QVBoxLayout(stock_frame)

            name_label = QLabel(f'<b>{name}</b> ({ticker})')
            name_label.setFont(QFont('Arial', 14))
            name_label.setStyleSheet("color: #FFFFFF;") # 흰색
            stock_layout.addWidget(name_label)

            price_layout = QHBoxLayout()
            current_price_label = QLabel('현재가: Calculating...')
            current_price_label.setFont(QFont('Arial', 16, QFont.Bold))
            current_price_label.setStyleSheet("color: #00FF00;") # 밝은 초록색
            price_layout.addWidget(current_price_label)

            target_label = QLabel(f'목표가: {target_price:,}')
            target_label.setFont(QFont('Arial', 14))
            target_label.setStyleSheet("color: #ADD8E6;") # 연한 파란색
            price_layout.addWidget(target_label)
            
            stock_layout.addLayout(price_layout)

            # 위젯들을 딕셔너리에 저장하여 나중에 업데이트할 때 사용
            self.stock_widgets[ticker] = {
                'frame': stock_frame,
                'current_price_label': current_price_label,
                'target_price': target_price # 목표가는 라벨이 아니라 값 자체를 저장
            }
            self.content_layout.addWidget(stock_frame)
    
    def update_stock_prices(self):
        # 모든 주식에 대해 가격 업데이트 시도
        for ticker, widgets in self.stock_widgets.items():
            try:
                stock_info = yf.Ticker(ticker).history(period='1d')
                if not stock_info.empty:
                    current_price = stock_info['Close'].iloc[-1]
                    widgets['current_price_label'].setText(f'현재가: {current_price:,.2f}')

                    # 목표 가격 대비 색상 변경
                    target_price = widgets['target_price']
                    if current_price >= target_price:
                        widgets['current_price_label'].setStyleSheet("color: #FFD700;") # 목표가 도달: 금색
                    elif current_price < target_price * 0.9: # 목표가의 90% 이하
                        widgets['current_price_label'].setStyleSheet("color: #FF6347;") # 주황색 (하락)
                    else:
                        widgets['current_price_label'].setStyleSheet("color: #00FF00;") # 기본: 밝은 초록색 (중간)

                else:
                    widgets['current_price_label'].setText('현재가: N/A')
                    widgets['current_price_label'].setStyleSheet("color: #AAAAAA;") # 회색
            except Exception as e:
                widgets['current_price_label'].setText('현재가: Error')
                widgets['current_price_label'].setStyleSheet("color: #FF0000;") # 빨간색
                print(f"Error fetching {ticker}: {e}")

# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Qt 애플리케이션 기본 스타일 시트 (선택 사항)
    app.setStyleSheet("""
        QWidget {
            background-color: #222222; /* 전체 배경 어둡게 */
            color: #EEEEEE; /* 기본 글자색 밝게 */
            font-family: Arial;
        }
        QLabel {
            padding: 2px;
        }
        QScrollArea {
            border: 1px solid #555555;
            border-radius: 5px;
        }
    """)
    
    stock_app = StockMonitorApp()
    stock_app.show()
    sys.exit(app.exec_())

"""_summary_

주식 가격을 실시간으로 확인하고 목표 가격에 도달하면 알림을 보내는 프로그램입니다.
"""

import yfinance as yf
import time
from plyer import notification

# 설정
stock_symbol = "AAPL"          # 주식 심볼 (예: AAPL, TSLA, GOOG 등)
target_price = 170.00          # 알림을 받고 싶은 목표 가격
check_interval = 60            # 가격 확인 간격 (초 단위)

# 코카콜라 티커
coca_cola = yf.Ticker("KO")
# 코카콜라 주식 가격 가져오기
coca_cola_price = coca_cola.history(period="1d")["Close"].iloc[-1]

print(f"현재 {coca_cola_price} 가격: ${coca_cola_price:.2f}")
            

def send_notification(current_price):
    notification.notify(
        title=f"{stock_symbol} 목표가 도달!",
        message=f"현재 가격: ${current_price:.2f}",
        timeout=5
    )

def track_stock():
    while True:
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period="1d", interval="1m")
        if not data.empty:
            current_price = data['Close'].iloc[-1]
            print(f"현재 {stock_symbol} 가격: ${current_price:.2f}")
            
            if current_price >= target_price:
                send_notification(current_price)
                break
        else:
            print("데이터를 불러올 수 없습니다.")

        time.sleep(check_interval)

if __name__ == "__main__":
    track_stock()

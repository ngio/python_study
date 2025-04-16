""" # 코카콜라 주가 추이 (6개월 & 1년)
"""

# 코카콜라 주가 추이 (6개월 & 1년)



import yfinance as yf
import matplotlib.pyplot as plt

# 티커 불러오기
ko = yf.Ticker("KO")

# 6개월 데이터
data_6m = ko.history(period="6mo")
# 1년 데이터
data_1y = ko.history(period="1y")

# 그래프 설정
plt.figure(figsize=(14,6))

# 6개월 그래프
plt.subplot(1, 2, 1)
plt.plot(data_6m.index, data_6m['Close'], label='Close Price')
plt.title("Coca-Cola (KO) - Last 6 Months")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)

# 1년 그래프
plt.subplot(1, 2, 2)
plt.plot(data_1y.index, data_1y['Close'], label='Close Price', color='orange')
plt.title("Coca-Cola (KO) - Last 1 Year")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)

plt.tight_layout()
plt.show()


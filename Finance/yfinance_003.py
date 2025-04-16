# 코카콜라 주가 추이 (6개월, 1년, 3년)
# 최고/최저가 출력

import yfinance as yf
import matplotlib.pyplot as plt

# 티커 불러오기
ko = yf.Ticker("KO")

# 각 기간별 데이터 가져오기
data_6m = ko.history(period="6mo")
data_1y = ko.history(period="1y")
data_3y = ko.history(period="3y")

# 최고/최저가 계산 함수
def get_high_low(data):
    high = data['Close'].max()
    low = data['Close'].min()
    return high, low

# 각각 계산
high_6m, low_6m = get_high_low(data_6m)
high_1y, low_1y = get_high_low(data_1y)
high_3y, low_3y = get_high_low(data_3y)

# 그래프 그리기
plt.figure(figsize=(18, 6))

# 6개월
plt.subplot(1, 3, 1)
plt.plot(data_6m.index, data_6m['Close'], label='Close Price')
plt.title("KO - Last 6 Months")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
# 텍스트 추가
plt.text(0.5, -0.15, f"High: ${high_6m:.2f} | Low: ${low_6m:.2f}", 
         ha='center', va='center', transform=plt.gca().transAxes, fontsize=10)

# 1년
plt.subplot(1, 3, 2)
plt.plot(data_1y.index, data_1y['Close'], label='Close Price', color='orange')
plt.title("KO - Last 1 Year")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.text(0.5, -0.15, f"High: ${high_1y:.2f} | Low: ${low_1y:.2f}", 
         ha='center', va='center', transform=plt.gca().transAxes, fontsize=10)

# 3년
plt.subplot(1, 3, 3)
plt.plot(data_3y.index, data_3y['Close'], label='Close Price', color='green')
plt.title("KO - Last 3 Years")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.text(0.5, -0.15, f"High: ${high_3y:.2f} | Low: ${low_3y:.2f}", 
         ha='center', va='center', transform=plt.gca().transAxes, fontsize=10)

plt.tight_layout()
plt.show()


# 이제 코카콜라(KO), 인텔(INTC), 맥도날드(MCD), **몬스터 베버리지(MNST)** 각각에 대해
# 6개월 / 1년 / 3년 가격 추이 그래프
# 각 그래프 하단에 최고/최저가 텍스트
# 이미지로 저장 (파일명: 주식코드_년월일.png)

  
import os
from pathlib import Path 

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# 저장 날짜 포맷
today = datetime.today().strftime('%Y%m%d')

# 티커 리스트
tickers = ['KO', 'INTC', 'MCD', 'MNST']

# output 폴더 생성 (없으면)
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)


# 함수 정의
def plot_and_save(ticker):
    stock = yf.Ticker(ticker)
    
    # 데이터 수집
    data_6m = stock.history(period="6mo")
    data_1y = stock.history(period="1y")
    data_3y = stock.history(period="3y")
    
    # 최고/최저가 계산
    def get_high_low(data):
        return data['Close'].max(), data['Close'].min()
    
    high_6m, low_6m = get_high_low(data_6m)
    high_1y, low_1y = get_high_low(data_1y)
    high_3y, low_3y = get_high_low(data_3y)

    # 그래프 그리기
    plt.figure(figsize=(18, 6))

    # 6개월
    plt.subplot(1, 3, 1)
    plt.plot(data_6m.index, data_6m['Close'], label='Close Price')
    plt.title(f"{ticker} - Last 6 Months")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.text(0.5, -0.15, f"High: ${high_6m:.2f} | Low: ${low_6m:.2f}", 
             ha='center', va='center', transform=plt.gca().transAxes, fontsize=10)

    # 1년
    plt.subplot(1, 3, 2)
    plt.plot(data_1y.index, data_1y['Close'], label='Close Price', color='orange')
    plt.title(f"{ticker} - Last 1 Year")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.text(0.5, -0.15, f"High: ${high_1y:.2f} | Low: ${low_1y:.2f}", 
             ha='center', va='center', transform=plt.gca().transAxes, fontsize=10)

    # 3년
    plt.subplot(1, 3, 3)
    plt.plot(data_3y.index, data_3y['Close'], label='Close Price', color='green')
    plt.title(f"{ticker} - Last 3 Years")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.text(0.5, -0.15, f"High: ${high_3y:.2f} | Low: ${low_3y:.2f}", 
             ha='center', va='center', transform=plt.gca().transAxes, fontsize=10)

    plt.tight_layout()
    
    # 이미지 저장
    # 저장 경로 설정
    filename = f"{ticker}_{today}.png"
    save_path = os.path.join(output_dir, filename)
    
    plt.savefig(save_path)
    plt.close()
    print(f"📁 저장 완료: {save_path}")

# 모든 티커 처리
for ticker in tickers:
    plot_and_save(ticker)


# 이미지 폴더
output_dir = "./output"
image_files = [f for f in os.listdir(output_dir) if f.endswith(".png")]


# HTML 생성
html_path = os.path.join(output_dir, "index.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write("<html><head><title>Stock Charts</title></head><body style='font-family:sans-serif;'>\n")
    f.write("<h1>📊 생성된 주가 그래프</h1>\n")
    for image in image_files:
        f.write(f"<h3>{image}</h3>\n")
        f.write(f"<img src='{image}' alt='{image}' style='max-width:100%; height:auto; margin-bottom:40px;'><hr>\n")
    f.write("</body></html>")

print(f"✅ HTML 페이지 생성 완료: {html_path}")


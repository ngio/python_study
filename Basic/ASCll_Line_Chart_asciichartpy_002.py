"""
    **asciichartpy**는 파이썬에서 터미널(콘솔) 환경에 깔끔하고 읽기 쉬운 텍스트 기반의 ASCII 아트 그래프를 그려주는 라이브러리입니다. 📈
"""

import asciichartpy as ac

series1 = [20, 25, 22, 28, 30, 24, 35, 32, 26]
series2 = [10, 15, 12, 18, 20, 14, 25, 22, 16]

# 두 개의 계열을 하나의 차트에 표시
print(ac.plot([series1, series2], {'height': 15, 'colors': [ac.red, ac.blue]}))

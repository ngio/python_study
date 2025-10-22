# ASCll_Line_Chart_asciichartpy_001.py

"""
    **asciichartpy**는 파이썬에서 터미널(콘솔) 환경에 깔끔하고 읽기 쉬운 텍스트 기반의 ASCII 아트 그래프를 그려주는 라이브러리입니다. 📈
"""

import asciichartpy 

data = [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
print("ASCll Line Chart Example")
print(asciichartpy.plot(data, {'height': 10}))


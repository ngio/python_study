"""
    pip install plotly
    Plotly를 사용한 게이지 차트 (Gauge Chart) 생성 예제 (Python Code)

    https://plotly.com/python-api-reference/plotly.graph_objects.html

    Plotly는 인터렉티브한 시각화가 가능한 파이썬 그래픽 라이브러리 입니다. 
    기본적인 시각화부터 통계, 재무, 지리 과학 및 3-dimensional 을 포함한 40개 이상의 차트 타입을 제공하는 오픈소스 입니다. 
    기본적으로 쥬피터 노트북에 시각화가 가능하며 인터렉티브한 dashboards 위해 Dash 또는 Chart Studio와 같은 라이브러리와 통합 및 확장이 가능합니다.
"""

import plotly.graph_objects as go
import plotly.offline as pyo

# --- 게이지 차트 데이터 설정 ---
value = 75  # 현재 값 (예: 판매 목표 달성률 75%)
max_value = 100 # 최대 값
title_text = "판매 목표 달성률"
unit_text = "%"

# --- Plotly Indicator 객체 생성 ---
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta", # 게이지, 숫자, 델타(변화량)를 표시
    value = value,
    number = {'suffix': unit_text}, # 숫자 뒤에 단위 표시
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': title_text, 'font': {'size': 24}},
    
    # --- 게이지 설정 ---
    gauge = {
        'shape': "angular", # 게이지 모양 (angular: 원형, bullet: 수평 막대)
        'axis': {'range': [None, max_value], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"}, # 현재 값 막대의 색상
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        
        # --- 구간별 색상 설정 (Thresholds) ---
        'steps': [
            {'range': [0, 50], 'color': "lightgray"},   # 0% ~ 50%
            {'range': [50, 85], 'color': "lightblue"},  # 50% ~ 85%
            {'range': [85, 100], 'color': "yellowgreen"} # 85% ~ 100% (목표 근접/달성)
        ],
        
        # --- 목표선 설정 (Threshold) ---
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75, # 목표선의 두께
            'value': 90 # 목표 값 (예: 90%)
        }
    }
))

# --- 레이아웃 설정 ---
fig.update_layout(
    paper_bgcolor = "white", # 배경 색상
    font = {'color': "black", 'family': "Arial"},
    margin = dict(l=20, r=20, t=50, b=20) # 여백 설정
)

# --- 차트 출력 (브라우저에서 확인) ---
# pyo.plot(fig, filename='gauge_chart.html')

# --- (선택 사항) Notebook 환경에서 출력 ---
fig.show()

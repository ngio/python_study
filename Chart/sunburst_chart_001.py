# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

"""
    Sunburst Chart는 계층적 데이터를 시각화하는 데 사용되는 원형 차트입니다. 
    데이터의 루트는 중앙에 있고, 
    계층적으로 데이터를 표현하며, 내부에서 외부로 확장됩니다. 
    각 섹션은 데이터를 크기별로 구분하여 보여줍니다.
"""

import plotly.express as px
from PIL import Image

# 계층적 데이터 정의
data = dict(
    labels=["Root", "Child 1", "Child 2", "Grandchild 1", "Grandchild 2", "Grandchild 3"],
    parents=["", "Root", "Root", "Child 1", "Child 1", "Child 2"],
    values=[10, 5, 5, 2, 3, 5]
)

# Sunburst Chart 생성
fig = px.sunburst(
    data,
    names='labels',
    parents='parents',
    values='values',
    title="Sunburst Chart Example"
)

# fig.show()

# Sunburst Chart를 이미지로 저장
image_path = "sunburst_chart_001.png"
fig.write_image(image_path, width=800, height=600)
print(f"Sunburst chart saved as '{image_path}'")

# 저장된 이미지 출력
image = Image.open(image_path)
image.show()  # 기본 이미지 뷰어로 열기


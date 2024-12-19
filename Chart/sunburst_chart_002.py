# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


import plotly.graph_objects as go
from PIL import Image


# Sunburst Chart 데이터 정의
fig = go.Figure(go.Sunburst(
    labels=["Root", "Child 1", "Child 2", "Grandchild 1", "Grandchild 2", "Grandchild 3"],
    parents=["", "Root", "Root", "Child 1", "Child 1", "Child 2"],
    values=[10, 5, 5, 2, 3, 5],  # 값은 각 섹션의 크기를 정의
    branchvalues="total"  # 'total' 또는 'remainder'
))

# 레이아웃 설정
fig.update_layout(
    title="Sunburst Chart Example",
    margin=dict(t=50, l=25, r=25, b=25)
)

# Sunburst Chart를 이미지로 저장
image_path = "sunburst_chart_002.png"
fig.write_image(image_path, width=800, height=600)
print(f"Sunburst chart saved as '{image_path}'")

#fig.write_image("sunburst_chart.png", width=800, height=600)  # PNG 파일로 저장
#print("Sunburst chart saved as 'sunburst_chart.png'")


# 저장된 이미지 출력
image = Image.open(image_path)
image.show()  # 기본 이미지 뷰어로 열기
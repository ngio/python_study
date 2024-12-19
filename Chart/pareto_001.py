# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

"""_summary_
Pareto Chart를 만드는 방법입니다. matplotlib 라이브러리를 사용하여 구현합니다. 
Pareto Chart는 데이터를 막대 그래프와 누적 비율 선 그래프로 시각화한 차트입니다.
"""

import matplotlib.pyplot as plt
import numpy as np 

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [50, 30, 10, 7, 3]

# Sort values and categories in descending order
sorted_indices = np.argsort(values)[::-1]
values = np.array(values)[sorted_indices]
categories = np.array(categories)[sorted_indices]

# Calculate cumulative percentage
cumulative_percentage = np.cumsum(values) / np.sum(values) * 100

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart (primary y-axis)
bars = ax1.bar(categories, values, color='skyblue', alpha=0.7, label='Values')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Line chart (secondary y-axis)
ax2 = ax1.twinx()
line = ax2.plot(categories, cumulative_percentage, color='red', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.axhline(80, color='green', linestyle='--', alpha=0.5, label='80% Line')

# Add text labels to the line chart
for i, value in enumerate(cumulative_percentage):
    ax2.text(i, value + 2, f"{value:.1f}%", ha='center', color='red')

# Title and legend
plt.title('Pareto Chart')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Pareto Chart를 이미지로 저장
image_path = "pareto_chart_001.png"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
print(f"Pareto chart saved as '{image_path}'")

# Show the chart
plt.show()

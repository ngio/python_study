import seaborn as sns           # pip install seaborn
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 준비
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 25, 15, 30]

# 데이터프레임 생성 (seaborn에서는 DataFrame 사용이 편리함)
data = pd.DataFrame({
    'Categories': categories,
    'Values': values
})

# seaborn 스타일 설정
sns.set(style="whitegrid") 

# 바 그래프 생성
plt.figure(figsize=(8, 6))
sns.barplot(x='Categories', y='Values', data=data, palette="viridis")

# 그래프에 라벨 추가
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Example with Seaborn')

# 그래프 표시
plt.show()
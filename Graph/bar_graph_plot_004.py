from bokeh.plotting import figure, show #pip install bokeh
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource

# Bokeh 노트북 출력 설정 (Jupyter Notebook 사용 시)
output_notebook()

# 데이터 준비
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 25, 15, 30]

# 데이터 소스 설정
source = ColumnDataSource(data=dict(categories=categories, values=values))

# Bokeh Figure 생성
p = figure(x_range=categories, height=400, title="Bar Graph Example with Bokeh", toolbar_location=None, tools="")

# 바 그래프 추가
p.vbar(x='categories', top='values', width=0.4, source=source, color="navy")

# 축 라벨 설정
p.xaxis.axis_label = "Categories"
p.yaxis.axis_label = "Values"

# 그래프 표시
output_notebook()
show(p)
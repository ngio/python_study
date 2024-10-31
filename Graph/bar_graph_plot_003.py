import plotly.express as px   #pip install plotly

# 데이터 준비
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 25, 15, 30]


# Bar 그래프 생성
fig = px.bar( x=categories, y=values , labels={'x':'Categories', 'y':'Values'}, title='Bar Graph Example with Plotly')

# 그래프 표시
fig.show()
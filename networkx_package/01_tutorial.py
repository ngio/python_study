# https://networkx.org/documentation/stable/tutorial.html#examining-elements-of-a-graph



import networkx as nx
import matplotlib.pyplot as plt # 그래프를 보여주기 위해 필요

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])

H = nx.path_graph(10) # 0부터 9까지의 노드를 가진 경로 그래프 H 생성

# H 그래프의 노드들을 G에 추가합니다. (0, 1, 2, ..., 9 노드가 G에 추가됨)
G.add_nodes_from(H)

# G.add_node(H) # 경고: 이 줄은 그래프 객체 H 자체를 노드로 추가하려고 시도합니다.
              # 일반적으로 의도하는 바가 아니며, 오류를 유발할 수 있습니다.
              # 만약 의도했다면 H는 해시 가능하지 않으므로 에러 발생 가능성이 높습니다.


# 그래프 그리기
plt.figure(figsize=(8, 6)) # 그래프 크기 설정 (선택 사항)
nx.draw(G,
        with_labels=True,      # 노드 레이블 표시
        node_color='lightblue', # 노드 색상 지정 (선택 사항)
        font_weight='bold',    # 노드 레이블 텍스트 굵게 (오타 수정 및 기능 반영)
        node_size=700,         # 노드 크기 지정 (선택 사항)
        font_size=10           # 노드 레이블 폰트 크기 지정 (선택 사항)
       )

plt.title("Modified Graph Drawing") # 그래프 제목 추가 (선택 사항)
plt.show() # 그래프를 화면에 표시

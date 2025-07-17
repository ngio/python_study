## https://data-science-note.tistory.com/89

import networkx as nx

G = nx.Graph()  # 무향그래프
V = {"서울", "부산", "인천", "대구"}  # 문자열, 클래스, 다른 networkx 그래프와 같이 해시가능한 객체
E = [
    ("서울", "부산"),
    ("서울", "인천"),
    ("서울", "대구"),
    ("부산", "대구")
]
G.add_nodes_from(V)
G.add_edges_from(E)

print(f"V = {G.nodes}")
print(f"E = {G.edges}")

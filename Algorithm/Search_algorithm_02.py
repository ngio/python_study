# 정렬/탐색 알고리즘 : https://modulabs.co.kr/blog/algorithm-python/
# Search 탐색 2 : BFS(너비 우선 탐색) & DFS(깊이 우선 탐색)

from collections import deque

graph_list = { 1: set([2, 3]),
                2: set([1, 3, 4]),
                3: set([1, 5]),
                4: set([1]),
                5: set([2,6]),
                6: set([3,4])}

root_node = 1

def bfs(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += graph[node] - set(visited)
    return visited

print(bfs(graph_list, root_node))

def dfs(graph, root):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += graph[node] - set(visited)
    return visited

print(dfs(graph_list, root_node))
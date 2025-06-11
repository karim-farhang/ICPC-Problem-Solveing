"""
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
-----------------------
['A', 'B', 'C', 'E', 'D', 'G', 'F']
"""
from collections import defaultdict


def DFS(Graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for nebar in Graph[start]:
        if not visited[nebar]:
            DFS(Graph, nebar, visited, path)
    return path


graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = 'A'
visited = defaultdict(bool)
path = []
dfsTravvaral = DFS(graph, start, visited, path)

print(dfsTravvaral)

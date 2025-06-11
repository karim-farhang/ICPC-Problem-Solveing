"""
5 5
A B
B D
D A
A C
D E
"""
from collections import defaultdict

graph = defaultdict(list)
nodes = set()
color = {}
parent = {}
v, e = map(int, input().split())
for _ in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    nodes.add(u)
    nodes.add(v)
for _ in nodes:
    if _ not in graph:
        graph[_] = []
    color[_] = 'W'
    parent[_] = None


def DFS(u, color, parent):
    color[u] = 'G'
    for v in graph[u]:
        if color[v] == 'W':
            cycle = DFS(v, color, parent)
            if cycle == True:
                return True
        elif color[v] == 'G':
            return True
        color[u] = 'B'
    return False


cyle = False
for u in graph.keys():
    if u in color:
        if color[u] == 'W':
            cyle = DFS(u, color, parent)
            if cyle:
                break

print(cyle)

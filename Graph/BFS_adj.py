"""
5 4
0 1
0 2
0 3
2 4
"""
from collections import defaultdict, deque
from queue import Queue

v, e = map(int, input().split())
adj = [[0] * v for i in range(v)]
vis = [[False] * v for i in range(v)]
for i in range(e):
    u, v = map(int, input().split())
    adj[u][v] = 1

graph = defaultdict(list)
for i in range(len(adj)):
    for j in range(len(adj[i])):
        if adj[i][j] == 1:
            graph[i].append(j)

path = list()
visited = defaultdict(bool)
q = deque()
start = 0
q.append(start)
path.append(start)
visited[start] = True
while len(q) != 0:
    s = q.popleft()
    for neb in graph[s]:
        if not visited[neb]:
            q.append(neb)
            path.append(neb)
            visited[s] = True
print(*path)

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
-------------------------
['A', 'B', 'C', 'F', 'G', 'D', 'E']
"""
from collections import defaultdict, deque

v, e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)


start = 'A'
q = deque()
q.append(start)
path = list()
path.append(start)
visited = defaultdict(bool)
visited[start] = True
while len(q) != 0:
    x = q.pop()
    for neg in graph[x]:
        if not visited[neg]:
            visited[neg] = True
            q.append(neg)
            path.append(neg)

print(path)

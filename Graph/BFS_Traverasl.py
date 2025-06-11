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
A B C F E D G
"""
from collections import defaultdict, deque


def BFS(edges, start):
    Q = deque()
    Q.append(start)

    visited = defaultdict(bool)
    visited[start] = True

    path = []
    path.append(start)

    while len(Q) != 0:
        tempNode = Q.popleft()
        for neighbour in edges[tempNode]:
            if not visited[neighbour] == True:
                path.append(neighbour)
                Q.append(neighbour)
                visited[neighbour] = True
    return path


nodes = set()
edges = defaultdict(list)

n, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    edges[u].append(v)
    edges[v].append(u)
    nodes.add(v)
    nodes.add(u)

start = 'A'
bfsTravarsal = BFS(edges, start)
print(bfsTravarsal)

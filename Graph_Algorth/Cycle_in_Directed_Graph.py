from collections import defaultdict


def DFS(Graph, start, visited, path=[]):
    visited[start].append(True)
    path.append(start)
    if


n, e = map(int, input().split(' '))
G = defaultdict(list)
for i in range(e):
    u, v = map(int, input().split(' '))
    G[u].append(v)


def path(a, b):
    print(a, end=' ')
    pathUtil(a, b)
    print(b)


def pathUtil(a, b):
    if G[a][b] == -1:
        return
    pathUtil(a, G[a][b])
    print(G[a][b], end=' ')
    pathUtil(G[a][b], b)

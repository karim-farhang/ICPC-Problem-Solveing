from collections import defaultdict
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

"""
def allPath(G, src, dest, path=[]):
    path = path + [src]
    Paths = []
    values = []
    if src == dest:
        return [path]
    if src not in G:
        return []
    for neb in G[src]:
        if neb not in path:
            newPath = allPath(G, neb, dest, path)
            for u in newPath:
                Paths.append(u)
    return Paths


graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(allPath(graph,'A','G'))
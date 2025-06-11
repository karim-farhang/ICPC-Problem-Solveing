from collections import defaultdict, deque


def allPath(G, src, dest, path=[]):
    path = path + [src]
    Paths = []
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
t = int(input())
while t > 0:
    n, e = map(int, input().split(' '))
    nodes = [x for x in range(1, n + 1)]
    g = defaultdict(list)
    for _ in range(e):
        u, v = map(int, input().split(' '))
        g[u].append(v)
    start = int(input())
    paths = list()
    count =0
    for i in range(1,n+1):
        if i != start:
            paths=allPath(g,start,i)
            if len(paths) == 0:
                print(-1,end=" ")
            else:
                print((len(paths[0])-1)*6,end=" ")
    print()
    t -= 1

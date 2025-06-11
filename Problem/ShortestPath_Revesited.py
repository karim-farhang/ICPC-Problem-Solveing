import sys
from collections import defaultdict


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


def costOFpath(paths, val):
    costs = list()
    for i in range(len(paths)):
        cost = []
        for j in range(len(paths[i]) - 1):
            x = (paths[i][j], paths[i][j + 1])
            cost.append(x)
        c = list()
        for y in cost:
            for p in val:
                if y[0] == p[0] and y[1] == p[1]:
                    c.append(p[2])
                    break
        costs.append(c)
    return costs


n, e, k = map(int, input().split(' '))
g = defaultdict(list)
val = list()
for _ in range(e):
    u, v, w = map(int, input().split(' '))
    g[u].append(v)
    g[v].append(u)
    val.append((u, v, w))
    val.append((v, u, w))

res = list()
for i in range(1, n + 1):
    paths = allPath(g, 1, i)
    cost = costOFpath(paths, val)
    short = [sys.maxsize]
    for j in range(len(cost)):
        for o in range(k):
            if len(cost[j]) >= k:
                cost[j].remove(max(cost[j]))
    for co in cost:
        if sum(co) < sum(short):
            short = co
    if sum(short)>0:
        print(min(short), end=' ')
    else:
        print(0,end=' ')
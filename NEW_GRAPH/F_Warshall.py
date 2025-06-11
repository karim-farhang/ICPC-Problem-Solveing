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
        c = 0
        for y in cost:
            for p in val:
                if y[0] == p[0] and y[1] == p[1]:
                    c += p[2]
                    break
        costs.append(c)
    return costs


t = int(input())
while t > 0:
    n = int(input())
    g = defaultdict(list)
    val = list()
    su, de, ed = map(int, input().split(' '))
    for i in range(ed):
        s, d, w = map(int, input().split(' '))
        g[s].append(d)
        g[d].append(s)
        val.append((s, d, w))
        val.append((d, s, w))
    path = allPath(g, su, de)
    cost = costOFpath(path, val)
    print(path)
    print(cost)
    t -= 1

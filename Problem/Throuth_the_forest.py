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


while True:
    inp = input()
    if inp[0] != '0':
        n, e = map(int, inp.split(' '))
        g = defaultdict(list)
        G = [[0] * n for _ in range(n)]
        val = list()
        for _ in range(e):
            u, v, w = map(int, input().split(' '))
            g[u].append(v)
            g[v].append(u)
            val.append((u, v, w))
            val.append((v, u, w))
        paths = allPath(g, 1, 2)
        x = costOFpath(paths, val)
        out = min(x)
        print(x.count(out))
    else:
        break

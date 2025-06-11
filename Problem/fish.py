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


n, e, f = map(int, input().split(' '))
fish = dict()
for _ in range(f):
    fish_no, node = map(str, input().split(' '))
    fish[node] = int(fish_no)
g = defaultdict(list)
val = list()
for _ in range(e):
    u, v, w = map(str, input().split(' '))
    g[u].append(v)
    val.append((u, v, int(w)))
paths = allPath(g, '1', str(n))
cost = costOFpath(paths, val)
fishes = list()
for i in paths:
    c = 0
    for j in i:
        c += fish[j]
    fishes.append(c)
fe = max(fishes)
piont = fishes.index(fe)
if fishes.count(fe) > 1:
    for i in range(len(fishes)):
        if cost[i] < cost[fishes.index(fe)] and fishes[i] == max(fishes):
            piont = i
    print(cost[piont])
else:
    print(cost[piont])

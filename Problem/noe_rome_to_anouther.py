from collections import defaultdict


def allPath(G, src, dest, path=[]):
    count = 0
    path = path + [src]
    Paths = []
    if src == dest and count > 0:
        return [path]
    if src not in G:
        return []
    count += 1
    for neb in G[src]:
        if neb not in path:
            newPath = allPath(G, neb, dest, path)
            for u in newPath:
                Paths.append(u)
    return Paths


t = int(input())
while t > 0:
    n = int(input())
    roms = list(map(int, input().split(' ')))
    g = defaultdict(list)
    for i in range(n - 1):
        g[roms[i]].append(roms[i + 1])
    g[roms[-1]].append(roms[0])
    print(g)
    paths = []
    for i in range(1, n + 1):
        x = allPath(g, i, i)
        print(x)
        paths.append(x)
    t -= 1

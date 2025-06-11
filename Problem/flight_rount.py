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


cost = int(input())
node = int(input())
edge = int(input())
val = list()
aor = list()
mones = list()
G = defaultdict(list)
for _ in range(edge):
    u, v, delay, mony = map(int, input().split(' '))
    G[u].append(v)
    val.append((u, v, mony))
    aor.append((u, v, delay))
    mones.append(mony)
src = int(input())
dist = int(input())

if (node * (node - 1) / 2) < edge or  edge < 1:
    print('Error')
elif 1 > cost > 1000:
    print('Error')
elif 1 > src < node or 1 > dist > node:
    print('Error')
else:
    p = allPath(G, src, dist)
    if len(p) == 0:
        print('Error')
    else:
        c = costOFpath(p, val)
        t = costOFpath(p, aor)
        spend_mony = min(c)
        spend_time = t[c.index(spend_mony)]
        rout = p[c.index(spend_mony)]
        for i in range(len(rout)):
            if i != len(rout) - 1:
                print(rout[i], end="->")
            else:
                print(rout[i], end=" ")
        print(spend_time + 1, spend_mony + ((spend_time + 1) * cost))

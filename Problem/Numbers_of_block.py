import math
from collections import defaultdict


def search(parent, i):
    if parent[i] == i:
        return i
    return search(parent, parent[i])


def apply_union(parent, rank, x, y):
    xroot = search(parent, x)
    yroot = search(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(g, nodes):
    result = []
    i, e = 0, 0
    g = sorted(g, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(nodes):
        parent.append(node)
        rank.append(0)
    while e < nodes - 1:
        u, v, w = g[i]
        i = i + 1
        x = search(parent, u)
        y = search(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            apply_union(parent, rank, x, y)
    res = 0
    for u, v, weight in result:
        res += weight
    return res


cites = int(input())
x = list(map(int, input().split(' ')))
val = []
G = defaultdict(list)
dd = 0
for _ in range(cites - 1):
    u, v = x[_], x[_ + 1]
    w = math.gcd(u, v)
    G[u].append(v)
    val.append((_, _ + 1, w))
    dd += w
res = kruskal(val, cites)
print(val)
print(res)
print(dd)

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
    return result


val = list()
n, e = map(int, input().split(' '))
for _ in range(e):
    u, v, w = map(int, input().split(' '))
    val.append((u - 1, v - 1, w))
    val.append((v - 1, u - 1, w))

x = kruskal(val, n)
res = 0
for i, j, p in x:
    res += p
print(res)

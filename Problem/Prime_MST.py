import sys


def minKey(g, nodes, key, mstSet):
    min = sys.maxsize
    min_index = -1
    for v in range(nodes):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index


def primMST(g, nodes):
    key = [sys.maxsize] * nodes
    parent = [None] * nodes
    key[0] = 0
    mstSet = [False] * nodes
    parent[0] = -1
    for cout in range(nodes):
        u = minKey(g, nodes, key, mstSet)
        mstSet[u] = True
        for v in range(nodes):
            if 0 < g[u][v] < key[v] and mstSet[v] == False:
                key[v] = g[u][v]
                parent[v] = u
    val = list()
    for i in range(1, nodes):
        val.append((parent[i], i, g[i][parent[i]]))
    return val


n, e = map(int, input().strip().split(' '))
m = [[0] * n for i in range(n)]
for _ in range(e):
    u, v, w = map(int, input().strip().split(' '))
    m[u - 1][v - 1] = w
start = int(input().strip()) - 1
x = primMST(m, n)
count = 0
for o, p, q in x:
    count += q
print(count)

import sys


def printMST(g, nodes, parent):
    print("Edge \tWeight")
    for i in range(1, nodes):
        print(parent[i], "-", i, "\t", g[i][parent[i]])


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
            if g[u][v] > 0 and mstSet[v] == False and key[v] > g[u][v]:
                key[v] = g[u][v]
                parent[v] = u
    printMST(g, nodes, parent)


g = [[0, 2, 0, 6, 0],
     [2, 0, 3, 8, 5],
     [0, 3, 0, 0, 7],
     [6, 8, 0, 0, 9],
     [0, 5, 7, 9, 0]]
primMST(g, 5)

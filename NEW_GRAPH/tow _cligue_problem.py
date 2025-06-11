from queue import Queue


def isBipartiteUtil(G, nodes, src, colorArr):
    colorArr[src] = 1
    q = Queue()
    q.put(src)
    while not q.empty():
        u = q.get()
        for v in range(nodes):
            if G[u][v] and colorArr[v] == -1:
                colorArr[v] = 1 - colorArr[u]
                q.put(v)
            elif G[u][v] and colorArr[v] == colorArr[u]:
                return False
    return True


def isBipartite(G, nodes):
    colorArr = [-1] * nodes
    for i in range(nodes):
        if colorArr[i] == -1:
            if not isBipartiteUtil(G, nodes, i, colorArr):
                return False
    return True


def canBeDividedinTwoCliques(G, nodes):
    GC = [[None] * nodes for i in range(nodes)]
    for i in range(nodes):
        for j in range(nodes):
            GC[i][j] = not G[i][j] if i != j else 0
    return isBipartite(GC, nodes)


adj = [[0, 1, 1, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0]]
if canBeDividedinTwoCliques(adj, 5):
    print("Yes")
else:
    print("No")

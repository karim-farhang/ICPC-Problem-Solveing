from collections import defaultdict
import sys
import heapq


def dijkstra(G, nodes, src, d):
    dist = [sys.maxsize] * nodes
    dist[src] = 0
    SP_Set = [False] * nodes
    if src == dist:
        return 0
    if (src not in range(nodes + 1)) or (d not in range(nodes + 1)):
        return -1
    else:
        for cout in range(nodes):
            min = sys.maxsize
            u = 0
            for v in range(nodes):
                if dist[v] < min and SP_Set[v] == False:
                    min = dist[v]
                    u = v
            SP_Set[u] = True
            for v in range(nodes):
                if G[u][v] > 0 and SP_Set[v] == False and dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
    return dist


def printMST(g, nodes, parent):
    for i in range(1, nodes):
        return (parent[i], i), g[i][parent[i]]


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


def SP(G, src, dest):
    path = []
    heapq.heappush(path, (0, src))
    while len(path) != 0:
        cost, edge = heapq.heappop(path)
        if edge == dest:
            return cost
        for neb, neb_cost in G[edge]:
            heapq.heappush(path, (cost + neb_cost, neb))


t = int(input())
while t > 0:
    node = int(input())
    s, d, e = map(int, input().split(' '))
    G = [[0] * node for _ in range(node)]
    nodes = [range(1, node)]
    g = defaultdict(list)
    for i in range(e):
        u, v, w = map(int, input().split(' '))
        G[u - 1][v - 1] = w
        G[v - 1][u - 1] = w
        g[u].append((v, w))
        g[v].append((u, w))
    start = 1
    dest = node
    x = primMST(G, node - 1)
    print(x)
    t -= 1

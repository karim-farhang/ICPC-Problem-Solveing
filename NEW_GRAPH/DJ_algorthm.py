import sys


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
    return dist[d]


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]
x = dijkstra(graph, 9, 0, 2 - 1)
print(x)

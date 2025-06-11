import sys
import itertools


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


"""
5 10
1 3 875
2 0 866
2 1 131
0 1 274
4 3 38
4 2 605
1 3 263
4 3 380
4 3 196
1 0 67
3
2
1
4
---------
998
"""
n, e = map(int, input().split(' '))
adj = [[0] * n for _ in range(n)]
for i in range(e):
    u, v, w = map(int, input().split(' '))
    adj[u][v] = w
    adj[v][u] = w
q = int(input())
que = list()
for ii in range(q):
    y = int(input())
    que.append(y)
pr = list(itertools.permutations(que))
s = dijkstra(adj, n, 0, que[0])
for i in range(len(que) - 1):
    s += dijkstra(adj, n, que[i], que[i + 1])
s += dijkstra(adj, n, que[-1], 0)
print(s)

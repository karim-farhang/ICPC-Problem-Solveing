"""
6 5
2 4 3
2 3 4
2 1 2
2 5 6
1 5 2

"""
from collections import defaultdict
import heapq


def shortestPath(graph, src, dest):
    path = []
    heapq.heappush(path, (0, src))
    while len(path) != 0:
        currcost, currvtx = heapq.heappop(path)
        if currvtx == dest:
            return currcost
        for neigh, neighcost in graph[currvtx]:
            heapq.heappush(path, (currcost + (neighcost * currvtx), neigh))


graph = defaultdict(list)
nod, edg = map(int, input().split(' '))
for i in range(edg):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))
    graph[v].append((u, w))

for i in range(nod):
    if i == nod:
        break
    if (i+1) not in graph.keys():
        print(-1)
    else:
        print(shortestPath(graph, 1, i + 1))

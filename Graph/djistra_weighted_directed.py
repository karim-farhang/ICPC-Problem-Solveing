import heapq
from collections import defaultdict


def shortestPath(graph, src, dest):
    path = []
    heapq.heappush(path, (0, src))
    while len(path) != 0:
        currcost, currvtx = heapq.heappop(path)
        if currvtx == dest:
            print(f'path exisits {src} to {dest} with cost {currcost}')
            break
        for neigh, neighcost in graph[currvtx]:
            heapq.heappush(path, (currcost + neighcost, neigh))


graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u, v, w = map(str, input().split())
    graph[u].append((v, int(w)))

print(graph)
src, dest = map(str, input().split())
shortestPath(graph, src, dest)

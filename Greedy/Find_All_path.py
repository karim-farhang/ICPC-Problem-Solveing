from collections import defaultdict
import heapq


def allPath(Graph, start, end, path=[]):
    path = path + [start]
    Paths = list()
    if start == end:
        return [path]
    if start not in Graph:
        return []
    for neb,c in Graph[start]:
        if neb not in path:
            newPath = allPath(Graph, neb, end, path)
            for u in newPath:

                Paths.append(u)
    return Paths


def shortestPahtBYnode(Graph, start, end, path=[]):
    path = path + [start]
    short = None
    if start == end:
        return path
    if start not in Graph:
        return []
    for neb in Graph[start]:
        if neb not in path:
            sp = shortestPahtBYnode(Graph, neb, end, path)
            if short == None or len(sp) < len(short):
                short = sp
    return short


def shortestPath(graph, src, dest):
    path = []
    heapq.heappush(path, (0, src))
    while len(path) != 0:
        currcost, currvtx = heapq.heappop(path)
        if currvtx == dest:
            return currcost
        for neigh, neighcost in graph[currvtx]:
            heapq.heappush(path, (currcost + neighcost, neigh))


graph = defaultdict(list)
n, e = map(int, input().split(' '))
for _ in range(e):
    u, v, w = map(str, input().split(' '))
    graph[u].append((v, int(w)))

start, end = map(str, input().split(' '))

x = shortestPath(graph, start, end)
print(x)

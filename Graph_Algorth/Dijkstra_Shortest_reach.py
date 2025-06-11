from collections import defaultdict
import heapq


def SP_DJ(G, src, dest):
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
    n, e = map(int, input().split(' '))
    G = defaultdict(list)
    nodes = set()
    for i in range(e):
        u, v, w = map(int, input().split(' '))
        G[u].append((v, w))
        G[v].append((u, w))
        nodes.add(u)
        nodes.add(v)
    src = int(input())
    nodes = list(nodes)
    for i in range(1,n+1):
        if i not in nodes:
            print(-1)
        elif i != src:
            print(SP_DJ(G,src,i),end=" ")
    t -= 1

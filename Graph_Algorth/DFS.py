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


G = defaultdict(list)
n, e = map(int, input().split(' '))
for _ in range(e):
    u, v, w = map(int, input().split(' '))
    G[u].append((v, w))
Q = int(input())
res = list()
for _ in range(Q):
    src, dest = map(int, input().split(' '))
    x = SP_DJ(G, src, dest)
    if x == None:
        res.append(-1)
    else:
        res.append(x)
for i in res:
    print(i)

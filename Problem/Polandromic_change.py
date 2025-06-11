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


st = list(input())
e = int(input())
graph = defaultdict(list)
for _ in range(e):
    u, v, w = map(str, input().split(' '))
    graph[u].append((v, int(w)))
p, q = 0, len(st) - 1
count = 0
while st != st[::-1]:
    if st[p] != st[q]:
        x = SP_DJ(graph, st[p], st[q])
        y = SP_DJ(graph, st[q], st[p])
        if x == None:
            st[p] = st[q]
            count += y
        elif y == None:
            st[q] = st[p]
            count += x
        elif x > y:
            count += y
            st[q] = st[p]
        else:
            count += x
            st[p] = st[q]
    p += 1
    q -= 1
print(count)

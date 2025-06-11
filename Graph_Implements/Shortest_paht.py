from collections import defaultdict
import heapq


def SP(G, s, d):
    paht = []
    heapq.heappush(paht, (0, s))
    while len(paht) != 0:
        cost, e = heapq.heappop(paht)
        if e == d:
            return cost
        for nb, c in G[e]:
            heapq.heappush(paht, (cost + c, nb))


t = int(input())
while t > 0:
    G = defaultdict(list)
    n, e = map(int, input().split(' '))
    start = '1'
    flag = True
    for i in range(e):
        u, v, w = map(str, input().split(' '))
        if flag:
            start = u
        G[u].append((v, int(w)))
    x = SP(G, start, str(n))
    if x != None:
        print(x)
    else:
        print(-1)
    t -= 1

from collections import defaultdict


def allPath(G, s, d, path=[], valu=[]):
    path = path + [s]


n, e = map(int, input().split(' '))
g = defaultdict(list)
for i in range(e):
    u, v, w = map(str, input().split(' '))
    g[(u, w)].append((v, w))
    g[(v, w)].append((u, w))

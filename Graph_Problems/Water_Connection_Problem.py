from collections import defaultdict


def DFS(Graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for nebar in Graph[start]:
        if not visited[nebar]:
            DFS(Graph, nebar, visited, path)
    return path


house, pipe = map(int, input().split(' '))
graph = defaultdict(list)
start = list()
repet = list()
graphv = list()
for i in range(pipe):
    s, d, v = map(int, input().split(' '))
    start.append(s)
    repet.append(d)
    if start == 0:
        start = s
    graph[s].append(d)
    graphv.append((s, d, v))

res = list()
for i in repet:
    if i in start:
        start.remove(i)
for i in start:
    visted = defaultdict(list)
    path = list()
    kk = DFS(graph, i, visted, path)
    for j in graphv:
        if j[0] == kk[-2] and j[1] == kk[-1]:
            res.append((i, kk[-1], j[2]))

res.sort(key=lambda x: x[0])
print(len(res))
for i in res:
    print(*i)

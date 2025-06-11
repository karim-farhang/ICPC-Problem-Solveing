from collections import defaultdict
def AllPath(Graph, start, end, path=[]):
    path = path + [start]
    allPaht = list()
    if start == end:
        return path
    if start not in Graph:
        print('333')
        return []
    for neb in Graph[start]:
        if neb not in path:
            newPaht = AllPath(Graph, neb, end, path)
            for x in newPaht:
                allPaht.append(x)
    return allPaht
graph = defaultdict(list)
n, e = map(int, input().split(' '))
for _ in range(e):
    u, v, w = map(str, input().split(' '))
    graph[(u, 0)].append((v, int(w)))
print(graph)
quey = int(input())
for _ in range(quey):
    star, des = map(str, input().split(' '))
    print(AllPath(graph, (star, 0), (des, 0)))
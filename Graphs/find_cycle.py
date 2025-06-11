from collections import defaultdict
def getPaht(graph, star, end, path=[]):
    path = [star]+[end]
    allPath = list()
    if star == end:
        return [path]
    if star not in graph:
        return []
    for n in graph[star]:
        if n not in path:
            new_path = getPaht(graph, n, end, path)
            for x in new_path:
                allPath.append(x)
    return allPath


nod, edge = map(int, input().split(' '))
graph = defaultdict(list)
for i in range(edge):
    u, v = map(int, input().split(' '))
    graph[u].append(v)

print(getPaht(graph, 0, 3))

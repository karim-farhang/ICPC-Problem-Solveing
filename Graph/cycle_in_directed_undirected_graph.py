"""
4 6
0 1
0 2
1 2
2 0
2 3
3 3

"""
from collections import defaultdict


def DFSs(graph, start, vis, pa=[]):
    visited[start] = True
    pa.append(start)
    for i in graph[start]:
        if not visited[i]:
            return DFSs(graph, i, vis, pa)
    return pa


visited = defaultdict(bool)
helper = defaultdict(bool)
path = list()


def DFS(graph, i, visited, helper, path=[]):
    visited[i] = True
    helper[i] = True
    path.append(i)
    for k in range(len(graph[i])):
        if visited[k] == True and helper[k] == True:
            return True
        else:
            return DFS(graph, k, visited, helper, path)
    return False


nod, edg = map(int, input().split(' '))
graph = defaultdict(list)
for i in range(edg):
    u, v = map(int, input().split(' '))
    graph[u].append(v)

pa = list()
vis = defaultdict(list)
nodes = DFSs(graph, 0, visited, pa)
for jk in nodes:
    print(DFS(graph, jk, visited, helper, path))

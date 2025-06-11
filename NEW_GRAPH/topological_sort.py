import collections


def DFSUtil(graph, node, visited, stack):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    stack.insert(0, node)


def topoSort(nodes, graph):
    visited = [False] * nodes
    stack = []
    for i in range(nodes):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    return stack


"""
6 6
5 0
4 0
4 1
1 3
2 3
5 2

"""
n, e = map(int, input().strip().split(' '))
g = collections.defaultdict(list)
for i in range(e):
    u, v = map(int, input().split(' '))
    g[u].append(v)
x = topoSort(n, g)
print(x)

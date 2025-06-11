"""
4 5
0 1
1 2
2 3
2 0
3 3
-------------
is cycle True
"""
from collections import defaultdict
def DFS_Util(graph, node, visited, recStack):
    visited[node] = True
    recStack[node] = True
    for nebr in graph[node]:
        if not visited[nebr]:
            if DFS_Util(graph, nebr, visited, recStack):
                return True
        elif recStack[nebr]:
            return True
    recStack[node] = False
    return False


# Returns true if graph is cyclic else false
def isCyclic(graph, nodes):
    visited = [False] * (nodes + 1)
    recStack = [False] * (nodes + 1)
    for node in range(nodes):
        if not visited[node]:
            if DFS_Util(graph, node, visited, recStack):
                return True
    return False


n, e = map(int, input().split(' '))
G = defaultdict(list)
for i in range(e):
    u, v = map(int, input().split(' '))
    G[u].append(v)

print(f'is cycle-> {isCyclic(G, n)}')

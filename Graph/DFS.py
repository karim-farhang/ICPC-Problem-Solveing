from collections import defaultdict


def DFS(graph, visited, start, path):
    path.append(start)
    visited[start] = True
    for nebar in graph[start]:
        if not visited[nebar]:
            DFS(graph, visited, nebar, path)
    return path


graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)


start = 'A'
path = list()
visited = defaultdict(bool)
dfs = DFS(graph, visited, start, path)
print(dfs)

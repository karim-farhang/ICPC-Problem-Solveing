from collections import defaultdict, deque

visted = defaultdict(bool)
path = list()


def DFS(graph, start, visited, path=[]):
    visited[start] = True
    path.append(start)
    for _ in graph[start]:
        if not visited[_]:
            DFS(graph, _, visited, path)
    return path


def BFS(graph, start):
    visited = defaultdict(bool)
    path = [start]
    que = deque()
    que.append(start)
    while que:
        x = que.pop()
        for i in graph[x]:
            if not visited[i] == True:
                que.append(i)
                path.append(i)
                visited[i] = True
    return path


graph = defaultdict(list)
node, edge = map(int, input().split(' '))
for _ in range(edge):
    u, v = map(int, input().split(' '))
    graph[u].append(v)

print(BFS(graph, 0))
print(DFS(graph, 1, visted, path))

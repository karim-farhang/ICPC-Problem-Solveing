from collections import defaultdict, deque


n, e = map(int, input().split(' '))
G = defaultdict(list)
for i in range(e):
    u, v = map(str, input().split(' '))
    G[u].append(v)


start = 'A'
q = deque()
q.append(start)
path = [start]
visited = defaultdict(bool)
visited[start] = True
while len(q) != 0:
    x = q.pop()
    for neg in graph[x]:
        if not visited[neg]:
            visited[neg] = True
            q.append(neg)
            path.append(neg)

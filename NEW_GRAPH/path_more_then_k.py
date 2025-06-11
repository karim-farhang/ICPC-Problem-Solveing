def pathMoreThanK(graph, nodes, src, k):
    path = [False] * nodes
    path[src] = True
    return pathMoreThanKUtil(graph, src, k, path)


def pathMoreThanKUtil(adj, src, k, path):
    if k <= 0:
        return True
    i = 0
    while i != len(adj[src]):
        v = adj[src][i][0]
        w = adj[src][i][1]
        i += 1
        if path[v]:
            continue
        if w >= k:
            return True
        path[v] = True
        if pathMoreThanKUtil(adj, v, k - w, path):
            return True
        path[v] = False
    return False


n, e = map(int, input().split())
adj = [[] * n for _ in range(n)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])
    adj[v].append([u, w])
sr, k = map(int, input().split())
x = pathMoreThanK(adj, n, sr, k)
if x:
    print(True)
else:
    print(False)

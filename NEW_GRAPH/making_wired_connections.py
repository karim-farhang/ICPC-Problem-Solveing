def DFS(adj, node, visited):
    if visited[node]:
        return
    visited[node] = True
    if node in adj:
        for x in adj[node]:
            if not visited[x]:
                DFS(adj, x, visited)


def make_con(node, G_adj, edge):
    visited = [False] * node
    adj = {}
    edges = 0
    for i in range(edge):
        if G_adj[i][0] in adj:
            adj[G_adj[i][0]].append(G_adj[i][1])
        else:
            adj[G_adj[i][0]] = []
        if G_adj[i][1] in adj:
            adj[G_adj[i][1]].append(G_adj[i][0])
        else:
            adj[G_adj[i][1]] = []
        edges += 1
    components = 0
    for i in range(node):
        if not visited[i]:
            components += 1
            DFS(adj, i, visited)
    if edges < node - 1:
        return -1
    redundant = edges - ((node - 1) - (components - 1))
    if redundant >= (components - 1):
        return components - 1
    return -1

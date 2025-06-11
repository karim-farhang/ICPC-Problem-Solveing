from collections import defaultdict


# find cycle none directed graph
def dfs(g, node, vist, par):
    vist[node] = True
    for child in g[node]:
        if not vist[child]:
            return dfs(g, child, vist, node)
        else:
            if child != par:
                return True
    return False


n, e = map(int, input().split(' '))
G = defaultdict(list)
for i in range(e):
    u, v = map(int, input().split(' '))
    G[u].append(v)
    G[v].append(u)

visited = defaultdict(bool)
temp = dfs(G, 1, visited, -1)
print(temp)

"""
5 5
0 1
1 2
2 3
3 4
4 1
--------
True
"""
from collections import defaultdict

def DFS_Util(u, par, adj, vis):
    vis[u] = True
    for v in adj[u]:
        if v == par:
            continue
        elif vis[v]:
            return True
        else:
            if DFS_Util(v, u, adj, vis):
                return True
    return False

def isCycle(n, adj):
    vis = [False for i in range(n)]
    for i in range(n):
        if not vis[i]:
            if DFS_Util(i, -1, adj, vis):
                return True
    return False


n, e = map(int, input().split(' '))
g = defaultdict(list)
for _ in range(e):
    u, v = map(int, input().strip().split(' '))
    g[u].append(v)
    g[v].append(u)

print(isCycle(n, g))

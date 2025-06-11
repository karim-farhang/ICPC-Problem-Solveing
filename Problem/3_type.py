from collections import defaultdict

n, e = map(int, input().split(' '))
val = list()
g = defaultdict(list)
for i in range(e):
    u, v, w = map(str, input().split(' '))
    g[u].append(v)
    g[v].append(u)
    val.append((u, v, int(w)))
    # val.append((v, u, int(w)))

val.sort(key=lambda x: x[2])
for i in val:
    print(*i)


def dfs(g, node, vist, par):
    vist[node] = True
    for child in g[node]:
        if not vist[child]:
            return dfs(g, child, vist, node)
        else:
            if child != par:
                return True
    return False


def MST(val):
    val.sort(key=lambda x: x[2])
    mst = list()

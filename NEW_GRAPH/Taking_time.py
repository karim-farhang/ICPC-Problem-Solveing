import collections


def printOrder(graph, n):
    indegree = [0] * (n + 1)
    for i in graph:
        for j in graph[i]:
            indegree[j] += 1
    job = [0] * (n + 1)
    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            job[i] = 1
    while q:
        cur = q.pop(0)
        for adj in graph[cur]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                job[adj] = 1 + job[cur]
                q.append(adj)
    for i in range(1, n + 1):
        print(job[i], end=" ")


"""
10 13
1 3
1 4
1 5
2 3
2 8
2 9
3 6
4 6
4 8
5 8
6 7
7 8
8 10
"""
g = collections.defaultdict(list)
n, e = map(int, input().strip().split(' '))
for i in range(e):
    u, v = map(int, input().strip().split(' '))
    g[u].append(v)
printOrder(g, n)

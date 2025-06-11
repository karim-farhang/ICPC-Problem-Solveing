from itertools import permutations
from sys import maxsize


def Salesman(graph, node, start):
    vertex = [x for x in range(node) if node != start]
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = start
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][start]
        min_path = min(min_path, current_pathweight)
    return min_path


n, e = map(int, input().split(' '))
cost = list(map(int, input().split(' ')))
if n == 1:
    print(cost[n - 1])
else:
    G = [[0] * n for _ in range(n)]
    for _ in range(n):
        u, v, w = map(int, input().split(' '))
        G[u - 1][v - 1] = w
        G[v - 1][u - 1] = w
    print(Salesman(G, n, 0))

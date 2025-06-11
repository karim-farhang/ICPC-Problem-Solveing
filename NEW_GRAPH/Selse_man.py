from sys import maxsize
from itertools import permutations
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


n,e = map(int,input().split(' '))
g = [[0]*n for i in range(n)]
for i in range(e):
    s,v,w = map(int,input().split(' '))
    g[s][v] = w
    g[v][s]=w
start = 0
print(Salesman(g, n, start))

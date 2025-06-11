from sys import maxsize
from itertools import permutations


def travellingSalesmanProblem(graph, nodes, src):
    vertex = []
    for i in range(nodes):
        if i != src:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = src
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][src]
        min_path = min(min_path, current_pathweight)
    return min_path


graph = [[0, 10, 15, 20], [10, 0, 35, 25],
         [15, 35, 0, 30], [20, 25, 30, 0]]
start = 0
print(travellingSalesmanProblem(graph, 4, start))

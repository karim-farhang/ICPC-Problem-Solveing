"""
a b c d
7
a b
a b
b d
a d
a c
a c
c d
---------------------
directed
a b c
3
a b 10
c a 20
c b 30
-----------------
1 3 4 5
7
1 0
1 0
0 2
0 2
3 0
3 1
3 2
"""
from collections import namedtuple


def adjacency_List(edge):
    edges = {}
    for i in range(edge):
        fromA, toB = input().split(' ')
        if fromA and toB in nodes:
            if fromA not in edges:
                edges[fromA] = [toB]
            if toB not in edges:
                edges[toB] = [fromA]
            else:
                edges[fromA].append(toB)
                edges[toB].append(fromA)
    return edges


def adjacency_matrix(edge, nodes):
    matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    for i in range(edge):
        node1, node2 = [int(x) for x in input().split(' ')]
        matrix[node1][node2] += 1
        matrix[node2][node1] += 1
    return matrix


def is_directed(edge):
    directed = {}
    for i in range(edge):
        x, y, weg = input().split(' ')
        if x not in directed:
            directed[x] = [(y, weg)]
        else:
            directed[x].append((y, weg))
    return directed


graph = namedtuple('Graph', ('nodes', 'edges', 'is_directed'))

nodes = [x for x in input().split(' ')]
edge = int(input())
# edges = adjacency_List(edge)
# edges = adjacency_matrix(edge, len(nodes))
diretc = is_directed(edge)
G = graph(nodes, [], diretc)
print(*G.nodes)
for i in G.edges:
    print(i, G.edges[i])
for i in G.is_directed:
    print(i, ":", G.is_directed[i])

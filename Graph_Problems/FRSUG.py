"""
7
0 1 4
0 3 8
1 4 1
1 2 2
4 2 3
2 5 3
3 4 2
0
4
1
4
5
7
--------------
4
5
9
----
"""
import heapq
from collections import defaultdict


def shortest_Path(graph, src, dest):
    path = []
    heapq.heappush(path, (0, src))
    while len(path) != 0:
        current_cost, current_node = heapq.heappop(path)
        if current_node == dest:
            return int(current_cost)
        for neighbour, neighbour_cost in graph[current_node]:
            heapq.heappush(path, (current_cost + neighbour_cost, neighbour))


result = list()
graph = defaultdict(list)
nodes = set()
number_of_edge = int(input())
for edge in range(number_of_edge):
    a, b, w = map(int, input().split(' '))
    graph[a].append((b, w))
    nodes.add(a)
    nodes.add(b)
sugest = int(input())
people = []
query = int(input())
while query > 0:
    x = int(input())
    people.append(x)
    query -= 1
people.sort()
for i in people:
    if i not in nodes:
        result.append('----')
    else:
        result.append(shortest_Path(graph, sugest, i))
for i in result:
    print(i)

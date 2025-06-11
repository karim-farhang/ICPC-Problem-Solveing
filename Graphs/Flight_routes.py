"""
mumbai,paris,new york,dubai,toronto,boston,hartford
9
mumbai,paris,4000
mumbai,dubai,500
paris,dubai,2000
paris,new york,3000
dubai,new york,6000
new your,toronto,400
mumbai,boston,5000
boston,hartford,200
hartford,new york,100
-------------------------------------------------
mumbai,paris,new york,dubai,toronto,boston,hartford
9
mumbai,paris
mumbai,dubai
paris,dubai
paris,new york
dubai,new york
new york,toronto
mumbai,boston
boston,hartford
hartford,new york


-------------------------"""
from collections import namedtuple

Graph = namedtuple('Graph', ['nodes', 'edges'])

nodes = input().split(' ')
edge = int(input())
edges = {}
for i in range(edge):
    x, y = input().split(' ')
    if x not in edges:
        edges[x] = [y]
    else:
        edges[x].append(y)
for i in edges:
    print(i, edges[i])


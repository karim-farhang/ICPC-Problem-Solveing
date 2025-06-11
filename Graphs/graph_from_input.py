edge, node = [int(x) for x in input().strip().split(' ')]
graph = [[0 for x in range(edge - 1)] for y in range(node - 1)]
nodes = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}
print()
for i in range(node):
    nodeA, nodeB = [str(x) for x in input().strip().split(' ')]
    graph[nodes[nodeA]][nodes[nodeB]] = 1

for i in graph:
    for j in i:
        print(j, end=' ')
    print()
inp = 0
out = 0
degree = []
for row in range(len(graph)):
    for col in range(len(graph)):
        print(col, row, ' - ', col, row)
        if graph[row][col] == 1:
            out += 1
        if graph[col][row] == 1:
            print(col, row)
            inp += 1

    degree.append([inp, -out])
    inp = 0
    out = 0

for i in nodes:
    print(i, degree[nodes[i]])

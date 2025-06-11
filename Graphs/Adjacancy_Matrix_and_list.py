
graph = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

node = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            print(f'{node[i]} -> {node[j]}')


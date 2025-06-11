def bellman_ford(graph, nodes, src):
    dist = [float("Inf")] * nodes
    dist[src] = 0
    for _ in range(nodes - 1):
        for a, b, c in graph:
            if dist[a] != float("Inf") and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c
    for a, b, c in graph:
        if dist[a] != float("Inf") and dist[a] + c < dist[b]:
            print("Graph contains negative weight cycle")
    return dist
g = {
    (0, 1, 2),
    (0, 2, 4),
    (1, 3, 2),
    (2, 4, 3),
    (2, 3, 4),
    (4, 3, -5),
}

x = bellman_ford(g, 5, 0)
print(x)

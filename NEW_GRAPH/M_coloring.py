def isSafe(graph, v, colour, c, V):
    for i in range(V):
        if graph[v][i] == 1 and colour[i] == c:
            return False
    return True


def graphColourUtil(graph, m_color, colour, v, nodes):
    if v == nodes:
        return True
    for c in range(1, m_color + 1):
        if isSafe(graph, v, colour, c, nodes):
            colour[v] = c
            if graphColourUtil(graph, m_color, colour, v + 1, nodes):
                return True
            colour[v] = 0
    return False


def graphColoring(graph, m_color, nodes):
    colour = [0] * nodes
    if not graphColourUtil(graph, m_color, colour, 0, nodes):
        return False
    return True


n, e = map(int, input().split())
graph = [[] * n for _ in range(n)]
for i in range(e):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = 1
    graph[v - 1][u - 1] = 1

color = int(input())
x = graphColoring(graph, color, n)
print(x)

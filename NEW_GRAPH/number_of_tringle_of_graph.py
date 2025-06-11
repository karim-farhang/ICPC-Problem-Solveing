def countTriangle(g, isDirected):
    nodes = len(g)
    count_Triangle = 0
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if i != j and i != k and j != k and g[i][j] and g[j][k] and g[k][i]:
                    count_Triangle += 1
    if isDirected:
        return count_Triangle // 3
    else:
        return count_Triangle // 6
print(countTriangle(adj, False))

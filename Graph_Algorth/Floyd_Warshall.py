n, e = map(int, input().split(' '))
G = [[float('inf')] * n for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            G[i][j] = 0
for _ in range(e):
    u, v, w = map(int, input().split(' '))
    G[u][v] = w

# apply floyd warshall
for i in range(n):
    for j in range(n):
        for k in range(n):
            if G[j][i] + G[i][k] < G[j][k]:
                G[j][k] = G[j][i] + G[i][k]

for x in G:
    for y in x:
        print(y, end='\t')
    print()

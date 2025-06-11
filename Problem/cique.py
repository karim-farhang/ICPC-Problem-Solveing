t = int(input())
n, e = map(int, input().split(' '))
G = [[0] * n for _ in range(n)]
for _ in range(e):
    u, v = map(int, input().split(' '))
    G[_][_] = 1
degrees = list()
for i in range(len(G)):
    d = 0
    for j in range(len((G[i]))):
        if G[i][j] == 1:
            d += 1
    degrees.append(d)
print(degrees.count(max(degrees)))

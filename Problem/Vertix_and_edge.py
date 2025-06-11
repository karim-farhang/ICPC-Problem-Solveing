import sys


class Floyd:
    reslut: list = []

    def int(self, p):
        self.p = p

    def floyed1(self, n, w, x, y):
        d = [[0 for i in range(n)] for j in range(n)]
        self.p = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                d[i][j] = w[i][j]
                self.p[i][j] = -1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        self.p[i][j] = k

    #  print(d[x][y])
    def rec(self, u, v):
        self.reslut.append(u + 1)
        self.pathutil(u, v)
        self.reslut.append(v + 1)

    def pathutil(self, u, v):
        if (self.p[u][v]) == -1:
            return
        else:
            self.pathutil(u, self.p[u][v])
            self.reslut.append(self.p[u][v] + 1)
            self.pathutil(self.p[u][v], v)


n, e = map(int, input().split(' '))
arr = [[0] * n for rr in range(n)]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i != j:
            arr[i][j] = sys.maxsize

for _ in range(e):
    u, v, w = map(int, input().split(' '))
    arr[u - 1][v - 1] = w
    arr[v - 1][u - 1] = w

g = Floyd()
g.floyed1(n, arr, 1 - 1, n - 1)
g.rec(1 - 1, n - 1)
rs = g.reslut

for i in range(1, n + 1):
    if i in rs:
        print('all')
    else:
        print('none')

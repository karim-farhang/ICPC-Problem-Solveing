"""
4
1 0 0 0
1 1 0 1
1 1 0 0
0 1 1 1
-----------
DDRDRR DRDDRR
"""
def setup():
    global v
    v = [[0] * 100 for _ in range(100)]
    global ans
    ans = []


def path(arr, x, y, pth, n):
    if x == n - 1 and y == n - 1:
        global ans
        ans.append(pth)
        return
    global v
    if arr[x][y] == 0 or v[x][y] == 1:
        return
    v[x][y] = 1
    if x > 0:
        path(arr, x - 1, y, pth + 'U', n)
    if y > 0:
        path(arr, x, y - 1, pth + 'L', n)
    if x < n - 1:
        path(arr, x + 1, y, pth + 'D', n)
    if y < n - 1:
        path(arr, x, y + 1, pth + 'R', n)
    v[x][y] = 0


def findPath(matrix, size):
    global ans
    ans = []
    if matrix[0][0] == 0 or matrix[size - 1][size - 1] == 0:
        return ans
    setup()
    path(matrix, 0, 0, "", size)
    ans.sort()
    return ans


n = int(input().strip())
maz = list()
for i in range(n):
    row = list(map(int, input().strip().split(' ')))
    maz.append(row)
print(*findPath(maz, n))

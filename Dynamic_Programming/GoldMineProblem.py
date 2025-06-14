def collectGold(gold, x, y, n, m):
    if ((x < 0) or (x == n) or (y == m)):
        return 0
    rightUpperDiagonal = collectGold(gold, x - 1, y + 1, n, m)
    right = collectGold(gold, x, y + 1, n, m)
    rightLowerDiagonal = collectGold(gold, x + 1, y + 1, n, m)
    return gold[x][y] + max(max(rightUpperDiagonal, rightLowerDiagonal), right)
def getMaxGold(gold, n, m):
    maxGold = 0
    for i in range(n):
        goldCollected = collectGold(gold, i, 0, n, m)
        maxGold = max(maxGold, goldCollected)
    return maxGold
gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]
m, n =4,4
print(getMaxGold(gold, n, m))
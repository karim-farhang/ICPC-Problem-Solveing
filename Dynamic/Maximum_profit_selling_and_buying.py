# maximum profit buying and selling
# a person buys a stock and sells it on some future date
def maxProfit(K, N, A):
    profit = [[0 for i in range(N + 2)] for i in range(K + 2)]
    for i in range(K + 1):
        profit[i][0] = 0
    for j in range(N + 1):
        profit[0][j] = 0
    INT_MIN = -1 * (1 << 32)
    for i in range(1, K + 1):
        prevDiff = INT_MIN
        for j in range(1, N):
            prevDiff = max(prevDiff, profit[i - 1][j - 1] - A[j - 1])
            profit[i][j] = max(profit[i][j - 1], A[j] + prevDiff)
    return profit[K][N - 1]
K = 3
N = 4
A = [20, 580, 420, 900]
print(maxProfit(K, N, A))

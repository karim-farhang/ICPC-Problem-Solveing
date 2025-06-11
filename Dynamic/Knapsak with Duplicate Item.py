
# 0-1 Knapsack with Duplicate Items
def knapSack(N, W, val, wt):
    dp = [0 for i in range(W + 1)]
    for i in range(W + 1):
        for j in range(N):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    return dp[W]
N = 4
W = 8
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
print(knapSack(N, W, val, wt))

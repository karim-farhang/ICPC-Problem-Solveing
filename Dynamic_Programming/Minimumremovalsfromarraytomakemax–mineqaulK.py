MAX = 100
dp = [[0 for i in range(MAX)]
      for i in range(MAX)]
for i in range(0, MAX):
    for j in range(0, MAX):
        dp[i][j] = -1
def countRemovals(a, i, j, k):
    global dp
    if (i >= j):
        return 0
    elif (a[j] - a[i]) <= k:
        return 0
    elif (dp[i][j] != -1):
        return dp[i][j]
    elif ((a[j] - a[i]) > k):
        dp[i][j] = 1 + min(countRemovals(a, i + 1,j, k),countRemovals(a, i,j - 1, k))
    return dp[i][j]
def removals(a, n, k):
    a.sort()
    if n == 1:
        return 0
    else:
        return countRemovals(a, 0,n - 1, k)
a = [1, 3, 4, 9, 10,
     11, 12, 17, 20]
n = len(a)
k = 4
print(removals(a, n, k))

# This code is contributed by
# Manish Shaw(manishshaw1)

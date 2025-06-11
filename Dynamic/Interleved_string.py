def isInterleave(a, b, c):
    m = len(a)
    n = len(b)
    dp = [[False] * (n + 1) for i in range(m + 1)]
    if m + n != len(c):
        return False
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                if b[j - 1] == c[j - 1]:
                    dp[i][j] = dp[i][j - 1]
            elif j == 0:
                if a[i - 1] == c[i - 1]:
                    dp[i][j] = dp[i - 1][j]
            elif a[i - 1] == c[i + j - 1] and b[j - 1] != c[i + j - 1]:
                dp[i][j] = dp[i - 1][j]
            elif a[i - 1] != c[i + j - 1] and b[j - 1] == c[i + j - 1]:
                dp[i][j] = dp[i][j - 1]
            elif a[i - 1] == c[i + j - 1] and b[j - 1] == c[i + j - 1]:
                dp[i][j] = (dp[i - 1][j] or dp[i][j - 1])
    return dp[m][n]

a = 'XY'
b = 'X'
c = 'XXY'
print(isInterleave(a, b, c))

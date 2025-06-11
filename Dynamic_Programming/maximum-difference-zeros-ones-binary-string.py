MAX = 100
def allones(s, n):
    co = 0
    for i in s:
        co += 1 if i == '1' else 0
    return co == n
def findlength(arr, s, n, ind, st, dp):
    if ind >= n:
        return 0
    if dp[ind][st] != -1:
        return dp[ind][st]
    if not st:
        dp[ind][st] = max(arr[ind] +
                          findlength(arr, s, n, ind + 1, 1, dp),
                          (findlength(arr, s, n, ind + 1, 0, dp)))
    else:
        dp[ind][st] = max(arr[ind] +
                          findlength(arr, s, n, ind + 1, 1, dp), 0)
    return dp[ind][st]
def maxLen(s, n):
    if allones(s, n):
        return -1
    arr = [0] * MAX
    for i in range(n):
        arr[i] = 1 if s[i] == '0' else -1
    dp = [[-1] * 3 for _ in range(MAX)]
    return findlength(arr, s, n, 0, 0, dp)
s = "11000010001"
n = 11
print(maxLen(s, n))
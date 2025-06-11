# ----- word wrap problem ---------
# Given an array nums[] of size n,
# where nums[i] denotes the number of characters in one word.
# Let K be the limit on the number of characters that can be
# put in one line (line width).
# Put line breaks in the given sequence such that the lines are
# printed neatly.
import sys


def solveWordWrap(nums, k):
    n = len(nums)
    dp = [0] * n
    ans = [0] * n
    dp[n - 1] = 0
    ans[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        currlen = -1
        dp[i] = sys.maxsize
        for j in range(i, n):
            currlen += (nums[j] + 1)
            if currlen > k:
                break
            if j == n - 1:
                cost = 0
            else:
                cost = ((k - currlen) * (k - currlen) + dp[j + 1])
            if cost < dp[i]:
                dp[i] = cost
                ans[i] = j
    i = 0
    res = 0
    while i < n:
        pos = 0
        for j in range(i, ans[i] + 1):
            pos = pos + nums[j]
        x = ans[i] - i
        if ans[i] + 1 != n:
            res = res + (k - x - pos) ** 2
        i = ans[i] + 1
    return res


words = [3, 2, 2, 5]
k = 6  # number of character can be one line
print(solveWordWrap(words, k))  # -> 10 line

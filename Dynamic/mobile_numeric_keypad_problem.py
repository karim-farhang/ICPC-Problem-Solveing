# --- Mobile numeric keypad ----
"""
Given the mobile numeric keypad.You can only press buttons
that are up, left, right, or down to the current button or
the current button itself (like 00,11, etc.). You are not
allowed to press the bottom row corner buttons (i.e. * and # ).
Given a number N, the task is to find out the number of
possible numbers of the given length
"""


def solve(i, j, n, keypad, dp):
    if n == 1:
        return 1
    if dp[keypad[i][j]][n] != -1:
        return dp[keypad[i][j]][n]
    a = solve(i, j, n - 1, keypad, dp)
    if j - 1 >= 0 and keypad[i][j - 1] != -1:
        a += solve(i, j - 1, n - 1, keypad, dp)
    if j + 1 < 3 and keypad[i][j + 1] != -1:
        a += solve(i, j + 1, n - 1, keypad, dp)
    if i - 1 >= 0 and keypad[i - 1][j] != -1:
        a += solve(i - 1, j, n - 1, keypad, dp)
    if i + 1 < 4 and keypad[i + 1][j] != -1:
        a += solve(i + 1, j, n - 1, keypad, dp)
    dp[keypad[i][j]][n] = a
    return a


def getCount(n):
    ans = 0
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    dp = [[-1 for _ in range(n + 1)] for _ in range(10)]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] != -1:
                ans += solve(i, j, n, keypad, dp)
    return ans


print(getCount(1))  # --> 10
print(getCount(2))  # --> 36

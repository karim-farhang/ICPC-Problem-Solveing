# --- BBT counter ------
# Given a height h, count the maximum number of balanced
# binary trees possible with height h. Print the result modulo 109 + 7.
# Note : A balanced binary tree is one in which for every node,
# the difference between heights of left and right subtree is
# not more than 1.
# Python3 program to count number of balanced
# binary trees of height h.

def countBT(h):
    MOD = 1000000007
    dp = [0 for i in range(h + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, h + 1):
        dp[i] = (dp[i - 1] * ((2 * dp[i - 2]) % MOD + dp[i - 1]) % MOD) % MOD
    return dp[h]
h = 3
print("No. of balanced binary trees of height is: " + str(countBT(h)))  # --> 15

# ------- Boolean Presentation ------------------
# Count the number of ways we can parenthesize
# the expression so that the value of expression evaluates to true.

# Backend complete function template for Python 3

def countWays(N, S):
    mod = 1003
    dp = []
    for i in range(201):
        temp = []
        for j in range(201):
            x = [-1] * 2
            temp.append(x)
        dp.append(temp)

    def solve(S, i, j, isTrue):
        if i > j:
            dp[i][j][isTrue] = 0
            return 0
        if i == j:
            if isTrue:
                if S[i] == 'T':
                    dp[i][j][isTrue] = 1
                else:
                    dp[i][j][isTrue] = 0
            else:
                if S[i] == 'F':
                    dp[i][j][isTrue] = 1
                else:
                    dp[i][j][isTrue] = 0
            return dp[i][j][isTrue]

        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]

        ans = 0
        for k in range(i + 1, j, 2):
            if S[k] == '|':
                if isTrue:
                    ans += ((solve(S, i, k - 1, 1) * solve(S, k + 1, j, 1))
                            + (solve(S, i, k - 1, 1) * solve(S, k + 1, j, 0))
                            + (solve(S, i, k - 1, 0) * solve(S, k + 1, j, 1))) % mod
                else:
                    ans += (solve(S, i, k - 1, 0) * solve(S, k + 1, j, 0)) % mod
            elif S[k] == '&':
                if isTrue:
                    ans += (solve(S, i, k - 1, 1) * solve(S, k + 1, j, 1)) % mod
                else:
                    ans += ((solve(S, i, k - 1, 0) * solve(S, k + 1, j, 0))
                            + (solve(S, i, k - 1, 0) * solve(S, k + 1, j, 1))
                            + (solve(S, i, k - 1, 1) * solve(S, k + 1, j, 0))) % mod
            else:
                if isTrue:
                    ans += ((solve(S, i, k - 1, 0) * solve(S, k + 1, j, 1))
                            + (solve(S, i, k - 1, 1) * solve(S, k + 1, j, 0))) % mod
                else:
                    ans += ((solve(S, i, k - 1, 1) * solve(S, k + 1, j, 1))
                            + (solve(S, i, k - 1, 0) * solve(S, k + 1, j, 0))) % mod

        dp[i][j][isTrue] = ans % mod
        return dp[i][j][isTrue]

    return solve(S, 0, N - 1, 1)

S = 'T^F|F'
print(countWays(len(S), S))

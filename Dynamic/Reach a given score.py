# ------ Reach a given score -------
# Consider a game where a player can score 3 or 5 or 10 points in a move.
# Given a total score n,
# find number of distinct combinations to reach the given score.
# input : 8 , 20 , 13 output: 1, 4, 2
# Explanation
# For 1st example when n = 8 { 3, 5 } and {5, 3}
# are the two possible permutations but these represent the same
# combination. Hence, output is 1
def count(n):
    ways = [3, 5, 10]
    return solve(ways, 3, n)
def solve(ways, n, target):
    if target == 0:
        return 1
    if n == 0:
        return 0
    if ways[n - 1] <= target:
        return solve(ways, n, target - ways[n - 1]) + solve(ways, n - 1, target)
    else:
        return solve(ways, n - 1, target)
print(count(20))

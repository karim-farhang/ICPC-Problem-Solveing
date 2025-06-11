# Coin game winner where every player has three choices
# A and B are playing a game. At the beginning there are n coins.
# Given two more numbers x and y. In each move a player can pick x or y or 1 coins.
# A always starts the game. The player who picks the last coin wins the
# game or the person who is not able to pick any coin loses the game.
# For a given value of n, find whether A will win the game or not if both are playing optimally.
# Python3 program to find winner of game
# if player can pick 1, x, y coins
def findWinner(x, y, n):
    dp = [0 for i in range(n + 1)]
    dp[0] = False
    dp[1] = True
    for i in range(2, n + 1):
        if i - 1 >= 0 and not dp[i - 1]:
            dp[i] = True
        elif i - x >= 0 and not dp[i - x]:
            dp[i] = True
        elif i - y >= 0 and not dp[i - y]:
            dp[i] = True
        else:
            dp[i] = False
    return dp[n]


x = 3
y = 4
n = 5
if findWinner(x, y, n):
    print('A')
else:
    print('B')

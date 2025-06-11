# -- Optimal Strategy For A Game ------
# You are given an array A of size N.
# The array contains integers and is of even length.
# The elements of the array represent N coin of values V1, V2, ....Vn.
# You play against an opponent in an alternating way
def optimalStrategyOfGame(arr, n):
    table = [[0 for i in range(n)] for i in range(n)]
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if (i + 2) <= j:
                x = table[i + 2][j]
            y = 0
            if (i + 1) <= (j - 1):
                y = table[i + 1][j - 1]
            z = 0
            if i <= (j - 2):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    return table[0][n - 1]


A = [5, 3, 7, 10]
print(optimalStrategyOfGame(A, len(A)))  # --> 15

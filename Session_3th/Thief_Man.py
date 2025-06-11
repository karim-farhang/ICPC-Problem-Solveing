m = 8
W = [0, 2, 3, 4, 5]
V = [0, 1, 2, 5, 6]

table = [[0 for j in range(m + 1)] for i in range(len(V) + 1)]
for i in range(len(table)):
    for j in range(len(table[i])):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif W[i - 1] <= j:
            table[i][j] = max(table[i - 1][j], table[i - 1][j - W[i]] + V[i])
        else:
            table[i][j] = table[i - 1][j]
        print(f'{table[i][j]}\t', end="")
    print()

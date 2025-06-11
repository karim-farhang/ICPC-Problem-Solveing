val = [5, 4, 7, 7]
wt = [5, 6, 8, 4]
n1 = 4
n2 = 13
W = 13
n = len(val)
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
for i in range(n + 1):
    for w in range(W + 1):
        if i == 0 or w == 0:
            K[i][w] = 0
        elif wt[i - 1] <= w:
            K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
        else:
            K[i][w] = K[i - 1][w]

print(K[n1][n2])
j = n2
for i in range(n1, 0, -1):
    if K[i][j] != K[i - 1][j]:
        print(i, end=" ")
        j -= wt[i - 1]
print()
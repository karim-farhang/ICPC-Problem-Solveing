# Largest rectangular sub-matrix whose sum is 0
# Given a matrix mat[][] of size N x M.
# The task is to find the largest rectangular sub-matrix by area whose sum is 0.
def largest_rectanglar_sum_is_0(A):
    if not A:
        return 0
    C = len(A[0])
    col_expanded = []
    for row in A:
        expanded = []
        for i in range(C):
            s = 0
            for j in range(i, C):
                s += row[j]
                expanded.append(s)
        col_expanded.append(expanded)
    total = 0
    for i in range(len(col_expanded[0])):
        for j in range(len(col_expanded)):
            s = 0
            for k in range(j, len(col_expanded)):
                s += col_expanded[k][i]
                if s == 0:
                    total += 1
    return total


mat = [[9, 7, 16, 5],
       [1, -6, -7, 3],
       [1, 8, 7, 9],
       [7, -2, 0, 10]]
print(largest_rectanglar_sum_is_0(mat))

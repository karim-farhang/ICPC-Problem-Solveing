# Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.
def kadanes(arr, n):
    s, maxi = arr[0], arr[0]
    for i in range(1, n):
        s += arr[i]
        s = max(s, arr[i])
        maxi = max(s, maxi)
    return maxi


def maximumSumRectangle(R, C, M):
    res = M[0][0]
    for starti in range(R):
        subMatSum = [0 for _ in range(C)]
        for i in range(starti, R):
            for j in range(C):
                subMatSum[j] += M[i][j]
            res = max(res, kadanes(subMatSum, C))
    return res
R = 4
C = 5
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]
print(maximumSumRectangle(R, C, M))

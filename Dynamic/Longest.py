# Largest area rectangular sub-matrix with equal number of 1’s and 0’s
# Given a binary matrix. The problem is to find the largest area rectangular
# sub-matrix with equal number of 1’s and 0’s. Examples:
def maximalRectangleArea(A):
    n = len(A)
    m = len(A[0])
    for i in range(m):
        s = 0
        for j in range(n):
            if A[j][i] == 1:
                s += 1
                A[j][i] = s
            else:
                s = 0
    resultArea = 0
    for i in range(n):
        firstMinLeft = []
        firstMinRight = []
        st = []
        for j in range(m):
            while st and st[-1][0] >= A[i][j]:
                st.pop()
            if st:
                firstMinLeft.append(st[-1][1])
            else:
                firstMinLeft.append(-1)
            st.append((A[i][j], j))
        st = []
        for j in range(m - 1, -1, -1):
            while st and st[-1][0] >= A[i][j]:
                st.pop()
            if st:
                firstMinRight.append(st[-1][1])
            else:
                firstMinRight.append(m)
            st.append((A[i][j], j))
        firstMinRight = firstMinRight[::-1]
        for j in range(m):
            area = (firstMinRight[j] - firstMinLeft[j] - 1) * A[i][j]
            resultArea = max(area, resultArea)
    return resultArea
A = [[1, 1, 1],
     [0, 1, 1],
     [1, 0, 0]]
print(maximalRectangleArea(A))

# ----- max sub square ----------
R = 6
C = 5
def printMaxSubSquare(M):
    global R, C
    Max = 0
    S = [[0 for col in range(C)] for row in range(2)]
    for i in range(R):
        for j in range(C):
            Entrie = M[i][j]
            if Entrie:
                if j:
                    Entrie = 1 + min(S[1][j - 1], min(S[0][j - 1], S[1][j]))
            S[0][j] = S[1][j]
            S[1][j] = Entrie
            Max = max(Max, Entrie)
    print("Maximum size sub-matrix is: ")
    for i in range(Max):
        for j in range(Max):
            print("1", end=" ")
        print()
M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
printMaxSubSquare(M)
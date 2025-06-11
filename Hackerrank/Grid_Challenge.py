grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']


def check(A):
    B = sorted([[A[j][i] for j in range(len(A))] for i in range(len(A[0]))])
    for i in range(len(B) - 1):
        for j in range(len(B[i]) - 1):
            if B[j][i] < B[j + 1][i + 1]:
                return False
    return True


print(check(grid))

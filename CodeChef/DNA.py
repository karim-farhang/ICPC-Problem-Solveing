def check(A, B):
    isValid = True
    for i in range(len(A)):
        if A[i] == B[i]:
            return 'invalid'
        else:
            if A[i] == 'G' and B[i] == 'C':
                pass
            elif B[i] == 'G' and A[i] == 'C':
                pass
            elif A[i] == 'T' and B[i] == 'A':
                pass
            elif B[i] == 'T' and A[i] == 'A':
                pass
            else:
                isValid = False
            if not isValid:
                return 'invalid'
    return 'valid'


t = int(input().strip())
rt = []
for i in range(t):
    x = [p for p in input().strip()]
    y = [k for k in input().strip()]
    rt.append(check(x, y))
for j in rt:
    print(j)

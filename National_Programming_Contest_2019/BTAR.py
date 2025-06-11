# greedy algorithm
"""
1
7
1 2 3 1 2 3 8
3
"""


def gemMin(A):
    coun = 0
    coun2 = 0
    for i in range(len(A)):
        coun2 = coun
        if A[i] % 4 != 0:
            for j in range(i, len(A)):
                if (A[i] + A[j]) % 4 == 0 and (i != j) :
                    coun += 1
                    A[j] = 0
                    break
            if coun2 == coun:
                return -1
    return coun


t = int(input().strip())
rt = []
while t > 0:
    expres = 0
    s = int(input().strip())
    if s <= 0:
        input()
        rt.append(0)
    else:
        num = [int(x) for x in input().strip().split(' ')]
        num = num[:s]
        rt.append(gemMin(num))
    t -= 1
for i in rt:
    print(i)

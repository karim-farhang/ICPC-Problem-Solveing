t = int(input().strip())
rt = []
while t > 0:
    A = input().strip().split(' ')
    precedence = ['2', '3', 'A', 'K', 'J', '7', '8', '9', '10', 'Q']
    sA = list(set(A))
    highest = sA[0]
    count = 0
    for i in sA:
        if A.count(i) >= A.count(highest):
            if precedence.index(i) >= precedence.index(highest) and A.count(i) >= 2:
                highest = i
                count = A.count(i)
    highest = highest + ' '
    rt.append(highest * count)
    t -= 1
for i in rt:
    print(i)

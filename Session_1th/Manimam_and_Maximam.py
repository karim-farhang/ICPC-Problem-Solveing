tc = int(input())
reultCase = []
while tc > 0:
    dimin = int(input())
    matric = list()
    row = list()
    col = list()
    reuslt = list()
    for i in range(dimin):
        x = [int(x) for x in input().split(" ")]
        matric.append(x)
        row.append([min(x), max(x)])
    trax = [[matric[t][r] for t in range(len(matric))] for r in range(len(matric[0]))]
    for i in trax:
        col.append([min(i), max(i)])
    reuslt.append(row)
    reuslt.append(col)
    reultCase.extend(reuslt)
    tc -= 1

rows = 0
for t_case in reultCase:
    for i in t_case:
        print("{0} {1}".format(i[0], i[1]))
    print()

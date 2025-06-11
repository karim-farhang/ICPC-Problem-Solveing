import sys

student = int(input())
stu = list()
for i in range(student):
    name = input()
    score = float(input())
    stu.append([name, score])
stu.sort(key=lambda x: x[1])
rem = stu[0][1]
for i in range(len(stu)):
    if stu[i][1] == rem:
        stu[i][1] = sys.maxsize
stu.sort(key=lambda x: x[1])
if stu[0][1] == stu[1][1]:
    res = [stu[1][0], stu[0][0]]
    res.sort()
    print(res[0])
    print(res[1])
else:
    print(stu[0][0])

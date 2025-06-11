plat, trin = map(int, input().split(' '))
platforms = [['0' for i in range(3)] for j in range(plat)]
transs = list()
for i in range(trin):
    arive, dept, pl = map(str, input().split(' '))
    transs.append([arive, dept, pl])

transs.sort(key=lambda x: x[0])
count =0
for i in transs:
    index = int(i[2])-1
    if i[0] >= platforms[index][1]:
        platforms[index][0]=i[0]
        platforms[index][1] = i[1]
        platforms[index][2] = i[2]
        count+=1
print(platforms)
print(count)


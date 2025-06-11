
res = list()
siz = int(input())
list1 = list()
result = list()
for i in range(siz):
    list1.append(input())
for i in list1:
    for j in list1:
        if i == j[::-1] and len(i) % 2 == 1:
            result.append((len(i), j[len(j) // 2]))
result = list(set(result))
res.append(result)
for i in res:
    for j in i:
        print(*j, end='')

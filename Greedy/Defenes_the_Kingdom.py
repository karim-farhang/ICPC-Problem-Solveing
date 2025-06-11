arr = [
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
]

x = 3
y = 2

x1 = list()
flag = False
for i in range(len(arr[0])):
    x2 = list()
    for j in range(len(arr)):
        x2.append(arr[i][j])
        if i == (x - 1) and j == (y - 1):
            flag = True
            break
    x1.append(x2)
    if flag:
        break
for i in x1:
    print(*i)


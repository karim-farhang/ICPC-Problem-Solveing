def rotate(a):
    res = []
    for i in range(len(a[0])):
        x = []
        for j in range(len(a)):
            x.append(a[j][i])
        res.append(x)
    return res[::-1]


arr = [
    [5, 6, 7, 8, 4, 5, 5, 6, 7, 8, 4, 5],
    [5, 6, 7, 8, 4, 5, 5, 6, 7, 8, 4, 5],
    [9, 0, 1, 2, 5, 6, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 2, 0, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
    [3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5],
]
total = len(arr[0]) * len(arr)
while total != 0:
    print(*arr[0])
    total -= len(arr[0])
    arr.remove(arr[0])
    if len(arr) > 0:
        arr = rotate(arr)

"""
3 4
5 71 2
8 9 15
2 20 1645
57 40 105
"""
col, row = [int(y) for y in input().strip().split(' ')]
arr = []
for i in range(row):
    x = [int(j) for j in input().split(' ')]
    arr.append(x)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != 0:
            if arr[i][j] % 3 == 0 and arr[i][j] != 3:
                arr[i][j] = pow(arr[i][j], 2)
            elif arr[i][j] % 5 == 0 and arr[i][j] != 5:
                for p in range(1, row + 1):
                    arr[i][j] /= 5
            elif arr[i][j] % 5 == 0 and arr[i][j] % 3 == 0:
                arr[i][j] /= 5
print()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(int(arr[i][j]), end=' ')
    print()

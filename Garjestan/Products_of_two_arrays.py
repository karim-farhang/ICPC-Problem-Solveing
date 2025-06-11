"""
5
1
2
-3 -2
3 -5
"""
n_time = int(input())
n2 = int(input())
k = int(input())
arr: list[list[int]] = []
for i in range(k):
    arr.insert(i, [int(j) for j in input().split(" ")])

n = len(arr[0])
for i in range(n):
    for j in range(n - i - 1):
        if arr[0][j] > arr[0][j + 1]:
            arr[0][j], arr[0][j + 1] = arr[0][j + 1], arr[0][j]

for i in range(n_time):
        arr[0][0] -= i+1

minm = sum(arr[0]) + sum(arr[1])
print(minm)

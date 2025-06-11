arr = [4,2,9,7,5]
arr.sort()
res = 0
for i in range(len(arr)):
    res += abs(arr[i] - arr[-(i + 1)])
print(res)
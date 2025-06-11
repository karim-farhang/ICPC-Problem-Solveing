def minAbsult(arr):
    m = abs(arr[0] - arr[1])
    arr.sort()
    for i in range(len(arr) - 1):
        m = min(m, abs(arr[i] - arr[i + 1]))
    return m


print(minAbsult([3, -7, 0]))

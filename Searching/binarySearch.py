import bisect


def binSearch(A, L, R, K):
    while L <= R:
        mid = (R + L) // 2
        if A[mid] == K:
            return mid, A[mid]
        elif K >= A[mid]:
            L = mid + 1
        else:
            R = mid - 1
    return -1


a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x = binSearch(a, 0, len(a) - 1, 70)
print(x)

x = bisect.bisect_left(a, 70, 0, len(a) - 1)
print(x)

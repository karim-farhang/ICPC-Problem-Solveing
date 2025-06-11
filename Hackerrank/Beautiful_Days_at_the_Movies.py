i, j, k = map(int, input().split())
count = 0
for u in range(i, j + 1):
    x = str(u)[::-1]
    res = (u - int(x))
    if res % k == 0:
        count += 1
print(count)

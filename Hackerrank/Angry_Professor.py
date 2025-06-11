t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    st = list(map(int, input().split()))
    count = 0
    for j in st:
        if j <= 0:
            count += 1
    if count >= k:
        print("NO")
    else:
        print("YES")

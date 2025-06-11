for _ in range(int(input())):
    x, i, y, j = map(int, input().split())
    p = x - y
    q = i - j
    if p < q:
        print("First")
    elif p == q:
        print("any")
    else:
        print('Second')

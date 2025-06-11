for _ in range(int(input())):
    x, y, z = map(int, input().split())
    p = (x + y)
    count = 0
    if p > z:
        print(0)
    else:
        while p <= z:
            count += 1
            p += x
        print(count)

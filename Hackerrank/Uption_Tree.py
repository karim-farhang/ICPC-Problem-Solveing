t = int(input())
for _ in range(t):
    x = int(input())
    s = 1
    for i in range(1,x + 1):
        if i % 2 != 0:
            s *= 2
        else:
            s += 1
    print(s)

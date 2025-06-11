for _ in range(int(input())):
    x_rop, expen = map(int, input().split())
    if (x_rop / 30) >= expen:
        print('YES')
    else:
        print('NO')

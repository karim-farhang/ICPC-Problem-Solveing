for _ in range(int(input())):
    x, y = map(int, input().split())
    x = (x * y)
    y = (y * 10)
    if x >= y:
        print('Cloth')
    else:
        print('Disposable')

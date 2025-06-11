for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y < (x + 200):
        print('yes')
    else:
        print('no')

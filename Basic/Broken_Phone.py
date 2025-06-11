for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < y:
        print('REPAIR')
    elif x == y:
        print("ANY")
    else:
        print("NEW PHONE")
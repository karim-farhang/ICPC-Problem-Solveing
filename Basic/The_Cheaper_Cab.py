for i in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print('FIRST')
    elif a == b:
        print('ANY')
    else:
        print('SECOND')

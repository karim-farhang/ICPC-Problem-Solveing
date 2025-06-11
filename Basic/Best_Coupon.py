for _ in range(int(input())):
    x = int(input())
    res = (10/100)*x
    if res >= 100:
        print(int(res))
    else:
        print(100)
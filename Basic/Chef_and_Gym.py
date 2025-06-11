for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if z >= (x + y):
        print(2)
    elif x <= z <= (x + y):
        print(1)
    elif z < x:
        print(0)

for t_case in range(int(input())):
    x, y = map(int, input().split())
    if x >= y:
        print("Yes")
    else:
        print("No")

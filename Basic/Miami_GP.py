for _ in range(int(input())):
    x, y = map(int, input().split())
    if y <= x or y <= ((107 / 100) * x):
        print("Yes")
    else:
        print("No")

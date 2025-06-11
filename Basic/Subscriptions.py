for _ in range(int(input())):
    n, x = map(int, input().split())
    if n > 6 and n % 6 != 0:
        print(((n // 6) + 1) * x)
    if n > 6 and n % 6 == 0:
        print((n // 6) * x)
    if n != 0 and n <= 6:
        print(x)

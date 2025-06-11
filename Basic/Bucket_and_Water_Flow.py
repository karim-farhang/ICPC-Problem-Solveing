for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    r = w + (y * z)
    if r > x:
        print("overFlow")
    if r == x:
        print("filled")
    if r < x:
        print("unfilled")

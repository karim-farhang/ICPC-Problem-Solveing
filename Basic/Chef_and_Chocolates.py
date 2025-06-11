for _ in range(int(input())):
    x, y, z = map(int, input().split())
    res = ((x * 5) + (y * 10)) // z
    print(res)

# -----
# cook your dish here
for _ in range(int(input())):
    c, x, y = map(int, input().split())
    res = ((c-x)*y)
    print(res)

x = int(input())
for i in range(x):
    prisoner, sweet, start = map(int, input().split())
    val = (prisoner + sweet + start - 1) % prisoner
    if val == 0:
        print(prisoner)
    else:
        print(val)

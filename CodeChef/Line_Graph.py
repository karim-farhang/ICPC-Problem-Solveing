t = int(input().strip())
rt = []
while t > 0:
    m, x, b = [int(x) for x in input().strip().split(' ')]
    y = m * x + b
    rt.append(y)
    t -= 1
for x in rt:
    print(x)

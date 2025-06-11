x = sorted([int(x) for x in input().split(",")])
max = 0
for i in range(len(x)):
    max += (x[i] * i)

print(max)

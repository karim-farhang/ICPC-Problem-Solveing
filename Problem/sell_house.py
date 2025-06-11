import sys

c, h = map(int, input().split(' '))
want = list()
houses = list()
for _ in range(c):
    area, price = map(int, input().split(' '))
    want.append((area, price))
for _ in range(h):
    area, price = map(int, input().split(' '))
    houses.append((area, price))

houses.sort(key=lambda x: x[0])
want.sort(key=lambda x: x[0])
count = list()
for i in want:
    for j in houses:
        if j[0] >= i[0] and j[1] <= i[1]:
            count.append(j)
            break

print(len(count))
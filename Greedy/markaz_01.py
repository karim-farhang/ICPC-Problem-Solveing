
"""
1
4 60
1 2 3 4
40 100 50 60
20 10 40 30
--------
"""
result = list()
t = int(input())
for _ in range(t):
    res = [0, []]
    t = 0
    n, bag = map(int, input().split(' '))
    ids = input().split()
    price = [int(i) for i in input().split(' ')]
    weigth = [int(i) for i in input().split(' ')]
    z = list(zip(price, weigth, ids))
    z.sort(key=lambda x: x[0], reverse=True)
    for i in z:
        if t + i[1] <= bag:
            t += i[1]
            res[1].append(i[2])
            res[0] += i[0]
    result.append(res)
for _ in result:
    print(_[0])
    print(" ".join(sorted(_[1], reverse=True)))

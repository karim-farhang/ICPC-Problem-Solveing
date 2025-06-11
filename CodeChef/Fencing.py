"""
3
4 6
......
.x.x..
....x.
..xx..
8 8
........
...xx...
..x...x.
.....x..
.x.xx...
..xx.x..
...x....
........
1 1
x
"""
tc = int(input())
rtc = []
while tc > 0:
    row, col = [int(x) for x in input().split(' ')]
    mt = []
    for i in range(row):
        x = list(input())
        if x.count('x') > 0:
            mt.append(x)
    mt = [[mt[i][j] for i in range(len(mt))] for j in range(len(mt[0]))]
    dim = []
    for i in mt:
        if i.count('x') > 0:
            dim.append(i)
    rtc.append([len(dim[0]), len(dim)])
    tc -= 1
for i in rtc:
    print(*i)

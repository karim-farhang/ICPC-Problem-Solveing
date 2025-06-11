"""
2
4 5 2 4 5 4 3 9 10 3 2 6 2 7 6 9 4 5 2 4
10 10 10 3 2 1 9 1 2 0 9 2 10 10 10 3 2 1 9 6
---------------------------------------------
4 5 2 4
4
10 10 10 3 2 1 9
7
"""
import collections as colc

t = int(input())
rtc = []
while t > 0:
    cc = colc.Counter([x for x in input().split(' ')])
    x = map(tuple, zip(cc.values(), cc.keys()))
    print(x)
    t -= 1

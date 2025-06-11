"""
3
0100110101
0111100010
0000000000
---------------------
4
3
-1
"""
import collections

t = int(input())
rt = []
while t > 0:
    count1 = 0
    count0 = 0
    countT = 0
    st = input()
    y = collections.Counter(st)
    if y['0'] != y['1']:
        countT = -1
    else:
        for i in st:
            if i == '0':
                count0 += 1
            if i == '1':
                count1 += 1
            if count0 == count1:
                countT += 1
                count0 = 0
                count1 = 0
    rt.append(countT)
    t -= 1
for i in rt:
    print(i)

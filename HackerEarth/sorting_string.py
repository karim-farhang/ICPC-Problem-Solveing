"""
3
aabbccdd
aabcc
hackerearth
------------------
aabbccdd
baacc
cktaaeehhrr
"""

import collections
tc = int(input())
rtc = []
while tc > 0:
    x = input()
    y = collections.Counter(x)
    zip1 = sorted(zip(y.values(), y.keys()))
    p = ''
    for i in zip1:
        p += i[1] * i[0]
    rtc.append(p)
    tc -= 1
for i in rtc:
    print(i)

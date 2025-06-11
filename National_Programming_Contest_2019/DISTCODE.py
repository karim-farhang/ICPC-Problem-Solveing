from itertools import *

tc = int(input().strip())
Rtc = []
while tc > 0:
    Rtc.append(set(pairwise(list(map(str, input().strip())))))
    tc -= 1

for i in Rtc:
    print(len(i))

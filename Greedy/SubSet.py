import itertools
import math
import sys

arr = [-1,-1,-2, 4,3]
subs = list()
m = -sys.maxsize - 1
for i in range(len(arr) + 1):
    subs.append(list(itertools.combinations(arr, i)))
for i in subs:
    for j in i:
        x = [int(p) for p in j]
        mu = 1
        mu = math.prod(x)
        if mu > m:
            m = mu
print(m)

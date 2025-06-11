import math
import sys
from itertools import pairwise

point = int(input())
x = [int(i) for i in input().split(" ")]
y = [int(j) for j in input().split(" ")]
x = x[:point]
y = y[:point]

xs = list(pairwise(x))
ys = list(pairwise(y))

m = sys.maxsize
for i in range(len(xs)):
    d = math.sqrt((pow(xs[i][1] - xs[i][0], 2)) + (pow(ys[i][1] - ys[i][0], 2)))
    print(d)
    m = min(m, d)

print(m)

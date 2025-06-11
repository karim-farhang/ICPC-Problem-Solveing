"""
10
2
4
2
6
1
7
8
9
2
1
----------
19
"""
import sys

si = int(input())
y = -sys.maxsize
rating = 0
count = 0
for i in range(si):
    x = int(input())
    if x > y and i > 0:
        rating += 1
    else:
        rating = 0
    count += rating + 1
    y = x
print(count)

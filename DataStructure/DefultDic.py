from collections import defaultdict

name = 'karim farhang'
d = defaultdict(lambda: 2)
for i in name:
    d[i] += 1
print(d)

d1 = {}
for i in name:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1
print(d1)

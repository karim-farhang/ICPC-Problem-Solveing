"""
2
ABCD CDAB
ABCD ACBD
-------------
true
false
"""
t = int(input())
rt = []
while t > 0:
    st1, st2 = list(map(str, input().split(' ')))
    if len(st1) != 0 and len(st2) != 0:
        if ''.join([st1 + st1]).count(st2) > 0:
            rt.append(True)
        else:
            rt.append(False)
    else:
        rt.append(False)
    t -= 1

for i in rt:
    print(i)

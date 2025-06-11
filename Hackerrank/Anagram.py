# -- anagram --------
from collections import Counter
res = []
t = int(input())
while t > 0:
    st = input()
    if len(st) % 2 != 0:
        res.append(-1)
    else:
        st1 = st[:len(st) // 2]
        st2 = st[len(st) // 2:]
        dic = Counter(st1) - Counter(st2)
        res.append(sum(dic.values()))
    t -= 1
for i in res:
    print(i)

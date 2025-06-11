# --- sherlock and the valid string --------
from collections import Counter

st = input()
dic = Counter(st)
most = Counter(dic.values())
ma = 0
key = ''
for i, j in most.items():
    if j > ma:
        ma = j
        key = i
count = 0
for i in dic.values():
    if i != key and i == 1:
        count += 1
    elif i != key:
        count += abs(int(i) - key)
if count <= 1:
    print("YES")
else:
    print("NO")

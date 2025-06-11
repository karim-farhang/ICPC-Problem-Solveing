"""
aba
---------
a,b,a,aba
4
"""
st = 'aba'
subSet = list()
count = 0
for i in range(len(st)):
    for j in range(i, len(st)):
        sub = st[i:j + 1]
        subSet.append(sub)
for i in subSet:
    jj = i[0]
    if len(i) % 2 != 0:
        if i == i[::-1]:
            count += 1
        elif i.count(jj) == len(i) and len(i) > 1:
            count += 1
print(count)

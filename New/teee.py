import string
from collections import Counter
st = input()
st = st.lower().replace(' ', '')
l = list()
for i in st:
    if i in string.ascii_lowercase:
        if [i, st.count(i), st.index(i)] not in l:
            l.append([i, st.count(i)])
l.sort(key=lambda x: x[1], reverse=True)
print(l)
res = list()
for i in range(len(l)-1):
    if l[i][1] == l[i+1][1]:
        res.append([l[i][0],l[i][1]])
    else:
        print(res)
        res = list()

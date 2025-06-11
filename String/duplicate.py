s = input()
set = list(set(s))
res = list()
for i in set:
    res.append(s.count(i))
count = 0
for i in res:
    if int(i) > 1:
        count+=1
print(count)
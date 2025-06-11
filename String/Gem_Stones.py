t = int(input())
res = []
res1 = []
for i in range(t):
    st = input()
    res += st
    res1.append(st)
res = list(set(res))
count =0
b = True
print(res)
for i in res:
    b=True
    for j in res1:
        if i not in j:
            b=False
            break
    if b:
        count +=1
print(count)
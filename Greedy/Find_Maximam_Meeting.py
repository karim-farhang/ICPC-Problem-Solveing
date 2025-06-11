s = [1,3,0,5,8,5]
f = [2,4,6,7,9,9]
res = []
for i in range(len(s)):
    res.append([s[i],f[i]])
res.sort(key=lambda x:x[1])

for i in range(len(res)):
    s[i]=res[i][0]
    f[i]=res[i][1]

i = 0
j =1
count =1
while j < len(s):
    if f[i] <= s[j]:
        count +=1
        i=j
        j+=1
    else:
        j+=1
print(count)
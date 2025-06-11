st = input()
st1 = list(set(st))
res = []
for i in st1:
    res.append(st.count(i))
odd , even = 0,0
for i in range(len(res)):
    if res[i] % 2 == 0:
        even+=1
    else:
        odd+=1
if odd <=1:
    print("YES")
else:
    print("NO")
n , q = map(int,input().split(' '))
st = input()
st = list(st)
while q > 0:
    s,e = map(int,input().split(' '))
    res = list()
    for i in range(s,e+1):
        for j in range(i+1,e+2):
            sub = st[i:j]
            if sub not in res:
                res.append(sub)
    print(len(res))
    q-=1
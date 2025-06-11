# --- funny string -------
q = int(input())
while q > 0:
    st = input()
    st1 = st[::-1]
    res = []
    res1 = []
    for i in range(len(st)-1):
        res.append(abs(ord(st[i])-ord(st[i+1])))
    for i in range(len(st1)-1):
        res1.append(abs(ord(st1[i])-ord(st1[i+1])))
    b = True
    for i in range(len(res)):
        if res[i] != res1[i]:
            b = False
    print('Funny' if b else 'Not Funny')
    q -=1
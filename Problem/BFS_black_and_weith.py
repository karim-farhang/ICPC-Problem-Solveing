si = int(input())
st = input()
cb = 0
cw = 0
W = 0
B = 0
for i in st:
    if i == 'W':
        cw += 1
        if cw>=3:
            W+=1
            cw=0
    if i=='B':
        pass

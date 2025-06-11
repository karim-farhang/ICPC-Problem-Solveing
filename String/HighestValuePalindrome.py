n,k = map(int,input().split(' '))
s = input()
s = list(s)
n = len(s)
mark = [0]*n
l = 0
r = n-1
while l <= r:
    if s[l] != s[r]:
        if s[l] > s[r]:
            s[r]=s[l]
            mark[r]=1
        else:
            s[l]=s[r]
            mark[l]=1
        k-=1
    l+=1
    r-=1
if k < 0:
    print(-1)
else:
    l=0
    r=n-1
    while l <= r:
        if l == r and k>=1:
            s[l]="9"
            break
        if s[l] < "9":
            if mark[l] ==0 and mark[r] == 0 and k >=2:
                s[l]=s[r]="9"
                k-=2
            if (mark[l] == 1 or mark[r] == 1) and k >=1:
                s[l]=s[r]="9"
                k-=1
        l+=1
        r-=1
    print("".join(s))

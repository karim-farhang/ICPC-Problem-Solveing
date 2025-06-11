n,s = map(int,input().split())
ar = list(map(int,input().split(',')))
b=False
for i in range(n+1):
    for j in range(i+1,n+1):
       if sum(ar[i:j]) == s:
           print(i+1,' ',j)
           b=True
           break
    if b:
        break
if not(b):
    print(-1)

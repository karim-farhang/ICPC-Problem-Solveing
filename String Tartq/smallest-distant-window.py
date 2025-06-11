# -- smallest distant window ---
import sys
s = list(input())
s1 = list(set(s))
print(s)
s1.sort()
print(s1)
min = sys.maxsize
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        sub = s[i:j]
        sub.sort()
        if len(sub) < min and s1 in s:
            min = len(sub)
print(min)
from collections import Counter
n = int(input())
s = list(input().split(','))
dic = Counter(s)
dic = sorted(zip(dic.values(),dic.keys()))
for i,y in dic:
    if i > 1:
        print(y)
        break

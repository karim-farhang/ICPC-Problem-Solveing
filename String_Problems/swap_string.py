from collections import Counter

x = list(input())
y = list(input())
count = 0
if Counter(x) != Counter(y):
    print(-1)
else:
    for i in range(len(x)):
        if y[i] != x[i]:
            count += 1
if count > 1:
    count /= 2
print(int(count))

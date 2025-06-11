ss = list(map(int, input().split(" ")))
d = int(input())
ss.sort()
ss = [x for x in ss if x != d]
ex = 0
for i in range(len(ss)):
    if ss[i] % d == 0 and ss[i] != 0:
        ss[i] = 0
        ss.remove(0)
        i -= 1
        ex += 1
sm = 0
for i in ss:
    sm += i
    ex += 1
print(ex)
n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
sub = list()
ls = []
for i in a:
    ls.append(i)
    for j in a:
        ls.append(abs(j - i))
    sub.append([ls[0], sum(ls)])
    ls = []
sub.sort(key=lambda x: x[1])
print(sub)
sub = [sub[i][0] for i in range(m)]
print(sub)
print(max(sub) - min(sub))

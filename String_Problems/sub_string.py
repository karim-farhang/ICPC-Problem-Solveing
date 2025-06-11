st = input()
count = 0
subs = list()
for i in range(len(st)):
    for j in range(i, len(st)):
        sub = st[i:j + 1]
        if ('a' in sub) and ('b' in sub) and ('c' in sub):
            pass
        else:
            count += 1
            subs.append(sub)
print(count)

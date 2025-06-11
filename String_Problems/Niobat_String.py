t = int(input())
result = list()
while t > 0:
    words = ['hello', 'world']
    p = len(words)-1
    p = -p
    q = 0
    while abs(p) != q:
        temp = words[p]
        words[p] = words[q]
        words[q] = temp
        p -= 1
        q += 1
    for i in range((len(words) // 2)):
        x, y = words[-i - 1], words[i]
        words[-i - 1], words[i] = y, x
    result.append(words)
    t -= 1
for i in result:
    print(*i)

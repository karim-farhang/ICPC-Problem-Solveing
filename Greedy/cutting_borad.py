a = int(input())
for i in range(a):
    x, y = map(int, input().split(' '))
    xCost = map(int, input().split(' '))
    yCost = map(int, input().split(' '))
    hacks = []
    for j in xCost:
        hacks.append((j, 0))
    for p in yCost:
        hacks.append((p, 1))
    pieces = [1, 1]
    ans = 0
    for i in sorted(hacks, reverse=True):
        ans += (i[0] * pieces[1 - i[1]]) % (10 ** 9 + 7)
        ans %= 10 ** 9 + 7
        pieces[i[1]] += 1
    print(ans)

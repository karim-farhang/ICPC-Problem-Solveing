"""
3
Redivide
please do not step on the pets there.
The owl Ate my metal worm
--------------------------
1
15
7
"""
t = int(input())
rtc = []
while t > 0:
    count = 0
    x = list(input().replace(' ', ''))
    r = 0
    l = -1
    while True:
        if x[r] != x[l]:
            x[r] = 'right'
            x.remove('right')
            count += 1
        if x[l] != x[r]:
            x[l] = 'left'
            x.remove('left')
            count += 1
        else:
            l -= 1
            r += 1
        if x == x[::-1]:
            break
    rtc.append(count)
    t -= 1
for i, value in enumerate(rtc):
    print(f'{i} -> {value}')

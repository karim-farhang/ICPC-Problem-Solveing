day, foot, spend = map(int, input().split(' '))
x = day * spend
closeDay = day // 7
y = day - closeDay
y = y * foot
if y > x:
    print('YES')
else:
    print('NO')
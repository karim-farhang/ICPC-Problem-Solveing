"""
3
235
5:10,10:6,20:4,50:3
370
10:4,5:20,40:4,70:3,100:2,50:5
172
10:4,5:20,40:4,70:3,100:2,50:5
-------------------------------
Customer1:
50 3
20 4
5 1
Customer2:
100 2
70 2
10 3
Customer3:
Impossible
"""
tc = int(input())
rtc = []
customer = 1
while tc > 0:
    back = int(input())
    money = [list(map(int, x.split(':'))) for x in input().split(',')]
    money.sort(key=lambda x: x[0], reverse=True)
    print(f'Customer {customer}')
    result = []
    count = 0
    for i in range(len(money)):
        while back >= money[i][0] and money[i][1] > 0:
            back -= money[i][0]
            money[i][1] -= 1
            count += 1
        if count > 0:
            result.append([money[i][0], count])
            count = 0
    if 0 < back < money[-1][0]:
        result.clear()
        print('Imposable')
        break
    else:
        for i in result:
            print(*i)
    customer += 1
    tc -= 1

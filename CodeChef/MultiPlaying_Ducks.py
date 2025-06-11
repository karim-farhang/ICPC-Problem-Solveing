"""
3
10 02/01
55 06/17
1 12/31
# ---------------

tc = int(input())
while tc > 0:
    inti, pub_date = [str(x) for x in input().split(' ')]
    inti = int(inti)
    pub_date = pub_date.replace('/', ' ').split(' ')
    month = int(pub_date[0])
    day = int(pub_date[1])
    total_day = 0
    for i in range(1, month + 1):
        if i in [4, 6, 9, 11]:
            total_day += 30
        if i == 2:
            total_day += 28
        else:
            total_day += 31
    total_day += day
    pass_away = 0
    doubles = 0
    count = 0
    while count != total_day:
        count += 1
        if count
    tc -= 1
"""
"""
2
500 300
90 24
"""
tc = int(input())
rtc = []
while tc > 0:
    hits = input().split(' ')
    johan = int(hits[0])
    under = int(hits[1])
    result = ''
    if johan * (1 / 3) > under:
        result = 'John Cina'
    else:
        result = 'Under Taker'
    rtc.append(result)
    tc -= 1
for i in rtc:
    print(i)

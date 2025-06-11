from collections import Counter

tc = int(input())
tcR = list()
while tc:
    sers = list(map(int, input().split(" ")))
    day = int(input())
    get = sers.count(day)
    tcR.append(get)
    tc -= 1

for i in tcR:
    print(i)

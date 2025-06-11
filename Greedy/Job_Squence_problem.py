"""
2
4
1 4 20
2 1 10
3 1 40
4 1 30
5
1 2 100
2 1 19
3 2 27
4 1 25
5 1 15
------------
2 60
2 127
"""
t = int(input())
rtc = []
while t > 0:
    n = int(input())
    Dictionary = {}
    IDes = []
    deads = []
    for i in range(n):
        ID, deadline, profit = [int(x) for x in input().split(' ')]
        if deadline not in deads:
            deads.append(deadline)
        IDes.append((ID, profit))

    Profit = 0
    for j in range(len(deads)):
        mx = max(IDes, key=lambda x: x[1])
        Profit += mx[1]
        IDes.remove(mx)
    rtc.append(Profit)
    t -= 1
for i in rtc:
    print(i)
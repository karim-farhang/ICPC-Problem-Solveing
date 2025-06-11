tc = int(input())
rtc = []
while tc > 0:
    day, job = [int(x) for x in input().split(' ')]
    for i in range(day):
        x = [int(i) for i in input().split(' ')]
        for i in range(len(x) - 1):
            if x[i + 1] < x[i]:
                rtc.append(x.index(x[i])+1)
                break
    tc -= 1
for i in rtc:
    print(i)

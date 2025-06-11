"""
2
1 3 0 5 8 5
2 4 6 7 9 9
75250 50074 43659 8931 11273 27545 50879 77924
112960 114515 81825 93424 54316 35533 73383 160252
-----------------------------------------------------
4
3
"""
t = int(input())
rtc = []
while t > 0:
    start = [int(x) for x in input().split(' ')]
    end = [int(x) for x in input().split(' ')]
    act = zip(start, end)
    act = list(sorted(act, key=lambda x: x[1]))
    i = 0
    count = 1
    for j in range(len(act)):
        st = act[j][0]
        if act[i][1] < st:
            count += 1
            i = j
    rtc.append(count)
    t -= 1
for i in rtc:
    print(i)


def maximumMeetings(self, n, start, end):
    act = zip(start, end)
    act = list(sorted(act, key=lambda x: x[1]))
    i = 0
    count = 1
    for j in range(len(act)):
        st = act[j][0]
        if act[i][1] < st:
            count += 1
            i = j
    return count

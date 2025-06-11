tc = int(input().strip())
rtc = []
while tc > 0:
    pol, time_per_year, ratio_interest, year = [float(x) for x in input().split(' ')]
    amount = pol * (1 + ratio_interest / time_per_year) ** (time_per_year * year)
    rtc.append('$' + str(int(amount)))
    tc -= 1
for i in rtc:
    print(i)

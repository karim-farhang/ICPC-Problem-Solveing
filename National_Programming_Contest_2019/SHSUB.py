tc = int(input().strip())
rtc = []
while tc > 0:
    names = [str(x) for x in input().strip().split(',')]
    names.sort(key=len, reverse=True)
    sub = ''

    tc -= 1

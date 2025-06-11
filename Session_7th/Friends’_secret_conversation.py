"""
2
hello
you are cute
-------------
ifmmp
zpv bsf dvuf
"""
tc = int(input())
rtc = []
while tc > 0:
    orginial_msg = input()
    result = ''
    for i in orginial_msg:
        if i == 'z':
            result += 'a '
        if i == ' ':
            result += ' '
        else:
            result += chr(ord(i) + 1)
    rtc.append(result)
    tc -= 1
for i in rtc:
    print(i)

def int_to_Roman(num):
    lookup = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
              ]
    res = ''
    for (n, roman) in lookup:
        (d, num) = divmod(num, n)
        res += roman * d
    return res


"""
4
46
19
392
88
"""
tc = int(input())
rtc = []
while tc > 0:
    rtc.append(int_to_Roman(int(input())))
    tc -= 1
print()
for i in rtc:
    print(i)

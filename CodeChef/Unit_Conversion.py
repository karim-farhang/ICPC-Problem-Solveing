"""
2
2
1 dime equals 10 cent
100 cent equals 1 dollar
20 dime to dollar
3
300 floor equals 1 zinc
1 din equals 20 zinc
1 din equals 5000 rand
1000 rand to zinc
----------------------------
"""

t = int(input())
rtc = []
while t > 0:
    rows = int(input())
    unit = []
    for i in range(rows):
        u_1, name_1, _, u_2, name_2 = input().split(' ')
        unit.append([(int(u_1), name_1), (int(u_2), name_2)])
    total, from_un, _, to_un = input().split(' ')
    total = int(total)
    for i in unit:
        
        pass
    print('------------------')
    t -= 1
print(*rtc)

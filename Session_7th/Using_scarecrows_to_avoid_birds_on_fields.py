"""
3
3
.#.
11
...##....##
2
##
"""
tc = int(input())
rtc = []
while tc > 0:
    siz = int(input())
    field = input()
    field = list(field[:siz])
    field.sort()
    cont = 0
    mat = 0
    for i in range(len(field)):
        if field[i] == '.':
            cont += 1
        if cont == 2:
            mat += 1
            cont = 0
    rtc.append(mat)
    tc -= 1
for i in range(len(rtc)):
    print(f'Case {i + 1}: {rtc[i]}')

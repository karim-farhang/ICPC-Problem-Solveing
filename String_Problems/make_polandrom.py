"""
2
baba//aaa/ab//
72
23
aba/bab/
4
6
--------
213
10
"""
t = int(input())
result = []
while t > 0:
    strings = list(input())
    aCout = int(input())
    bCoust = int(input())
    j = len(strings) - 1
    i = 0
    count = 0
    if '/' not in strings and strings != strings[::-1]:
        result.append(-1)
    else:
        while strings != strings[::-1]:
            if strings[i] == '/' and strings[j] == '/':
                if aCout < bCoust:
                    strings[i] = 'a'
                    strings[j] = 'a'
                    count += (aCout * 2)
                    j -= 1
                    i += 1
                else:
                    strings[j] = 'b'
                    strings[i] = 'b'
                    j -= 1
                    j += 1
                    count += (bCoust * 2)
            elif strings[i] != strings[j]:
                if strings[i] == '/' and strings[j] == 'a':
                    strings[i] = 'a'
                    count += aCout
                    j -= 1
                    i += 1
                if strings[i] == '/' and strings[j] == 'b':
                    strings[i] = 'b'
                    count += bCoust
                    j -= 1
                    i += 1
                if strings[j] == '/' and strings[i] == 'a':
                    strings[j] = 'a'
                    count += aCout
                    j -= 1
                    i += 1
                if strings[j] == '/' and strings[i] == 'b':
                    strings[j] = 'b'
                    count += bCoust
                    j -= 1
                    i += 1
            else:
                j -= 1
                i += 1
    result.append(count)
    t -= 1
for i in result:
    print(i)

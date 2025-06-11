t = input()
result = list()
if not str(t).isdigit():
    result.append('Invalid Test')
if str(t).isdigit():
    t = int(t)
    if t > 10 or t == 0:
        result.append('Invalid Test')
    else:
        while t > 0:
            stirng = input()
            lower = 0
            upere = 0
            if len(stirng) > 100:
                result.append('Invalid Input')
            else:
                for i in stirng:
                    if i.islower():
                        lower += 1
                    if i.isupper():
                        upere += 1
                if upere == 0 and lower == 0:
                    result.append('Invalid Input')
                else:
                    change = min(lower, upere)
                    result.append(change)
            t -= 1
for i in result:
    print(i)

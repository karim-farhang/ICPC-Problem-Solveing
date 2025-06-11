x = '100:2,50:4,20:2'
x = [int(i) for i in x.replace(':', ',').split(',')]
y = 390
print(x)
get = []
i = 0
while y != 0:
    if y >= x[i]:
        y -= x[i]
        get.append(x[i])
        x[i + 1] -= 1
        if x[i + 1] == 0:
            i += 2
    else:
        i += 2
print(get)
print(x)

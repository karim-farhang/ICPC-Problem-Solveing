t = int(input().strip())
result = []
while t > 0:
    siz = int(input().strip())
    star = siz
    spaceInside = 0
    ins = ' '
    x = ''''''
    for h in range(siz):
        x += ' ' * star + '/' + spaceInside * ins + '\\' + ' ' * star + "\n"
        star -= 1
        spaceInside += 2
        if (h + 2) == siz:
            ins = '_'

    result.append(x)
    t -= 1
for i in result:
    print(i)

t = int(input())
while t > 0:
    mk, dehqan = map(int, input().split(' '))
    maks = list()
    for i in range(dehqan):
        price, ma = map(int, input().split(' '))
        ratio = ma / price
        maks.append((price, ma, ratio))
    maks.sort(key=lambda x: x[2])
    get = 0
    count = 0
    print(maks)
    for i in range(len(maks)):
        if (maks[i][1] + get) <= mk:
            get += maks[i][1]
            count += maks[i][0] * maks[i][1]
            if mk == get:
                break
        else:
            x = (mk - get)
            count += (x * maks[i][2])
            break
    print(count)
    t -= 1

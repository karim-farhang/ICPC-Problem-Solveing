cons = [int(x) for x in input().split(' ')]
get = int(input())
cons.sort(reverse=True)
i = 0
x = []
while get != 0:
    if get >= cons[i]:
        get -= cons[i]
        x.append(cons[i])
    else:
        i += 1
print(x)

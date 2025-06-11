list1 = list()
result = list()
while True:
    inp = input().split(' ')
    for i in range(len(inp)):
        if '/' not in ''.join(inp[i]):
            inp[i] = inp[i].replace('->', '.')
    list1.append(inp)
    if ''.join(inp[0] + " " + inp[1]) == 'return 0;':
        break
for i in list1:
    print(*i)

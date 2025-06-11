def isPrine(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True


Tc = int(input())
result = []
for i in range(Tc):
    numb = [int(y) for y in input().split(" ")]
    prime = len([z for z in numb if isPrine(z)])
    result.append([prime])
    numb.reverse()
    result.append(numb)
for x in range(len(result)):
    for y in range(len(result[x])):
        print(result[x][y], end=" ")
    print()

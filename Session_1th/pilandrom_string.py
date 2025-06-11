tc = int(input())
result = []
while tc > 0:
    stram = input().split(" ")
    resultCas = []
    n = len(stram)
    for i in range(n):
        x = list(stram[i])
        y = []
        for j in range(len(x), 0, -1):
            y.extend(x[j - 1])
        if x == y:
            resultCas.append(stram[i])
    result.append(resultCas)
    tc -= 1
for i in result:
    print(i)

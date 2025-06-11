coder = int(input())
skil = [int(x) for x in input().split(" ")]
skil.sort()
skil.reverse()
for j in range(len(skil) - 1):
    if skil[j] >= skil[j + 1]:
        skil[j + 1] = 0
skil = [x for x in skil if x != 0]
skil.pop(len(skil) - 1)
print(sum(skil))

t = int(input())
d = {}
for _ in range(t):
    inp = input().split(' ')
    scor = [float(inp[x]) for x in range(1, len(inp))]
    d[inp[0]] = sum(scor) / len(scor)
sho = input()
result = format(d[sho], '.2f')
print(result)

def printMaxActivities(s, f):
    n = len(f)
    i = 0
    cont = 1
    for j in range(n):
        if s[j] >= f[i]:
            cont += 1
            i = j
    return cont

s = [1, 3, 0, 5, 5, 8]
f = [2, 4, 6, 7, 9, 9]

print(s)
print(f)
printMaxActivities(s, f)

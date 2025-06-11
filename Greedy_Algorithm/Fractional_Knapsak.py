w = [10, 20, 30]
v = [60, 100, 120]
capacity = 50

ratio = []
for i in range(len(w)):
    ratio.append(v[i] / w[i])
for i in range(len(w)):
    for j in range(len(w) - i - 1):
        if ratio[j] >= ratio[j + 1]:
            ratio[j], ratio[j + 1] = ratio[j + 1], ratio[j]
            w[j], w[j + 1] = w[j + 1], w[j]
            v[j], v[j + 1] = v[j + 1], v[j]

totalBarrow = []
totalWeight = []
print(w)
print(v)
print(ratio)
print()

for i in range(len(w)):
    if capacity == 0:
        break
    if w[i] <= capacity:
        totalBarrow.append(v[i])
        totalWeight.append(w[i])
        capacity -= w[i]
    elif w[i] >= capacity:
        re = w[i] - capacity
        x = w[i] - re
        totalWeight.append(x)
        moy = ratio[i] * x
        totalBarrow.append(moy)
        capacity -= x

print(capacity)
print(totalWeight)
print(totalBarrow)

print(sum(totalWeight))
print(sum(totalBarrow))

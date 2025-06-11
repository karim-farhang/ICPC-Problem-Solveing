from collections import Counter

A = [3, 5, 7, 11, 5, 8]
B = [5, 7, 11, 10, 5, 8]

ac = Counter(A)
bc = Counter(B)

print(ac)
print(bc)

pairs = 0
for val in ac:
    if val in bc:
        pairs += min(ac[val], bc[val])
        print(ac[val], bc[val])
    if pairs == len(A):
        pairs -= 1
    else:
        pairs += 1

print(pairs)
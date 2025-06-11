A = [1, 2, 3, 3]
x = 6
subs = []
sub = []
for i in range(len(A)):
    for j in range(len(A)):
        sub.clear()
        sub.insert(0, A[i])
        sub.extend(A[j:])
        print(sub)
        if sum(sub) == x:
            subs.append(sub)
print(subs)

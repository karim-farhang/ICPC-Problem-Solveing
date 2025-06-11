work = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
st = [0, 3, 1, 5, 5, 8]
fn = [6, 4, 2, 9, 7, 9]

print(work)
print(st)
print(fn)
print()
s = len(work)
for i in range(0, s):
    for j in range(0, s - i - 1):
        if fn[j] > fn[j + 1]:
            work[j], work[j + 1] = work[j + 1], work[j]
            st[j], st[j + 1] = st[j + 1], st[j]
            fn[j], fn[j + 1] = fn[j + 1], fn[j]

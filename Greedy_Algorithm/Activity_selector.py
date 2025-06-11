'''
0 3 1 5 5 8
6 4 2 9 7 9

0 3 1 5 5 8
6 4 2 9 7 9

1 3 0 5 3 5 6 8 8 2 12
4 5 6 7 8 9 10 11 12 13 14

8 9 10 11
9 10 11 12
'''
work = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11']
st = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
fn = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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

print(work)
print(st)
print(fn)

i = 0
print(work[0])
for j in range(s):
    if st[j] <= fn[i]:
        print(work[j])
        i = j

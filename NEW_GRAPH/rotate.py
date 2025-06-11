"""
4
+23
123
123
123
"""


def rotate90degree(a):
    r = len(a)
    c = len(a[0])
    result = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(a[j][i])
        result.append(row[::-1])
    return result


def transpose(a):
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def filp_horzontal_and_Virtical(a):
    return [[a[j][i] for i in range(len(a[0]))][::-1] for j in range(len(a))][::-1]


def filp_horzontal(a):
    return [[a[j][i] for i in range(len(a[0]))][::-1] for j in range(len(a))]


a = []
siz = int(input())
for i in range(siz):
    a.append(list(input()))

for i in a:
    print(i)
print('-----------')
b = transpose(a)
for i in b:
    print(i)
print('-------')
b = transpose(b)
for i in b:
    print(i)
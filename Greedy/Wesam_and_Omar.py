t = int(input())
while t > 0:
    matrix = list()
    for i in range(3):
        row = list(input())
        matrix.append(row)
    if t != 1:
        input()
    if matrix[1][1] == '.':
        print('YES')
    elif matrix[1][0] != '*' and matrix[2][1] != '*':
        print('YES')
    elif matrix[0][1] != '*' and matrix[1][2] != '*':
        print('YES')
    else:
        print('NO')
    t -= 1

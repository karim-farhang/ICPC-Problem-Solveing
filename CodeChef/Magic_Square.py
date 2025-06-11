t = int(input().strip())
rt = []
while t > 0:
    m_square = []
    count = 0
    for i in range(3):
        inp = [int(x) for x in input().strip().split(' ')]
        m_square.append(inp)
    row = 0
    col = 0
    min_di = 0
    sub_di = 0
    for x in range(len(m_square)):
        for y in range(len(m_square)):
            row += m_square[x][y]
            col += m_square[y][x]
            if x == y:
                min_di += m_square[x][y]
            if x + y == len(m_square) - 1:
                sub_di += m_square[x][y]
        if row != 15:
            count += 1
        if col != 15:
            count += 1
        row = 0
        col = 0
    if min_di != 15:
        count += 1
    if sub_di != 15:
        count += 1
    rt.append(count)
    t -= 1
for i in rt:
    print(i)

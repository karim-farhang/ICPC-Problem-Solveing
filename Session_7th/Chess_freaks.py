dic = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}

"""
3
a1 c3
d4 c3
h1 h3
-------
True
True
False
"""

tc = int(input())
rtc = []
while tc > 0:
    locations = list(input())
    b_row = int(dic[locations[0]])
    b_col = int(locations[1])
    p_row = int(dic[locations[3]])
    p_col = int(locations[4])

    fond = False
    # top Right
    row = b_row
    col = b_col
    for r in range(row, -1, -1):
        if r == p_row and col == p_col:
            fond = True
            break
        col += 1

    if not fond:
        # top left
        row = b_row
        col = b_col
        for r in range(row, -1, -1):
            if r == p_row and col == p_col:
                fond = True
                break
            col -= 1

    if not fond:
        # bottom left
        row = b_row
        col = b_col
        for r in range(row, 8, 1):
            if r == p_row and col == p_col:
                fond = True
                break
            col -= 1

    if not fond:
        # bottom left
        row = b_row
        col = b_col
        for c in range(col, 8, 1):
            if c == p_col and row == p_row:
                fond = True
                break
            row += 1

    rtc.append(fond)
    tc -= 1

for i in rtc:
    print(i)

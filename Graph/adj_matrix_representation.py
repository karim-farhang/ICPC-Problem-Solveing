"""
undirected unwieded
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
dircted widthed
----------------------------
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
A D
"""


def printMatrix(matrix):
    row, col = len(matrix), len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end='\t')
        print()


def undirectedGraph():
    v, e = map(int, input().split(' '))
    matrix = [[0] * v for i in range(v)]
    for i in range(e):
        s, d = map(str, input().split(' '))
        s = ord(s) - ord('A')
        d = ord(d) - ord('A')
        matrix[s][d] = 1
        matrix[d][s] = 1


def directedWidthedGraph():
    v, e = map(int, input().split(' '))
    matrix = [[0] * v for i in range(v)]
    for i in range(e):
        s, d, m = map(str, input().split(' '))
        s = ord(s) - ord('A')
        d = ord(d) - ord('A')
        m = int(m)
        matrix[s][d] = m
    printMatrix(matrix)


directedWidthedGraph()

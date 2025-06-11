from collections import deque


def isValid(x, y, N):
    return N > x >= 0 and N > y >= 0


def minStepToReachTarget(KnightPos, TargetPos, N):
    dxy = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    KnightPos[0] -= 1
    KnightPos[1] -= 1
    TargetPos[0] -= 1
    TargetPos[1] -= 1
    vis = [[False] * N for _ in range(N)]
    q = deque()
    q.append([KnightPos[0], KnightPos[1], 0])

    vis[KnightPos[0]][KnightPos[1]] = True

    while len(q) != 0:

        cur = q.popleft()
        x = cur[0]
        y = cur[1]
        steps = cur[2]

        if x == TargetPos[0] and y == TargetPos[1]:
            return steps

        for i in range(8):

            n_x = x + dxy[i][0]
            n_y = y + dxy[i][1]

            if isValid(n_x, n_y, N) and not vis[n_x][n_y]:
                q.append([n_x, n_y, steps + 1])
                vis[n_x][n_y] = True
    return -1


"""
6
4 5
1 1
-------
3
"""
n = int(input())
kingth = list(map(int, input().split(' ')))
target = list(map(int, input().split(' ')))
x = minStepToReachTarget(kingth, target, n)
print(x)

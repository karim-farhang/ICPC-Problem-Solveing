import sys

sys.setrecursionlimit(10 ** 8)


class Solution:
    def numIslands(self, arr):
        # code here
        visited = [[0] * len(arr[0]) for i in range(len(arr))]

        def isValid(x, y):
            if 0 <= x < n and 0 <= y < m:
                return True
            return False

        def dfs(grid, x, y):
            visited[x][y] = 1
            for i in [[-1, -1], [1, 1], [1, 0], [0, 1], [1, -1], [-1, 1], [-1, 0], [0, -1]]:
                if isValid(x + i[0], y + i[1]) and visited[x + i[0]][y + i[1]] == 0:
                    if grid[x + i[0]][y + i[1]] == 1:
                        dfs(grid, x + i[0], y + i[1])

        count = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if visited[i][j] == 0 and arr[i][j] == 1:
                    dfs(arr, i, j)
                    count += 1
        return count


n, m = map(int, input().strip().split(' '))
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
s = Solution()
x = s.numIslands(arr)
print(x)

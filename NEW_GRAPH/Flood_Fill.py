def floodFill(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image

    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


n = int(input())
image = list()
for _ in range(n):
    row = list(map(int, input().split(' ')))
    image.append(row)

i, j, color = map(int, input().strip().split(' '))
new = floodFill(image, i, j, color)
for t in new:
    print(*t)

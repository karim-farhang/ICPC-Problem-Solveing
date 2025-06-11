from collections import deque


class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)


def BFS(g, source, n):
    q = deque()
    discovered = [False] * (n + 1)

    discovered[source] = True
    q.append((source, 0))
    while q:
        vertex, min_dist = q.popleft()
        if vertex == n:
            return min_dist
        for u in g.adjList[vertex]:
            if not discovered[u]:
                discovered[u] = True
                q.append((u, min_dist + 1))


def findMinimumMoves(ladder, snake):
    n = 10 * 10
    edges = []
    for i in range(n):
        j = 1
        while j <= 6 and i + j <= n:
            src = i
            _ladder = ladder.get(i + j) if (ladder.get(i + j)) else 0
            _snake = snake.get(i + j) if (snake.get(i + j)) else 0
            if _ladder or _snake:
                dest = _ladder + _snake
            else:
                dest = i + j
            edges.append((src, dest))
            j = j + 1
    g = Graph(edges, n)
    return BFS(g, 0, n)


t = int(input())
while t > 0:
    l = int(input())
    ladder = {}
    for _ in range(l):
        u, v = map(int, input().split())
        ladder[u] = v
    s = int(input())
    snake = {}
    for _ in range(s):
        u, v = map(int, input().split())
        snake[u] = v
    print(findMinimumMoves(ladder, snake))
    t -= 1

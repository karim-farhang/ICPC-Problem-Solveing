def quickResult(snake, leader):
    leader.sort(key=lambda x: x[0])
    snake.sort(key=lambda x: x[0])
    borad = [[]]


t = int(input())
while t > 0:
    l = int(input())
    leaders = list()
    for _ in range(l):
        leaders.append(list(map(int, input().strip().split(' '))))
    s = int(input())
    snake = list()
    for _ in range(s):
        snake.append(list(map(int, input().strip().split(' '))))
    res = quickResult(snake, leaders)
    print(res)
    t -= 1

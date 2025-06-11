"""
ID Deadline Profit
4
1 4 20
2 1 10
3 1 40
4 1 30
"""


def JobScheduling(Jobs, n):
    res, count = 0, 0
    Jobs.sort(key=lambda x: x[1], reverse=True)
    result = [0 for i in range(n)]
    slot = [False for i in range(n)]
    for i in range(n):
        for j in range(min(n, Jobs[i][1]) - 1, -1, -1):
            if not slot[j]:
                result[j] = i
                slot[j] = True
                break
    for i in range(n):
        if slot[i]:
            res += Jobs[result[i]][2]
            count += 1
    ans = []
    ans.append(count)
    ans.append(res)
    return ans


n = int(input())
works = list()
for i in range(n):
    ID, deadline, profit = map(int, input().split(' '))
    works.append((ID, deadline, profit))

print(JobScheduling(works, n))

adj = []
visited = []
num = 0
def dfs(v):
    global adj, visited, num
    visited[v] = True
    num += 1
    for i in range(len(adj[v])):
        if not visited[adj[v][i]]:
            dfs(adj[v][i])


def numberOfPairs(N, arr):
    global adj, visited, num
    adj = []
    for i in range(N):
        adj.append([])

    for i in range(len(arr)):
        adj[arr[i][0]].append(arr[i][1])
        adj[arr[i][1]].append(arr[i][0])
    visited = [False] * N
    v = []
    num = 0
    for i in range(N):
        if not visited[i]:
            dfs(i)
            v.append(num)
            num = 0
    ans = N * int((N - 1) / 2)
    for i in range(len(v)):
        ans -= (v[i] * int((v[i] - 1) / 2))
    ans += 1
    print(ans)

n, e = map(int, input().split())
arr = list()
for _ in range(e):
    u, v = map(int, input().split())
    arr.append((u, v))
numberOfPairs(n, arr)

def dfs_cycle(graph, node, onpath, visited):
    if visited[node]:
        return False
    onpath[node] = visited[node] = True
    for neigh in graph[node]:
        if onpath[neigh] or dfs_cycle(graph, neigh, onpath, visited):
            return True
    return False

def canFinish(Tasks, prerequisites):
    graph = []
    for i in range(Tasks):
        graph.append([])
    for first, second in prerequisites:
        graph[second].append(first)
    onpath = [False] * Tasks
    visited = [False] * Tasks
    for i in range(Tasks):
        if not visited[i] and dfs_cycle(graph, i, onpath, visited):
            return False
    return True

task, per = map(int, input().strip().split(' '))
pre_task = list()
for i in range(per):
    f, s = map(int, input().strip().split(' '))
    pre_task.append((f, s))
print(f"Possible ->{canFinish(task, pre_task)}")

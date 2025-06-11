def addEdge(u, v, w):
    global adj
    adj[u].append((v, w))
def shortestPath(src):
    setds = {}
    dist = [10 ** 18 for i in range(n)]
    global adj
    setds[(0, src)] = 1
    dist[src] = 0
    while (len(setds) > 0):
        tmp = list(setds.keys())[0]
        del setds[tmp]
        u = tmp[1]
        for i in adj[u]:
            v = i[0];
            weight = i[1]
            if (dist[v] > dist[u] + weight):
                if (dist[v] != 10 ** 18):
                    del setds[(dist[v], v)]
                dist[v] = dist[u] + weight
                setds[(dist[v], v)] = 1

    return dist
def modelGraphWithEdgeWeight(edge, E, V):
    global adj
    for i in range(E):
        addEdge(edge[i][0], edge[i][1], 0)
        addEdge(edge[i][1], edge[i][0], 1)
def getMinEdgeReversal(edge, E, V, src, dest):
    modelGraphWithEdgeWeight(edge, E, V)
    dist = shortestPath(src)
    if (dist[dest] == 10 ** 18):
        return -1
    else:
        return dist[dest]
n, e = map(int,input().split())
edge = []
for i in range(e):
    sur , des = map(int,input().split())
    edge.append([sur,des])
adj =[[] for i in range(n+1)]
minEdgeToReverse = getMinEdgeReversal(edge, e, n, 0, 6)
if (minEdgeToReverse != -1):
    print(minEdgeToReverse)
else:
    print("Not possible")
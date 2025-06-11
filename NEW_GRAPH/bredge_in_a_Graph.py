import sys
from collections import defaultdict
brige = []
class Graph:
    global brige
    def __init__(self, graph, nodes):
        self.nodes = nodes
        self.graph = graph
        self.Time = 0

    def bridgeUtil(self, u, visited, parent, low, disc):
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    brige.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = [False] * self.nodes
        disc = [sys.maxsize] * self.nodes
        low = [sys.maxsize] * self.nodes
        parent = [-1] * self.nodes
        brig = list()
        for i in range(self.nodes):
            if not visited[i]:
                self.bridgeUtil(i, visited, parent, low, disc)
t = int(input())
while t > 0:
    n, e = map(int, input().split())
    G = defaultdict(list)
    for _ in range(e):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    g = Graph(G, n)
    g.bridge()
    print(brige)
    brige = []
    t -= 1

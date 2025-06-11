from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def printVertexCover(self):
        visited = [False] * (self.V)
        for u in range(self.V):
            if not visited[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        visited[u] = True
                        break
        for j in range(self.V):
            if visited[j]:
                print(j, end=' ')
        print()
n,e = map(int,input().split())
g = Graph(n)
for i in range(e):
    s,d = map(int,input().split())
    g.addEdge(s,d)
g.printVertexCover()

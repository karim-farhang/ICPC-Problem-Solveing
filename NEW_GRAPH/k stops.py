import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights, src, dst, K):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Form Q to be used as min-heap of weights
        Q = [(0, src, K)]

        while Q:
            # Greedly choose the path with minimum weight
            weight, node, k = heapq.heappop(Q)
            # Node arrived at destination
            if node == dst:
                return weight
            if k >= 0:
                for v, w in graph[node]:
                    added_weight = weight + w
                    heapq.heappush(Q, (added_weight, v, k - 1))
        return -1

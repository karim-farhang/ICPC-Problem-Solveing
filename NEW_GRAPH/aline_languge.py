from collections import defaultdict

class Solution:

    def __init__(self):
        self.vertList = defaultdict(list)

    def addEdge(self, u, v):
        self.vertList[u].append(v)

    def topologicalSortDFS(self, givenV, visited, stack):
        visited.add(givenV)
        for nbr in self.vertList[givenV]:
            if nbr not in visited:
                self.topologicalSortDFS(nbr, visited, stack)
        stack.append(givenV)
    def findOrder(self, dict, N, K):
        list1 = dict
        for i in range(len(list1) - 1):
            word1 = list1[i]
            word2 = list1[i + 1]
            rangej = min(len(word1), len(word2))
            for j in range(rangej):
                if word1[j] != word2[j]:
                    u = word1[j]
                    v = word2[j]
                    self.addEdge(u, v)
                    break
        stack = []
        visited = set()
        vlist = [v for v in self.vertList]
        for v in vlist:
            if v not in visited:
                self.topologicalSortDFS(v, visited, stack)
        result = " ".join(stack[::-1])
        return result


class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word
    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)
        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)
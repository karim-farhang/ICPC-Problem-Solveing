class val:
    def __init__(self, first, second):
        self.first = first
        self.second = second
def findMaxChainLen(p, n, prev, pos):
    global m
    if (val(pos, prev) in m):
        return m[val(pos, prev)]
    if (pos >= n):
        return 0
    if (p[pos].first <= prev):
        return findMaxChainLen(p, n, prev, pos + 1)
    else:
        ans = max(findMaxChainLen(p, n,p[pos].second, 0) + 1,findMaxChainLen(p, n,prev, pos + 1))
        m[val(pos, prev)] = ans
        return ans
def maxChainLen(p, n):
    global m
    m.clear()
    ans = findMaxChainLen(p, n, 0, 0)
    return ans
n = 5
p = [0] * n
p[0] = val(5, 24)
p[1] = val(39, 60)
p[2] = val(15, 28)
p[3] = val(27, 40)
p[4] = val(50, 90)
m = {}
print(maxChainLen(p, n))
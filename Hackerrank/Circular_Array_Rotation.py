n, k, q = map(int, input().split())
elem = list(map(int, input().split()))
for i in range(k):
    elem.insert(0, elem.pop())
for i in range(q):
    x = int(input())
    print(elem[x])

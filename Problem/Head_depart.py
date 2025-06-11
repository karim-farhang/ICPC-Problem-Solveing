from collections import defaultdict

g = defaultdict(list)

t = int(input())
while t > 0:
    nod = int(input())
    edge = int(input())
    subEde = list()
    for _ in range(edge):
        u, v = map(str, input().split(' '))
        g[u].append(v)
        subEde.append(v)
    head = list()
    for i in g.keys():
        if i in subEde:
            head.append(i)
    print(len(head))
    count = 1
    for h in head:
        em = []
        em.append(h)
        for k, v in g.items():
            if h in v and k not in head:
                em.append(k)
            if h == k:
                for x in v:
                    if x not in head:
                        em.append(x)
        for i in em:
            print(count, end=' ')
        count += 1
    print()
    print(*head)
    t -= 1

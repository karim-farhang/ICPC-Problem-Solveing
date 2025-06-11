"""
1
3 50
60,120,100
10,30,20
------------
240.00
"""
tc = int(input())
rtc = []
while tc > 0:
    t_item, kn_cap = [int(x) for x in input().split(' ')]
    v = [int(x) for x in input().split(',')]
    w = [int(x) for x in input().split(',')]
    ratio = [v[i] / w[i] for i in range(len(v))]
    v = v.sort(key=lambda x:ratio)
    w = w.sort(key=lambda x:ratio)
    print(v)
    print(w)
    print(ratio)
    tc -= 1

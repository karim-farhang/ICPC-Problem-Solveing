"""
100 100 50 40 40 20 10
5 25 50 120
"""
Score_bord = list(set([int(x) for x in input().split(' ')]))
scores = [int(x) for x in input().split(' ')]
for p in scores:
    count = 1
    for j in Score_bord:
        if int(p) < int(j):
            count += 1
    print(count)

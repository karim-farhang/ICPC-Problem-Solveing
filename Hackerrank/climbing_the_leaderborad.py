r = int(input())
ranking = list(set(map(int, input().split())))
ranking.sort(reverse=True)

s = int(input())
score = list(map(int, input().split()))

rank = 1
for i in score:
    for j in ranking:
        if i >= max(ranking):
            print(1)
            break
        if i < min(ranking) and i not in ranking:
            print(len(ranking) + 1)
            break
        else:
            if i >= j:
                print(ranking.index(j) + 1)
                break

"""
n = int(input().strip())
scores = list(reversed(sorted(list(set([int(scores_temp) for scores_temp in input().strip().split(' ')])))))
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

for x in alice:
    while len(scores) > 0 and scores[-1] <= x:
        del scores[-1]

    print(len(scores) + 1)
"""
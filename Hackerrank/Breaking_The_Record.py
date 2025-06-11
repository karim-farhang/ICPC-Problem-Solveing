Game = int(input())
score = list()
hieghts = list()
lowest = list()
x = list(map(int, input().split()))
for i in x:
    score.append(i)
    hieghts.append(max(score))
    lowest.append(min(score))
low = lowest[0]
hig = hieghts[0]
countH = 0
countL = 0
for i in range(Game):
    if hieghts[i] > hig:
        hig = hieghts[i]
        countH += 1
    if lowest[i] < low:
        low = lowest[i]
        countL += 1
print(f'{countH} {countL}')

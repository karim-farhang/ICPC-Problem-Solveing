Activitys = list(zip(map(int, input().split(" ")), map(int, input().split(" "))))
Activitys.sort(key=lambda x: x[1])
i = 0
print(Activitys[i])
for j in range(len(Activitys)):
    if Activitys[j][0] >= Activitys[i][1]:
        print(Activitys[j])
        i = j

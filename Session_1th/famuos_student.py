tc = int(input())
result = []
while tc > 0:
    res = []
    name = input().split(",")
    score = [int(x) for x in input().split(",")]
    mx = max(score)
    mi = min(score)
    in_max = score.index(mx)
    in_in = score.index(mi)
    res.append([name[in_max], score[in_max]])
    res.append([name[in_in], score[in_in]])
    result.append(res)
    tc -= 1
print()
tsss=0
for x in result:
    print("Test{0}".format(tsss+1))
    for j in x:
        print(j[0], " ", j[1])
    print()
    tsss+=1

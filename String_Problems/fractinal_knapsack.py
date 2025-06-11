val = [60,100]
wt = [10,20]
w = 50
result = []
for i in range(len(val)):
    div = val[i]/wt[i]
    sub = []
    sub.append(val[i])
    sub.append(wt[i])
    sub.append(div)
    result.append(sub)
result.sort(key=lambda x:x[2],reverse=True)
get = 0
sum1 = 0
for i in range(len(val)):
    if get+result[i][1] <= w:
        get+=result[i][1]
        sum1+=result[i][0]
    else:
        if get != 0:
            su = (w - get)*result[i][2]
            sum1 +=su
            break
print(sum1)
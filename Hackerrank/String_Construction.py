t = int(input())
while t > 0:
    st = input()
    sub =[]
    count =0
    for i in st:
        if i not in sub:
            sub.append(i)
            count+=1
    print(count)
    t -=1
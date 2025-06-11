t = int(input())
while t > 0:
    st = input()
    sum =0
    for i in range(len(st)//2):
        if ord(st[i]) != ord(st[-(i+1)]):
            if ord(st[i]) > ord(st[-(i+1)]):
                sum+=ord(st[i]) - ord(st[-(i+1)])
            elif ord(st[i]) < ord(st[-(i+1)]):
                sum+=ord(st[-(i+1)])- ord(st[i])
    print(sum)
    t -=1
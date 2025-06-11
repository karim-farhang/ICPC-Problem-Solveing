n = int(input())
st = input()

while st != "ENDOFINPUT":
    length = abs(n - len(st))
    if st == ' ':
        print("")
    if length > n // 2 or length == 0:
        print(st)
    elif len(st) > 50:
        breakword = st[50:]
        x = 0
        if breakword[0] != ' ':
            for i in range(50, 0, -1):
                if st[i] == ' ':
                    x = i
                    break
        breakword = st[x+1:]
        st = st[0:x] + '\n' + breakword
        print(st)
    else:
        p = 0
        just = False
        while not just:
            if st[p] == ' ' and st[p + 1] != ' ':
                st = st[0:p] + ' ' + st[p:]
                p += 2
            else:
                p += 1
            if p == len(st):
                p = 0
            if len(st) >= 50:
                just = True
                break
        print(st)
    st = input()

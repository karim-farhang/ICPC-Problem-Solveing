n = int(input())
while n > 0:
    st = list(input())
    b = True
    string = "hackerrank"
    for i in string:
        if i in st:
            ind = st.index(i)
            st = st[ind:]
            st.remove(i)
        elif i not in st:
            b=False
    if b:
        print("YES")
    else:
        print("NO")

    n -= 1

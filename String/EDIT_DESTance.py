# ecfbefdcfca badfcbebbf
st1, st2 = list(input().split(' '))
con = 0
if len(st1) < len(st2):
    for i in st2:
        if i in st1:
            st2.remove(i)
            st1.remove(i)
        else:
            con += 1
if len(st2) < len(st1):
    for i in st1:
        if i in st2:
            st2.remove(i)
            st1.remove(i)
        else:
            con += 1
print(con)

# -- string rotation of another string --
s = input()
s1 = input()

if len(s) != len(s1):
    print("NO")
else:
    temp = s + s
    if temp.count(s1) > 0:
        print("YES")
    else:
        print("NO")

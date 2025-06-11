line = int(input())
frinds = []
user = []
for i in range(line):
    x = input().split(",")
    frinds.append(x)
    user.append(x[0])
userr = input().split(",")
mutual = []
for i in userr:
    ind = user.index(i)
    mutual.append(frinds[ind])
set1=set(mutual[0])
set2=set(mutual[1])
x = len(set1.intersection(set2))
print(x)

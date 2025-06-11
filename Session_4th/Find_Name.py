names = input().split(",")
find = input()
cont = 1
for i in names:
    if find == i:
        print(cont)
        break
    else:
        cont += 1

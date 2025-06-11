for _ in range(int(input())):
    tem1, tem2 = map(int, input().split())
    if tem1 != 0:
        if tem1 >= tem2:
            print("Yes")
        else:
            print('No')
    else:
        print("No")

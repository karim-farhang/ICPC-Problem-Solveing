for _ in range(int(input())):
    ar = list(map(int, input().split()))
    Res = "No"
    for i in ar:
        if i > sum(ar) - i:
            Res = "Yes"
            break
    print(Res)

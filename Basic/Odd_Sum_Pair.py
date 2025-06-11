for _ in range(int(input())):
    na = list(map(int, input().split()))
    res = 'No'
    for i in na:
        for j in na:
            if (i + j) % 2 == 1:
                res = 'Yes'
                break
        if res == 'Yes':
            break
    print(res)

def equal_1(arr):
    max_arr = max(arr)
    min_arr = min(arr)
    diff = max_arr - min_arr
    count = 0
    increment = 0
    while(diff!=0):
        if diff >= 5:
            increment = 5
        elif diff < 5 and diff >=2:
            increment = 2
        else :
            increment = 1
        for i in range(0,len(arr)):
            if max_arr != arr[i]:
                arr[i] = arr[i] + increment
        count += 1
        max_arr = max(arr)
        min_arr = min(arr)
        diff = max_arr - min_arr
    return count
t = int(input())
while t >0:
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    print(equal_1(arr))
    t -=1
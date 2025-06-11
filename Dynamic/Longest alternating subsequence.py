# A sequence {x1, x2, .. xn} is alternating sequence if its elements satisfy one of the following relations :
# x1 < x2 > x3 < x4 > x5..... or  x1 >x2 < x3 > x4 < x5.....
# Your task is to find the longest such sequence.

def AlternatingaMaxLength(arr):
    inc = 1
    dec = 1
    n = len(arr)
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc = dec + 1
        elif arr[i] < arr[i - 1]:
            dec = inc + 1
    return max(inc, dec)
nums = [1, 5, 4]
print(AlternatingaMaxLength(nums)) # --> 3

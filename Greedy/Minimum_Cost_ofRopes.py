"""
4
4 3 2 6
"""
n = int(input())
arr = list([int(i) for i in input().split(' ')])
sum1 = 0
while len(arr) > 1:
    number1 = min(arr)
    arr.remove(number1)
    number2 = min(arr)
    arr.remove(number2)
    add_num = number1+number2
    sum1 +=add_num
    arr.append(add_num)
print(sum1)
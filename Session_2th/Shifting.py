shefting_N = int(input())
numbers = [int(i) for i in input().split(" ")]

for i in range(shefting_N):
    numbers.insert(0, numbers.pop())

for i in numbers:
    print(i, end=" ")

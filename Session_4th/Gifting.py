student = int(input())
gift = list(map(int, input().split(" ")))
if student == gift[0]:
    for i in range(student):
        print(1, 0, end=" ")
else:
    print('Error')

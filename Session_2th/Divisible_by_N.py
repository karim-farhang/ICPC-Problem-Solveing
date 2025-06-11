T = int(input())
RT = []
while T > 0:
    number = [int(x) for x in input().split(" ")]
    N = int(input())
    number = [d for d in number if d % N == 0]
    RT.append(len(number))
    T -= 1
for x in RT:
    print(x)

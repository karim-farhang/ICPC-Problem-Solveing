T = int(input())
x = []
for i in range(T):
    p = [int(x) for x in input().split(" ")]
    x.extend(p)
x.sort()
for j in x:
    print(j, end=" ")

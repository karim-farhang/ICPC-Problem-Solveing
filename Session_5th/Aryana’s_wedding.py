tc = int(input())
result = []
while tc:
    names = list(map(str, input().split(",")))
    names.sort()
    print(names)
    per = str(input())
    if per in names:
        print("present")
    else:
        print("Hap-sent")

    tc -= 1

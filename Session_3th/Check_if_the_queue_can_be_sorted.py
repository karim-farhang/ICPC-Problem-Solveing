def can_be_sorted(li):
    for i in range(len(li)):
        li.insert(0, li.pop())
        if sorted(li) == li:
            return True
    return False


tc = int(input())
while tc:
    print(can_be_sorted([int(x) for x in input().split(" ")]))
    tc -= 1

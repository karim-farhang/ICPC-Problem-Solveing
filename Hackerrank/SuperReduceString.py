st = input()
while True:
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            st = st[0:i] + st[i + 2:]
            break
    b = False
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            b = True
    if not (b):
        break
if len(st) == 0:
    print("Empty String")
else:
    print(st)

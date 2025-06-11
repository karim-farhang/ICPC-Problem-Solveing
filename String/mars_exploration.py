st = input()
count =0
arr = []
for i in range(0,len(st)-2,3):
    if st[i] != 'S':
        count +=1
    if st[i+1] != 'O':
        count +=1
    if st[i+2] != 'S':
        count +=1
print(count)
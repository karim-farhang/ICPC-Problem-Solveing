num = int(input().strip())
numb = []
for i in range(num):
    numb.append(int(input().strip()))
numb.sort(reverse=True)
for i in numb:
    print(i)

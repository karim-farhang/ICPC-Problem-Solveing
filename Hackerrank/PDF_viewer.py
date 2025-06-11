import string

character = list(map(int, input().split()))
position = string.ascii_lowercase
word = input()
count = 1
ss = list()
for i in word:
    index = position.index(i)
    value = character[index]
    ss.append(value)
result = max(ss) * len(ss)
print(result)
